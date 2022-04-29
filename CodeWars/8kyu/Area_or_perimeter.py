def area_or_perimeter(l , w):
    # First we check if it's an area by checking if the length is the same as the width
    if l == w:
        # Area is calculated by multiplying the length of each side
        return l * l
    # Else we can assume it is a perimeter
    else:
        # Perimeter is the distance around a two-dimensional shape
        # We can calculate this by just adding all sides together
        return l + w + l + w
    
