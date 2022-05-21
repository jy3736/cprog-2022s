#include <iostream>
#include <iomanip>

using namespace std;

// 參考 main() 函數補上所需的程式

void reverse(int dat[], int len) {
    for(int i=0; i<len/2; i++) {
        swap(dat[i],dat[len-i-1]);
    }
}

// ==============================================
// -----vv----- 不得修改『以下』的程式 -----vv-----
// ==============================================


int main()
{
    int arr[100];
    int i = 0;
    while(cin>>arr[i++]);
    i--;
    reverse(arr,i);
    dump(arr,i);

    return 0;
}