"""
This program calculates the sum of the first n prime numbers."""

def sum_of_n_primes(n: int) ->int:
    """
    Calculate the sum of the first n prime numbers.
    """
    prime =[True]*n
    prime[0]=prime[1]=False
    i=2
    while i*i<=n:
        if prime[i]:
            for j in range(i*i,n,i):
                prime[j]=False
        i+=1
    s=0
    for i in range(n):
        if prime[i]:
            s+=i
    return s
if __name__ == "__main__" :
    try:
        number = int(input("Enter the limit: "))
        print(sum_of_n_primes(number))
    except ValueError:
        print("Please enter a valid integer.")