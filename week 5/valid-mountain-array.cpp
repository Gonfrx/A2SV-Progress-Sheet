class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        bool inc = false; 
        bool dec = false; 
        if(arr.size() == 1) return false; 
        for(int i =0; i < arr.size()-1; i++) {
            if(arr[i] < arr[i+1]){
                if(dec == true) return false; 
                inc = true; 
            }
            else if(arr[i] > arr[i+1]){
                if(inc == false) return false; 
                dec = true; 
            }
            else return false; 
        }
        if(dec == false) return false; 
        return true; 
    }
};