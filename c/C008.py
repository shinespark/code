# coding: utf-8
import sys

lines = sys.stdin.readlines()

first_line = lines[0].split()
start_word = first_line[0]
end_word = first_line[1]
target_text = lines[1]

def extraction(target_text):
    start = target_text.find(start_word)
    if start == -1:
        return
    end = target_text.find(end_word, start)
    if end == -1:
        return

    find_text = target_text[start + len(start_word):end]
    if len(find_text) == 0:
        print '<blank>'
    else:
        print find_text

    return extraction(target_text[end + len(end_word):])

extraction(target_text)
