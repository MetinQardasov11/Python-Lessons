from enumbers import show_more
from datetime import datetime
import time

for _ in range(100):
    current_time = datetime.now()
    hours = str(current_time.hour).zfill(2)
    minutes = str(current_time.minute).zfill(2)
    seconds = str(current_time.second).zfill(2)
    print(show_more(f'{hours}:{minutes}:{seconds}', color='green'))
    print('\n')
    time.sleep(1)