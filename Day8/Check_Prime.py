#Write your code below this line ๐


def prime_checker(number):
  isprime = True
  if number not in prime:
    for divisor in prime:        
      if (number%divisor==0):
        isprime = False
    
  if isprime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime = [2, 3, 5, 7]
prime_checker(number=n)



