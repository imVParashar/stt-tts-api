# controllers.py
from fastapi import APIRouter
from app.utilities.logger import logger
from app.utilities import response_handler
from app.auth.constants import AuthSuccessMessages
from typing import Dict

# Defining the router 'auth'
router = APIRouter(prefix="/auth")


@router.get("/health")
def health() -> Dict:
    """
    This method is used for health
    check for auth blueprint.
    @return: JSON
    """
    logger.info(AuthSuccessMessages.HEALTH_CHECK_DONE)
    return response_handler.success_response(
        AuthSuccessMessages.HEALTH_CHECK_DONE,
        200
    )
