class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int r = numbers.size() - 1; 
        int i = 0; 
        while(i != r) {
            if(numbers[i] + numbers[r] > target)
                r--; 
          else   if(numbers[i] + numbers[r] ==  target) {
              return {i+1, r+1}; 
          }
           else   if(numbers[i] + numbers[r] < target)
               i++; 
        }
        return {0};
    }
};