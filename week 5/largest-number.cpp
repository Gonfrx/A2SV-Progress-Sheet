class Solution {
public:
    string largestNumber(vector<int>& nums) {
       for(int i = 0; i < nums.size();i++){
           for(int j = 0; j < nums.size()-i-1;j++){
               string st = to_string(nums[j]); 
               string st1 = to_string(nums[j+1]); 
               if(st+st1 < st1+st) swap(nums[j], nums[j+1]); 
           }
       } 
       string ans = ""; 
       for(auto val: nums){
           ans += to_string(val); 
       }
       if(ans.size() >= 1) {
           if(ans[0] =='0') return "0"; 
       }
       return ans; 
        
    }
};