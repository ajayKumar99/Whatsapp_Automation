import pywhatkit as kit
import datetime
import schedule
import time

NUMBER = "7829829873"
MESSAGE = "I love you"
INTERVAL = 30

def send_message():
    print('Sending next message in 2 minutes...')
    t = datetime.datetime.now() + datetime.timedelta(minutes=2)
    kit.sendwhatmsg("+91"+NUMBER, MESSAGE, t.hour, t.minute)

schedule.every(INTERVAL).minutes.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)