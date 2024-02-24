from loguru import logger

# Configure Loguru to log messages at the "INFO" level and above
logger.add("tictactoe.log", rotation="10 MB", level="INFO")
