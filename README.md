# Working With Files

## Error and Exception Handling

### `try`, `except` and `finally` block of codes

- They as if and else block.
```
# Create a function called greetings
# def greetings():
#       pass

# name = 'devops'
# year = 2021
# print(name + year)
try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    # raise
# Creating aliases
    print("order.txt not found" + str(errmsg))

finally:
    print("Thank you for visiting, hope to see you again!")
```
```
### Handling files - Reading files- We have already opened a file and we have begun to handle some of the errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening`open(file, mode)`
| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|
```