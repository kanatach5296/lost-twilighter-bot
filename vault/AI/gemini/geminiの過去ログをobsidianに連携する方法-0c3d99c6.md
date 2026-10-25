---
id: gemini_0c3d99c67b092580
title: Geminiの過去ログをObsidianに連携する方法
source: gemini
url: "https://gemini.google.com/app/0c3d99c67b092580"
created: "2026-10-23T00:05:56+00:00"
modified: "2026-10-23T00:05:56+00:00"
tags:
  - ai-conversation
  - gemini
message_count: 23
---

> [!QUESTION] User
> 拡張機能のほうがいいよおぶりあんと相性いいし

> [!NOTE] Gemini
> 拡張機能でObsidian向けに全チャットを出力したい場合、先ほどのエラー（画面が固まる・取得漏れするバグ）を回避できる別の拡張機能を使うか、設定を少し調整して通すのが手っ取り早いです。
> 
> Obsidianと相性が良く、全件出力に対応している拡張機能の選択肢です。
> 
> ### 1\. もうひとつの専用ツール：『Gemini to Obsidian』
> 
> 先ほど試したツールとは別作者による、Obsidian直結型の拡張機能です。File System Access APIを使ってObsidianのVaultフォルダを直接指定できるため、ダウンロードフォルダを経由せず自動でノートが生成されます。
> 
> -   **Chromeウェブストアで検索**: `Gemini to Obsidian`（作者: Terry Ting）
>     
> -   **特徴**:
>     
>     -   最初に対象のObsidian Vaultフォルダを指定して書き込み許可を出す
>         
>     -   コールアウト（引用枠）、LaTeX数式、コードブロックをObsidian向け記法で維持して出力
>         
>     -   画面に読み込まれているチャットをワンクリックでVault内に直接保存
>         
> 
> ### 2\. 『Gemini Chat Exporter』（Obsidian / Notion向け軽量設計）
> 
> ObsidianなどのPKM（知識管理ツール）連携に特化したシンプルなMarkdownエクスポーターです。余計な一括API通信を挟まないためクラッシュしにくいのが特徴です。
> 
> -   **Chromeウェブストアで検索**: `Gemini Chat Exporter`
>     
> -   **特徴**:
>     
>     -   プレーンなMarkdown形式で書き出し
>         
>     -   構文崩れ（見出しタグやリストの重複）が起きにくい
>         
> 
> ### ※先ほどの拡張機能（Export Gemini Chats to Obsidian）で「バグらせずに一括出力する」コツ
> 
> もし先ほどの拡張機能のまま全件出力したい場合は、次の点を確認すると成功しやすいです。
> 
> 1.  **画面の左サイドバー（過去履歴）を一度一番下までスクロールしておく**
>     
>     Geminiは過去チャットを「スクロールするたびに後から読み込む（遅延読み込み）」仕様のため、一括処理時に履歴が読み込まれていないと通信エラーで止まります。
>     
> 2.  **「Bulk Export」ではなく「Selective Export」を使う**
>     
>     一括で何百件も同時に走らせるとGemini側のレート制限に引っかかってフリーズします。設定の「Selective Export」を選び、20〜30件ずつ小分けにしてチェックを入れて出力すると安定して通ります。

> [!QUESTION] User
> https://chromewebstore.google.com/detail/obsidian-ai-exporter/edemgeigfbodiehkjhjflleipabgbdeh?hl=ja&utm_source=ext_sidebar

