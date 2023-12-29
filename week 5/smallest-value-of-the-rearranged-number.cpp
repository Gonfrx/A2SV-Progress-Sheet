class Solution {
public:
    long long smallestNumber(long long num) {
        string s = to_string(abs(num)); 
        if(num >= 0){
            sort(s.begin(), s.end()); 
        }
        else{
            sort(s.begin(), s.end(), greater <int> ()); 
        }
        if(num > 0){
            int index = s.find_first_not_of('0'); 
            swap(s[index], s[0]); 
        }
        if(num < 0) {
            return (-1 * stoll(s)); 
        }
        return stoll(s); 
    }
};