is_nice = True

#Using ternary operator
state = "nice" if is_nice else "not nice"

#Equivalent code using multi-line if statements
if is_nice:
    state = "nice"
else:
    state = "not nice"
    
print(state)