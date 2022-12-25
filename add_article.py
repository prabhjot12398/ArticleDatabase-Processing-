import pymongo

def Add_Article(db):
    
    dblp=db["dblp"]
    found=False

    while found==False:
        unique_id=input("Enter the unique id: ")
        unique_id=unique_id.strip()
        test=list(dblp.find({"id":unique_id}))
        if len(test)==0:
            found=True
        else:
            print("not a unique ID, try again")

    
    
    title=input("Enter the title of the article you want to add: ")
    year=input("Enter the year of publication: ")
    list_of_Author=[]
    no_of_Authors=int(input("Enter the number of Authors you want to add: "))
    i=1
    while i<=no_of_Authors:
        Author=input("Enter the Author: ")
        list_of_Author.append(Author)
        i=i+1
    
    added_articles = [
        {
            "id": unique_id,
            "title": title,
            "year": year,
            "authors": list_of_Author,
            "abstract":None,
            "venue":None,
            "references":[],
            "n_citation":0

        }
    ]
    dblp.insert_many(added_articles)
    return True 