//write a program to enter 3 persons and print the oldest one
#include <iostream>
using namespace std;
int main(){
    int p1,p2,p3;
    cout<<"enter age of first person :- ";
    cin>>p1;
    cout<<"enter age of second person :- ";
    cin>>p2;
    cout<<"enter age of third person :- ";
    cin>>p3;
    cout<<((p1>p3)?((p1>p2)?"person 1 is oldest":"person 2 is oldest"):((p3>p2)?"person 3 is oldest":"person 2 is oldest"));
}