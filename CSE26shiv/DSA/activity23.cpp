//factorial of a number
#include <iostream>
using namespace std;
int main() {
    int factorial = 1,n;
    cin>>n;
    for(int i=1;i<=n;i++){
        factorial *= i;
    }
    cout<<factorial;
}