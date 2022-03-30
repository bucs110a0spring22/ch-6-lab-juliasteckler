import turtle

def seq3np1(n):
    count = 0
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    while(n != 1):
        count = count + 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
             n = n * 3 + 1
    return count             # the last print is 1
print(seq3np1(3))

def main():
  ubr = int(input("Please enter positive integer:"))
  start = 1
  if ubr < start:
    exit(main)
  seq3np1(3)
  for i in range(1, ubr + 1):
    start = 1 + 1
    seq3np1(start)
    return start
  print(start)
main()

print(seq3np1(3))


  
def draw(#interation): 
  window = turtle.Screen()
  will = turtle.Turtle()
  will.speed(0)
  count_two = 0