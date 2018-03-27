def run_with_posit(func,*args):
    return func(*args)
def sum_args(*args):
    return sum(args)
def sub(*args):
    return args[0]-args[1]
def multiple(*args):
    return args[0]*args[1]
def divide(*args):
    if args[0]==0 or args[1]==0:
        print('error')
    else:
        return args[0]/args[1]
