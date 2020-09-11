#include<iostream>
#include<vector>
#include<deque>
using namespace std;

int main(){
    int T;
    cin >> T;
    while (T--){
        int x,n,m,t;
        cin >> x;
        if(x<10){
            cout<<x<<endl;
        }
        else{
            n=x/9;
            m=x%9;
            if(m!=0){
                cout<<m;
            }
            for(int i=0;i<n;i++){
                cout<<9;
            }
            cout<<endl;
        }
    }
    return 0;
}
