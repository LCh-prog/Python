#Import of libraries
import json, re, datetime, hashlib


#The global variables: contains the current timestamp and format
#of email to check by regular expressions
curr_dt=str(datetime.datetime.now())
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Open file and assign content to the "data" variable
f = open('json_data.json')
data = json.load(f)


#Adding to the very begin of the "out.json" file the Json's
#root element before looping
with open('out.json', 'w') as file:
    file.write('{"root": [')


#Reading from the root element "json_data" of the "json_data.json" file
#and building the looping
for i in data['json_data']:

#Checking if the emails strutures are correct
  if(re.fullmatch(regex, i["email"])):
#Need to convert a dictionary to the list, in order to easily
#add the "0" indexed the "unique_id" new element to the very begin of the
#each row which originated from hashsum
    lst = list(i.items())
    lst.insert(0, ('unique_id', hashlib.md5((str(i["id"]) + i["first_name"] + i["last_name"] + str(curr_dt)).lower().encode('utf-8')).hexdigest()))
#Again converting to the dictionary and feeding to the "i" variable
    i = dict(lst)

#Another new element to array, feeding the values from the "curr_dt" variable
    i["curr_dt"]=curr_dt

#Writing all rows with "a" - Append mode - Opens a file for appending,
#creates the file if it does not exist, "\n" switch to the next line of file
    print("Valid Email",i)

    arr_len = len(data['json_data'])

    j = open('out.json', "a")
    if(arr_len > i["id"]):
      j.write(json.dumps(i) + ", " + '\n')
#Adding the close tag of the root element to the very end
    if(arr_len == i["id"]):
      j.write(json.dumps(i) + "]} " + '\n')
      
      j.close()

#Otherwise (in case of emails strutures are not correct)
#invalid emails go away to error.log file
  else:

    l = open('error.log', "a")
    l.write(i["email"] + '\r\n')
    l.close()

    print("Invalid Email",i)

f.close()
