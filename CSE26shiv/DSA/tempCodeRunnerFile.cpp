int factorial(int n, int fact);
int main(){
    int n;
    cout<<"enter a number u want to find factorial of : ";
    cin>>n;
    cout<<factorial(n,1);

}
int factorial(int n, int fact){
    if (n>0){
        fact = fact*n;
        n--;
        factorial(n,fact);}
    else{
        return fact;
    }
}