#include <iostream>
#include <iomanip>

using namespace std;

// 詳細閱讀 README.md 並參考 main() 函數補上所需的程式

// ==============================================
// -----vv----- 不得修改『以下』的程式 -----vv-----
// ==============================================

int main()
{
    int x, y;

    cin >> x;
    cin >> y;
    cout << setw(5) << x << setw(5) << y << endl;
    myswap(x, y);
    cout << setw(5) << x << setw(5) << y << endl;

    return 0;
}