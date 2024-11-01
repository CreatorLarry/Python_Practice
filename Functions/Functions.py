# Functions == takes input and gives results
# YouTube video by Corey Schafer
# Instance 1 -- Intro to functions
def hello_function(): # defining a function
    pass  # used to pass the function without error if it's empty

hello_function() # calling the function since print is already in it
# functions are used to make your code DRY - Don't Repeat Yourself


# Instance 2

def hello_function(): # defining a function
    print('Hello Function!')

hello_function() # calling the function since print is already in it
# functions are used to make your code DRY - Don't Repeat Yourself




# Instance 3 -- returning our value to print
def hello_function(): # defining a function
    return 'Hello Function!'

print(hello_function())



# Instance 4 -- Passing parameters to our function
def hello_function(greeting, name = 'Anonymous'): # defining a function
    return '{}, {}'.format(greeting, name)

print(hello_function('Hi', 'Lawrence'))



#Instance 5 - Arguments- *args and **kwargs- Allowing us to accept an arbitrary number of positional or keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ['Maths', 'Art'] #Dictionary 1
info = {'name': 'Jane', 'age': 22} # Dictionary 2
# passing a function with random values
student_info(courses, info) # Doesn't unpack when run hence remains a keyword argument
student_info(*courses, **info) # Unpacks the keyword arguments