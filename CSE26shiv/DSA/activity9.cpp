/*You are building a digital calendar app that must correctly calculate the number of days in february.
to do that, you need to know if the entered year is a leap year*/
#include <iostream>
using namespace std;
int main() {
    int year;
    cout<<"Year :- ";
    cin>>year;
    if((year%4==0 && year%100!=0)||(year%400==0)){
        cout<<"Leap Year";
    }
    else{
        cout<<"Not Leap Year";
    }
}