#include <iostream>
#include <string>
using namespace std;
int main() {
    string str1 = "AB",str2 = "A";
    bool a = (str1>str2),b = (str1<str2),c = (str1==str2);

    std::cout<<a<<b<<c;
    return 0;
}