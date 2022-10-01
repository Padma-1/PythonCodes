#given an array of integer nums..A pair (i,j) is called good if nums[i]==nums[j] and i<j. Return the number of good pairs.if nums=[1,2,3,1,1,3]-->(0,3),(0,4),(2,5),(3,4)-->4 are good_pairs
nums=list(map(int,input().split()))
good_pairs=0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]==nums[j] and i<j:
            good_pairs+=1
print(good_pairs)

#python
nums=[1,2,3,1,1,3]
d={}
res=0
for i in nums:
    d[i]=d.get(i,0)+1
for j in d.values():
    res+=(j*(j-1))//2
print(res)

#cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums)
    {
        unordered_map<int,int>dict;
        int n=sizeof(nums),res=0;
        for (auto i:nums)
        {
            dict[i]+=1;
        }
        for (auto j:dict)
        {
            res+=((j.second*(j.second-1))/2);
        }
        return res;

    }
};

            
            
          
