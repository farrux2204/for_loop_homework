def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    x=[]
    for a in list1:    
        x.append(a.title())
    return x
print(main(['farrux','azim',"sarvar"]))