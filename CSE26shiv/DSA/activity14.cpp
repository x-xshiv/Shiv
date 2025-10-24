//basic simple calculator using switch case
#include <iostream>
using namespace std;
int main(){
    char ch;
    float x,y;
    cout<<"Calculate: ";
    cin>>x>>ch>>y;
    switch(ch){
        case '+':
        cout<<x+y;
        break;

        case '-':
        cout<<x-y;
        break;

        case '/':
        cout<<x/y;
        break;

        case '*':
        cout<<x*y;
        break;

        case '%':
        cout<<int(x)%int(y);
        break;

        default:
        cout<<"invalid operator";

    }
}