class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
       sort(tasks.begin(), tasks.end()); 
       sort(processorTime.begin(), processorTime.end()); 
       int mx = 0, c = 0, counter = 0, j = 0; 
       for(int i = tasks.size()-1; i >=0 ;i--){  
             counter += 1; 
             c = max(c, tasks[i]);  
             if(counter == 4) {
                 mx = max(processorTime[j] + c, mx); 
                 counter = 0; 
                 c = 0; j++; 
             } 
         }
         return mx; 
    }
};