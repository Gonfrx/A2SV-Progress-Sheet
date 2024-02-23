class Solution {
public:
    int maxVowels(string s, int k) {
        int count=0,  maxi = 0, n = s.size(); 
        int mini = 0, j =0; 
        char first = s[j]; 
        for(int i =0;i < n ;i++) {
            if(mini < k) {
            if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' ){
                mini++;
            
                count++;}
            else { 
                mini++; 
            }
            }
         else  if(mini == k) {
                maxi = max(count , maxi); 
                first = s[j];  
                if(first == 'a' or first== 'e' or first == 'i' or first  == 'o' or first == 'u') count--; 
                if(s[i]  == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u') count++; 
                j++; 
            }
        }
        maxi = max(count, maxi); 
        return maxi; 

    }
};