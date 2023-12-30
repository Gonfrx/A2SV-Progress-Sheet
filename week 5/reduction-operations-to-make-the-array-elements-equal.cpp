class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end()); 
        vector<int> v(mx+1, 0); 
        for(auto val: nums) v[val]++; 
        int curr = 0, temp = 0; 
        for(int i = v.size()-1; i > 0; i--){
            curr += v[i]; 
            if(v[i] != 0) v[i] = curr; 
        }
        int sm = 0; 
        for(auto val: v ){
            sm += val; 
        } 
        for(auto val: v) {
            if(val != 0) {
                sm -= val; break; 
            }
        }
        return sm;
    }
};