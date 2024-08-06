from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6701285365:AAGpb6I2yCCZQkuy8lZ4VmDtMpUIX5-6oPg")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority",
)
