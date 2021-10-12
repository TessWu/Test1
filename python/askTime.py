# import time
# ticks=time.time()
# print("現在時間:",ticks)
# now=time.localtime(time.time())
# print("本地時間:",now)
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("url",help="https://www.youtube.com/watch?v=FPn3d7_K9e0")

args= parser.parse_args()

print("視訊網址:", args.url)