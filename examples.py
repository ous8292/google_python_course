
# Lists and Tuples


def file_size(file_info):
    name, file_extension, bytes = file_info
    return "{:.2f}".format(bytes / 1024)


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21

# enumerate example

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


def skip_elements(elements):
    # code goes here
    element = []
    for i, e in enumerate(elements):
        if i % 2 == 0:
            element.append(e)
    return element
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements
    (['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']










"""


# list Comprehensions

# classic way
multiples = []
for x in range(1, 11):
    multiples.append( x *7)

print(multiples)

# using comprehension
multipless = [ x* 7 for x in range(1, 11)]
print(multipless)


"""









"""
The odd_numbers function returns a list of odd numbers between 1 and n, inclusively.
Fill in the blanks in the function, using list comprehension.
Hint: remember that list and range counters start at 0 and end at the limit minus 1.
"""


def odd_numbers(n):
    return [x for x in range(0, n + 1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []