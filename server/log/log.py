from dream_main1 import *
import logging
import logging.config

# TODO Log(file save)
# 로그 출력
logger = logging.getLogger()
# 로그의 출력 기준 (DEBUG, INFO, WARNING, ERROR, WARNING)
logger.setLevel(logging.INFO)
# log 출력 포맷
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 기존 log파일에 이어서 출력
file_handler = logging.FileHandler('C:\\vsCode\dream_dream_explan\server\log\\test.log', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# TODO 로그 출력
@app.before_request
def before_request():
    stream_handler = logging.StreamHandler()
    formatter =logging.Formatter('%(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)