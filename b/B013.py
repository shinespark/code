# coding: utf-8
import sys
import datetime


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    dummy = '''30 30 10
3
6 0
7 0
8 0'''
    lines = [x.strip('\n') for x in dummy.split('\n')]

    to_paiza, to_gino, to_office = [int(x) for x in lines[0].split()]
    to_station, to_office = to_paiza, to_gino + to_office
    train_num = int(lines[1])
    train_lines = lines[2: 2 + train_num]

    input_time_format = '%Y-%m-%d %H:%M:%S'
    output_time_format = '%H:%M'
    limit_time = datetime.datetime.strptime('2000-01-01 09:00:00', input_time_format)

    catch_wakeup_time = None

    for line in train_lines:
        h, m = [int(x) for x in line.split()]
        train_start_time = datetime.datetime.strptime('2000-01-01 %02d:%02d:00' % (h, m), input_time_format)
        arrive_time = train_start_time + datetime.timedelta(minutes=to_office)
        if arrive_time < limit_time:
            catch_wakeup_time = train_start_time - datetime.timedelta(minutes=to_station)

    print(catch_wakeup_time.strftime(output_time_format))


if __name__ == "__main__":
    main()
