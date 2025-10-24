//if else ladder conditions
#include <iostream>
using namespace std;
int main(){
    int money;
    cout<<"how much money you have :- ";
    cin>>money;
    if (money>=1000){
        cout<<"yayy!! you can enjoy coffee and more in starbucks";
    }
    else if(money>=500 && money<1000){
        cout<<"you can atleat enjoy a cup of coffee in starbucks";
    }
    else{
        cout<<"you need to save more money to enjoy a coffee in starbucks";
    }
}