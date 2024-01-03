class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        //-1, -1, 1, 2,3
        sort(nums.begin(), nums.end()); 
        int l = 0, r= nums.size()-1; 
        int count = 0; 
        while(l < r) {
            if(nums[l] + nums[r] >= target) r--; 
            else {
                count += r - l; l++; 
            }
        }
        return count; 
    }
};