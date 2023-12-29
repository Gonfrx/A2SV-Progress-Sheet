class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
       int mx = *max_element(nums.begin(), nums.end()); 
       vector<int> v(mx+1,0);
       for(auto val: nums) v[val]++; 
       int curr = 0, temp = 0; 
       for(int i = 0; i < v.size();i++){
           if(v[i] > 0) {
               temp = v[i]; 
               v[i] = curr; 
               curr += temp; 
           }
       } 
       vector <int> ans; 
       for(auto val: nums) {
           ans.push_back(v[val]); 
       }
       return ans;
    }
};