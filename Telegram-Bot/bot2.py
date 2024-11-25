from flask import Flask, request
import telepot
import urllib3
from mytoken import mytoken
from mtranslate import translate

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (
    urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "BOT"
bot = telepot.Bot(mytoken)
bot.setWebhook("https://thepythonist4.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':  # text bashe
        if msg['text'] == "/start":
            bot.sendMessage(chat_id, "Hello! Welcome to my bot")
        else:
            reply = translate(msg['text'], "fa", "en")  # tarjome har matn daryafti be farsi az englisi
            bot.sendMessage(chat_id, reply)

    else:  # text nabashe
        bot.sendMessage(chat_id, "Only text messages are allowed")


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            handle(update['message'])
        else:
            bot.sendMessage(chat_id, "Only text messages are allowed")
    return "OK"
