def loe_failist(file:str)->str:
	f=open(file,"r")
	stroka=f.read()#str
	stroka=f.readlines()#list
	f.close()
	return stroka
stroka=loe_failist("users.txt")
print(stroka)
def loe_failist_listisse(file:str)->list:
	f=open(file,"r")
	list_=[]
	for stroka in f:
		list_.append(stroka.strip())
	f.close()
	return list_
