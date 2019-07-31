index = 1
t = [1,2,3]
def f():
    global  index
    print(t)
    t.pop(0)
    index +=1
    print(index)