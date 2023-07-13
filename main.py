from aiogram import Bot, Dispatcher, types, F,Router
from aiogram.types import ChatJoinRequest , message
from aiogram.filters import Command
from inline import trai_inline, feed_inline, reg_inline, dep_inline
from config import *


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




file_id = None
file_id_2 = None
file_id_3 = None
file_id_4 = None
file_id_5 = None
file_id_6 = None




@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    global file_id
    if file_id is None:
        with open('video1/main_AbOtVDSR.mp4', 'rb') as main:
            message = await bot.send_video(chat_id=message.chat.id,
                                           video=main, 
                                           caption = f"""
Hello {message.from_user.full_name}, My name is Marcos and my team and I have developed a strategy according to which you always win!
We have created a bot according to this strategy so that you can use it and win at any time
To start using the bot, follow 3 simple steps:

1. Create your own gaming account LINK with promo code you will get bonus 500% to first deposit, like if you deposit 1000rs you get 2500rs to your account!
PROMOCODE: https://kzz.kz/6gZgPf 

2. Recharge your account (Minimum 500rs)

3. Send me the screenshot of your account

If you completed these steps just text me and we can start immediately @https://t.me/thakurprbot 👈👈 TEXT ME""",
                        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
                                [types.InlineKeyboardButton(text='⚡️Training⚡️', callback_data='training')],
                                [types.InlineKeyboardButton(text='💣+500%BONUS💣', url='https://kzz.kz/6gZgPf')],
                                [types.InlineKeyboardButton(text='🫂FeedBack🫂', callback_data='feedback')],
                            ]))
            file_id = message.video.file_id
    else:
        try:
            await bot.send_video(chat_id=message.chat.id,
                                           video=file_id, 
                                           caption = f"""
Hello {message.from_user.full_name}, My name is Marcos and my team and I have developed a strategy according to which you always win!
We have created a bot according to this strategy so that you can use it and win at any time
To start using the bot, follow 3 simple steps:

1. Create your own gaming account LINK with promo code you will get bonus 500% to first deposit, like if you deposit 1000rs you get 2500rs to your account!
PROMOCODE: https://kzz.kz/6gZgPf 

2. Recharge your account (Minimum 500rs)

3. Send me the screenshot of your account

If you completed these steps just text me and we can start immediately @https://t.me/thakurprbot 👈👈 TEXT ME""",
                        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
                                [types.InlineKeyboardButton(text='⚡️Training⚡️', callback_data='training')],
                                [types.InlineKeyboardButton(text='💣+500%BONUS💣', url='https://kzz.kz/6gZgPf')],
                                [types.InlineKeyboardButton(text='🫂FeedBack🫂', callback_data='feedback')],
                            ]))
        except:
            with open('video1/main_AbOtVDSR.mp4', 'rb') as main:
                message = await bot.send_video(chat_id=message.chat.id,
                                                    video=main, 
                                                    caption = f"""
Hello {message.from_user.full_name}, My name is Marcos and my team and I have developed a strategy according to which you always win!
We have created a bot according to this strategy so that you can use it and win at any time
To start using the bot, follow 3 simple steps:

1. Create your own gaming account LINK with promo code you will get bonus 500% to first deposit, like if you deposit 1000rs you get 2500rs to your account!
PROMOCODE: https://kzz.kz/6gZgPf 

2. Recharge your account (Minimum 500rs)

3. Send me the screenshot of your account

If you completed these steps just text me and we can start immediately @https://t.me/thakurprbot 👈👈 TEXT ME""",
                        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
                                [types.InlineKeyboardButton(text='⚡️Training⚡️', callback_data='training')],
                                [types.InlineKeyboardButton(text='💣+500%BONUS💣', url='https://kzz.kz/6gZgPf')],
                                [types.InlineKeyboardButton(text='🫂FeedBack🫂', callback_data='feedback')],
                            ]))
                file_id = message.video.file_id
        main.close()
    
@dp.callback_query_handler(lambda c: c.data == 'training')
async def train(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id, '🔥training🔥', reply_markup=trai_inline())






@dp.callback_query_handler(lambda c: c.data == 'feedback')
async def feedback(callback_query: types.CallbackQuery):
    global file_id_2
    if file_id_2 is None:
        with open('video/next1.mp4', 'rb') as next1:
            res = await bot.send_video(chat_id=callback_query.from_user.id, video=next1, reply_markup=types.InlineKeyboardMarkup(
                    inline_keyboard=[
                                        [types.InlineKeyboardButton(text='➡️NEXT', callback_data='NEXT_1')],
                                
                                    ]))
            file_id_2 = res.video.file_id
    else:
        try:
            await bot.send_video(chat_id=callback_query.from_user.id, video=file_id_2, reply_markup=types.InlineKeyboardMarkup(
                    inline_keyboard=[
                                        [types.InlineKeyboardButton(text='➡️NEXT', callback_data='NEXT_1')],                        
                                ]))        
        except:
             with open('video/next1.mp4', 'rb') as next1:
                res = await bot.send_video(chat_id=callback_query.from_user.id, video=next1, reply_markup=types.InlineKeyboardMarkup(
                        inline_keyboard=[
                                            [types.InlineKeyboardButton(text='➡️NEXT', callback_data='NEXT_1')],
                                    
                                        ]))
                file_id_2 = res.video.file_id
        next1.close()






    

