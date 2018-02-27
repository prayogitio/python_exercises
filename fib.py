def fib(num):
	if (num < 2):
		return num
	if (memo[num] != -1):
		return memo[num]
	else:
		memo[num] = fib(num-1) + fib(num-2)
		return memo[num]

n = input("please input your number: ")
n = int(n)
memo = []
for i in range(0,99):
	memo.append(-1)
print("Hey there.. the result is :", fib(num = n))

print("here's another solution of fibbonaci")
print()
def fibb(n):
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
if __name__ == "__main__":
   f = fibb(100)
   print(f)