#list basics
l=["sanjana","nancy","poonam","bipin"]
print(l)
print(len(l))
diff_data=["sanjana",54,70.15]#differnt data types
print(type(diff_data))
lc=list((1,2,3))# note the double round-brackets for creating using constructor
print(lc)
#list slicing
print(lc[:1])
print(lc[1:])
print(lc[-2])
#in operator
if 1 in lc:
  print("lc 1 exists")
#change valise
lc[1]=15
print(lc)
lc[1:3]=["sanjana","pawar"]
print(lc)
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#insert at given value
thislist.insert(0,"orange")
print(thislist)
#append
thislist.append("appended")
print(thislist)
#extend
l2=["extended","list"]
thislist.extend(l2) # add any iterable
print(thislist)
###################################################################################
#removing list items
###############################################################################3#

# remove : remove given value if multiple occurences the remove the first occurence

thislist.append("apple")
print(thislist)
thislist.remove("apple")
print(thislist)

#pop : removes last item

thislist.pop()
print(thislist)

# del to fel using position
del thislist[1]
print(thislist)

#clear to clear list
# thislist.clear()
# print(thislist)

#loop in list
for i in thislist:
  print(i)

#list comprehensions : List Comprehension offers the shortest syntax for looping through lists:
[print(x) for x in thislist]
[print(x) for x in thislist if "a" in x]

#newlist = [expression for item in iterable if condition == True]
l1=[1,2,3,4,5]
############################
#  sort
##########################
l1.sort(reverse=True)
print(l1)
l1.sort()
print(l1)

#customized sort
def mysort(n):
  return abs(n)

li3=[70,-70,-80,80,50,-40]#stable 
#li3.sort(key=mysort)
#li3.sort(key=mysort,reverse=True)
li3.reverse()
print(li3)
# sort() method is case sensitive, to make it insensitive thislist.sort(key = str.lower)
#######################################
#   copy list
################################################
# method 1
# cp=li3.copy()
# print(cp)
#method 2
cp=list(li3)
print(cp)

#################################################
# join list
#############################################
# 1. append()
# 2. extend()
# 3. +
################################################
cp=cp+li3
cp.append(70)
print(cp)
print(cp.count(70))# count method returns count of element
#############################################
# index
##################################################
print(cp.index(70))
