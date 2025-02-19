#include<iostream>
#include<stdio.h>
using namespace std;
namespace first {
    int x= 1;
}
namespace second {
    int x= 2;
}
int main(){
    int x = 3;
    system("cls");
    cout<<x;
    cout<<"\n"<<first::x;
    cout<<"\n"<<second::x;
    return 0;
}