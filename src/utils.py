"""Model containing shared useful functions"""

import logging

from fastapi.responses import JSONResponse


def respond(status: int, detail: str, message: str, log_level: str = "error"):
    """

    Args:
        status (int): status code
        detail (str): detail
        message (str): message
        log_level (str): log level (e.g., 'debug', 'info', 'warning', 'error','critical')


    Returns:
        JSONResponse: response
    """
    # q: change below logging to olazy formating %
    log_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    logging.log(log_map.get(log_level, logging.ERROR), "%s: %s", message, detail)

    return JSONResponse(
        status_code=status,
        content={"status code": status, "message": message, "detail": detail},
    )
