#include<iostream>
#include<vector>
#include<deque>
using namespace std;

int slover(vector<int>& h, int k){
    int n=h.size();
    int a[1000][2]={0};/*C++数组初始化值不为0*/
    a[0][0]=a[0][1]=1;
    for(int i=0;i<n;i++){
            for(int j=i-1;j>=0 && j>=i-k;j--){/*从后向前看*/
                if(a[j][0]){/*在不使用机会时能达到*/
                    if(h[i]<=h[j]){
                        a[i][0]=1;
                    }
                    else{
                        a[i][1]=1;
                    }
                }
                if(a[j][1]){/*在使用机会了时看看能不能达到*/
                    if(h[i]<=h[j]){
                        a[i][1]=1;
                    }
                }
            }
    }
    return a[n-1][1];
}

int main(){
    int T;
    cin >> T;
    while (T--){
        int n, k;
        cin >> n >> k;
        vector<int> h(n);
        for (int i=0; i<n; ++i){
            cin >> h[i];
        }
        if (slover(h, k))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