> [!NOTE] Gemini
> その「Obsidian AI Exporter」は非常に相性が良く、おすすめの拡張機能です。
> 
> 日本の開発者（しょっさん氏）が作成・頻繁にアップデートしており、Geminiの画面上に紫色の「Sync」ボタンが出て、Obsidianのコールアウト記法（`[!NOTE]` など）や画像、数式を綺麗に保持したまま保存できます。
> 
> ### 出力方法は2通りあります
> 
> #### ① 【簡単】ファイル（.md）としてダウンロードする方法（設定不要）
> 
> Obsidian側のプラグイン設定などをせず、すぐ使いたい場合の手順です。
> 
> 1.  拡張機能をChromeに追加する。
>     
> 2.  Web版Geminiで保存したいチャットを開く。
>     
> 3.  画面上に表示される紫色の **「Sync」ボタン** をクリックする。
>     
> 4.  出力先で **「File」** を選択する。
>     
> 5.  ダウンロードされた `.md` ファイルを、ObsidianのVault（フォルダ）にドラッグ＆ドロップする。
>     
> 
> #### ② 【完全自動】Obsidianに1クリックで直接書き込む方法
> 
> 拡張機能からObsidianへ直接ノートを送信する連携方法です。
> 
> 1.  **Obsidian側で準備**:
>     
>     -   Obsidianの「設定」→「コミュニティプラグイン」を開く。
>         
>     -   **「Local REST API」** プラグインを検索してインストールし、有効化する。
>         
>     -   プラグインの設定画面を開き、表示されている **API Key** をコピーする。
>         
> 2.  **Chrome拡張機能側の設定**:
>     
>     -   Chrome右上の「Obsidian AI Exporter」アイコンをクリックして設定を開く。
>         
>     -   コピーした **API Key** を貼り付け、保存先フォルダ（例: `AI/Gemini` など）を指定する。
>         
> 3.  **エクスポート**:
>     
>     -   Gemini画面の「Sync」ボタンを押して「Obsidian」を選ぶだけで、自動でObsidian内にノートが作られます。
>         
> 
> ### 過去の全チャットを処理する際の注意点
> 
> -   このツールには自動スクロール機能（Auto-scroll）が内蔵されているため、長い会話でも途切れずに取得できます。
>     
> -   会話ごとに「チャットを開く → Syncボタンを押す」という形で順番に保存していくのが、エラーを起こさず確実にObsidianへ移す一番安定した方法です。

> [!QUESTION] User
> Please configure your Obsidian API key in the extension settings

> [!NOTE] Gemini
> そのメッセージは、拡張機能がObsidianと通信するための**APIキーが未入力**であることを示しています。
> 
> 以下の手順でObsidianからキーを発行し、拡張機能に貼り付けてください。
> 
> ### 手順1：Obsidian側でAPIキーを取得する
> 
> 1.  **Obsidian**を開きます。
>     
> 2.  左下の歯車アイコン（**設定**）をクリックします。
>     
> 3.  左サイドバー下部にある「コミュニティプラグイン」の項目から **「Local REST API」** を選択します。
>     
>     -   ※まだ入れていない場合は、「コミュニティプラグイン」→「閲覧」から「Local REST API」を検索してインストール・有効化してください。
>         
> 4.  設定画面内にある **「API Key」**（文字列）の横にあるコピー用アイコンをクリック、または文字列をコピーします。
>     
>     -   ※「Status: Running」と表示されていればプラグインが正常に動作しています。
>         
> 
> ### 手順2：Chrome拡張機能にAPIキーを貼り付ける
> 
> 1.  ブラウザ（Chrome）右上の拡張機能アイコン（パズルピースのマーク）をクリックします。
>     
> 2.  **「Obsidian AI Exporter」** の三点リーダー（縦の…）をクリックし、**「オプション」**（または設定アイコン）を開きます。
>     
> 3.  設定項目の中にある **「API Key」** の入力欄に、先ほどコピーしたキーを貼り付けます。
>     
> 4.  その下にある「Path」や「Folder」などの項目に、ノートの保存先（例: `Gemini` や `AI Chats` など、Obsidian内のフォルダ名）を入力します（空欄でもルートに保存されます）。
>     
> 5.  設定を保存（「Save」ボタンがある場合はクリック）します。
>     
> 
> ### 手順3：動作確認
> 
> 1.  Web版Geminiのチャット画面を再読み込み（F5 / Ctrl + R）します。
>     
> 2.  表示される紫色の「Sync」ボタンをクリックし、エラーが出ずにObsidian側へ新規ノートが自動作成されれば連携完了です。

> [!QUESTION] User
> Cannot reach Obsidian. Is it running?

