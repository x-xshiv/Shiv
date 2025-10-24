//to check whether a user is applicable to vote or not
#include <iostream>
using namespace std;
int main() {
    int age;
    cout<<"enter the age :- ";
    cin>>age;
    if(age>=18){
        cout<<"you are applicable to vote";
    }
    else{
        cout<<"you cant vote yet";
    }
}