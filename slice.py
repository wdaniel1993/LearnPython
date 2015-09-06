__author__ = 'Daniel'

name = 'Daniel Wallner'

print(name[:3])
print(name[3:])
print(name[::-1])
print(name[1:-1])
print(name[-5:])
print(name[-5:-3])
print(name[3:1])
print(name[::2])

myDict = {'name' : 'Daniel Wallner', 'age' : 22, 'title' : 'BA'}

myStr = "Name: %(name)s Age: %(age)d" % myDict
#myStr = "Name: %(person[name])s Age: %(person[age])d" % {'person':myDict}

print(myStr)