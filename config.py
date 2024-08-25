from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7204172210:AAFhbgjtVsmG9Dxx63BJEwhO8sst9lC4JpE")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://devilkingp0404:devilkingp0404@cluster0.iw04afs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
