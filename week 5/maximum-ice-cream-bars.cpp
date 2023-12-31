class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
       int mx = *max_element(costs.begin(), costs.end()); 
       vector<int> v(mx+1,0);
       for(auto val: costs)v[val]++;
       int counter = 0, i = 0; 
       while( i < v.size() and coins > 0){
           if(v[i] > 0) {
               while(coins > 0 and v[i] > 0) {
                   coins -= i; 
                   v[i]--; 
                   if(coins >= 0) counter++; 
               }
           }
           i++; 
       }
       return counter; 
    }
};