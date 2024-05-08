#include <bits/stdc++.h>
using namespace std;

int main11(){
string s ="Hello World";
string x="";
string a="";
string o="";

for(char c:s){
    x=x+(char)(c^127);
    a=a+(char)(c&127);
    o=o+(char)(c|127);
}
cout<<x<<endl;
cout<<a<<endl;
cout<<o<<endl;
}