> [!NOTE] Gemini
> このエラー（**Cannot reach Obsidian. Is it running?**）は、ブラウザ拡張機能がPC上のObsidian本体やLocal REST APIプラグインと通信できていないときに出ます。
> 
> 原因は「HTTPSの証明書をブラウザがブロックしている」**か**「ポート番号の不一致 / 設定の不備」がほとんどです。順番に確認して解消していきましょう。
> 
> ### ステップ1：Obsidian本体とプラグインの稼働確認
> 
> 1.  **Obsidianを起動**した状態にしておく（※裏で動いていないと通信できません）。
>     
> 2.  Obsidianの左下「設定（歯車）」→「コミュニティプラグイン」→ **「Local REST API」** を開く。
>     
> 3.  一番上のステータスが **「Status: Running」**（緑色）になっているか確認する。
>     
>     -   ※もし止まっている場合は、プラグインのトグルを一度オフにしてから再度オンにしてください。
>         
> 
> ### ステップ2：ブラウザの証明書エラーを解除する（一番多い原因）
> 
> Local REST APIは安全な通信（HTTPS）を行うため、パソコン内に自己署名証明書を作成します。Chrome側が「安全ではない接続」として通信を遮断しているケースが多いです。
> 
> 1.  Chromeの新しいタブを開き、URLバーに以下を入力してEnterを押す：
>     
>     Plaintext
>     
>     ```
>     https://127.0.0.1:27124
>     ```
>     
> 2.  画面に **「この接続ではプライバシーが保護されません」** や「保護されていない通信」といった警告が出たら、**「詳細設定」** をクリックする。
>     
> 3.  画面下部に表示される **「127.0.0.1 にアクセスする（安全ではありません）」** をクリックする。
>     
> 4.  画面にJSONの英語メッセージ（`{"status":"OK", ...}` など）が表示されれば、ブラウザ側の通信ブロックが解除されました。
>     
> 
> ### ステップ3：拡張機能の設定（ポート番号とプロトコル）を合わせる
> 
> 1.  Chrome右上の拡張機能アイコンから **「Obsidian AI Exporter」のオプション（設定画面）** を開く。
>     
> 2.  以下の項目がObsidianの設定と一致しているか確認する：
>     
>     -   **Protocol**: `HTTPS`（非暗号化にしている場合は `HTTP`）
>         
>     -   **Host**: `127.0.0.1`（または `localhost`）
>         
>     -   **Port**: `27124`（※Local REST APIの標準ポート番号）
>         
>     -   **API Key**: ステップ1でコピーしたキーが正しく貼られているか（前後に余分な空白スペースが入っていないか確認）
>         
> 3.  設定を保存する。
>     
> 
> ### ステップ4：Gemini画面を再読み込みしてテスト
> 
> 1.  Geminiのチャット画面に戻り、ページを再読み込み（Ctrl + R / F5）する。
>     
> 2.  紫色の「Sync」ボタンを押して、Obsidianに同期されるか試す。

> [!NOTE] Gemini
> 設定画面を確認しました。`Encrypted (HTTPS) server` が緑のチェックでポート `27124` で稼働しています。
> 
> PNG
> 
> ブラウザ拡張機能が接続できない主な原因は、**Chromeがローカルの自己署名HTTPS証明書を拒否していること**です。次の手順で解決します。
> 
> ### 解決手順
> 
> 1.  **Chromeで証明書を許可する**
>     
>     -   Chromeで新しいタブを開き、URLバーに `[https://127.0.0.1:27124/](https://127.0.0.1:27124/)` と入力してEnterを押します。
>         
>     -   「この接続ではプライバシーが保護されません」と表示されたら、画面左下の **「詳細設定」** をクリックします。
>         
>     -   下部に出てくる **「127.0.0.1 にアクセスする（安全ではありません）」** をクリックします。
>         
>     -   画面に英字のメッセージ（`{"status":"OK", ...}` など）が表示されれば、ブラウザのブロック解除は完了です。
>         
> 2.  **拡張機能（Obsidian AI Exporter）の設定を確認する**
>     
>     -   Chrome右上の拡張機能アイコンから「Obsidian AI Exporter」のオプションを開きます。
>         
>     -   画像に表示されているAPIキーを右側のコピーアイコンでコピーし、拡張機能の **API Key** 欄に貼り付けます。
>         
>         PNG
>         
>     -   接続先設定が以下になっているか確認します：
>         
>         -   **Protocol**: `HTTPS`
>             
>         -   **Host**: `127.0.0.1`
>             
>         -   **Port**: `27124`
>             
> 3.  **Gemini画面で再試行**
>     
>     -   Web版Geminiのタブをリロード（Ctrl + R）し、紫の「Sync」ボタンを押します。
>         
> 
> > **※もし上記でもHTTPS接続で弾かれる場合（一番簡単な回避策）** 画像下部にある **「Enable non-encrypted (HTTP) server」** のトグルスイッチを**オン**（有効）にしてください。 その後、拡張機能側の設定を **Protocol: `HTTP`** / **Port: `27123`** に切り替えると、証明書の警告なしで直接繋がるようになります。
> > 
> > PNG他 1 件

