#Q1

def largestnuminlist(list1):
	list1.sort()
	return list1[-1]

#Q2
def secondlargestinlis(list1):
	list2 = list(set(list1))
 
# Sorting the  list
	list2.sort()
	return list2[-2]

#Q3
def splitoddandeven(n):
	for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
	even=[]
	odd=[]
	for j in a:
	    if(j%2==0):
	        even.append(j)
	    else:
	        odd.append(j)
	return even
	return odd
#Q4
def twolistsameornot(list1,list2):
	list1.sort()
	list2.sort()
	if list1 == list2:
		return true
	else:
		return false
#Q5
def unionoftwolis(lis1,lis2):
	final_lis = lis1+lis2
	return final_lis

#Q6
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def  



