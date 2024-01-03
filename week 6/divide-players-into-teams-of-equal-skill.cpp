class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
       sort(skill.begin(), skill.end()); 
       int l = 0, r = skill.size()-1; 
       long long count = 0, mx = 0; 
       mx = skill[l] + skill[r]; 
       while(l < r) {
           if(skill[l] + skill[r] != mx)return -1; 
           count += skill[l] * skill[r]; 
           l++; r--; 
       }
       return count;
    }
};