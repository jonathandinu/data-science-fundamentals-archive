import time
import peewee as pw

db = pw.SqliteDatabase('better_breakfasts.db')

payload = {
    'client_id': os.environ['FOURSQUARE_ID'],
    'client_secret': os.environ['FOURSQUARE_SECRET'],
    'v': '20160101'
}

# EXTRACT
res = requests.get('https://api.foursquare.com/v2/venues/explore', params={
    **payload,
    **{
        'near': 'Pittsburgh, PA',
        'section': 'coffee'}
})

data = res.json()
record = data['response']['groups'][0]['items'][0]

# TRANSFORM
v = transform.parse_venue(record['venue'])

# Interstitial
class Venue(pw.Model):
    fid = pw.CharField()
    name = pw.CharField()
    price = pw.IntegerField()
    rating = pw.FloatField()
    ratingSignals = pw.IntegerField()
    url = pw.CharField()
    latitude = pw.DecimalField()
    longitude = pw.DecimalField()

    def __repr__(self):
        return "{0} has a rating of {1} based on {2} ratings.".format(
            self.name,
            self.rating,
            self.ratingSignals
        )

    class Meta:
        database = db


# LOAD
pw.Venue(**v).save()