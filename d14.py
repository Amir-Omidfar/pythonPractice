class Difference:
    def __init__(self, a):
        self.__elements = a
	# Add your code here

    '''def computeDifference(self):
        maxDiffArr = [0] * len(a)
        for i in range(len(a)):
            maxDiffArr[i]=0
            for j in range(len(a)):
                if abs(a[i]-a[j]) > maxDiffArr[i]:
                    maxDiffArr[i]=abs(a[i]-a[j])
        return maxDiffArr'''
    def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
