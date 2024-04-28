import re
text="I am an DevOps Engineer"
find=r"DevOps"
search = re.search(find,text)

if search:
    print("text found ", search.group())
else:
    print("text not found")