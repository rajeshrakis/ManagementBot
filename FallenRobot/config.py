class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 8045459
    API_HASH = "e6d1f09120e17a4372fe022dde88511b"

    CASH_API_KEY = "8PSQY07AG6Y5P6SN"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://arfzmkcz:42i-_S_KvPgvm_soGuX-KbbEbqG5QO-T@raja.db.elephantsql.com/arfzmkcz"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001515341564)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://zewdatabase:ijoXgdmQ0NCyg9DO@zewgame.urb3i.mongodb.net/ontap?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://images.hdqwalls.com/wallpapers/agent-cat-girl-4k-jw.jpg"

    SUPPORT_CHAT = "HeartBeat_Offi"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1281282633  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
