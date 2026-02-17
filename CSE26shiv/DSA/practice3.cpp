#include <iostream>
#include <string>
using namespace std;
// int main(){
//     string str1 ={"hello"};
//     string str2 {"joy"};
//     string str3 {str2};
//     string str4 (5,'a');
//     //string str5 (5," shiv"); string not valid
//     cout<<str1<<endl<<str2<<endl<<str3<<endl<<str4;//<<endl<<str5;
//     return 0;
// }

// int main(){
//     string str1={"abcdefgh"};
//     string str2 {str1,1};
//     string str3 {"deepika",2};
//     cout<<str1<<endl<<str2<<endl<<str3;

// }

int main(){
    string str = "hello, world !!";
    str.erase(5,8);
    cout<<str;
    return 0;
}