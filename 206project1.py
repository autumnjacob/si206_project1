import os
import filecmp
import datetime

def getData(file):

    opfile = open(file,"r")
    first=True
    datalist = []
    for line in opfile:
        if first==True:
            datakeys = line.strip().split(",")
            first=False
        else:
            values=line.strip().split(",")
            datadic = {}
            for pos in range(5):
                datadic[datakeys[pos]] = values[pos]
            datalist.append(datadic)
    return datalist

#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

#Your code here:
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
    sorted_lst = sorted(data, key = lambda x: x[col])
    return sorted_lst[0]['First'] + ' ' + sorted_lst[0]['Last']

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
    Classes = {'Senior':0, 'Junior':0, 'Freshman':0, 'Sophomore': 0}
    for x in data:
        if x['Class'] == 'Senior':
            Classes['Senior']+= 1
        elif x['Class'] == 'Junior':
            Classes['Junior']+= 1
        elif x['Class'] == 'Freshman':
            Classes['Freshman']+= 1
        elif x['Class'] == 'Sophomore':
            Classes['Sophomore']+= 1
    sorted_Classes = sorted(Classes, key = lambda x:Classes[x],reverse=True)
    Class_Totals = []
    for x in sorted_Classes:
        Class_Totals.append((x,Classes[x]))
    return Class_Totals


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
    days = {}
    #print(a)
    for x in a:
        #print(x)
        date = x['DOB'].split('/')
        #print(date)
        day = date[1]
        if day not in days:
            days[day] = 1
        else:
            days[day] += 1
    days_lst = list(days.items())
    sorted_days = sorted(days_lst, key=lambda x: x[1], reverse= True)
    return int(sorted_days[0][0])



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
    age = []
    for student in a[1:]:
        birth_month, birth_day, birth_year = student['DOB'].split('/')
        today_year = int(datetime.date.today().year)
        today_month = int(datetime.date.today().month)
        today_day = int(datetime.date.today().day)
        if ((today_day >= int(birth_day)) and (today_month) >= int(birth_month)):
            age.append(today_year - int(birth_year))
        else:
            age.append(today_year - int(birth_year) + 1)
    return round((sum(age) / len(age)), 0)
            

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
    f = open(fileName, "w")
    sorted_list = sorted(a, key=lambda x: x[col])
    for person in sorted_list:
        firstname = person['First']
        lastname = person['Last']
        email = person['Email']
        
        data = [firstname, lastname, email]
        
        f.write(','.join(data) + '\n')
    f.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

