/*in a university result management system the progam shows*/
#include <iostream>
using namespace std;
int main() {
    int grade;
    cout<<"enter your grades :- ";
    cin>>grade;
    if (grade>=90 && grade<=100){
        cout<<"A";
    }
    else if(grade>=75){
        cout<<"B";
    }
    else if(grade>=60){
        cout<<"C";
    }
    else if(grade>=45){
        cout<<"D";
    }
    else{
        cout<<"Fail";
    }
}