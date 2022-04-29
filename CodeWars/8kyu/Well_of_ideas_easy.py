def well(x):
    good_ideas = 0
    # Loops through the list and adds 1 to good_ideas for every 'good' there is in the list
    for g in x:
        if g == 'good':
            good_ideas += 1
    # Checks first if there are 0 good ideas, in that case return Fail
    if good_ideas == 0:
        return 'Fail!'
    # If good ideas exceeds 2...
    elif good_ideas > 2:
        return 'I smell a series!'
    # Anything else will return publish
    else:
        return 'Publish!'
      
