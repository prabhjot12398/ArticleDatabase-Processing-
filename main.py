from pymongo import MongoClient
from Search_articles import search_articles
from add_article import Add_Article
from searchAuthors import search_authors
from list_venue import list_venues

def main():

	
	port_number=input("enter the current mongodb port number: ")
	client = MongoClient('mongodb://localhost:'+port_number)
	db = client["291db"]
	dblp=db["dblp"]
	
	quits=False

	
	while quits==False:
		print("press 1 to search for articles")
		print("press 2 to search for authors")
		print("press 3 to list the venues")
		print("press 4 to add an article")
		print("press 5 to quit")
		options=input()
		if options!='1' and options!='2' and options!='3' and options!='4' and options!='5':
			print("try again")
			continue

		if options=='1':
			search_articles(db)
		if options=='2':
			search_authors(db)
		if options=='3':
			list_venues(db)
		if options=='4':
			Add_Article(db)
			
		if options=='5':
			quits=True





	return

if __name__ == "__main__":
	main()