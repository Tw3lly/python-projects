# Create a function that will abbreviate a two word name in a single string, and add a dot inbetween. 

def abbrev_name(name):
  # First let's split the name using the split function
  name =name.split()
  # Now we pick out the first letter of the first index, make it upper case, add a dot inbetween and do the same for the second part of the string. 
  name = name[0][0].upper() + "." + name[1][0].upper()
  
  #Debug Print Statements
  #print(name)
  #print(name[0], name[1])
  
  return name


