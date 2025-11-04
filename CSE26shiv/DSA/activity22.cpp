//write the program to print the multiplication table of a number upto n.
#include <iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    cout<<endl<<"#############################"<<endl;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=10;j++){
            cout<<i<<" "<<"x"<<" "<<j<<" = "<<i*j<<endl;
        }
        cout<<endl<<"#############################"<<endl;
    }
}