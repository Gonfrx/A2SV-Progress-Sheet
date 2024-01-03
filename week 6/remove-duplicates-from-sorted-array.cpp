class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
     int counter = 1; 
     int l = 0, r = 1; 
     while(r < nums.size()){
         if(nums[l] == nums[r]) r++; 
         else if(nums[l] != nums[r]) {
             l++;swap(nums[l], nums[r]); 
             r++;counter++;  
         }
     }
     return counter; 
    }

    
};