> [!QUESTION] User
> {
> "message": "Authorization required.  Find your API Key in the 'Local REST API with MCP' section of your Obsidian settings.",
> "errorCode": 40101
> }

> [!NOTE] Gemini
> ブラウザとObsidian間の通信自体は繋がりましたが、APIキーの認証に失敗している状態（401エラー）です。
> 
> キーの貼り付け時に前後に余分なスペースが入っているか、拡張機能側でキーが正しく保持されていない可能性があります。以下の手順で再設定してください。
> 
> ### 対処手順
> 
> 1.  **ObsidianからAPIキーを確実に再取得する**
>     
>     -   Obsidianの「設定」→ コミュニティプラグイン「Local REST API with MCP」を開く。
>         
>     -   **API key** の入力欄の右端にある **コピーアイコン（四角が重なったマーク）** を直接クリックする。
>         
>         -   *※ドラッグして選択コピーすると、目に見えない空白や改行が混ざりやすいため、必ずコピーボタンを使用してください。*
>             
> 2.  **拡張機能「Obsidian AI Exporter」の設定を更新する**
>     
>     -   Chrome右上の拡張機能アイコンから「Obsidian AI Exporter」の **オプション（設定）** を開く。
>         
>     -   入力されている **API Key** 欄の文字を一度 **すべて削除（全選択してバックスペース）** する。
>         
>     -   先ほどコピーしたキーをそのまま **貼り付け（Ctrl + V）** する。
>         
>     -   設定保存ボタン（Save / 保存）があればクリックする。
>         
> 3.  **反映確認**
>     
>     -   Geminiのタブに戻り、ページを再読み込み（Ctrl + R）する。
>         
>     -   紫色の「Sync」ボタンを押して、Obsidianに同期が通るか確認する。

> [!QUESTION] User
> c03414db220c79f4e2cc652ef87e733295e61aab1ac6dfce25ed9b6c64ef9bb8

> [!NOTE] Gemini
> Hada huwa l-API key l-kamel dyalek. Daba khassak tdiru f-l'extension f-Chrome bach yetlaga m3a Obsidian bla machekil.
> 
> Taba3 had l-khotowat:
> 
> 1.  **Kopi l-key l-kamel**: Kopi had l-code kamel bla matzid m3ah chi farragh (espace):
>     
>     Plaintext
>     
>     ```
>     c03414db220c79f4e2cc652ef87e733295e61aab1ac6dfce25ed9b6c64ef9bb8
>     ```
>     
> 2.  **Dkhol l-paramètres dyal l'extension f-Chrome**:
>     
>     -   Klike 3la l'icône dyal les extensions (chkel puzzle) lfo9 3la limen f-Chrome.
>         
>     -   Klike 3la tlatat dyal nqati 9ddam **Obsidian AI Exporter**, w khtar **Options** (aw Settings).
>         
> 3.  **Lassaq l-key**:
>     
>     -   Mseh dakchi li mktoub f-lkhana dyal **API Key**.
>         
>     -   Dirlu **Coller (Ctrl + V)** l-had l-code l-kamel.
>         
>     -   Dir **Save** (ila kant l-bouton bayna).
>         
> 4.  **Rejje3 l-Gemini w jerrab**:
>     
>     -   Rejje3 l-la page dyal Gemini w dir liha **Actualiser (Ctrl + R)**.
>         
>     -   Klike 3la l-bouton l-bnefsajiya dyal **Sync** bach tchouf wach ghadi ytsifet l-Obsidian direct.

> [!QUESTION] User
> まちがえた

