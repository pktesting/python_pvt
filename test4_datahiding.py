class Queue:
    def __init__(self,contents):
        self._hiddenlist= list(contents)   #made a method to access contents of the init function

    def push(self,value):
        self._hiddenlist.insert(0,value)

    def pop(self):
          return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue= Queue([1,2,3])
print (queue)
print (queue._hiddenlist)   # printing the queue function before the pop method 
queue.push(0)
print (queue)
queue.pop()
print(queue)
print (queue._hiddenlist)
