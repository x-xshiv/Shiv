#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int>numbers={1,2,3,4,5};
    int i;
    for (int i=0;i<numbers.size();i++){
        cout<<numbers[i];
    }
    cout<<"\n"<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;
    cout<<"---------------------\n";
    numbers.push_back(6);
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.push_back(7);
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.push_back(8);
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.push_back(9);
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.push_back(10);
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.push_back(11);
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"++++++++++++++++++++++++\n\n";

    cout<<"---------------------\n";
    numbers.pop_back();
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.pop_back();
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.pop_back();
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.pop_back();
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.pop_back();
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;

    cout<<"---------------------\n";
    numbers.pop_back();
    cout<<numbers.size()<<endl;
    cout<<numbers.capacity()<<endl;
}