> [!NOTE] Gemini
> 大丈夫です！
> 
> 先ほど送っていただいた文字列がObsidianの完全なAPIキーですので、こちらをコピーして設定に貼り付ければOKです。
> 
> Plaintext
> 
> ```
> c03414db220c79f4e2cc652ef87e733295e61aab1ac6dfce25ed9b6c64ef9bb8
> ```
> 
> ### 設定手順
> 
> 1.  上のAPIキーをコピーします（前後に余分なスペースが入らないように注意してください）。
>     
> 2.  Chrome右上の拡張機能アイコン（パズルマーク）から「**Obsidian AI Exporter**」のオプション（設定）を開きます。
>     
> 3.  **API Key** の入力欄に入っている文字を一度すべて消して、コピーしたキーを貼り付け（Ctrl + V）します。
>     
> 4.  設定を保存します。
>     
> 5.  Web版Geminiの画面に戻り、ページを再読み込み（Ctrl + R / F5）してから紫色の「**Sync**」ボタンを押してみてください。

> [!QUESTION] User
> Cannot reach Obsidian. Is it running?

> [!NOTE] Gemini
> ブラウザ（Chrome）がObsidian側のポートへの通信をブロックしているか、プラグインの設定と拡張機能の設定が食い違っていることが原因です。
> 
> 確実に接続を通すため、**暗号化なしのHTTP接続（ポート 27123）に切り替える方法**を試してください。証明書のエラーを完全に回避できるため、一番トラブルが起きにくい設定です。
> 
> ### 1\. Obsidian側の設定（HTTPを有効化）
> 
> 1.  **Obsidian**を開き、左下の設定（歯車）→ コミュニティプラグイン → **「Local REST API with MCP」** を開きます。
>     
> 2.  画面下部にある **「Enable non-encrypted (HTTP) server」** のトグルスイッチを**オン**にします。
>     
> 3.  画面上部の **「Non-encrypted (HTTP) server」** の表示が緑色のチェックマーク（`[http://127.0.0.1:27123/](http://127.0.0.1:27123/)`）に変わったことを確認します。
>     
> 4.  **API key** の右側にあるコピーアイコンをクリックして、キーをコピーしておきます。
>     
> 
> ### 2\. Chrome拡張機能（Obsidian AI Exporter）の設定
> 
> 1.  Chrome右上の拡張機能アイコンから **「Obsidian AI Exporter」** のオプション（設定）を開きます。
>     
> 2.  以下の通りに入力・変更します：
>     
>     -   **Protocol**: `HTTP`（※HTTPSではなくHTTPを選択）
>         
>     -   **Host**: `127.0.0.1`（または `localhost`）
>         
>     -   **Port**: `27123`（※HTTP用のポート番号）
>         
>     -   **API Key**: 先ほどコピーしたキー（`c03414db220c79f4e2cc652ef87e733295e61aab1ac6dfce25ed9b6c64ef9bb8`）を貼り付け
>         
> 3.  設定を保存します。
>     
> 
> ### 3\. ブラウザで接続確認と実行
> 
> 1.  Chromeの別タブで `[http://127.0.0.1:27123/](http://127.0.0.1:27123/)` にアクセスし、英字のメッセージが表示されるか確認します（警告画面が出ずに表示されれば通信成功です）。
>     
> 2.  Web版Geminiのチャット画面に戻り、ページを再読み込み（Ctrl + R）します。
>     
> 3.  紫色の **「Sync」** ボタンを押して同期を実行します。

> [!QUESTION] User
> {
> "status": "OK",
> "manifest": {
> "id": "obsidian-local-rest-api",
> "name": "Local REST API with MCP",
> "version": "5.5.2",
> "minAppVersion": "1.13.1",
> "description": "A secure REST API and Model Context Protocol (MCP) server for your vault.",
> "author": "Adam Coddington",
> "authorUrl": "https://adamcoddington.net/",
> "isDesktopOnly": true,
> "dir": ".obsidian/plugins/obsidian-local-rest-api"
> },
> "versions": {
> "obsidian": "1.14.4",
> "self": "5.5.2"
> },
> "service": "Obsidian Local REST API",
> "authenticated": false
> }

