/*problem :- a temperature sensor records daily readings. if the temperature is positive,
it means above freezing, if negative it means below freezing, and if zero, its exactly at freezing point*/
#include <iostream>
using namespace std;
int main(){
    int temp;
    cout<<"temperature :- ";
    cin>>temp;
    if (temp<0){
        cout<<"negative";
    }
    else if(temp>0){
        cout<<"positive";
    }
    else {
        cout<<"zero";
    }
}