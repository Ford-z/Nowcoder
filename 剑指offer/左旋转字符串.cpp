class Solution {
public:
    string LeftRotateString(string str, int n) {
        string ans=str;
        int m=str.size()-1;
        for(int i=0;i<str.size();i++){
            if(i<str.size()-n){
                ans[i]=str[i+n];
            }
            else{
                ans[i]=str[i+n-m-1];
            }
        }
        return ans;
    }
};
