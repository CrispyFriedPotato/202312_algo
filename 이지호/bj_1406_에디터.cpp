#include <stdcpp.h>
#include <list>
using namespace std;

int main(){
    string first;
    getline(cin,first);

    list<char> first_input;

    for(size_t i=0; i<first.length(); i++){
        first_input.insert(first_input.end(),first[int(i)]);
    }
    list<char>::iterator iter = first_input.end();

    int sent_num;
    cin >> sent_num;
    cin.ignore();

    for(int i=0;i<sent_num;i++){ 
        string input;
        getline(cin, input);
        switch(input[0]){
            case 'L':
                if (iter == first_input.begin())  break;
                else{
                    iter--;
                    break;
                }
            case 'D':
                if (iter == first_input.end()) break;
                else{
                    iter++;
                    break;
                }
            case 'B':
                if (first_input.empty())  break;
                // else if(iter == first_input.end()){ break;}
                else if(iter == first_input.begin()){break;}
                else{
                    iter = first_input.erase(--iter);
                    break;
                }
            case 'P':
                if (iter == first_input.end()){
                    first_input.push_back(input[2]);
                    break;
                }
                else{ 
                    if (iter == first_input.begin()) {
                        first_input.push_front(input[2]); break;
                        }
                    first_input.insert(iter,input[2]); 
                    break;
                }
        }
    }
    
    for(auto i:first_input) cout<<i;
}