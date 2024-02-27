class MinStack {
public:
    vector <int> nums{}; 
    multiset <int> mp; 
    int temp = 0; 
    MinStack() {
        
    }
    
    void push(int val) {
        nums.push_back(val); 
        mp.insert(val); 
    }
    
    void pop() {
        temp = nums[nums.size()-1]; 
        nums.pop_back();
        auto it = mp.find(temp); 
        if(it != mp.end()) {
            mp.erase(it); 
        }
    }
    
    int top() {
        return nums[nums.size()-1]; 
    }
    
    int getMin() {
        auto it = mp.begin(); 
        return *it; 
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */