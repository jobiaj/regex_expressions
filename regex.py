import re
def remove_multiple_newline(string1):
	return re.sub(r'([\n])(\1+)', r'\1', string1)

def remove_whitespace(string1):
	return "".join(string1.split())

#If you want a general format to replace any sequence of repeated characters with just one of those characters:
s='aaa,,bb,c'
def remove_repeated_all(s):
	return re.sub(r'(.)(\1+)', r'\1', s)
#result:'a,b,c'

#substitution method
def more_symbols_reduced_to_one():
	return re.sub(r'\.\.+', '.', 'A..a.b.c')
#gives  'A.a.b.c'