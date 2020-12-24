import pytz, datetime
import time
import time
import datetime
import pytz
if __name__=="__main__":


    tz = pytz.timezone('Asia/Shanghai') #东八区

    t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

    print(t)