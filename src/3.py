# Take the number that you need to factorize, find all numbers less than its
# square root that divide it completely (remainder == 0)
# this gives you a list of divisors, to find prime factors:
#   order the divisors, and check if any of the divisors is divided by another
#   divisor less than it
#   If it is, then it is not prime so you generate a new list that is without
#   that number
#   Recursively do this, until the length of the divisor list does not reduce 
#   this means all the divsors are mutually indivisible, which is the condition
#   to be prime
import math 

def sieve(factor_list: set):
    factor_list = sorted(list(factor_list))
    print(factor_list)
    sieve_2 = set(
        [p for i,p in enumerate(factor_list) 
               for t in factor_list[1:i] 
               if p%t==0] 
    )
    print(sieve_2)
    reduced_in_size = len(factor_list)>len(sieve_2)
    return reduced_in_size, sieve_2

def compute(limit:int = 13195):
    sieve_1 = set(
        [p for p in range(1,int(math.sqrt(limit)))
                             if limit%p == 0]
    )
    reduced_in_size = False
    depth = 1
    while not reduced_in_size:
        reduced_in_size, sieve_2 = sieve(sieve_1)
        print(f"depth: {depth}", sieve_1, sieve_2)
        # if not reduced_in_size:
        #     return sieve_1 - sieve_2
        sieve_1 = sieve_1 - sieve_2
        depth+=1
    return sieve_1

if __name__ == "__main__":
    print(compute(limit=12234655367))
    # prime 6923790551475143
