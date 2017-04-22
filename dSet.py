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
				self.findPrimes(math.ceil(max / 2)) #Make sure we don't forget any possible prime divisors
			
			for i in range(primes[len(primes) - 1], max + 1):
				#Begin where we left off
				if i % 2 != 0:
					#Exclude evens
					j = 0 
					
					while j in range(0, len(primes)):
						a = primes[j] #Only search primes for divisors to up speed
						
						if i % a == 0:
							break #Obviously not a prime
						
						j += 1 #To iterate through set and keep track of how many iterations
					
					if j == len(primes):
						primes.append(i) #If it made it through all of the primes
		
		self.prePrimes = primes #Update the primes we've already calculated
		
		return primes #Return it for easy use
	
	def findSums(self, n):
		sums = [] #All of our sums of "n"
		a = self.findPrimes(n) #Search for the primes up to "n" to check forpossible sums
		
		for i in a:
			if n - i > 0:
				#Only if both are positive
				sum = [i, n - i] #Obviously both add up to "n"
			
				if n - i in a:
					sums.append(sum) #Only if "n - i" is prime
				
				if n - i > 0:
					b = self.findSums(n - i) #Look to see if "n - i" can be represented as sum of primes
				else:
					b = [] #No primes for negatives
				
				for j in b:
					sum = [i] #Our value
					
					for k in j:
						sum.append(k) #Our numbers that sum to "n - i"
					
					sums.append(sum) #This is now another sum of primes
					
		return sums #Return it for easy use
	
	def findDivisors(self, n):
		divisors = [] #All of our divisors, not only primem, with 1 but not itself
	
		for i in range(1, math.ceil(n / 2) + 1):
			if n % i == 0:
				divisors.append(i) #If it divides "n", it is a divisor (obviously)
		
		return divisors #Return it for easy use
		
	def isPerfect(self, n):
		a = self.findDivisors(n) #Find the divisors (including "1")
		s = 0 #Our sum
		
		for i in a:
			s += i #Sum 'em up
		
		if s == n:
			return True #If "n" is perfect
		else:
			return False #If it isn't
	
	def dSets(self, n):
		a = self.findSums(n) #Find the sums of prime factors for "n"
		dSet = [] #Our set of numbers
		
		if n in self.prePrimes:
			dSet.append([n, n]) #Make sure to include itself if prime
		
		for i in a:
			s = 1 #Our multiplier
			
			for j in i:
				s *= j #Find the number corresponding with prime divisors
			
			j = 0 #Initialize our variable
			
			while j in range(0, len(dSet)):
				if dSet[j][0] == s:
					break #Remove any repeats
				
				j += 1
			if j == len(dSet):
				dSet.append([s , i]) #Append if unique
			
		return dSet #Return it for easy use
	
	def iterate(self, isPrint):
		for i in range(2, self.max + 1):
			a = self.dSets(i)
			
			if isPrint:
				#Only print if you want to
				print(i, ":")
				
				for j in a:
					print({j[0] : j[1]}, self.isPerfect(j[0]))
					#Iterate through sums, and print their prime divisors and whether they are perfect
#start_time = time.time() <- Timer
example1 = UpdateSums(40) #Our max value
example1.iterate(True) #Iterate and print out values
#print("%a: %s seconds" % (a, time.time() - start_time)) <- Timer
