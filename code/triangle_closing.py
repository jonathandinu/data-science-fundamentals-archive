import csv, sys, webbrowser
import collections as coll

def find_listings(records, user_id):
    listings = set()

    # find listings of user
    for row in records:
        if row[3] == user_id:
            listings.add(row[0])

    return listings

def find_travelers(records, listings):
    fellow_travelers = set()

    # find fellow travelers
    for row in records:
        if row[0] in listings:
            fellow_travelers.add(row[3])

    return fellow_travelers

def count_triangles(records, fellow_travelers):
    triangles = []

    # find triangles user is a part of
    for row in records:
        if row[3] in fellow_travelers:
            triangles.append(row[0])

    return coll.Counter(triangles)

def recommend_listings(counts, user_listings, num=10):
    for listing in user_listings:
        if listing in counts:
            counts.pop(listing)

    return counts.most_common(num)

def main(csvfile, user_id):
    reader = csv.reader(csvfile)
    headers = next(reader)
    records = list(reader)

    user_listing = find_listings(records, user_id)
    user_fellows = find_travelers(records, user_listing)
    counts = count_triangles(records, user_fellows)
    return recommend_listings(counts, user_listing)

if __name__ == '__main__':
    filename, user_id = sys.argv[1:]
    csvfile = open(filename, newline='')

    recommendations = main(csvfile, user_id)

    # present the results!
    for rec in recommendations:
        webbrowser.open('http://airbnb.com/rooms/' + rec[0])

    print(recs)
