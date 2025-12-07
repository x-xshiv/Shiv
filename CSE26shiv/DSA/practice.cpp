
// void modify(int &x,int &y);
// int main(){
//     int a,b;
//     cout<<"enter two number you want to swap : ";
//     cin>>a>>b;
//     cout<<"\n";
//     cout<<"before swap"<<endl;
//     cout<<a<<" "<<b<<endl;
//     modify(a,b);
//     cout<<"after swap"<<endl;
//     cout<<a<<" "<<b;
//     return 0;
// }

// void modify(int &x,int &y){
//     x=x+y;
//     y=x-y;
//     x=x-y;
// }
// int main(){
//     int a=5,*p;
//     cout<<&a<<endl;
//     p=&a;
//     cout<<p<<endl<<*p;
// }
// int factorial(int n, int fact);
// int main(){
//     int n;
//     cout<<"enter a number u want to find factorial of : ";
//     cin>>n;
//     cout<<factorial(n,1);
// }
// int factorial(int n, int fact){
//     if (n>1){
//         fact = fact*n;
//         n--;
//         return factorial(n,fact);}
//     else{
//         return fact;
//     }
// }
// #include <iostream>
// using namespace std;
// int fibonacci(int n,int a,int b){
//     if(n>0){
//         cout<<a<<" ";
//         n--;
//         b=a+b;
//         a=b-a;
//         return fibonacci(n,a,b);
//     }
//     return 0;
// }
// int main(){
//     int n;
//     cin>>n;
//     return fibonacci(n,0,1);
// }
#include <iostream>
#include <cstring>
using namespace std;
// int fibonacci(int n,int a,int b){
//     if(a<=n){
//         cout<<a<<" ";
//         b=a+b;
//         a=b-a;
//         return fibonacci(n,a,b);
//     }
//     return 0;
// }
// int main(){
//     int n;
//     cin>>n;
//     return fibonacci(n,0,1);
// }
int main(){
    char f[20],l[20],fl[40];
    cout<<"enter your full name : ";
    cin>>f>>l;
    cout<<strlen(f)<<" "<<strlen(l)<<endl;
    strcpy(fl,f);
    strcat(fl," ");
    cout<<"my name is : "<<strcat(fl,l);

}