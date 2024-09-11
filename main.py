from app import create_app
from config import PORT, HOST
from app.utilities.logger import logger
from uvicorn import run

# Creating the app
app = create_app()

if __name__ == "__main__":
    logger.info(f"App started successfully on - {HOST}:{PORT}")

    # Running the app
    run("main:app", host=HOST, port=PORT, log_level="info")
