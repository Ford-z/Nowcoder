//给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的）,https://www.nowcoder.com/questionTerminal/9cf027bf54714ad889d4f30ff0ae5481
#include <vector>
#include <algorithm>
using namespace std;
 
class Solution {
public:
    /**
     * return the longest increasing subsequence
     * @param arr int整型vector the array
     * @return int整型vector
     */
    vector<int> LIS(vector<int>& arr) {
        // write code here
        // 第一步：利用贪心+二分求最长递增子序列长度
        vector<int> res;
        vector<int> maxLen;
        if (arr.size() < 1) return res;
        res.emplace_back(arr[0]);  // 注：emplace_back(val)作用同push_back，效率更高
        maxLen.emplace_back(1);
        for (int i = 1; i < arr.size(); ++i) {
            if (arr[i] > res.back()) {
                res.emplace_back(arr[i]);
                maxLen.emplace_back(res.size());
            } else {
                // lower_bound(begin, end, val)包含在<algorithm>中
                // 它的作用是返回有序数组begin..end中第一个大于等于val的元素的迭代器
                int pos = lower_bound(res.begin(), res.end(), arr[i]) - res.begin();
                res[pos] = arr[i];
                maxLen.emplace_back(pos+1);
            }
        }
        // 第二步：填充最长递增子序列
        for (int i = arr.size()-1, j = res.size(); j > 0; --i) {
            if (maxLen[i] == j) {
                res[--j] = arr[i];
            }
        }
        return res;
    }
};
