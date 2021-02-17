#include <iostream>
#include <sstream>
using namespace std;

int main(){

    string input; cin >> input;
    char prev = input[0];
    cout << input[0];
    for (int i = 1; i < input.length(); i += 1){
        if (input[i] != prev){
            cout << input[i];
            prev = input[i];
        }
    }



    return 0;
}
