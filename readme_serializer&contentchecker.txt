
The assignment details, a Python Code:

1. Generate json file with 1000 rows (you can you use https://www.mockaroo.com/)
2. Each row has: (id, first name, last name, email)
3. Iterate the whole file, check the correct email
4. If email is not correct send that record to error.log
5. Create other file with structure:  (unique id,  id, first name, last name, email, current date time)
6. Make unique  id as (concat id, first name, last name, now-timestamp)
7. Save that file to local 


Solution:
1) Create 1 folder
2) Put together the 2 files here: JSON.py, json_data.Json
3) Double click on JSON.py
4) Should to appear out.Json and error.log file

Notes: In this code I've hardcoded the filenames and root element names, but at work I tend to avoid and use parameterization.
