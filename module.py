def loe_failist(file:str)->str:
	f=open(file,"r")
	stroka=f.read()#str
	stroka=f.readlines()#list
	f.close()
	return stroka
stroka=loe_failist("users.txt")
stroka=loe_failist("passwords.txt")
print(stroka)
def loe_failist_listisse(file:str)->list:
	f=open(file,"r")
	list_=[]
	for stroka in f:
		list_.append(stroka.strip())
	f.close()
	return list_
def paskontroll(psword: str)->bool:
	ls=list(psword)
	for e in ls:
		if e.isdigit(): d=True
		if e.isalpha(): a=True
		if e.isupper(): u=True
		if e.islower():l=True
		if e in list(".,:;!_*-+()/#¤%&"): s=True
	if d==True and a==True and u==True and l==True and s==True:
		t=True
	else:
		t=False
	return t