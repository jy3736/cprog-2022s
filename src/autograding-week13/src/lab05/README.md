## 一維陣列的應用：輸出陣列中排第 `n` 『順位』的整數。

- 解題方式『不可』先將陣列排序。
- 建議函數原型：
```C++
int nthNum(int dat[], int len, ...);
```
- 其他參數請參閱主程式 main() 的使用，提供適當的參數定義。

### 在 Windows 使用簡易測試
```shell
lab05> .\test.ps1
============================================================
Test Data : 93 45 3 52 91 37 87 72 44 59 94
            3 37 44 45 52 59 72 87 91 93 94
============================================================
3
37
45
59
94

lab05> .\test.ps1
============================================================
Test Data : 9 40 72 30 82 60 49 85 96 6 67 55 14 87 90
            6 9 14 30 40 49 55 60 67 72 82 85 87 90 96
============================================================
6
9
49
60
96
```

### 在 Windows 使用自動批閱測試
```shell
lab05> make test
g++ -o main ./main.cpp
python ../../tools/chk_lab05.py
Test Data : 64 98 99 71 12 48 80 29 52 85 22 87 93 94
            [12, 22, 29, 48, 52, 64, 71, 80, 85, 87, 93, 94, 98, 99]
Test Data : 64 99 38 7 75 13 47 16 17 83 23 89
            [7, 13, 16, 17, 23, 38, 47, 64, 75, 83, 89, 99]
Test Data : 96 97 34 4 72 40 12 84 21 54 53 56 27 60 93 94
            [4, 12, 21, 27, 34, 40, 53, 54, 56, 60, 72, 84, 93, 94, 96, 97]
Test Data : 64 65 1 99 7 9 77 14 79 17 18 49 52 25 90 92 31
            [1, 7, 9, 14, 17, 18, 25, 31, 49, 52, 64, 65, 77, 79, 90, 92, 99]
Test Data : 64 2 3 100 69 98 43 85 54 24 57 93 30
            [2, 3, 24, 30, 43, 54, 57, 64, 69, 85, 93, 98, 100]
Test Data : 67 68 39 45 84 52 54 26 59 61
            [26, 39, 45, 52, 54, 59, 61, 67, 68, 84]
Test Data : 32 97 67 100 38 74 43 75 77 45 78 18 21 30 93 62
            [18, 21, 30, 32, 38, 43, 45, 62, 67, 74, 75, 77, 78, 93, 97, 100]
Test Data : 96 33 98 67 37 73 74 10 13 14 55 86 87
            [10, 13, 14, 33, 37, 55, 67, 73, 74, 86, 87, 96, 98]
Test Data : 64 97 66 68 10 44 79 48 47 82 55 54 23 85 59 60 31
            [10, 23, 31, 44, 47, 48, 54, 55, 59, 60, 64, 66, 68, 79, 82, 85, 97]
Test Data : 98 3 67 5 4 41 10 12 46 78 18 22 87 88 59 31
            [3, 4, 5, 10, 12, 18, 22, 31, 41, 46, 59, 67, 78, 87, 88, 98]

測試通過!

3
4
18
41
98
````