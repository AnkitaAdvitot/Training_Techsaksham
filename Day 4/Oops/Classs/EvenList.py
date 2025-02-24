class EvenList:
    def __init__(self,nums):
        self.nums=nums
    def display_even(self):
        for i in self.nums:
            if i%2==0:
                print(i,end=" ")

even=EvenList([10,20,30,17,334,21])
even.display_even()