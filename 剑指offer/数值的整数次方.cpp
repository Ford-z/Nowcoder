/*给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0*/
class Solution {
public:
    double Power(double base, int exponent) {
    double res = 1.0;
    if (base == 0)
        return 0;
    if (exponent == 0)
        return 1;
    if (exponent < 0)
        base = 1.0 / base;
    while (exponent){
        res *= base;
        exponent = (exponent>0) ? (--exponent) : (++exponent);
    }
    return res;
    }
};
