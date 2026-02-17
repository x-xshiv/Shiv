#include <iostream>
#include <string>
using namespace std;
class student{
    public:
    int roll;
    string name;
    void roll_no(){
        cout<<"your roll no. is "<<roll;
    }
    void names(){
        cout<<"your name is "<<name;
    }
};
int main(){
    student s;
    s.roll=43;
    s.name="shiv";
    s.roll_no();
    cout<<endl;
    s.names();
}