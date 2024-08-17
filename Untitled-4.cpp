#include <iostream>

using namespace std;

int main() {
    int r,c,i,j;
    cout << "enter number or rows : ";
    cin >> r;
    cout << "enter number or columns : ";
    cin >> c;
    float A[r][c],B[r][c];
    for (i=0 ; i<r ; i++){
        for(j=0 ; j<c ; j++){
            cout << "Justice League [" << i+1 << "]" << "[" << j+1 <<"] : ";
            cin >> A[i][j];
        }
    }
    for (i=0 ; i<r ; i++){
        for(j=0 ; j<c ; j++){
            cout << "Villains [" << i+1 << "]" << "[" << j+1 <<"] : ";
            cin >> B[i][j];
        }
    }
    int Justice_League=0,Villains=0;
    for (i=0 ; i<r ; i++){
        for(j=0 ; j<c ; j++){
            if (A[i][j] > B[i][j]){Justice_League++;}
            else if (B[i][j] > A[i][j]){Villains++;}
        }
    }
    if (Justice_League > Villains){cout << "Justice_League";}
    else if (Villains > Justice_League){cout << "Villains";}
    else {cout << "Tie";}
    return 0;}