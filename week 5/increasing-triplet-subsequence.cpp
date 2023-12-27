class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        vector<int> win; 
        vector<int> temp ; 
        win.push_back(nums[0]); 
        for(int i = 1; i < nums.size();i++){
            if(win.size()==1){
                if(nums[i] > win[0]) win.push_back(nums[i]); 
                else{
                    win.clear(); 
                    win.push_back(nums[i]); 
                }
            }
            else{
            if(nums[i] > win[1]){
               return true;  
            }
            if(nums[i] > win[0]){
                win[1] = nums[i]; 
            }
            else if(nums[i] < win[0]){
                if(temp.size()==0){
                    temp.push_back(nums[i]); 
                }
                else{
                    if(nums[i] < temp[0]) {
                        temp.clear(); 
                        temp.push_back(nums[i]); 
                    }
                    else{
                        win.clear(); 
                        win.push_back(temp[0]); 
                        win.push_back(nums[i]); 
                    }
                }
            }
            else if(nums[i] == win[0]){
                if(temp.size() == 1){
                    if(nums[i] > temp[0]){
                        win.clear(); 
                        win.push_back(temp[0]); 
                        win.push_back(nums[i]); 
                        temp.clear(); 
                    }
                }
            }

            }
        }
        return false; 
    }
};