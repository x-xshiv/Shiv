//reverse of a number
#include <iostream>
using namespace std;
int main(){
    int n,m=0;
    cin>>n;
    while(n>0){
        m=(m+(n%10))*10;
        n=n/10;
    }
    cout<<m/10;
}