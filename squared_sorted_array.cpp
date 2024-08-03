#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> result(n);
        int left = 0;
        int right = n - 1;
        int index = n - 1;
        while (left <= right)
        {
            int l_2 = pow(nums[left], 2);
            int r_2 = pow(nums[right], 2);
            if (l_2 > r_2)
            {
                result[index] = l_2;
                left++;
            }
            else
            {
                result[index] = r_2;
                right--;
            }
            index--;
        }
        return result;
    }
};

int main()
{
    Solution solution;
    vector<int> nums = {-4, -1, 0, 1, 3};
    vector<int> result = solution.sortedSquares(nums);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
}