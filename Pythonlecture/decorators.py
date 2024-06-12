def announce(f):
    def wrapper():
        print("About to run a function..")
        f()
        print("done")
    return wrapper
@announce
def hello():
    print("hello guys")
hello()