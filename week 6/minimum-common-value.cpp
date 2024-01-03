class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int f = 0, s = 0; 
        long long mn = 10e10; 
        while(f < nums1.size() && s < nums2.size()){
           if(nums1[f] < nums2[s]) f++; 
           else if(nums1[f] > nums2[s]) s++; 
           else { 
               mn = min(mn, static_cast<long long>(nums1[f]));f++;s++; 
           }
        }
        if(mn == 10e10) return -1; 
        return mn; 
    }
};