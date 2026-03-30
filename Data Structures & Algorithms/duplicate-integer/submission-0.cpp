class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> freq;

        for (int num : nums) {
            if (freq.count(num) > 0) {
                return true;
            }
            freq.insert(num);
        }

        return false;
    }
};