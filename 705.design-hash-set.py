#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet(object):
    capacity = 10007 


    def __init__(self):
        self.list = [None for _ in range(self.capacity)]

    def hash(self, key):
        return key % self.capacity

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self.hash(key)


        if not self.list[idx]:
            self.list[idx] = [key]
        elif key not in self.list[idx]:
            self.list[idx].append(key)

        
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self.hash(key)
        if self.list[idx] and key in self.list[idx]:
            self.list[idx].remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        idx = self.hash(key)
        if self.list[idx]:
            return key in self.list[idx]
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

