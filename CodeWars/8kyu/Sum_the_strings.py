def sum_str(a, b):
  #if statements will check if a or/and b is empty, if so respective variable is equal to 0
    if a == "":
        a = 0
    if b == "":
        b = 0
   # Sum the values as integers
    sequence = int(a) + int(b) 
    # Return the value as a string
    return str(sequence)

