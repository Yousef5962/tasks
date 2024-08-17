#include <iostream>

using namespace std;

int main() {
    int i;
    cout << "Number of elements = ";
    cin >> i;

    float f[i];

    for (int j = 0; j < i; j++) {
        cout << "Element [" << j  << "]: ";
        cin >> f[j];
    }

    cout << "what is your target ? : ";
    int target;
    cin >> target;
    int index = -1;
    for (int j = 0; j < i; j++) {
        if (f[j]==target){
            index=j;
            break;}
    }
    cout << "target located at index : " <<index<<endl;
    return 0;
}
