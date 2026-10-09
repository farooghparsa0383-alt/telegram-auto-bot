
import os
import json
import urllib.request
import urllib.error

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHAT_IDS = [
    "-1002642313117",
    "-1002842378723",
]

MESSAGE = "اماده پاسخگویی هستیم"


def send_message(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = json.dumps({
        "chat_id": chat_id,
        "text": MESSAGE
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        result = json.loads(response.read().decode("utf-8"))

    if not result.get("ok"):
        raise RuntimeError(f"ارسال به گروه {chat_id} ناموفق بود")

    print(f"پیام به گروه {chat_id} ارسال شد")


def main():
    if not BOT_TOKEN:
        raise RuntimeError("متغیر BOT_TOKEN تنظیم نشده است")

    for chat_id in CHAT_IDS:
        try:
            send_message(chat_id)
        except Exception as error:
            print(f"خطا در گروه {chat_id}: {error}")


if __name__ == "__main__":
    main()
