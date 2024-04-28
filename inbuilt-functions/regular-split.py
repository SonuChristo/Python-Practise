import re
text="Apple,mango,orange,pine"
patt=r","
split_text=re.split(patt,text)
print(split_text)