import sys
from random import randint
from mylibs import chk_template

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def expected():
    n = randint(1, 10)
    s = "*"*20+"\n"
    sym = "*"
    if n % 2 == 0:
        sym = "#"
    for i in range(1, n+1):
        s += sym*i+"\n"
    s += "*"*20+"\n"
    print(f"Test Data : {n}")
    return f"{n}", s


chk_template.expected = expected

if __name__ == "__main__":
    root = f"./src/{sys.argv[0].split('_')[-1].split('.')[0]}"
    loops = 10
    if len(sys.argv) == 2:
        loops = int(sys.argv[1])
    chk_template.main(root, 0, loops)
