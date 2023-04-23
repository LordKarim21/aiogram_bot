from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from config_data.config import BOT_TOKEN


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
# Объект бота
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()

# Диспетчер
dp = Dispatcher(bot, storage=storage)
