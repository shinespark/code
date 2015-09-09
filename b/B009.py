# coding: utf-8
import sys
import datetime


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    presenter_num = int(lines[0])
    presenter_lines = lines[1: 1 + presenter_num]

    time_init = '2000-01-01 10:00:00'
    time_format = '%H:%M'

    break_time = 10
    lunch_time = 60
    lunch_start_time = datetime.datetime.strptime('2000-01-01 12:01:00', '%Y-%m-%d %H:%M:%S')
    lunch_flag = False

    start_time = datetime.datetime.strptime(time_init, '%Y-%m-%d %H:%M:%S')

    for i, line in enumerate(presenter_lines):
        presenter_name, presenter_time = line.split()

        end_time = start_time + datetime.timedelta(minutes=int(presenter_time))
        output_string = '%s - %s %s' % (start_time.strftime(time_format), end_time.strftime(time_format), presenter_name)

        print output_string

        # 次回のstart_time計算
        # 発表予定者のトーク終了予定時刻（現在の発表者の終了時刻 + 10分休憩 + 次の発表者の持ち時間）が
        # 12:01 以降になる場合においては、現在のトークが終了後、10分休憩の代わりに1時間のお昼休憩を一度だけとります。
        if presenter_num - 1 == i:
            break

        if lunch_flag:
            start_time = end_time + datetime.timedelta(minutes=break_time)
            continue

        next_presenter_end_time = end_time + datetime.timedelta(minutes=break_time) + datetime.timedelta(minutes=int(presenter_lines[i+1].split()[1]))
        if next_presenter_end_time >= lunch_start_time:
            lunch_flag = True
            start_time = end_time + datetime.timedelta(minutes=lunch_time)
        else:
            start_time = end_time + datetime.timedelta(minutes=break_time)


if __name__ == "__main__":
    main()
