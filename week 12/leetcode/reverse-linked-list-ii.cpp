/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int length = 1;
    ListNode *curr = new ListNode; 
    ListNode *temp = new ListNode;
    curr = head;
    ListNode *prev = new ListNode;
    prev = head;
    while(length != left){
        prev = curr;
        curr = curr->next;
        length++;
    }

    ListNode *coprev = new ListNode;
    coprev = prev;
    ListNode *cotemp = new ListNode;
    cotemp = curr;


    temp = curr;
    prev = curr;
    while(temp->next != nullptr && length != right) {
        temp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = temp;
        length++;
    }
    ListNode *x = new ListNode;
    x = curr->next;
    curr->next = prev;
    if(left > 1) {
    cotemp->next = x;
    coprev->next = curr;
    }
    else
        {
            cotemp->next = x;
            head = curr;
        }
    return head; 
    
    }
};