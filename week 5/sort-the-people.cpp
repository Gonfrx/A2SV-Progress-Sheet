class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        unordered_map <int, string> mp; 
        for(int i = 0; i < names.size();i++){
            mp.insert({heights[i],names[i]}); 
        }
        for(int i = 0; i < heights.size();i++){
            for(int j = 0; j < heights.size()-i-1; j++){
                if(heights[j] < heights[j+1]) swap(heights[j], heights[j+1]); 
            }
        }
        vector <string> ans; 
        for(auto val: heights){
            ans.push_back(mp[val]); 
        }
        return ans; 
    }
};