class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int mx = *max_element(nums1.begin(), nums1.end()); 
        vector<int> v(mx+1, 0); 
        vector<int> ans; 
        for(auto val: nums1) v[val]++; 
        for(int i = 0; i < nums2.size();i++){
            if(nums2[i] <= mx) {
                if(v[nums2[i]] > 0) {
                    ans.push_back(nums2[i]); 
                    v[nums2[i]]--; 
                }
            }
        }   
        return ans; 
    }
};