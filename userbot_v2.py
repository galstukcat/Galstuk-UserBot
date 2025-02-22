from pyrogram import Client
import time
import art

api_id = ''  # api_id
api_hash = ''  # api_hash

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

        while True:
            try:
                sticker_id = "CAACAgIAAxkBAAEMwxFntz7DUX2d-I_uPpEF6WkFGUIHrgACwmwAAtmluUnvqFWES1kS5zYE"
                app.send_sticker(chat_id, sticker_id)
                print(f"sended to {chat_id}")
            except Exception as e:
                print(f"err: {e}")
            except KeyboardInterrupt:
                print("stop")

if __name__ == "__main__":
    main()
