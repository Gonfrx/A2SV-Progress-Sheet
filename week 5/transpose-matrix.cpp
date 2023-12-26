class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        vector <vector<int>> v; 
        for(int i =0 ; i< matrix[0].size();i++) {
            vector <int> temp; 
            for(auto j: matrix){
                temp.push_back(j[i]); 
            }
            v.push_back(temp); 
        }
        return v; 
    }
};