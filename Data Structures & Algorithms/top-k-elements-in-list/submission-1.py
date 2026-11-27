class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}    # number - freq
        kList = []

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        sortedHashMap = dict(sorted(hashmap.items(), key=lambda x:x[1], reverse = True))

        return list(sortedHashMap.keys())[:k]


            