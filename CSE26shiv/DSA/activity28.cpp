#include <iostream>
using namespace std;
int main() {
    long long a=0,b=1,n;
    cout<<"enter number of term you need in fibonacci series";
    cin>>n;
    for(int i=1;i<=n;i++){
        cout<<a<<", ";
        b=a+b;
        a=b-a;
    }
}