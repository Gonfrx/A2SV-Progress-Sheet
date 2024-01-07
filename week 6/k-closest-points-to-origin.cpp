class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<pair<int, vector<int>>> v; 
       for(int i = 0; i < points.size();i++) {
 v.push_back({(points[i][0] * points[i][0] + points[i][1] * points[i][1]), {points[i][0], points[i][1]}}); 
       } 
       nth_element(v.begin(),v.begin()+k,v.end()); 
       vector<vector<int>> ans;
       // 18 26 20 
       int i = 0;  
       while(k-- >0){
           ans.push_back(v[i++].second); 
       }
       return ans;  
    }
};