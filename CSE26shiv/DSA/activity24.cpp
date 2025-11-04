#include <iostream>
using namespace std;
int main() {
    int n,i=2;
    bool check = true;
    cin>>n;
    if(n==1){
        cout<<"not a prime number";
    }
    else if(n==2){
        cout<<"prime number";
    }
    else{
        while(check==true && i*i<=n){
            if(n%i==0){
                check=false;
            } 
            else{
                i++;
            }
        }
        if(check){
            cout<<"prime number";
        }
        else{
            cout<<"not a prime";
        }
    }
}