def Exchangevals():
	val1,val2=val2,val1
	return val1,val2


def positiveornot(n):
	if n>0:
		return positive
	else:
		return negetive


def Numberdivisible(n , k):
	for i in range (1,k):
		if n%k==0:
			return k*i


def Quotientrem(a,b):
	q=a/b
	r=a%b
return q,r


def Printoddnum(n):
	for i in range(1,n):
		if i%n!=0:
			return n


def Sumofdigit(n):
	sum=0
	rem=n%10
	sum+=rem
	n=n/10
return sum

def Smallestdivisor(n):
	return 1

def compute(n):
	a=(n*10)+n
	b=(n*100)+(n*10)+n
	sum=n+a+b
return sum

def Reversenum(n):
	while n!=0:
		digit=n%10
		rev=rev*10+digit
		n=n/10

def AverageOfList(list1[]):
	n=list1.length
	for i in range(1,n):
		sum=sum+list1[i]
	average = sum/n
	return average


def Countdigit(n):
	while n!=0:
		n=n/10
		count=count+1
	return count

def Palindrome(n):

	temp=n
	rev=0
	while(n>0):
	    dig=n%10
	    rev=rev*10+dig
	    n=n//10
	if(temp==rev):
	    ans = "YES"
	else:
	    ans = "NO"
	return ans




