//小A刚学了二进制，他十分激动。为了确定他的确掌握了二进制，你给他出了这样一道题目：给定N个非负整数，将这N个数字按照二进制下1的个数分类，二进制下1的个数相同的数字属于同一类。求最后一共有几类数字？
#include<iostream>
#include<vector>
using namespace std;
int bin(int num){
    int count=0;
     while(num>0){
        if(num%2==1){
            count++;
        }
         num/=2;
     }
    return count;
}

int main(){
    int T=0;
    cin>>T;
    for(int i=1;i<=T;i++){
        int n=0;
        cin>>n;
        int j=1;
        vector<int>ans(32,0);
        while(j<=n){
            int num;
            cin>>num;
            int a=bin(num);
            ans[a]++;
            j++;
        }
        int sum=0;
        for(int k=0;k<32;k++){
            if(ans[k]!=0){
                sum++;
            }
        }
        cout<<sum<<endl;
    }
    return 0;
}
