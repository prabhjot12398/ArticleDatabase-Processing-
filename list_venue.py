from operator import itemgetter
import pymongo
from pymongo import MongoClient
def list_venues(db):
    dblp=db["dblp"]
    n = int(input("Enter a number: "))
    venues = []
    venue_names = []
    output = dblp.find({"$and":[{"venue": {"$ne": ""}},{"venue": {"$ne":None}}]})
    for info in output:
        if info['venue'] not in venue_names:
            if 'references' not in info.keys():
                venue_names.append(info['venue'])
                venues.append([info['venue'], 1, []])
            else:
                venue_names.append(info['venue'])
                venues.append([info['venue'], 1, info['references']])

        else:
            if 'references' not in info.keys():
                venues[venue_names.index(info['venue'])][1] += 1
            else:
                venues[venue_names.index(info['venue'])][1] += 1
                venues[venue_names.index(info['venue'])][2] = list(set(venues[venue_names.index(info['venue'])][2] + info['references']))

    new_venues = []
    for each_venue in venues:
        new_venues.append((each_venue[0], each_venue[1], len(each_venue[2])))

    # sorted_venues = sorted(new_venues, key=lambda x: x[1], reverse=True)
    sorted_venues = sorted(new_venues, key=itemgetter(2), reverse=True)
    for i in range(n):
        print("\n")
        print("Index :", i+1)
        print("Venue :", sorted_venues[i][0])
        print("Number of articles :", sorted_venues[i][1])
        print("Number of articles that reference a paper in that venue :", (sorted_venues[i][2]))
        def main():
            main()
            if __name__ == "__main__":
                main()