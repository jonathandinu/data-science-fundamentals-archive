import json

def parse_venue(data):
    return {
        'id': data['id'],
        'name': data['name'],
        'price': data['price']['tier'],
        'rating': data['rating'],
        'ratingSignals': data['ratingSignals'],
        'url': data['url'],
        'latitude' : data['location']['lat'],
        'longitude': data['location']['lng']
    }

    return venue

def parse_user(data):
    return {
        'id': data['id'],
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'gender': data['gender'],
        'photo': data['photo']['prefix'] + 'original' + data['photo']['suffix']
    }

def parse_tip(data, whitelist=['id', 'createdAt', 'text', 'type', 'canonicalUrl']):
    user = parse_user(data['user'])
    tip = { key: data[key] for key in whitelist }

    return (tip, user)

def parse_response(data):
    tips = []
    users = {}

    venue = parse_venue(data['venue'])

    for tip in data['tips']:
        tip, user = parse_tip(tip)
        tip['user_id'] = user['id']
        tip['venue_id'] = venue['id']
        tips.append(tip)

        if user['id'] not in users:
            users[user['id']] = user

    return (venue, list(users.values()), tips)
