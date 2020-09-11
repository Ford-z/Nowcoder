#include<iostream>
using namespace std;

const int maxn=1e5+5;
long long a[maxn];

int main(){
    int t,n;
    cin>>t;
    while(t--){
        cin>>n;
        long long sum=0;
        for(int i=0;i<n;i++){
            cin>>a[i];
            sum+=a[i];
        }
        if(sum%2!=0){
            cout<<"NO"<<endl;/*若为奇数*/
        }
        else{
            long long ans = sum/2;
            long long res = 0;
            bool flag = false;
            int i=0,j=0;
            while(i<n && j<n){
                if(res==ans){
                    flag=true;
                    break;
                }
                else if(res<ans){/*最远处向右滑*/
                    res+=a[j++];
                }
                else{/*最近处向右滑*/
                    res-=a[i++];
                }
            }
            if(flag){
                cout<<"YES"<<endl;
            }
            else{
                cout<<"NO"<<endl;
            }
        }
        }
    return 0;
}