> [!NOTE] Gemini
> ブラウザとObsidian本体の接続（`127.0.0.1:27124`）自体は完全に成功しています。
> 
> 末尾の `"authenticated": false` は「APIキーをリクエストヘッダーに含めていないため、まだ未認証状態である」ことを示しており、ブラウザから直接URLを叩いた場合はこの表示で正常です。
> 
> この状態であれば通信ブロックは解除されているため、拡張機能「Obsidian AI Exporter」側で正しくAPIキーを認識させれば同期が通ります。以下の手順で設定を完了させてください。
> 
> ### 手順1：拡張機能の設定を開いて再入力する
> 
> 1.  Chrome右上の拡張機能アイコン（パズルマーク）をクリックします。
>     
> 2.  **「Obsidian AI Exporter」** の横にある「︙」（三点リーダー）をクリックし、**「オプション」**（または設定アイコン）を開きます。
>     
> 3.  設定項目を以下のように合わせます：
>     
>     -   **Protocol**: `HTTPS`
>         
>     -   **Host**: `127.0.0.1`
>         
>     -   **Port**: `27124`
>         
>     -   **API Key**: 以下のキーを前後に空白が入らないように貼り付けます。
>         
>         Plaintext
>         
>         ```
>         c03414db220c79f4e2cc652ef87e733295e61aab1ac6dfce25ed9b6c64ef9bb8
>         ```
>         
> 4.  画面内に **「Save」** や **「保存」** ボタンがある場合は必ずクリックします。
>     
> 
> ### 手順2：Geminiで同期を実行する
> 
> 1.  Web版Geminiのタブに戻ります。
>     
> 2.  ページを **再読み込み（Ctrl + R または F5）** します（拡張機能の最新設定を読み込ませるため必須です）。
>     
> 3.  画面上に表示される紫色の **「Sync」** ボタンをクリックします。
>     
> 
> Obsidian側の保管庫（Vault）内に、現在のチャットタイトルの新しいノートが自動生成されていれば連携完了です。

> [!QUESTION] User
> できない

> [!NOTE] Gemini
> 通信や認証が引っかかって自動同期が通らない場合のトラブルを切り分けます。
> 
> 原因として最も多いのは「Obsidian AI Exporterの設定画面で保存（Save）が押せていない・入力形式が違う」**、または**「Geminiの画面側で権限ブロックが起きている」のどちらかです。
> 
> 以下の2つの対処法を順番に試してください。
> 
> ### 対処法1：拡張機能の設定画面の入力項目を再点検する
> 
> Obsidian AI Exporterのオプション画面を開き、入力内容が以下の形式と完全に一致しているか確認してください。
> 
> 1.  **Host**: `127.0.0.1` または `localhost`
>     
>     -   ※`https://` や末尾の `/` は入れず、IPまたはホスト名のみ入力します。
>         
> 2.  **Port**: `27124`
>     
> 3.  **Protocol**: `HTTPS`
>     
> 4.  **API Key**:
>     
>     Plaintext
>     
>     ```
>     c03414db220c79f4e2cc652ef87e733295e61aab1ac6dfce25ed9b6c64ef9bb8
>     ```
>     
> 5.  **Save（保存）**: 画面下部に **Save** や **Update** ボタンがある場合は必ずクリックします。
>     
>     -   ※保存後、設定画面を閉じてGeminiのタブを必ずリロード（F5 / Ctrl + R）してください。
>         
> 
> ### 対処法2：ワンクリックで「ファイル書き出し（File）」に切り替える（API不要・即座に完了）
> 
> Local REST API経由の同期エラーを完全に迂回し、拡張機能の本来の機能である**Markdownファイル直接ダウンロード**を使う方法です。APIや設定の通信トラブルに関係なく即座にObsidian用ノートを作成できます。
> 
> 1.  Gemini画面に表示されている紫色の **「Sync」ボタン（またはその横の矢印/メニュー）** をクリックします。
>     
> 2.  保存先やモードの選択肢が出たら、`Obsidian` ではなく **`File`**（または `Download Markdown` / `.md`）を選択します。
>     
> 3.  ブラウザのダウンロードフォルダに、チャット内容がObsidian形式でフォーマットされた `.md` ファイルが保存されます。
>     
> 4.  そのファイルをObsidianのVault（フォルダ）へドラッグ＆ドロップします。
>     
> 
> ### 対処法3：Chromeのコンソールエラーを確認する（REST API連携を維持したい場合）
> 
> どうしてもAPI直接連携で通したい場合、Geminiの画面で `F12` キー（または右クリック →「検証」）を押し、上部の **「Console（コンソール）」** タブを開いた状態で「Sync」ボタンを押してみてください。 赤文字で表示されるエラー（例: `CORS error`、`Failed to fetch`、`401 Unauthorized` など）の内容を教えていただければ、具体的な原因を特定できます。

