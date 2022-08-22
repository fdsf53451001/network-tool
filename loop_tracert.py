import os
import schedule
from datetime import datetime

def run():
    print('testing,',datetime.now())
    stream = os.popen('tracert mega.nz')
    outputs = stream.readlines()
    # print(outputs)

    with open('data/tracert_data.txt','a') as f:
        f.writelines(str(datetime.now())+'\n')
        for line in outputs[4:][:-2]:
            f.writelines(line)
        f.writelines('='*60+'\n')

os.makedirs(os.path.dirname('data/'), exist_ok=True)

run()
schedule.every(1).hours.do(run)
while True:
    schedule.run_pending()

