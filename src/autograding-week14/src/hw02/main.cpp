#include <iostream>
#include <iomanip>

using namespace std;

// 參考 main() 函數補上所需的程式


// ==============================================
// -----vv----- 不得修改『以下』的程式 -----vv-----
// ==============================================

void dump(float dat[], int len)
{
    for (int i = 0; i < len; i++)
    {
        cout << setprecision(4)
             << dat[i] << " ";
    }
    cout << endl;
}

int main()
{
    float arr[100];
    int n;
    int len = 0;
    while (cin >> arr[len++])
        ;
    len--;

    mul(arr, len, 0.5);
    dump(arr, len);
    mul(arr, len, 1.5);
    dump(arr, len);
    mul(arr, len, 0);
    dump(arr, len);

    return 0;
}