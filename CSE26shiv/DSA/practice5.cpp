#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
int p01();
// int p02();
// int p03();
// int p04();
// int p05();
// int p06();
// int p07();
// int p08();
// int p09();
// int p10();
int main(){
    int i;
    cin>>i;
    char a[100];
    cin.getline(a,100);
    if(i==1){
        return p01();
    }
    // else if(i==2){
    //     return p02();
    // }
    // else if(i==3){
    //     return p03();
    // }
    // else if(i==4){
    //     return p04();
    // }
    // else if(i==5){
    //     return p05();
    // }
    // else if(i==6){
    //     return p06();
    // }
    // else if(i==7){
    //     return p07();
    // }
    // else if(i==8){
    //     return p08();
    // }
    // else if(i==9){
    //     return p09();
    // }
    // else if(i==10){
    //     return p10();
    // }
}
int p01(){
    string str1 = "here we go again!! ";
    string str2(5,'A');
    cout<<str1<<str2<<endl;
    cout<<str1.length()<<endl;
    str1.append(str2);
    cout<<str1<<endl;
    char b[5]={'s','h','i','v','\0'};
    char s[] = "abcdefg";
    for(int i=0;s[i]!='\0';i++){
        cout<<s[i];
    }
    cout<<endl<<s<<b;
    char str3[100];
    cout<<endl<<"enter a string : ";
    cin.getline(str3,100);
    cout<<endl<<str3;
    string str4;
    cout<<endl<<"enter a string : ";
    getline(cin,str4);
    cout<<str4<<endl;
    cout<<strlen(b);
    strcpy(s,b);
    cout<<endl<<s<<b;
    strcat(str3,b);
    cout<<str3<<"\n";

    cout<<strcmp("hello","hello");
    for(char c:str4){
        cout<<c;
    }
    cout<<endl;
    cout<<int('A')<<int('Z');
    cout<<endl<<int('a')<<int('z')<<endl;
    // if("abcd"=="abce"){
    //     cout<<"true0"<<endl;
    // }
    // if("abcd"=="abcd"){
    //     cout<<"true1"<<endl;//true
    // }
    // if("abc">"abce"){
    //     cout<<"true2"<<endl;//true
    // }
    // if("abcd"<"abce"){
    //     cout<<"true3"<<endl;//true
    // }
    // if("ab"<"Ab"){
    //     cout<<"true4"<<endl;
    // }
    // it is a better practice first assign string to string type data other wise it may interpret it as char.
    cout<<(str4.compare("hello"));
    cout<<(str4.substr(3,5));
    cout<<endl<<str4.find("78")<<endl<<str4.find("78",9)<<endl<<str4.rfind("78",9)<<endl<<str4.rfind("78",11);
    string x="hello",y=" My Name is Goyal",z=" shiv";
    x.insert(5,y,0,11);
    x.insert(16,z);
    x.insert(21,y,11,6);
    cout<<x<<endl;
    y.replace(11,6,z,2,3);
    cout<<y<<endl;
    y.erase(8,3);
    cout<<y<<endl;
}
