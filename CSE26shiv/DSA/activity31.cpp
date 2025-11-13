#include <iostream>
using namespace std;
int main() {
    int a[2][3],sum=0;
    for(int i=0;i<2;i++){
        for(int j=0;j<3;j++){
            cin>>a[i][j];
            sum+=a[i][j];
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<"sum = "<<sum;
}