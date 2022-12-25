import pymongo


def search_articles(db):


	
	dblp=db["dblp"]
	quits=False
	
	#starts the search
	while quits==False:
		print("type in a keyword, or type .quit to go back to the main menu, please put spaces between keywords")
		search2=input()
		
		if search2.lower()=='.quit':
			quits=True
			
		else:
			#gets your input, and strips it of extra white space	
			search=search2.strip()
			search_list=search.split() #splits it to look at every individual part
				
			string=''
			for search3 in search_list:
				string=string+"\""+search3+"\"" #puts in a way text search can use, and searchs every word with AND semantics
			
			#result=list(dblp.find({"$text":{"$search":string}}))	
			result=list(dblp.find({"$text":{"$search":string}}))
			#print(string)	
					
				
								
			quits3=False
			while quits3==False:
				count=0
				
				for results in result:
					#prints everything that was matched
					print(str(count)+":","/ID:",results["id"],"/title:", results["title"],"/year:", results["year"], "/venue:",results["venue"] )
					count=count+1 #is the index
				
		
				quits2=False
				#the selection process, what you want to see
				while quits2==False:
					choice=input("select the number of the article you want to see or type .search to go back to searching :")
					#if choice.lower()==".back": #reloads everything, if you selected something
					#	quits2=True
					if choice.lower()==".search": #bring syou back to the search page
						quits2=True
						quits3=True
					else:
						if choice.isnumeric()!=True: #makes sur eyou put a number
							continue
						
						if int(choice)>count-1 or int(choice)<0: #makes sure the number is valid
							continue
						
						else:
												
							select=result[int(choice)] #gets the row
							if "abstract" not in select: #chance there is no abstract
								print("no abstract")	
							if "venue" not in select:
								print("no venue")
							else:
								print("venue:",select["venue"])
							print("ID:",select["id"],"/title:", select["title"],"/year:", select["year"],"/authors:", select["authors"], "/n_citation:", select["n_citation"] )
							refrence=list(dblp.find({"references":select["id"]})) #gets all the thinsg that refrenced the article
							if "references" in select: #checks if there is a reference page
								print("references:",select["references"])
							else:
								print("no references")


							print("referenced by:")
							for ref in refrence:
								#print("test")
								print("ID:",ref["id"],"/title:", ref["title"], "/year:", ref["year"]) 
							

							if "abstract" in select: #if there is an abstract
								print("abstract")
								print(select["abstract"])
							
							exit1=False
							
							while exit1==False: #makes sure you enter the righ thing
								within_choice=input("type .back to go back to the list of results, or .search to search something new: ")
								if within_choice.lower()==".back":
									quits2=True
									exit1=True
								if within_choice.lower()==".search":
									quits2=True
									exit1=True
									quits3=True
								if within_choice.lower()!=".search" and within_choice.lower()!=".back":
									print("not a valid input, try again")


	return
	








def main():
	
	search_articles(None)




if __name__ == "__main__":
	main()