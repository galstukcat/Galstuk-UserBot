from pyrogram import Client
import time
import art

api_id = '' # api_id from my.telegram.org
api_hash = '' # api_hash from my.telegram.org

# Создание клиента
app = Client("userbot", api_id, api_hash)

def main():
    art.tprint("Galstuk UserBot")
    print("GitHub: https://github.com/galstukcat/Galstuk-UserBot/")
    with app:
        print("bot started")
        print("chat_list")
        for dialog in app.get_dialogs():
            print(dialog.chat.id, dialog.chat.title)
        chat_id = input("chat_id: ")

        try:
            while True:
                sticker_id = "CAACAgIAAxkBAAEMwxFntz7DUX2d-I_uPpEF6WkFGUIHrgACwmwAAtmluUnvqFWES1kS5zYE" # sticker_id
                app.send_sticker(chat_id, sticker_id)
                print(f"sended to {chat_id}")
                time.sleep(0.8)
        except KeyboardInterrupt:
            print("stop")
        except Exception as e:
            print(f"err: {e}")

if __name__ == "__main__":
    main()
