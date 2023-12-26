class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
       int n = (mat.size() + mat[0].size())-1; 
       vector<int> ans; 
       vector <int> s; 
       int c = 0; 
       for(int i = 0; i < mat[0].size();i++){
           s.push_back(c); 
           c++; 
       }
       for(int i = 0; i < mat.size()-1; i++){
           s.push_back(c); 
           c++; 
       }
       bool flag = false; 
       for(int x = 0;x < s.size();x++){
           vector<int> temp; 
           for(int i = 0;i < mat.size();i++){
               for(int j = 0;j < mat[i].size();j++){
                   if((i+j) == s[x]) temp.push_back(mat[i][j]);  
               }
           }
           if(flag == true){
               for(auto val: temp) ans.push_back(val); 
               flag = false; 
           }
           else{
               for(int m = temp.size()-1; m >= 0; m--)ans.push_back(temp[m]); 
               flag = true;  
           }
       }
       return ans;  
    }
};