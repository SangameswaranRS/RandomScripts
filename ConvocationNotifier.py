from urllib.request import urlopen
import smtplib,time

UNIVERSITY_FE_URL = "https://annauniv.edu"

GRADUATION_KEY_WORDS =['Graduation Day', 'Convocation Day 2019']


def notificationHandler():
    site_contents = str(urlopen(UNIVERSITY_FE_URL).read())
    found_keywords =  []
    for key in GRADUATION_KEY_WORDS:
        if key in site_contents:
            found_keywords.append(key)
    if len(found_keywords)>0:
        print(found_keywords)
        print('[INFO] Notifying User!')
        smtp_instance = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_instance.starttls()
        smtp_instance.login('xx','xx')
        smtp_instance.sendmail('xx','xx', 'Prescribed Key words found! Head on to the university site')
        smtp_instance.quit()
        print('[INFO] User Notified')
    else:
        print('[INFO] Trying after an hour!')

def entryPoint():
    while(True):
        print('[INFO]'+str(time.asctime(time.localtime(time.time()))) + ' --  Checking for notifications')
        notificationHandler()
        time.sleep(3600)


entryPoint()
