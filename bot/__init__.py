import logging, os, sys, time
import telegram.ext as tg


StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)


# if version < 3.9, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 9:
    LOGGER.error(
        "You must have a python version of at least 3.9! Multiple features depend on this. Bot quitting."
    )
    sys.exit()

TOKEN = os.environ.get("TOKEN")
else:
    TOKEN = "secrets.TOKEN"

WORKERS = 8

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)

dispatcher = updater.dispatcher

updater.start_polling()
