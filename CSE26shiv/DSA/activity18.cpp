#include <iostream>
using namespace std;
int main(){
    int i=1;
    while(i<=10){
        if(i==7){
            i++;
            continue;
        }
        cout<<i<<endl;
        i++;
    }
    cout<<"now with the help of for loop"<<endl;
    for(i=1;i<=10;i++){
        if(i==7){
            continue;
        }
        cout<<i<<endl;
    }
}