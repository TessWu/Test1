import time
import sys

ident = 0  # How many spaces to indent. 縮排
identIncresing = True  # Whetehr the identation is increasing or not.

try:
    while True:
        print(" " * ident, end=" ")
        print("********")
        time.sleep(0.1)

        if identIncresing:
            ident = ident+1
            if ident == 20:
                identIncresing = False
        else:
            ident = ident-1
            if ident == 0:
                identIncresing = True

except KeyboardInterrupt:
    sys.exit()
