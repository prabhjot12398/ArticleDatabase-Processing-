import pymongo


def search_authors(db):
    dblp=db["dblp"]
    keyword = input("Provide Keyword or quit to exit: ")
    if keyword.lower() == 'quit':
        return
    elif len(keyword) >0:
        result=list(dblp.find())#{"authors":keyword}))
        authorList = []
        for results in result:
            temp = results["authors"]
            authorList += temp
            #print(":","/ID:"i,results["id"], "/Author:",results["authors"] )
        #print(authorList)
        authorListSearched = []
        for i in authorList:
            if keyword.lower() in i.lower():
                authorListSearched.append(i)
        authorCount = {i[:]:authorListSearched.count(i[:]) for i in authorListSearched}
        count =1
        for k, v in authorCount.items():
            print(str(count)+": Author: "+k + " | Publications: " + str(v) )
            count+=1

        #exit = False
        #while exit != True:



    return



def main():

        search_authors(None)


if __name__ == "__main__":
        main()
        