class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
       int carry = 0; 
       vector<int> v; 
       if( digits[digits.size()-1] == 9){
           carry = 1; v.push_back(0); 
       }
       else{
           digits[digits.size()-1]++; 
           return digits; 
       }
      
        bool flag = true; 
        int k = 0; 
       for(int j = digits.size()-2; j >= 0; j--){

           if(digits[j] == 9){
             v.push_back(0); 
           }
           else{
               flag = false; 
               k = j; 
               digits[j]++; 
               break; 
           }
       } 
       if(flag == false){
           for(int i = k; i >= 0; i--){
               v.push_back(digits[i]); 
           }
       }
       else{
         v.push_back(1); 
       }
       reverse(v.begin(), v.end()); 
       return v; 
    }
};