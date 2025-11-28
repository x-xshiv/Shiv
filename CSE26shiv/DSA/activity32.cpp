//find largest number in an array
#include <iostream>
using namespace std;
int main() {
    int a[]={2,6,18,197,1092,89,7000,45,3,1,23,56,78,90,34,12,5,400,9999,10000,3456,2345,8765,4321,1111,2222};
    int largest=a[0],n=sizeof(a)/sizeof(int);
    for(int i=1;i<n;i++){
        if(largest<a[i]){
            largest=a[i];
        }
    }
    cout<<"Largest no. : "<<largest<<endl;
}