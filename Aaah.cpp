#include <iostream>
using namespace std;

int main(){

    string able; cin >> able;
    string needed; cin >> needed;

    if (able.length() >= needed.length()){
        cout << "go" << endl;
    }
    else {
        cout << "no" << endl;
    }

    return 0;
}
