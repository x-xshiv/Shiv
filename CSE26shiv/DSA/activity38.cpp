#include <iostream>
using namespace std;
float sum(float,float);
float subtract(float,float);
float divide(float,float);
float multiply(float,float);
int remainder(int,int);

int main(){
    cout<<sum(1,2);
    cout<<endl<<subtract(1,2);
    cout<<endl<<divide(1,2);
    cout<<endl<<multiply(1,2);
    cout<<endl<<remainder(1,2);
}

float sum(float a,float b){
    return a+b;
}
float subtract(float a,float b){
    return a-b;
}
float divide(float a,float b){
    return a/b;
}
float multiply(float a,float b){
    return a*b;
}
int remainder(int a,int b){
    return a%b;
}

