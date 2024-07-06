import requests

# LINE Notifyのアクセストークン
access_token = ""

# 送信するメッセージ
message = input('送信するメッセージを入力\n')

# LINE Notifyにメッセージを送信するAPIのURL
api_url = "https://notify-api.line.me/api/notify"

# ヘッダーにアクセストークンを設定
headers = {"Authorization": f"Bearer {access_token}"}

# 送信するデータを作成
data = {"message": message}

# HTTP POSTリクエストを送信
response = requests.post(api_url, headers=headers, data=data)

# レスポンスの確認
print(response.text)
