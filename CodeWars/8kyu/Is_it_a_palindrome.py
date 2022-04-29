def is_palindrome(s):
    # Reverses string and checks if it's the same as the OG string
    if s.lower() == s[::-1].lower():
 	    return True
    else:
        return False
