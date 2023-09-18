import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "instance", ".env")
dotenv.load_dotenv(dotenv_path)


SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY is None:
    SECRET_KEY = "Local Host Secret Key"