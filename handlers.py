from aiogram import Bot, Dispatcher, executor
from config import TOKEN,PAYMENTS_TOKEN
import asyncio
from aiogram.types import PreCheckoutQuery, ContentType, Message
from keyboards import keyboard
from database import PRICE

loop = asyncio.new_event_loop()
bot = Bot(token=TOKEN,parse_mode='HTML')
dp = Dispatcher(bot,loop)


@dp.message_handler()
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           "Welcome to Pokemon NFT", reply_markup=keyboard)

@dp.message_handler(content_types='web_app_data')
async def buy(web_app_message):
    print('buy')
    await bot.send_invoice(web_app_message.chat.id,
                           title='Title',
                           description='Title',
                           provider_token=PAYMENTS_TOKEN,
                           currency='rub',
                           need_email=True,
                           need_phone_number=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice'
                           )

@dp.pre_checkout_query_handler(lambda q: True)
async def check_out(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id,ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(message.chat.id,'Giao dich thanh cong')

def main():
    executor.start_polling(dp)
