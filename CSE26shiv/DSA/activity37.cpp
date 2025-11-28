#include <iostream>
using namespace std;
void p1();
void p2();
void p3();
void p4();
void p5();


int main(){
    int n;
    while(true){
        cout<<"for program 1 type 1\n";
        cout<<"for program 2 type 2\n";
        cout<<"for program 3 type 3\n";
        cout<<"for program 4 type 4\n";
        cout<<"for program 5 type 5\n";
        cout<<"for exiting type 0\n";
        cin>>n;
        switch(n){
            case 0:
                return 0;
            case 1:
                p1();
                break;
            case 2:
                p2();
                break;
            case 3:
                p3();
                break;
            case 4:
                p4();
                break;
            case 5:
                p5();
                break;
            default:
                cout<<"invalid program number\n#####################\n#####################\n";
                break;   
        }
        cout<<"\n\n\n";
    }
}


void p1(){
    int x,y;
    char ch;
    cout<<"enter a equation or operation you want to perform :- \n";
    cin>>x>>ch>>y;
    switch(ch){
        case '+':
            cout<<x+y;
            break;
        case '-':
            cout<<x-y;
            break;
        case '*':
            cout<<x*y;
            break;
        case '/':
            if(y==0){
                cout<<"error: zero division !!\n";
            }
            else{
                cout<<x/y;
            }
            break;
        default:
            cout<<"operator should be only +,-,*,/ !!\n";
            break;
    }
}


void p2(){
    int a,x,b,n,y;
    cout<<"enter the value of a,x,b,n respectively";
    cin>>a>>x>>b>>n;
    if(n==1){
        y=a*x%b;
        cout<<"y=a*x%b = "<<y<<endl;
    }
    else if(n==2){
        y=a*x*2+b*2;
        cout<<"y=a*x*2+b*2 = "<<y<<endl;
    }
    else if(n==3){
        y=a-b*x;
        cout<<"y=a-b*x = "<<y<<endl;
    }
    else if(n==4){
        if(b!=0){
            y=a+x/b;
            cout<<"y=a+x/b = "<<y<<endl;
        }
        else{
            cout<<"y=a+x/b = zero division error!!\n";
        }
    }
    else{
        cout<<"invalid value of n or n not 1,2,3,4.\n";
    }
}


void p3(){
    char ch;
    cout<<"enter a alphabet you want to check :\n";
    cin>>ch;
    switch(ch){
        case 'a':
            cout<<ch<<" is vowel\n";
            break;
        case 'e':
            cout<<ch<<" is vowel\n";
            break;
        case 'i':
            cout<<ch<<" is vowel\n";
            break;
        case 'o':
            cout<<ch<<" is vowel\n";
            break;
        case 'u':
            cout<<ch<<" is vowel\n";
            break;
        default:
            cout<<ch<<" is not a vowel\n";
            break; 
    }
}


void p4(){
    int n;
    cout<<"enter a number: ";
    cin>>n;
    bool check =(n%2==0);
    switch(check){
        case true:
            cout<<n<<" is a even number.\n";
            break;
        case false:
            cout<<n<<" is a odd number.\n";
            break;
    }
}


void p5(){
    int n;
    cout<<"areas : \n";
    cout<<"1 for circle/n2 for rectangle or square\n3 for triangle\n4 for trapezium\n";
    cin>>n;
    switch(n){
        case 1:
            float r;
            cout<<"radius : ";
            cin>>r;
            cout<<"area = "<<3.141*r*r<<endl;
            break;
        case 2:
            float l,b;
            cout<<"enter length and breadth: ";
            cin>>l>>b;
            cout<<"area = "<<l*b<<endl;
            break;
        case 3:
            float base,height;
            cout<<"enter base and height: ";
            cin>>base>>height;
            cout<<"area = "<<0.5*base*height;
            break;
        case 4:
            float h,b1,b2;
            cout<<"enter height,base 1, base2: ";
            cin>>h>>b1>>b2;    
            cout<<"area = "<<0.5*(b1+b2)*height;
            break;
        default:
            cout<<"enter a valid number of shape!!\n";
            break;
    }
}

