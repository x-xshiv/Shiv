#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

class Employee{
    public:
    string name;
    int id;
    string getname(){
        return name;
    }
    int getid(){
        return id;
    }
};

class Student{
    int roll;
    string name;
    public:
    //constructor
    Student(string name, int roll ){
        this->name = name;
        this->roll = roll;
    }
    // getter method 
    string getname(){
        return name;
    }
    int getroll(){
        return roll;
    }

    //setter method
    void setname(string name){
        this->name = name;
    }
    void setroll(int roll){
        this->roll = roll;
    }

    //instance method
    void displaydetails(){
        cout<<"student name : "<<name<<endl;
        cout<<" roll number : "<<roll<<endl;
    }

};

class Vehicle {
    public:
    // abstract method (pure virtual function)
    virtual void accelerate() = 0;
    virtual void brake() = 0;
    void startengine(){
        cout<<"Engine Started !!"<< endl;
    }
};
class Car : public Vehicle {
    string carname;
    public:
    //construct method
    Car(string carname){
        this->carname = carname;
    };
    //implement abstract method 
    void accelerate() override {
        cout<<carname<<" : pressing gas pedal....."<<endl;
    }
    void brake() override {
        cout<<carname<<" : applying brakes......."<<endl;
    }
};

class Animal{
    public:
    virtual void speak() = 0;
    void sleep(){
        cout<<"animal is sleeping"<<endl;
    }
    void eat(){
        cout<<"animal is eating"<<endl;
    }
};

class Cat : public Animal{
    private:
    string type;
    public:
    Cat(string type){
        this->type = type;
    }
    void speak() override{
        cout<<type<<" is meowing !!"<<endl;
    }
};

class Dog : public Animal{
    private:
    string type;
    public:
    Dog(string type){
        this->type = type;
    }
    void speak() override{
        cout<<type<<" is barking !!"<<endl;
    }
};



int main(){
    Employee emp1;
    emp1.name = "Shiv Goyal";
    emp1.id = 101;
    cout<<"emp1 name is "<<emp1.getname()<<" and id is "<<emp1.getid()<<endl;
    Student student1("shiv",1072);
    student1.displaydetails();
    Student student2("shiv",1072);
    student2.setname("kanav");
    student2.setroll(1077);
    student2.displaydetails();  
    Vehicle* mycar1 = new Car("mustang");
    mycar1->startengine();
    mycar1->accelerate();
    mycar1->brake();
    Vehicle* mycar2 = new Car("toyota");
    mycar2->startengine();
    mycar2->accelerate();
    mycar2->brake();
    Animal* cat1 = new Cat("kitty");
    Animal* dog1 = new Dog("puppy");
    cat1->eat();
    cat1->sleep();
    cat1->speak();
    dog1->eat();
    dog1->sleep();
    dog1->speak();
}
