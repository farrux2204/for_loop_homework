def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    x=[]
    for a in range (A,B+1):
        x.append(a)
    return x
print(main(1,5))