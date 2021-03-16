from os import path
import requests
import time
import random
import logging

#Variables:
fPath = path.basename(__file__)
fName = path.splitext(fPath)[0]
userAgents = requests.get('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt').content.decode('utf-8').split('\n')
userPlatforms = ('Win32', 'Linux x86_64', 'Linux', 'OpenBSD amd64', 'iPad', 'iPhone', 'Macintosh', 'Android')
userScreens = (360640, 640360, 411731, 731411, 411823, 823411, 320568, 568320, 375667, 667375, 414736, 736414, 375812, 812375, 7681024, 1024768, 10241366, 13661024, 540720, 720540, 1280720, 1600900, 1440900, 1366768, 12801024, 19201080)
userAppName = "Netscape"
userLanguage = "ru-RU"
userColorDepth = 24
logging.basicConfig(format='%(levelname)s: %(asctime)s - %(message)s', level=logging.INFO, handlers=[logging.FileHandler(f'{fName}.log'), logging.StreamHandler()])

#Options:
votes = 1793
timeouts = (5, 25) #min\max
uid = 80

#Programm:
logging.info('Programm Started')
def addVote():
    userAgent = random.choice(userAgents)
    userPlatform = random.choice(userPlatforms)
    userScreen = random.choice(userScreens)
    user = str(userScreen) + str(userColorDepth) + userAppName + userAgent + userLanguage + userPlatform
    res = requests.get('https://konkurs.kuz-edu.ru/index.php?id=9' + '&uid=' + str(uid) + '&key=' + requests.utils.quote(user, safe='') + '&_=' + str(int(time.time())))

    logging.debug(res.cookies)
    if res.content.decode('utf-8') == 'Ваш голос принят!':
        logging.info(f'Ответ сервера: {res.content.decode("utf-8")} | Голосов отправлено: {i} | Осталось отправить: {votes - i}')
        return 1
    else:
        logging.error(res.content.decode('utf-8') + f'\nErrorRequest: {res.request.url}\nГолосов отправлено: {i} | Осталось отправить: {votes - i}')
        return 0

i = 1
while i <= votes:
    if addVote():
        i += 1
    if i > votes:
        break
    time.sleep(random.randint(timeouts[0], timeouts[1]))
# addVote()
logging.info('Programm Finished')