@dp.callback_query_handler(lambda c: c.data == 'NEXT_1')
async def feedback(callback_query: types.CallbackQuery):
    global file_id_3
    if file_id_3 is None:
        with open('video/next2.mp4', 'rb') as next2:
            res = await bot.send_video(chat_id=callback_query.from_user.id, video=next2, reply_markup=types.InlineKeyboardMarkup(
                                inline_keyboard=[
                                    [types.InlineKeyboardButton(text='➡️NEXT', callback_data='NEXT_2')],
                                ]))
            file_id_3 = res.video.file_id
    else:
        try:
            await bot.send_video(chat_id=callback_query.from_user.id, video=file_id_3, reply_markup=types.InlineKeyboardMarkup(
                            inline_keyboard=[
                                [types.InlineKeyboardButton(text='➡️NEXT', callback_data='NEXT_2')],
                            ]))
        except:
             with open('video/next2.mp4', 'rb') as next2:
                res = await bot.send_video(chat_id=callback_query.from_user.id, video=next2, reply_markup=types.InlineKeyboardMarkup(
                                    inline_keyboard=[
                                        [types.InlineKeyboardButton(text='➡️NEXT', callback_data='NEXT_2')],
                                    ]))
            
                file_id_3 = res.video.file_id
        next2.close()






    
    

@dp.callback_query_handler(lambda c: c.data == 'NEXT_2')
async def feedback(callback_query: types.CallbackQuery):
    global file_id_4
    if file_id_4 is None:
       with open('video/next3.mp4', 'rb') as next3:    
            res = await bot.send_video(chat_id=callback_query.from_user.id, video=next3, reply_markup=reg_inline)
            file_id_4 = res.video.file_id
    else:
        try:
            await bot.send_video(chat_id=callback_query.from_user.id, video=file_id_4, reply_markup=reg_inline)
        except:
            with open('video/next3.mp4', 'rb') as next3:    
                res = await bot.send_video(chat_id=callback_query.from_user.id, video=next3, reply_markup=reg_inline())
                file_id_4 = res.video.file_id
        next3.close()
                



@dp.callback_query_handler(lambda c: c.data == 'register')
async def register(callback_query: types.CallbackQuery):
    await callback_query.answer()
    with open('photo_2023-07-04_16-29-15.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo,caption='https://kzz.kz/6gZgPf', reply_markup=reg_inline())






@dp.callback_query_handler(lambda c: c.data == 'deposit')
async def watch_video(callback_query: types.CallbackQuery):
    
    
    global file_id_5
    if file_id_5 is None:
        caption = 'Watch this video 👆'
        with open('algoritm.mp4', 'rb') as deposit:
            res = await bot.send_video(callback_query.from_user.id, video=deposit, caption=caption, reply_markup=dep_inline())
            file_id_5 = res.video.file_id
    else:
        try:
            await bot.send_video(callback_query.from_user.id, video=file_id_5, caption=caption, reply_markup=dep_inline())
        except:
             with open('algoritm.mp4', 'rb') as deposit:
                res = await bot.send_video(callback_query.from_user.id, video=deposit, caption=caption, reply_markup=dep_inline())
                file_id_5 = res.video.file_id
        deposit.close()


    # print(res)
    

@dp.callback_query_handler(lambda c: c.data == 'aviator')
async def avi(callback_query: types.CallbackQuery):
    global file_id_6

    if file_id_6 is None:
    
        caption = 'Watch this video 👆'
        with open('video1/how_to_play_сжатое.mp4', 'rb') as aviator:
            res = await bot.send_video(callback_query.from_user.id, video=aviator, caption=caption)
            file_id_6 = res.video.file_id
        
    else:
        caption = 'Watch this video 👆'
        try:
            await bot.send_video(callback_query.from_user.id, video=file_id_6, caption=caption)
        except:
             with open('video1/how_to_play_сжатое.mp4', 'rb') as aviator:
                res = await bot.send_video(callback_query.from_user.id, video=aviator, caption=caption)
                file_id_6 = res.video.file_id
        aviator.close()     




    



if __name__ == "__main__":
    dp.start_polling(skip_updates=True)
    