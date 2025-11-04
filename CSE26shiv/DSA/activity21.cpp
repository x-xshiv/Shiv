#include <iostream>
using namespace std;
int main() {
    long long n,i=0;
    cin>>n;
    while(n!=0){
    n = n/10;
    i++;
    }
    cout<<i;
}