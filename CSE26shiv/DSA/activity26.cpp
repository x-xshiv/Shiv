#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    //right triangle * pattern
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            cout<<"* ";
        }
        cout<<endl;
    }
    //right triangle * pattern upside down
    for(int i=n;i>0;i--){
        for(int j=i;j>0;j--){
            cout<<"* ";
        }
        cout<<endl;
    }


    //right triangle number pattern 
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            cout<<j<<" ";
        }
        cout<<endl;
    }
    //right triangle number pattern upside down
    for(int i=n;i>0;i--){
        for(int j=i;j>0;j--){
            cout<<j<<" ";
        }
        cout<<endl;
    }
    
}