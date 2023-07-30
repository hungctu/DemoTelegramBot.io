from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData


web_app = WebAppInfo(url='https://hungctu.github.io/')


keyboard = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="📊 Predict", callback_data="predict")],
        [KeyboardButton(text="🛍 Buy",web_app=web_app)],
        [KeyboardButton(text="💰 Sell", callback_data="sell")]
               ],
    resize_keyboard=True
)

# keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[[InlineKeyboardButton(text="📊 Predict", callback_data="predict")],
#                      [InlineKeyboardButton(text="🛍 Buy", web_app=web_app)],
#                      [InlineKeyboardButton(text="💰 Sell", callback_data="sell")]
#                      ]
# )



cb = CallbackData('btn','action')
markup = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton('Buy',callback_data='btn:buy')]]
)