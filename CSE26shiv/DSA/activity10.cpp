//whether a number is divisible with both 5 and 11 or not
#include <iostream>
using namespace std;
int main() {
    int N;
    cout<<"Enter a Number : ";
    cin>>N;
    if (N%5==0 && N%11==0){
        cout<<"is Divisible";
    }
    else {
        cout<<"not Divisible";
    }
}