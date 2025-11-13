#include <iostream>
using namespace std;
int main(){
    int a[5]={1,2,3,4,5},b[5]={1,2,3,4,5},sum[5];
    for(int i=0;i<5;i++){
        sum[i]=a[i]+b[i];
        cout<<sum[i]<<", ";
    }
}