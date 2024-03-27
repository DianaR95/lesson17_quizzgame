import logging

import coloredlogs

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s | %(filename)s | %(levelname)s | %line: (lineno)d | %(message)s', level=logging.DEBUG)
coloredlogs.install(level='DEBUG', logger=logger)

if __name__ == '__main__':

    logger.debug("Aici e un debug")
    logger.info("Aici e un infor print")
    logger.warning("Aici e un warning")
    logger.error("Aici e o eroare")