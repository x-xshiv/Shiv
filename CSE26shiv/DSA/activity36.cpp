#include <iostream>
using namespace std;
int main() {
    int n;
    cout<<"enter no. of rows in nxn matrix : ";
    cin>>n;
    cout<<"enter elements of matrix : "<<endl;
    int mat[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>mat[i][j];
        }                                                                               
    }
    int det=0;
    if(n==2){
        det=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0];
    }
    else if(n==3){
        for(int i=0;i<n;i++){
            
        }
    }
}
