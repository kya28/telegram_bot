from aiogram.contrib.fsm_storage.memory import MemoryStorage
from . local_settings import API_KEY
from aiogram import Bot, Dispatcher

bot = Bot(token=API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())