> [!NOTE] Gemini
> 設定画面の画像を確認しました。
> 
> PNG
> 
> この拡張機能（Obsidian AI Exporter）のデフォルト案内にもうっすら見えている通り、**Obsidian Local REST API の標準接続先は「HTTP」のポート `27123`** です。 現在設定されている `[https://127.0.0.1:27124](https://127.0.0.1:27124)` だと、Chromeのセキュリティ機能（自己署名SSL証明書のブロック）によって拡張機能からの通信が裏で遮断され、通信エラーになります。
> 
> PNG他 1 件
> 
> これを回避するため、**HTTP接続（27123）に切り替える**のが最も確実です。
> 
> ### 修正手順
> 
> 1.  **Obsidian側でHTTPを有効にする**
>     
>     -   Obsidianを開き、「設定」→ コミュニティプラグイン → **「Local REST API with MCP」** を開きます。
>         
>     -   下の方にある **「Enable non-encrypted (HTTP) server」** のトグルを**オン**にします。
>         
>     -   画面上の `Non-encrypted (HTTP) server` に緑のチェックが付けばOKです。
>         
> 2.  **拡張機能のURLを変更する**
>     
>     -   お送りいただいた設定画面の **「API URL」** の欄を、以下のように書き換えます：
>         
>         PNG
>         
>         Plaintext
>         
>         ```
>         http://127.0.0.1:27123
>         ```
>         
>         *（※ `https` ではなく **`http`**、末尾のポート番号を **`27123`** に変更します）*
>         
> 3.  **設定を保存する**
>     
>     -   画面下部にある保存ボタンをクリックします。
>         
> 4.  **Gemini画面で試す**
>     
>     -   Geminiのタブに戻り、**F5キー（Ctrl + R）でページを再読み込み**します。
>         
>     -   紫の **「Sync」** ボタンを押します。
>         
>     -   Obsidianのフォルダ内に新しいノートが作成されれば成功です。

> [!NOTE] Gemini
> 画像を確認しました。`Non-encrypted (HTTP) server` が緑のチェックになり、ポート `27123` で正常に起動しています。
> 
> PNG
> 
> これでSSL証明書によるブロックを回避できる状態になりましたので、拡張機能側の設定を合わせて同期を完了させます。
> 
> ### ステップ1：拡張機能「Obsidian AI Exporter」の設定を更新する
> 
> 1.  Chrome右上の拡張機能アイコン（パズルマーク）から「Obsidian AI Exporter」の **オプション（設定画面）** を開きます。
>     
> 2.  **API URL** の入力欄を以下のように書き換えます：
>     
>     Plaintext
>     
>     ```
>     http://127.0.0.1:27123
>     ```
>     
>     *（※ `https` ではなく `http`、末尾は `27123` です）*
>     
> 3.  **API Key** の入力欄に、以下のキーを余分な空白なしで貼り付けます：
>     
>     Plaintext
>     
>     ```
>     c03414db220c79f4e2cc652ef87e733295e61aab1ac6dfce25ed9b6c64ef9bb8
>     ```
>     
> 4.  画面下部にある **「Save」**（保存）ボタンをクリックします。
>     
>     -   **確認**: 画面上に「Settings saved」などの保存完了メッセージが出たことを確認します。
>         
> 
> ### ステップ2：ブラウザの通信テスト
> 
> 1.  Chromeで新しいタブを開き、URLバーに以下を入力してEnterを押します：
>     
>     Plaintext
>     
>     ```
>     http://127.0.0.1:27123/
>     ```
>     
> 2.  警告画面が出ずに、JSONの英字メッセージ（`{"status": "OK", ...}`）が表示されれば、ブラウザからObsidianへのHTTP通信ルートは完全に開通しています。
>     
> 
> ### ステップ3：Geminiで同期を実行する
> 
> 1.  Web版Geminiのチャット画面のタブに戻ります。
>     
> 2.  **Ctrl + R（または F5）でページを再読み込み**します。
>     
>     -   ※再読み込みしないと拡張機能側の最新設定が反映されません。
>         
> 3.  画面上に表示される紫色の **「Sync」** ボタンをクリックします。
>     
> 4.  **確認**: Obsidianを開き、Vault内に新しいノートが追加されていれば連携成功です。