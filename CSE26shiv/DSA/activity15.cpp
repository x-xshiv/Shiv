#include <iostream>
using namespace std;

int main(){
    float bs,da,hra,gross,pf,net_salary;
    cout<<"Salary Input : ";
    cin>>bs;
    da=0.25*bs;
    hra=0.15*bs;
    gross=bs+da+hra;
    pf=0.10*gross;
    net_salary=gross-pf;
    cout<<net_salary;
}