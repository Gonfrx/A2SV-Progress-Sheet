class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        vector <int> v; 
        int r_sum = 0; 
        int l_sum = 0; 
        int temp = 0;
        for(auto val: nums){
            if(val == 1){
                r_sum++; 
            }
        }
        v.push_back(r_sum); 
        for(int i = 0;i < nums.size();i++) {
            if(nums[i] == 1){
                r_sum -= 1; 
            }
            else{
                l_sum += 1; 
            }
            v.push_back((l_sum + r_sum)); 
        }
        vector<int> v2; 
        int mx = *max_element(v.begin(), v.end()); 
        for(int i = 0;i <v.size();i++){
            if(v[i]==mx)v2.push_back(i); 
        }
        return v2;  
    }
};