class Solution {
public:
    int maxCoins(vector<int>& piles) {
       //1 2 3 4 7 8  
        sort(piles.begin(), piles.end()); 
        int counter = 0;  
        for(int i = piles.size()-2;i > ((piles.size()/3)); i-=2) {
            counter += piles[i]; 
        }  
        counter+= piles[piles.size()/3];
        return counter; 
    }
};