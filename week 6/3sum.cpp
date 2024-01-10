class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
       vector <vector<int>> ans;
       sort(nums.begin(), nums.end());
       if(nums[0] > 0) {
           return {}; 
       }
       if(nums.size() < 3) return {}; 
    int n = nums.size(); 
    int l = 0, r = n-1, curr = 0; 
    int l_p = 0, r_p = 0; 
    bool b = false; 
    for(int i = 0;i < n; i++) {
        l = i+1; 
        r = n-1;
        if(nums[i] > 0) break; 
       if(i > 0 && nums[i] == nums[i-1]) continue; 
        while(r > l) {
           
            if(nums[i] + nums[l] + nums[r] > 0) r--; 
            else if(nums[i] + nums[l] + nums[r] < 0) l++; 
            else if(nums[i] + nums[l] + nums[r] == 0) {
                l_p = l;
                r_p =r;
                ans.push_back({nums[i], nums[l],nums[r]});
                 while(r > l && nums[l] == nums[l_p]) {
                            l++;
                        }
                        while(r > l && nums[r] == nums[r_p]) {
                            r--; 
                        }
            }
        }
      
    }
  
       return ans; 
    }
};