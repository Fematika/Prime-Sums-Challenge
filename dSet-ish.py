import math
import time

class UpdateSums():
	def __init__(self, max):
		self.max = max #Max value to iterate to
		self.prePrimes = [2] #All of the primes already calculated
	
	def findPrimes(self, max):
		primes = self.prePrimes #Start off with primes already calculated
	
		if max > primes[len(primes) - 1]: 
			if max / 2 > primes[len(primes) - 1]:
				self.findPrimes(math.ceil(max / 2))
			
			for i in range(primes[len(primes) - 1], max + 1):
				if i % 2 != 0:
					j = 0
					
					while j in range(0, len(primes)):
						a = primes[j]
						
						if i % a == 0:
							break
						
						j += 1
					
					if j == len(primes):
						primes.append(i)
		
		self.prePrimes = primes
		
		return primes
	
	def findSums(self, n):
		sums = []
		a = self.findPrimes(n)
		
		for i in a:
			if n - i > 0:
				sum = [i, n - i]
			
				if n - i in a:
					sums.append(sum)
				
				if n - i > 0:
					b = self.findSums(n - i)
				else:
					b = []
				
				for j in b:
					sum = [i]
					
					for k in j:
						sum.append(k)
					
					sums.append(sum)
					
		return sums
	
	def findDivisors(self, n):
		divisors = []
	
		for i in range(1, math.ceil(n / 2) + 1):
			if n % i == 0:
				divisors.append(i)
		
		return divisors
		
	def isPerfect(self, n):
		a = self.findDivisors(n)
		s = 0
		
		for i in a:
			s += i
		
		if s == n:
			return True
		else:
			return False
	
	def dSets(self, n):
		a = self.findSums(n)
		dSet = []
		
		if n in self.prePrimes:
			dSet.append([n, n])
		
		for i in a:
			s = 1
			
			for j in i:
				s *= j
			
			j = 0
			
			while j in range(0, len(dSet)):
				if dSet[j][0] == s:
					break
				
				j += 1
			if j == len(dSet):
				dSet.append([s , i])
			
		return dSet
	
	def iterate(self, isPrint):
		for i in range(2, self.max + 1):
			a = self.dSets(i)
			
			if isPrint:
				print(i, ":")
				
				for j in a:
					print({j[0] : j[1]}, self.isPerfect(j[0]))

start_time = time.time()
example1 = UpdateSums(40)
example1.iterate(True)
#print("%a: %s seconds" % (a, time.time() - start_time))