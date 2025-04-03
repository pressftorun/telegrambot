from datetime import timedelta,datetime
import time
delta=timedelta(datetime.now)
time.sleep(2)
delta2=timedelta(datetime.now)
print(str(delta.total_seconds()-delta2.total_seconds()))