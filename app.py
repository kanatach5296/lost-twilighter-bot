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
PROJECT_CONTEXT_PATH = BASE_DIR / "project_context.md"

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

def get_project_context():
    """プロジェクト設計書（クラウド同梱版）を読み込む"""
    if PROJECT_CONTEXT_PATH.exists():
        try:
            return PROJECT_CONTEXT_PATH.read_text(encoding='utf-8')
        except Exception:
            pass
    return "楽曲制作：三部作第3弾『ロストワイライター』(BPM 175 / Key: F#m)"

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
    print(f" モデル: gemini-3.8-flash (24時間常駐稼働)")
    print(f"==================================================")
    await bot.change_presence(activity=discord.Game(name="三部作第3弾『ロストワイライター』制作中"))

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
            context = get_project_context()

            system_prompt = f"""あなたはユーザー（会長・オーナー）専属のAI音楽メガプロダクション（総勢30名）の統括プロデューサーです。
制作中の楽曲：三部作第3弾『ロストワイライター』(BPM 175 / Key: F#m)
コアテーマ：表（奇跡・軌跡・エモさ）× 裏（禁句の繋がり・残されたメンバーへの想い・残酷さ・まだ見たかった笑顔・好きじゃねえ愛してる）

【現在のプロジェクト設計書】
{context}

ユーザーからのメッセージに対して、統括プロデューサーとして、また作詞部（エモーション、サツキアン、ポイズン等）やサウンド部（ビートマスター、エモコード等）の専門的な意見を交えて、情熱的・具体的に返答してください。
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
    return web.Response(text="MegaProduction Discord Bot is Alive and Running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    app.router.add_get("/healthz", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"[WEB SERVER] ポート {PORT} でWebサーバー稼働中（Render無料プラン対応）")

async def main():
    # WebサーバーとDiscord Botを並行稼働
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
