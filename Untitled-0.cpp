#include <iostream>
using namespace std;
void hello(string);
int main() { 
    string name;
    cout << "what is your name: ";
    getline(cin, name);
    hello(name);
    return 0;}
void hello(string name){
    cout << "hello, " << name <<"!\n";
}