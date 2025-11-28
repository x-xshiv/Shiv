//matrix multiplication

#include <iostream>
using namespace std;

int matrix(){
    int n1, n2, n3;

    // rows and columns
    cout << "Enter rows and columns for matrix 1 : ";
    cin >> n1 >> n2;
    cout << "Enter columns for matrix 2 (rows are " << n2 << "): ";
    cin >> n3;

    int mat1[n1][n2], mat2[n2][n3];

    // input 1 matrix
    cout << "Enter elements of first matrix:" << endl;
    for (int i = 0; i < n1; i++){
        for (int j = 0; j < n2; j++){
            cin >> mat1[i][j];
        }
    }

    // input 2 matrix
    cout << "Enter elements of second matrix:" << endl;
    for (int i = 0; i < n2; i++){
        for (int j = 0; j < n3; j++){
            cin >> mat2[i][j];
        }
    }    

    // initializing (method 1 time consuming)
    /*for (int i = 0; i < n1; i++)
        for (int j = 0; j < n3; j++)
            result[i][j] = 0;*/

    //initializing and multiplication and output (method 2 less time consuming)
    int result[n1][n3];
    cout << "resultant matrix:" << endl;
    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < n3; j++) {
            result[i][j] = 0;
            for (int k = 0; k < n2; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
            cout << result[i][j] << " ";
        }
        cout<<endl;
    }

    //method 3
    /*int sum;
    cout<<"resultant matrix: "<<endl;
    for (int i = 0; i<n1; i++){
        for(int j = 0; j<n3; j++){
            sum=0;
            for(int k = 0; k<n2; k++){
                sum+=mat1[i][k] * mat2[k][j];
            }
            cout<<sum<<" ";
        }
        cout<<endl;
    }*/

    //output (method 1 time consuming)
    /*cout << "Resultant matrix:" << endl;
    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < n3; j++)
            cout << result[i][j] << " ";
        cout << endl;
    }*/
    int n;
    cout<<"if you want to continue using this program enter 1 else just enter any number or 0: ";
    cin>>n;
    if(n==1){
        return matrix();
    }
    else{
        return 0;
    }
}

int main() {
    matrix();
}