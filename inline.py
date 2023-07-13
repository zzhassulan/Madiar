from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

# trai_inline = InlineKeyboardMarkup().add(
#       InlineKeyboardButton(text="How to register account⁉️", callback_data='register'),
#       InlineKeyboardButton(text= "How to make deposit⁉️", callback_data = 'deposit' ),
#       InlineKeyboardButton(text= "How to play aviator⁉️", callback_data='aviator')                
# )

def trai_inline():
    return InlineKeyboardMarkup().add(
      InlineKeyboardButton(text="How to register account⁉️", callback_data='register'),
      InlineKeyboardButton(text= "How to make deposit⁉️", callback_data = 'deposit' ),
      InlineKeyboardButton(text= "How to play aviator⁉️", callback_data='aviator')                
)

# feed_inline = InlineKeyboardMarkup(row_width=1).add(
#       InlineKeyboardButton(text="➡️NEXT", callback_data='next1'),
# )

def feed_inline():
    return InlineKeyboardMarkup(row_width=1).add(
      InlineKeyboardButton(text="➡️NEXT", callback_data='next1'),
)

# reg_inline = InlineKeyboardMarkup(row_width=1).add(
#       InlineKeyboardButton(text="🟢REGISTRATION🟢", url='https://kzz.kz/6gZgPf'),
#       InlineKeyboardButton(text= "✅TEXT ME✅", url='https://t.me/thakurprbot' ),
#       InlineKeyboardButton(text= "💣+500% BONUS💣", url= 'https://kzz.kz/6gZgPf')                
# )

def reg_inline():
    return InlineKeyboardMarkup(row_width=1).add(
      InlineKeyboardButton(text="🟢REGISTRATION🟢", url='https://kzz.kz/6gZgPf'),
      InlineKeyboardButton(text= "✅TEXT ME✅", url='https://t.me/thakurprbot' ),
      InlineKeyboardButton(text= "💣+500% BONUS💣", url= 'https://kzz.kz/6gZgPf')                
)

# dep_inline = InlineKeyboardMarkup(row_width=1).add(
#       InlineKeyboardButton(text="💸MAKE DEPOSIT 500RS💸", url='https://kzz.kz/6gZgPf '),
#       InlineKeyboardButton(text= "✅TEXT ME✅", url='https://t.me/thakurprbot' ),
                     
# )
def dep_inline():
    return InlineKeyboardMarkup(row_width=1).add(
      InlineKeyboardButton(text="💸MAKE DEPOSIT 500RS💸", url='https://kzz.kz/6gZgPf '),
      InlineKeyboardButton(text= "✅TEXT ME✅", url='https://t.me/thakurprbot' ),
                     
)
    
