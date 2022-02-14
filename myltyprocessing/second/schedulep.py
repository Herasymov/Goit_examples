import sched
import time
import multiprocessing

def good_luck():
#    schedule.every().day.at("00:00").do(good_luck)
    schedule.every(1).minutes.do(_good_luck)
    while True:
        schedule.run_pending()
        time.sleep(1)

def _good_luck():
    print("Good Luck for Test")


def assistant():
    while True:
        command = input('input: ')
        if command == '1':
            print('is it one')
        elif command.lower() == 'quit':
            return
        else:
            print('is not one')


if __name__ == '__main__':
    jobs = []
    p1 = multiprocessing.Process(target=good_luck)
    jobs.append(p1)
    p1.start()
    assistant()