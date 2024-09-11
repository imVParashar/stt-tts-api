from fastapi import APIRouter, File, UploadFile
from starlette.responses import FileResponse
from fastapi.responses import JSONResponse

from app.utilities.logger import logger
from app.auth.constants import AuthSuccessMessages
from app.utilities import response_handler
import shutil
import os

# Define the router
router = APIRouter(prefix="/stt_tts")


@router.get("/health")
def health():
    """
    This method is used for health
    check for tts blueprint.
    @return: JSON
    """
    logger.info(AuthSuccessMessages.HEALTH_CHECK_DONE)
    return response_handler.success_response(
        AuthSuccessMessages.HEALTH_CHECK_DONE,
        200
    )


@router.post("/upload_wav")
async def upload_wav(file: UploadFile = File(...)):
    """
    This method receives a .wav file and returns the same file.
    @param file: UploadFile
    @return: FileResponse
    """
    try:
        if file.content_type != "audio/wave":
            return JSONResponse(
                content={"error": "Only .wav files are allowed."},
                status_code=400
            )

        # Save the uploaded file to a temporary location
        temp_file_path = f"/tmp/{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Return the same file as response
        return FileResponse(
            path=temp_file_path,
            filename=file.filename,
            media_type="audio/wav"
        )

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
    finally:
        file.file.close()

# Ensure the temp folder exists
# if not os.path.exists('./temp'):
#     os.makedirs('./temp')
