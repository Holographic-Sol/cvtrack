import urllib.request, urllib.error, urllib.parse
import time
import datetime

attempt_int = 0


def funk0():
    global attempt_int
    try:
        date_time_now = datetime.datetime.now()
        url = 'https://www.worldometers.info/coronavirus/'
        print(date_time_now, 'crawling:', url)
        response = urllib.request.urlopen(url)
        webContent = response.read()

        date_time_now = datetime.datetime.now()
        date_time_now_str = str(date_time_now).replace('-', '_')
        date_time_now_str = date_time_now_str.replace(' ', '_')
        date_time_now_str = date_time_now_str.replace(':', '_')
        date_time_now_str = date_time_now_str.replace('.', '_')
        fname = date_time_now_str+'_cvtrack.html'
        print(date_time_now, 'creating:', fname)
        f = open(fname, 'wb')
        f.write(webContent)
        f.close()

        date_time_now = datetime.datetime.now()
        print(date_time_now, 'web page: should be saved')

        attempt_int = 0
    except:
        attempt_int += 1
        date_time_now = datetime.datetime.now()
        print(date_time_now, 'error', attempt_int, ':  waiting 3 seconds before next attempt')
        time.sleep(5)
        funk0()
        pass


while True:
    funk0()
    sl = 3600
    date_time_now = datetime.datetime.now()
    print(date_time_now, 'sleeping:', sl)
    time.sleep(sl)
