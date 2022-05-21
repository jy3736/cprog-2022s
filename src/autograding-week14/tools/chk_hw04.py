import sys
from random import randint
from mylibs import chk_template
from copy import deepcopy

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def expected():
    dat = [randint(1, 100) for _ in range(randint(5, 15))]
    print(dat)
    idat = " ".join([str(_) for _ in dat])
    dat.sort()
    odat = " ".join([str(_) for _ in dat])
    return idat, odat


chk_template.expected = expected

if __name__ == "__main__":
    root = f"./src/{sys.argv[0].split('_')[-1].split('.')[0]}"
    loops = 10
    if len(sys.argv) == 2:
        loops = int(sys.argv[1])
    chk_template.main(root, 0, loops)
