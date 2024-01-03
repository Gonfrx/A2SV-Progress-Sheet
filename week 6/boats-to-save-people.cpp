class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end()); 
        
        int l = 0, r = people.size()-1, counter = 0;  
        while(l != r && l < r) {
            if(people[l] + people[r] > limit) {
                r--; counter++; 
            }
            else if(people[l] + people[r] <= limit) {
                l++; r--; counter++; 
            } 
        }
        if( l == r) counter++; 
        return counter; 
    }
    
};