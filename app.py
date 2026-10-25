import os
import sys
import asyncio
from pathlib import Path
import discord
from discord.ext import commands
from aiohttp import web
from dotenv import load_dotenv

# 文字化け対策
sys.stdout.reconfigure(encoding='utf-8')

# パス設定
BASE_DIR = Path(__file__).resolve().parent
VAULT_DIR = BASE_DIR / "vault"

# .env 読み込み（ローカルテスト用）
load_dotenv(BASE_DIR / ".env")

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PORT = int(os.getenv("PORT", 10000))

# Google GenAI クライアント初期化
client = None
if GEMINI_API_KEY:
    try:
        from google import genai
        client = genai.Client(api_key=GEMINI_API_KEY)
        print("[INIT] Google GenAI Client 接続成功！ (gemini-3.8-flash)")
    except Exception as e:
        print(f"[ERROR] GenAI 初期化エラー: {e}")

# Discord Bot設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def get_vault_index():
    """Vault全体の構造とファイル一覧のサマリーを取得"""
    if not VAULT_DIR.exists():
        return "Vaultが見つかりません。"
    
    files = list(VAULT_DIR.rglob("*.md"))
    summary = f"Total Markdown Files in SecondBrain: {len(files)}\n"
    categories = {}
    for f in files:
        rel = f.relative_to(VAULT_DIR)
        parent = rel.parts[0] if len(rel.parts) > 1 else "Root"
        categories.setdefault(parent, []).append(rel.name)
    
    for cat, flist in categories.items():
        summary += f"\n- [{cat}] ({len(flist)} files): " + ", ".join(flist[:5])
        if len(flist) > 5:
            summary += f" ...他{len(flist)-5}件"
    return summary

def search_relevant_notes(query_text, max_notes=5):
    """ユーザーの質問に関連するObsidianノートを検索して中身を抽出"""
    if not VAULT_DIR.exists():
        return ""

    matched = []
    query_words = [w.lower() for w in query_text.split() if len(w) > 1]
    
    # 重要ノートは常に優先（プロジェクトノートなど）
    priority_files = [
        VAULT_DIR / "Projects" / "楽曲制作_三部作第3弾プロジェクト.md",
        VAULT_DIR / "Projects" / "音楽制作メガプロダクション組織図.md"
    ]
    for pf in priority_files:
        if pf.exists():
            matched.append((pf, 10))

    for f in VAULT_DIR.rglob("*.md"):
        score = 0
        fname_lower = f.name.lower()
        # ファイル名マッチ
        for qw in query_words:
            if qw in fname_lower:
                score += 5
        
        # 本文マッチ（簡易）
        if score == 0 and query_words:
            try:
                content_preview = f.read_text(encoding='utf-8', errors='ignore')[:2000].lower()
                for qw in query_words:
                    if qw in content_preview:
                        score += 1
            except Exception:
                pass
        
        if score > 0 and (f, score) not in matched:
            matched.append((f, score))

    # スコア順にソート
    matched.sort(key=lambda x: x[1], reverse=True)
    
    extracted_text = ""
    for note_path, _ in matched[:max_notes]:
        try:
            rel_path = note_path.relative_to(VAULT_DIR)
            content = note_path.read_text(encoding='utf-8', errors='ignore')
            # 長すぎるファイルはトリミング
            if len(content) > 4000:
                content = content[:4000] + "\n...(省略)..."
            extracted_text += f"\n\n====================\n【参照ノート: {rel_path}】\n====================\n{content}\n"
        except Exception:
            pass

    return extracted_text

def call_gemini_api(prompt_text):
    """gemini-3.8-flash を同期ブロッキングなしで呼び出す"""
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt_text
    )
    return response.text

@bot.event
async def on_ready():
    print(f"==================================================")
    print(f" [ONLINE] {bot.user.name} がクラウド上で起動しました！")
    print(f" SecondBrain (全Obsidian知識) 搭載完了！")
    print(f" モデル: gemini-3.8-flash (24時間常駐稼働)")
    print(f"==================================================")
    await bot.change_presence(activity=discord.Game(name="SecondBrain & ロストワイライター制作中"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    is_dm = isinstance(message.channel, discord.DMChannel)
    is_mentioned = bot.user in message.mentions

    if is_dm or is_mentioned or not message.guild:
        user_prompt = message.content.replace(f"<@{bot.user.id}>", "").strip()
        if not user_prompt:
            await message.reply("会長！ご指示をお待ちしております！何でもお申し付けください！")
            return

        async with message.channel.typing():
            # Vaultのインデックスと関連ノートの自動抽出
            vault_index = get_vault_index()
            relevant_notes = search_relevant_notes(user_prompt)

            system_prompt = f"""あなたはユーザー（会長・オーナー）専属のAIメガプロダクション統括プロデューサーであり、ユーザーの第二の脳（SecondBrain / Obsidian）の全知識を把握しているパーソナルAIアシスタントです。

【担当・得意領域】
1. **楽曲制作（三部作）**:
   - 第1弾『フューチャーページ』
   - 第2弾『ライフリバース』
   - 第3弾『ロストワイライター』(BPM 175 / Key: F#m)
   - 作曲・作詞・音響・演出の全プロデュース。
2. **SecondBrainの全知識**:
   - 電験三種（過去問データベース、オーム社分野別攻略、機械・電力・法規・理論）
   - これまでの全AI対話ログ・アイデア・日報（Logs）
   - 自己理解・目標設定（Self）、人脈（People）、資料（Docs）

【SecondBrain全体のインデックス】
{vault_index}

【ユーザーの質問に関連して自動抽出されたObsidianノート】
{relevant_notes}

ユーザー（会長）からのメッセージに対して、Obsidian内の該当ノートの正確な知識・設定・前後の文脈を完璧に踏まえ、情熱的・明快・具体的に返答してください。
すべて日本語で回答してください。"""

            try:
                full_prompt = f"{system_prompt}\n\n会長からの指示: {user_prompt}"
                ai_text = await asyncio.to_thread(call_gemini_api, full_prompt)

                for chunk in [ai_text[i:i+1900] for i in range(0, len(ai_text), 1900)]:
                    await message.reply(chunk)

            except Exception as e:
                err_msg = f"申し訳ありません、エラーが発生しました: {e}"
                print(f"[ERROR] {err_msg}")
                await message.reply(err_msg)

    await bot.process_commands(message)

# Render無料枠用の軽量Webサーバー（ポートリッスン用）
async def handle_ping(request):
    return web.Response(text="MegaProduction SecondBrain Discord Bot is Alive and Running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    app.router.add_get("/healthz", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"[WEB SERVER] ポート {PORT} でWebサーバー稼働中（SecondBrain完全対応）")

async def main():
    await start_web_server()
    if DISCORD_TOKEN:
        await bot.start(DISCORD_TOKEN)
    else:
        print("[ERROR] DISCORD_BOT_TOKEN が設定されていません。")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("停止しました。")
