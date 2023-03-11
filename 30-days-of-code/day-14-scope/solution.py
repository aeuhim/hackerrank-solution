class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        min_element = sorted_elements[0]
        max_element = sorted_elements[-1]
        result = abs(min_element - max_element)
        self.maximumDifference = result
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)