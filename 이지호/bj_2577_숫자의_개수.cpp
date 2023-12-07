#include <stdcpp.h>
using namespace std;
//13mins
//https://www.acmicpc.net/problem/2493
int main(){
    int a,b,c;
    cin>>a;cin.ignore();cin>>b;cin.ignore();cin>>c;cin.ignore();

    int result = a*b*c;
    vector<int> count(10,0); //[0,0,0,0,0,0,0,0,0,0]
    string str_result = to_string(result);
    int length = str_result.length();

    for(int i=0;i<str_result.length();i++){
        int idx = str_result[i]-'0';
        count[idx]+=1;
    }

    for(int i=0;i<10;i++){
        cout<<count[i]<<"\n";
    }



}