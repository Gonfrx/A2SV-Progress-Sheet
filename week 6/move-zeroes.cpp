class Solution {
public:
    void moveZeroes(vector<int>& nums) {
       int l = 0, r= 0; 
      
       while(l < nums.size() && r < nums.size()) {
            if(nums[l]!=0){
                  while(l < nums.size() && nums[l] != 0) l++; 
               }
            if(nums[r] == 0) {
                  while(r < nums.size() && nums[r] == 0) r++; 
               }
            if(l > r) {
               l = r; 
               while(r < nums.size() && nums[r]== 0) r++; 
            }
            if(r < nums.size() && l < nums.size()) 
           {swap(nums[l], nums[r]); l++; r++;} 
       }
    }
};