import sys
from random import randint
from mylibs import chk_template

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def dump(dat, wd=5, col=10):
    s = ""
    cnt = 0
    for v in dat:
        s += f"{v:{wd}}"
        cnt += 1
        if cnt % col == 0:
            s += "\n"
    return s


def expected():
    dat = [randint(1, 100) for _ in range(randint(10, 20))]
    print(f"Test Data : {dat}")
    s = dump(dat)
    s += f"\n{dump(dat,3)}"
    s += f"\n{dump(dat,10,3)}"
    sdat = " ".join([str(_) for _ in dat])
    return sdat, s


chk_template.expected = expected

if __name__ == "__main__":
    root = f"./src/{sys.argv[0].split('_')[-1].split('.')[0]}"
    loops = 10
    if len(sys.argv) == 2:
        loops = int(sys.argv[1])
    chk_template.main(root, 0, loops)
