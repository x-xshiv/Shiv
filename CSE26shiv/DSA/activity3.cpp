#include <iostream>
using namespace std;
int main(){
    int a,b;
    cin>>a>>b;
    cout<<"before\na = "<<a<<"\nb = "<<b<<endl;
    b = b-a;
    a = a+b;
    cout<<"after\na = "<<a<<"\nb = "<<b<<endl;
}