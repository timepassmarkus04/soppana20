from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6701285365:AAEKn6vbsY6D9uFYqYzoE7BO-Wefj-qjtQM")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://marwin2002:marwin2002@cluster0.ajht7rz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
