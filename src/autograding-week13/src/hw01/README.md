## 函數重載(Function Overloading)：以參數的(奇/偶)數，使用(*/#)繪製直角三角形圖。

- 請參閱主程式的函數使用方式，設計夠用的『重載』函數 drawLine(...)。
- 本題的解答方式『不可』使用內定參數(Default Parameters)。

### 在 Windows 使用簡易測試
```shell
hw01> .\test.ps1
Test Data : 4

********************
#
##
###
####
********************

hw01> .\test.ps1
Test Data : 6

********************
#
##
###
####
#####
######
********************

hw01> .\test.ps1
Test Data : 7

********************
*
**
***
****
*****
******
*******
********************
```

### 在 Windows 使用自動批閱測試
```shell
hw01> make test
g++ -o main ./main.cpp
python ../../tools/chk_hw01.py
Test Data : 3
Test Data : 6
Test Data : 6
Test Data : 5
Test Data : 7
Test Data : 8
Test Data : 2
Test Data : 9
Test Data : 3
Test Data : 7

測試通過!

********************
*
**
***
****
*****
******
*******
********************
```

