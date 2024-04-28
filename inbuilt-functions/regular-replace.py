import re
text="Im an DevOps Engineer"
find=r"DevOps"
replace= "AWS DevOps"

new_text=re.sub(find,replace,text)
print(new_text)