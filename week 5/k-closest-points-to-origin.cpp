class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<pair<int, int>> v; 
        int distance = 0; 
       for(int i = 0; i < points.size();i++) {
          distance = int((pow(points[i][0],2)+ pow(points[i][1],2)));  
          v.emplace_back(distance, i); 
       } 
       sort(v.begin(), v.end()); 
       //for(auto val: v) cout << val.first<< " "<< val.second << endl; 
       vector<vector<int>> ans; 
       int i = 0;  
       while(k>0){
           k--;  
           ans.push_back(points[v[i].second]);
           i++; 
       }
       return ans;  
    }
};