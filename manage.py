from app.configs.factory import create_app
from os import getenv
from dotenv import load_dotenv

load_dotenv()

current_env = getenv("FLASK_ENV")

app = create_app(environment=current_env)

if __name__ == "__main__":
    app.run()

else:
    application = app