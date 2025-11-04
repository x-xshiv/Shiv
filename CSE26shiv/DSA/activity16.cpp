#include <iostream>
using namespace std;

int main(){
    int n,palidrome;
    cout<<"enter a 4 digit number : ";
    cin>>n;
    /*palidrome = (n%10)*1000;
    n=n/10;
    palidrome += (n%10)*100;
    n=n/10;
    palidrome += (n%10)*10;
    n=n/10;
    palidrome += n;*/
    palidrome = (n%10)*1000 + ((n/10)%10)*100 + ((n/100)%10)*10 + (n/1000);
    (palidrome==n)?cout<<"is palidrome":cout <<"not a palidrome"<<endl;
    cout<<"reverse of a number is "<<palidrome;
}