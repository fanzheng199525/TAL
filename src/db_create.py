import sqlite3
import json
from datetime import datetime


filename = '2017-11'
#init of sql transaction
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(filename))
c = connection.cursor()

#create a table of database
def create_table():
	c.execute("""CREATE TABLE IF NOT EXISTS parent_Reply(
		parent_id TEXT PRIMARY KEY, parent TEXT,
	  comment TEXT, subreddit TEXT, unix INT, score INT)""")

#replace the symbol that we don't want
def format_data(data):
	data = data.replace('\n',' newlinechar ').replace('\r',' newlinechar ').replace('"',"'")
	return data

#filter the data that we want
def acceptable(data):
	if len(data.split(' '))>1000 or len(data)<1:
		return False
	elif len(data)>32000:
		return False
	elif data == '[deleted]':
		return False
	elif data == '[removed]':
		return False
	else:
		return True

#to find the existing score of matched topic and reply
def find_existing_score(pid):
	try:
		sql = """SELECT score FROM parent_Reply WHERE parent_id = '{}' LIMIT 1""".format(pid)
		c.execute(sql)
		result = c.fectchone()
		if result!= None:
			return result[0]
		else:return False
	except Exception as e:
		return False
#build the transaction and execute every 1000 sql
def transaction_bldr(sql):
	global sql_transaction
	sql_transaction.append(sql)
	if len(sql_transaction)>1000:
		c.execute("""BEGIN TRANSACTION""")
		for s in sql_transaction:
			try:
				c.execute(s)
			except:
				pass
		connection.commit()
		sql_transaction = []

#replace the better comment
def sql_insert_replace_comment(body, time, subreddit, score, pid):
	try:
		sql = """UPDATE parent_Reply SET comment = '{}', subreddit = '{}', unix = '{}', score = '{}' WHERE  parent_id = '{}';""".format(body, subreddit, int(time), score, pid)
		transaction_bldr(sql)
	except Exception as e:
		print('s0 insertion', str(e))
#insert the matched couple
def sql_insert(pid, parent, body, time,subreddit,score): 
	try:
		sql = """INSERT INTO parent_Reply(parent_id, parent, comment, subreddit, unix, score) VALUES("{}","{}","{}","{}",{},{});""".format(pid, parent, body, subreddit, int(time), score)
		transaction_bldr(sql)
	except Exception as e:
		print('s0 insertion', str(e))

if __name__=="__main__":
	create_table()
	row_counter = 0
	paired_rows = 0

	with open("/home/Download/RC_{}".format(filename),buffering = 1000) as f:
		for row in f:
			row_counter+=1
		#read the file json and get the information
			try:
				row = json.loads(row)
				parent_id = row['parent_id']
				body = format_data(row['body'])
				created_utc = row['created_utc']
				score = row['score']
				subreddit = row['subreddit']
				parent_data = row['permalink'].split('/')[5].replace('_',' ')

				if score>=2:
					existing_comment_score = find_existing_score(parent_id)
					if existing_comment_score:
						if score>existing_comment_score:
							if acceptable(body):
								sql_insert_replace_comment(body, created_utc, subreddit, score, parent_id)
					else:
						if acceptable(body):
								sql_insert(parent_id, parent_data, body, created_utc, subreddit, score)
								paired_rows +=1
			except Exception as e:
				print(str(e))	

			if row_counter % 100000 == 0:
				print('Total Rows Read: {}, Paired Rows: {}, Time: {}'.format(row_counter, paired_rows, str(datetime.now())))


		            
		            
		            
		            
		            
		            






