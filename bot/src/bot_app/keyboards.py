from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_button_der = InlineKeyboardButton('Женский', callback_data='женский')
inline_button_die = InlineKeyboardButton('Мужской', callback_data='мужской')
inline_button_das = InlineKeyboardButton('Средний', callback_data='средний')
inline_kb = InlineKeyboardMarkup()

inline_kb.add(inline_button_der)
inline_kb.add(inline_button_die)
inline_kb.add(inline_button_das)