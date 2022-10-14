src = not False and True or False and not True

# result = True or False and False # избавляемся от NOT
# result = True or False # избавляемся от логического AND
# result = True # избавляемся от OR

result = True

print(src == result)
