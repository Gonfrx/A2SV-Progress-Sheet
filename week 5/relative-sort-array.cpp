class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        int mx = *max_element(arr1.begin(), arr1.end());
        vector<int> v(mx+1, 0); 
        for(auto val: arr1){
            v[val]++; 
        }
        vector<int> ans; 
        for(auto val: arr2){
            while(v[val] > 0){
                ans.push_back(val); v[val]--; 
            }
        }
        for(int i =0 ; i < v.size();i++){
            while(v[i] > 0){
                ans.push_back(i); v[i]--; 
            }
        }
        return ans; 
    }
};