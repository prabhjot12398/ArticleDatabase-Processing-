from pymongo import MongoClient
 
import json



def load():


	
	file_name=input("enter a file name, with the extension: ")
	port_number=input("enter the current mongodb port number: ")
	

	client = MongoClient('mongodb://localhost:'+port_number)
	db = client["291db"]
	collist = db.list_collection_names()
	if "dblp" in collist:
		dblp= db["dblp"]
		dblp.drop()
	
	dblp= db["dblp"]
		
	values=[]
	
	#creates collection
	for line in open(file_name):
		dict_1=json.loads(line)
		dict_1["year"]=str(dict_1["year"])
		values.append(dict_1)

	dblp.insert_many(values)
	dblp.create_index([("authors","text"), ("title","text"), ("abstract","text"), ("venue","text"), ("year","text")],default_language="none")
	#dblp.create_index([("authors","text"), ("title","text"), ("abstract","text"), ("venue","text"), ("year","text")])	
	
	return db




def main():

	load()

if __name__ == "__main__":
    main()