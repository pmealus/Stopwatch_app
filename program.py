"""
A simple stopwatch app using datetime module
by Paul Mealus
"""

from datetime import datetime


def main():
    while True:
        print('\nHit Enter to start the stopwatch or "q" to quit...')
        cmd = input()
        if cmd == 'q':
            break
        elif cmd == '':
            print('Starting Timer')
            delt = stopwatch()
            print("Time Elapsed: {} mins {} secs".format(
                delt.seconds//60, delt.seconds % 60))
            continue

        else:
            print("I don't understand '{}', try again".format(cmd))


def stopwatch():

    start = datetime.now()

    while True:

        try:
            now = datetime.now()
            delt = now - start
            if delt.microseconds == 000000:
                print(delt)

            if delt.seconds % 10 == 0 and delt.microseconds == 000000:
                print('Press "Ctrl + C" to stop timer')

        except KeyboardInterrupt:
            return delt


if __name__ == '__main__':
    main()
