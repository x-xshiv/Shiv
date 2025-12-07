#include <iostream>
using namespace std;
void p1(int x, int y);
void p2(int n);
int p3(int n);
void p4(int n);
int p5(int n);


int main(){
    while(true){
        int x;
        cout<<"program 1 for compare 2 number\n";
        cout<<"program 2 for odd/even check\n";
        cout<<"program 3 for factorial of a number\n";
        cout<<"program 4 for fibonacci series upto n\n";
        cout<<"program 5 for sum of digits until digit become single\n";
        cout<<"enter 0 for exiting the program : ";
        cin>>x;
        if(x==0){
            return 0;
        }
        else if(x==1){
            int x,y;
            cout<<"enter two numbers : ";
            cin>>x>>y;
            p1(x,y);
        }
        else if(x==2){
            int n;
            cout<<"enter a number : ";
            cin>>n;
            p2(n);
        }
        else if(x==3){
            int n;
            cout<<"enter a number : ";
            cin>>n;
            cout<<p3(n);
        }
        else if(x==4){
            int n;
            cout<<"enter a number of terms: ";
            cin>>n;
            p4(n);
        }
        else if(x==5){
            int n;
            cout<<"enter a number: ";
            cin>>n;
            cout<<p5(n);
        }
        cout<<"\n\n\n";
    }
} 

void p1(int x,int y){
    if(x>y){
        cout<<x<<" is greater than "<<y;
        cout<<x<<" is greater than "<<y;
    }
    else if(x<y){
        cout<<y<<" is greater than "<<x;
    }
    else{
        cout<<x<<" is equal to "<<y;
    }
}

void p2(int n){
    if(n%2==0){
        cout<<n<<" is a even number";
    }
    else{
        cout<<n<<" is a odd number";
    }
}

int p3(int n){
    int fact = 1;
    for(int i=1;i<=n;i++){
        fact *= i;
    }
    return fact;
}

void p4(int n){
    int a=0,b=1,temp;
    cout<<a<<" "<<b<<" ";
    for(int i=3;i<=n;i++){
        temp =a+b;
        cout<<temp<<" ";
        a = b;
        b = temp;
    }
}

int p5(int n){
    int sum;
    do{
        sum=0;
        while(n>0){
            sum += n%10;
            n=n/10;
        }
        n = sum;
    }while(n>9);
    return n;
}