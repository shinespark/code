# coding: utf-8
import sys

lines = [x.strip() for x in sys.stdin.readlines()]
shiire, nama_hanbai, kako_hanbai = [float(x) for x in lines[0].split()]

print(shiire * (100 - nama_hanbai)/100 * (100 - kako_hanbai)/100)
