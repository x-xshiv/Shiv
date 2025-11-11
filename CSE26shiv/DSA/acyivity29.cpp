#include <iostream>
using namespace std;
int main() {
    int n,armstrong=0,count=0;
    cout<<"enter a number : ";
    cin>>n;
    int c=n,d=n;
    while(c>0){
        c=c/10;
        count++;
    }
    while(d>0){
        int r=1;
        for(int i=1;i<=count;i++){
            r*=(d%10);
        }
        d/=10;
        armstrong+=r;
    }
    if(n==armstrong){
        cout<<n<<" is a armstrong number.";
    }
    else{
        cout<<n<<"!="<<armstrong;
    }
}