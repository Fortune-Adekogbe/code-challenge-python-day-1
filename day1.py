
def twofer(*name):
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    a= list(name)[0] if len(name)>0 else 'you'
    return f'One for {a},one for me.'
