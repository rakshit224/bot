#include<iostream>
#include<string>
using namespace std;
class employee
{
    public:
    string name;
    int age;
    int salary;
    void entry()
    {
        cout<<"enter your name :";
        cin>>name;
        cout<<"enter your age :";
        cin>>age;
        cout<<"enter your salary :";
        cin>>salary;
    }
    void display(){
        cout<<"name :"<<name<<endl;
        cout<<"age :"<<age<<endl;
        cout<<"salary :"<<salary<<endl; 

    }
    
};
int main(){
    employee emp;
    emp.entry();
    emp.display();
    return 0;
    
}