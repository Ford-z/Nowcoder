/*链接：https://ac.nowcoder.com/acm/contest/9715/A
来源：牛客网

牛牛想知道在[0,n][0,n]范围中，选取一个最大的数xx，满足x \% a = bx%a=b，不过这个范围可能会很大，牛牛不知道该如何解决，所以他想请你帮忙。
给定如上所述的a , b , na,b,n，返回满足条件的最大的xx。*/
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 返回满足条件的最大的x。
     * @param a int整型 代表题意中的a
     * @param b int整型 代表题意中的b
     * @param n int整型 代表题意中的n
     * @return int整型
     */
    int solve(int a, int b, int n) {
        // write code here
        if(n>a+b){
            int t=a+b;
            int ans=(n-t)/a;
            return ans*a+t;
        }
        else if(n==a+b){
            return n;
        }
        else{
            return 0;
        }
    }
};
