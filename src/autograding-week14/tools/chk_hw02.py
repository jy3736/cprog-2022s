import sys
from random import randint
from mylibs import chk_template
from copy import deepcopy

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def mul(dat):
    datx = []
    dat = [v*0.5 for v in dat]
    datx.append(deepcopy(dat))
    dat = [v*1.5 for v in dat]
    datx.append(deepcopy(dat))
    datx.append([v*0 for v in dat])
    return datx


def expected():
    dat = [randint(1, 100) for _ in range(randint(5, 15))]
    idat = " ".join([str(_) for _ in dat])
    odat = " ".join([str(_) for _ in mul(dat)])
    print(f"Test Data : {idat}")
    odat = "\n".join([" ".join([str(_) for _ in a]) for a in mul(dat)])
    return idat, odat


chk_template.expected = expected

if __name__ == "__main__":
    root = f"./src/{sys.argv[0].split('_')[-1].split('.')[0]}"
    loops = 10
    if len(sys.argv)==2:
        loops = int(sys.argv[1])
    chk_template.main(root, 1, loops)

