def repeat_str(repeat, string):
  # Create an empty variable where we can add the repeat strings
  final_string = ""
  # We for loop using the range, where we take repeat as the input for how many times to loop through
  for r in range(repeat):
    # Concatenate using += into the previously empty variable
      final_string += string
  # Return final output 
  return(final_string)
