import re

text = '''

'''

# result = text.replace(' ', '')
# print(result)

text_mod = re.sub('^([0-9]{10}_)([0-9]{2})v[0-9](\.[0-9])?$',r'\2',text,flags=re.MULTILINE)

# text_mod = re.findall('^([가-힣I]+)$',text,flags=re.MULTILINE)

year_list = []

# print(text_mod)
print(type(text_mod))
year_list = text_mod.split()
# print(year_list)

print("max : ", max(year_list))
print("min : ", min(year_list))