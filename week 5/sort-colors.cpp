class Solution {
public:
    void sortColors(vector<int>& nums) {
      //for the most optimal approach we must use Dutch national flag algorithm
      // it is a way of sorting an array with only 3 distinct values.
      // use three pointers low high and mid where low will be at the first element
      // high in the last element and mid initially at the first element
      int low = 0, mid = 0, high = nums.size()-1; 
      while(mid <= high) {
         // the point is zero's before 'low'  
          if(nums[mid] == 0) {
              swap(nums[mid], nums[low]); 
              mid++; low++;  
          }
          // two's after high
          else if(nums[mid] == 2) {
              swap(nums[mid], nums[high]); 
              high--;
          }
          //don't touch the ones
          else mid++;
      }
    }
};