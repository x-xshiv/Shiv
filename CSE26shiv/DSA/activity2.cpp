//write a program to calculate average marks
#include<iostream>
using namespace std;
int main(){
    float a,b,c,d,e,f;
    cin>>a>>b>>c>>d>>e>>f;
    if ((a,b,c,d,e,f) < 101){
    cout<<"total sum : "<<(a+b+c+d+e+f)<<endl;
    cout<<"percentage : "<<(a+b+c+d+e+f)/6<<"%";
    }
    else{
        cout<<"marks should not be greater than maximum marks";
    }
}