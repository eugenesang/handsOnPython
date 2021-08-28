from math import factorial, pow, sqrt
def contains(array, number):
    for num in array:
        if num==number:
            return True
    return False


#Chapter 1: Elementary set Theory
#  definition 1.1 sets in mathematics are called lists in python universe
# 1.2.2 Rudiments of set theory
#  an item is an element of a set if it is contained in the set

def isElementIn(set, number):
    for num in set:
        if num==number:
            return True
    
    return False


# definition 1.2  an empty set is generaly an empty list
#  definition 1.3 a set A is a subset of another set B if all elements of A are contained in B

def isSubsetOf(subset, set):
    for num in subset:
        if not contains(set, num):
            return False
    return True


# def 1.4 if A is a subset of B and B is a subset of A then A and B are equal
def areEqual(setA, setB):
    if isSubsetOf(setA, setB) and isSubsetOf(setB, setA):
        return True
    else:
        return False


# def 1.5 if A is a subset of B and A is not equal to B then A is properly containes in B
def isProperlyContained(setA, setB):
    if isSubsetOf(setA, setB) and not areEqual(setA,setB):
        return True
    else :
        return False

# fun fact, - though there is no fun in maths - 
# there is only one empty set. try to proof this


# def 1.6 cadiality of a set 
def cadialityOf(setA):
    return len(setA)
# length of a list in python, 
# a singleton set has a length of 1, a finite set has an infinite length

# def 1.7 universal set 
# the set that contains all elements under consideration
# alias universe of discourse or simly the universe

# sets operations 
# 1.  compliment of a set
# is the set of a numbers contained in the universal set but not in the set provided
def setCompliment(universaSet, subSet):
    compliment=[]
    for num in subSet:
        if not contains(universaSet, num):
            compliment.append(num)
    return compliment


# 2. union , 
# is a set that is made when all elements of two or more sets are combined
def union(*array):
    ans=array[0]
    for element in array:
         n=[]
         for num in ans:
            n.append(num)
        
         for number in element:
            if not contains(n, number):
                n.append(number)
         ans=n      
    return ans


# 3. intersection
# a set that contains all elements present in both the sets specified
def intersection(*sets):
    ans=sets[0]
    for n in sets:
        ret=[]
        for number in ans:
            for digit in n:
                if number==digit:
                    if not contains(ret, number):
                        ret.append(number)
        ans=ret
    return ans


# def 1.8 disjoint set, sets that do not intersect
def areDisjoint(*sets):
    array=intersection(sets)
    if len(array)==0:
        return True
    else:
        return True


# 4. set difference, elements contained in set A but not in set B,
def setDifference(setA, setB):
    ans=[]
    for n in setA:
        if not contains(setB, n):
            ans.append(n)
    return ans


# 5. symetric difference of two sets, 
# a list of all elements that are in set A and set B but not in both of them

def symetricSetDifference(setA, setB, universalSet=[]):
    for element in union(setA, setB):
        if not contains(universalSet, element):
            universalSet.append(element)
    ans=setDifference(universalSet,intersection(setA, setB) )
    return ans
# alias boolean difference
def booleanDiference(setA, setB, setU):
    return symetricSetDifference(setA, setB, setU)


# 6. Cartesian Product of sets
# is a set that contains other sets where each set contains all one elment of each set provided
def cartesianProduct(setA, setB):
    ans=[]
    for a in setA:
        for b in setB:
            ans.append([a, b])
    return ans # though this needs some updates to be smarter


# def 1.9 power set, a set of subsets of A is the subset of a;

#1.3 laws of set theory, theoretical and visual representention and proofs of the set theory
## 1.3.1 ven diagriam
## 1.3.2 elements arguements method
#1.4 fundamental counting principle
## 1.4.1 counting and venn diagrams
# 1.5 Real number systems
## 1.1 Neutral  Numbers, unsigned integers zero excluded
## 1.2 Whole numbers, unsigned integers
## 1.3 intgers
## 1.4 rational numbers, its complicated** 
#      if r is a rational number then its a quotient of two integers a/b, 
#           where b!=0 and gcd of a & b =1; 
# 1.5 irrational number, not rational
# 1.6 real number rational or irrational


# chapter 2 - Elementary logic
# true, false, statements and conditions that form the reality. #Beyond the scope of my discussion

#chapter 3, permutation and combination
# basic counting principle[BCP]
# n events are occuring, for each event there are a number of ways that they may occur, the total number of ways all events may occur is n1*n2*n3*...nk
def bCP(*ways): 
    ans=1
    for event in ways:
        ans*=event
    return ans

# arranging letters, using bcp to arrange letters
# question : without repetttition how many three letter words can be formed from A, B,C, D and E

def letterArrangement(string, wordLength):
    n = []
    for el in range(len(string)-wordLength+1, len(string)+1):
        n.append(el)

    return bCP(*n)

# permutation, an odered arrangement of r objects without repetition selected from n distict objects is called a permutation of the n objects taken r at a time
def permutationLength (n,r):
    ans = factorial(n)
    ans/=factorial(n-r)
    return ans

def permute(s, answer='', ans=[]):
    if len(s)==0:
        ans.append(answer)
        return 
    
    for i in range(len(s)):
        ch=s[i]
        left_substr=s[0:i]
        right_substr= s[i+1:]
        rest=left_substr+right_substr

        permute(rest, answer+ch, ans)


def permutation(string):
    num=[]
    permute(string,'',num )
    return num


## example : four positions are to be occupied by a random selection of 20 people without repetition, how many states of candidates are possible, r=4, n=20 answer = 20! / 16! 
## example 2. how many ways can ten poeple sit around a table. n=9, r=8 since we are excluding one psition for a leader and the answe is 9!
def repeatedPermutation(n):
    myMap={}
    if not type(n) == dict:
        for l in n:
            if myMap.__contains__(l):
                myMap[l]+=1
            else:
                myMap[l]=1
    else:
        myMap=n
    numerator=0
    denomenator=1
    for num in myMap.values():
        numerator+=num
        denomenator*=factorial(num)
    return factorial(numerator)/denomenator

