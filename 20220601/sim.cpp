
/*Time: O(length of string * T), Mem: O(length of string)
*/
#include <bits/stdc++.h>
using namespace std;

int T;
list<char> l;
string user_i;
int main(){
    cin >> T;
    cin.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' ); // clear the \n from the input buffer before using getline
    for (int tc=0;tc<T;tc++){
        getline(cin,user_i);
        
        list<char>::iterator it = l.begin();
        for (int i=0;i<user_i.length();i++){
            //cout << i << endl;
            if (user_i[i] == ']'){
                it = l.end();
            }
            else if (user_i[i] == '['){
                it = l.begin();
            }
            else if (user_i[i] == '<'){
                list<char>::iterator temp = it;
                temp--;
                if (temp == --l.begin())continue;
                l.erase(temp);
            }
            else{
                l.insert(it, user_i[i]);
            }
            //for(auto i: l){cout << i;}cout << endl;
        }
        for(auto i: l){cout << i;}cout << endl;
        l.clear();
        
    }
    
    return 0;
}