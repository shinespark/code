# coding: utf-8
import sys
import re

# 該当IPアドレスを含んでいるかチェック
def isInclude(p, ip_address):
    result = p.match(ip_address)

    # マッチしなければダメ
    if result is None:
        return False

    # マッチ箇所が行頭じゃないならダメ
    if result.start() != 0:
        return False

    return True

def main():
    # 読み取り
    lines = [x.strip() for x in sys.stdin.readlines()]
    search_word = lines[0]
    log_num = int(lines[1])
    log_lines = lines[2: 2 + log_num]

    p = re.compile(search_word)

    for line in log_lines:
        splited_log_line = line.split()
        ip_address = splited_log_line[0]

        # 該当しない行はスルー
        if not isInclude(p, ip_address):
            continue

        access_date = splited_log_line[3].strip('[')
        access_file = splited_log_line[6]

        print ip_address, access_date, access_file


if __name__ == "__main__":
    main()
