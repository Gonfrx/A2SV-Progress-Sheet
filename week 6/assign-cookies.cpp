class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end()); 
        sort(s.begin(), s.end()); 
        if(s.empty() or g.empty()) return 0; 
        int l = g.size()-1, r = s.size()-1, count = 0; 
         while(l > 0 && g[l] > s[r]) {
             l--;
         }
         while(l >= 0 && r >= 0) {
             if(g[l] > s[r]) l--; 
             else {
                 count++; l--; r--; 
             }
         }
         return count; 
    }
};