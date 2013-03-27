#!/usr/bin/python
import sys
#address book app to store name, number, b'day, e-mail
#not using any db

def main():
	while True:	
		response=str(raw_input("want to add(1) or search(2) or exit(3)"))
		if response=='1':
			temp=open('book.txt','a')
			name=raw_input("insert name :")
			num=raw_input("insert num: ")
			bday=raw_input("insert b'day :")
			email=raw_input("insert mail :")
			temp.write(name+" "+num+" "+bday+" "+email+"\n")
			temp.close()
			print "added successfully"
		elif response=='2':
			patt=str(raw_input("enter name or anything"))
			temp=open('book.txt','rU')
			for line in temp:
				if patt in line: 
					print line
					break
		elif response=='3':
			print 'thank you'
			sys.exit(1)
		else:
			print "enter correct action"

if __name__=='__main__':
	main()
		

	
