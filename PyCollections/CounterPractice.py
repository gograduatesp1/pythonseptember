from collections import Counter

#A collection is a container to store different types of objects
#Counters
#OrderedDict - Depricated from 3.8 version dictionary is coming as ordered
#DefaultDict
#chainmap
#namedtuple
#Deque


#Counters -concept
#counter is a subclass of dictionary
# sampledict=dict()
# sampledict['dinesh']="value1"
# sampledict['naveen']='python'
# sampledict['krishna']='scala'
# print(sampledict)

# sampleList=[1,1,1,2,2,3,3,3,3,9]
# #counter with list
# x=Counter(sampleList)
# print(x)
# x.update([9,9,9,9,9,9])
# print(x)
# x.subtract([9,9,9])
# print(x)
# for key,value in x.items():
#     print(key,value)
# print(x.elements())
# for i in x.elements():
#     print(i)
# print(x.most_common(3))

#counter with dictionary
# y=Counter({"A":5,"B":6,"c":2})
# print(y)
# #counter with type
# z=Counter((1,2,3,1,2,3))
# print(z)

# print(Counter(A=3,B=6,C=9))

# def twoSum(nums, target):
#     result = list()
#     for i in range(0, len(nums)):
#
#         for j in range(1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 if (i < j):
#                     return list([i,j])
#
#
#
# twoSum([2,7,11,15],9)
# twoSum([3,2,4],6)
# print(twoSum([3,3],6))


def addTwoNumbers(l1, l2):
        l1=list(reversed(l1))
        l2=list(reversed(l2))
        int1=""
        for i in range(0,len(l1)):
            int1+=str(l1[i])

        int2=""
        for j in range(0,len(l2)):
            int2+=str(l2[j])

        result=int(int1)+int(int2)
        resultList=list()
        for i in str(result):
            resultList.append(int(i))
        print(list(reversed(resultList)))



addTwoNumbers([2,4,3],[5,6,4])
addTwoNumbers([0],[0])
addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])