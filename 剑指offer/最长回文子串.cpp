/*对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。
给定字符串A以及它的长度n，请返回最长回文子串的长度。*/

class Palindrome {
public:
    int getLongestPalindrome(string A, int n) {
        // write code here
        int ans=0;
        for(int i=0;i<=n;i++){
            int t=i;
            int temp=0;
            for(int j=0;(i-j)>=0&&(i+j)<=n;j++){
                if(A[i-j]!=A[i+j]){
                    break;
                }
                temp=j*2+1;
            }
            if(temp>ans){
                ans=temp;
            }
            for(int j=0;(i-j)>=0&&(i+j+1)<=n;j++){
                if(A[i-j]!=A[i+j+1]){
                    break;
                }
                temp=j*2+2;
            }
            if(temp>ans){
                ans=temp;
            }
        }
        return ans;
    }
};
