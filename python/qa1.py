# print("蘋果的英文?", end="")
# ans = input()

# msg="再接再厲"

#print("好棒棒"if ans.lower().strip() =="apple"or ans=="microsoft" else"再接再厲")
# print("剩下"+str(10)+"個")
# print("嗨!"*5)
# from typing import Type
# val=12
# print(float(val))

# int= 26
# name="Tess"
from typing import SupportsComplex


q_list = ["蘋果的英文?", "一打雞蛋用掉2個,還剩幾個?"]
a_list = ["apple", '10']
score = 0
i = 0
total = len(q_list)

while i < total:
    q = q_list[i]
    a = a_list[i]
    i += 1

    print(q, end='')
    ans = input().lower().strip()

    if ans == a:
        score += 10
        print("好棒")
    else:
        print("再接再厲!!")

    print()

print("總分:", score)


# print("姓名:%s"%name)
# print("姓名:%s"%name,"年紀:%d"%int)
# msg='{0}今年{1}歲。'
# msg=msg.format("Tess",20)
# print(msg)
# print("體積縮小{:.3f}%".format(33.456758))
# print('{:5},{:^8},{:5d}'.format(12,34,56))
# print('{:=^40s}'.format("傳說中的分隔線"))
# print("沒有作品"+"只好作秀")
# print("國中只會考"
# "會考會考的東西")
# print("求知若飢\n虛心若愚")
# print(r"C:\new")
# r=9

# print(f'若半徑={r},圓面積={3.14*r**2}')
# txt="我是分隔線"
# print(f"{txt:=^30}")
# print(id("hello"))
# print(dir(17))
"""
這樣是多行註解
"""
# 這樣是單行註解
