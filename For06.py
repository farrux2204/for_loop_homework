def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    y=0
    for a in range (A,B+1):
       y+=a 
    return y
print(main(2,5))
    