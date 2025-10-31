#include <iostream>
using namespace std;
int main() {
    long long n,i=1;
    cin>>n;
    while(n>9){
    n = n/10;
    i++;
    }
    cout<<i;
}