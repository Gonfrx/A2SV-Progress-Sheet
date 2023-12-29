class Solution {
public:
    string sortSentence(string s) {
        multimap <int, string> mp; 
        stringstream ss = stringstream(s); 
        string word = ""; 
        int x = 0; 
        while(ss >> word) {
            x = int(word[word.size()-1]); 
            word.pop_back(); 
            mp.insert({x,word}); 
        }
        string ans = "";
        for(auto val: mp) {
            ans += val.second;
            ans += " "; 
        }
        ans.pop_back(); 
        return ans; 
    }
};