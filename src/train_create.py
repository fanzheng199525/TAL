import sqlite3 
import pandas as pd
from datetime import datetime

filename = '2017-11'

connection = sqlite3.connect('{}.db'.format(filename))
c = connection.cursor()
limit = 10000
last_unix = 0
cur_length = limit
counter = 0
test_done = False

while cur_length == limit:
	#read the database and get the matched couple to build teh train set
	df = pd.read_sql("SELECT * FROM parent_Reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {};".format(last_unix,limit), connection)
	last_unix = df.tail(1)['unix'].values[0]
	cur_length = len(df)

	if not test_done:
		with open('test.from', 'a', encoding='utf8') as f:
			for content in df['parent'].values:
				f.write(content+'\n')

		with open('test.to', 'a', encoding='utf8') as f:
			for content in df['comment'].values:
				f.write(str(content)+'\n')
		test_done = True
	else:
		with open('train.from', 'a', encoding='utf8') as f:
			for content in df['parent'].values:
				f.write(content+'\n')

		with open('train.to', 'a', encoding='utf8') as f:
			for content in df['comment'].values:
				f.write(str(content)+'\n')
	counter+=1
	if counter % 20 ==0:
		print(counter*limit, 'rows completed so far\n', 
				str(datetime.now()), ' time_now')



				