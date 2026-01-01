'''
## Task
- Create a file inside Python
- Raed
- Write (No Overwrite)
- print
- read
- print new content
- close file
- print close
'''

file = open("Practice.txt","w")
file.write("first Line \n")

## If i want to change mode i don't need to close the file and re open it i just reopen it with a different mode

file = open("Practice.txt","r+")
content = file.read()
file.write("second line")
print(content)
file.seek(0)
content = file.read()
print(content)

file.close()

print(file.closed)