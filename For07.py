def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    y=0
    for a in range(N):
        if a%2==1:
            y+=a 
    return y
print(main(3)) 
