#include <iostream>
using namespace std;
int grt(int arr[],int n);
int main(){
    int x;
    cout<<"enter total number of elements : ";
    cin>>x;
    int y[x];
    cout<<"now enter elements by giving space in each number : ";
    for(int i=0;i<x;i++){
        cin>>y[i];
    }
    cout<<grt(y,0);
}
int grt(int arr[],int n){
    if(arr[n]<arr[n+1]){
        return grt(arr[],)
    }
}
