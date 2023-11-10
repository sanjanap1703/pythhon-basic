#cannot modify tuple
# duplicates allowed
#ordered and indexed
t1=(1,2,3,4)
print(t1)
print(len(t1))
print(t1[-3])
print(t1[-3:])
if 4 in t1:
    print("4 is present")
######################################################
# modification : perform on list
#$########################################################
'''Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)
######################################################################################################################
# unpacking tuple : (v1,v2,........vn)=tuple_var
###############################################################################################################
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
##################################################################################
# asterisk : Using Asterisk* If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
############################################################################
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
##################################################################################
# join tuples : +
# multiply tuples : *
#################################################################################
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple3=tuple3*3;
print(tuple3)