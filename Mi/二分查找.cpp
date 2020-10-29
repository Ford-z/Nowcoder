/*请实现有重复数字的有序数组的二分查找。
输出在数组中第一个大于等于查找值的位置，如果数组中不存在这样的数，则输出数组长度加一。*/
class Solution {
public:
    /**
     * 二分查找
     * @param n int整型 数组长度
     * @param v int整型 查找值
     * @param a int整型vector 有序数组
     * @return int整型
     */
    int upper_bound_(int n, int v, vector<int>& a) {
        // write code here
        if (a.back() < v){
            return n+1;
        }
        int l=0,r=n-1,m=0;
        while(l<r){
            m=(l+r)/2;
            if(a[m]>=v){
                r=m;
            }
            else{
                l=m+1;
            }
        }
        return l+1;
    }
};
