#include <iostream>
using namespace std;
void pattern(int n);
int main() {
    int n;//n number of rows
    cout << "Number of rows = " <<endl;
    cin >> n;
    pattern(n);
    return 0;
}
void pattern(int n){
    for(int i=0 ; i<n ; i++){
        for(int j=0; j<i+1 ;j++ ){cout <<"* " ;}
        cout << "\n";}
}