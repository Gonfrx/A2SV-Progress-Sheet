class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
    int x = nums.size(); 
     int i = x-1; 
     int j = x-1; 
     if(x == 0)
        return 0; 
    if(x == 1){
        if(val == nums[0]) 
           {
               nums.pop_back();
               return 0; 
           }
        return 1; 
    }
     int count =0; 
     if(nums[i] == val) {
         while(nums[i] == val && i > 0) {
             i--; 
            count++;
         }
         if(i == 0 && nums[i] == val) 
            {
                nums.clear(); 
                return 0; 
            }
     }
     while(i >= 0 && j >= 0) {
         if(nums[j] == val) {
             while(nums[j] == val && j >= 0) {
                j--;
             }
         }
         if(nums[i] != val) {
             i--; 
             continue; 
         }
         if(nums[i] == val) {
             int temp = nums[j]; 
             nums[j] = nums[i]; 
             nums[i] = temp; 
             while(nums[j] == val && j >= 0) {
                j--;
             }
             i--; 
             count++; 
         }
     }
     cout << count; 
     for(int i = 0;i < count; i++) {
         nums.pop_back(); 
     }
     return nums.size();  
    }
};