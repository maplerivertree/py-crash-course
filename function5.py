# function5.py :pass an arbituary number of arguments

""" Below function 'propagate' allows calling arbituary number of arguments"""



# create an initial list of policemen (a list of dictionaries)
db=[]
for i in range(1,5,1):
	robot = {'fraction' : 'police', 'HP' : 100}
	db.append(robot)
print('\nThese are the characters already living in this town.\n')
for i in db[:3]:
	print(str(i))
print('\n')


#--- FUNCTION 
def propagate(current_db, fraction, health, num_of_addition, **other):
	for i in range(1,num_of_addition+1,1):
		robot = {'fraction': fraction, 'HP': health}
		for v, k in other.items():
			robot[v] = str(k)
		current_db.append(robot)
	
	return(current_db)                                          
#---

# make user_interactive

f = input('What type of characters you wish to add? (terrorist/milk-delivery-guy/anything else): ')
n = input('How many to add? (1-10): ')
h = input("What's the health for these characters>? (1-100): ")

s1 = input('Do you want them to have a superpower? (y/n) :')
if s1 == 'y' or s1 == 'Y' or s1.title() == 'Yes':
	s = input("The superpower is :")
	sp = True
	""" USE of Flag """
else:
	sp = False
w = input('What weapon do they carry? :')
print('\n')

if sp == True:
	propagate(db, str(f), int(h), int(n),
		superpower = str(s), 
		weapon = str(w)
		)
else:
	propagate(db, str(f), int(h), int(n), 
		weapon = str(w)
		)

print('\nThe following characters will be propagated for this game.')
for i in db[:]:
	print(str(i))















