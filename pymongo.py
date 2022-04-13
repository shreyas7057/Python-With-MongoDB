
import pymongo

# connect to mongodb
client = pymongo.MongoClient('mongodb://localhost:27017')

print(client)
print(client.list_database_names())

# create database
# it will be registred when there is atleast 1 collection in that db 
# so now db is created but it will not show in the list of all databases once the collection is created then it will show in all the dbs list
db = client['students']
print(db)
print(client.list_database_names()) 


# create collection of that database
collection = db['name']
print(collection)


# insert data or document in the collection
x = collection.insert_one({'id':'1','name':'shreyas'})

# insert multiple documents
dict = [
    {'id':'1','name':'shreyas'},
    {'id':'2','name':'def'}
]
x = collection.insert_many(dict)

# find the document from collection
x = collection.find_one()
print(x)

# find multiple document and print
for i in collection.find():
    print(i)


# fetch documents 
# this will fetch the data which are equal to name shreyas
x = collection.find_one({'name':{'$eq':'shreyas'}})
# this will fetch the data which name is shreyas and its id is 1
x = collection.find_one({'name':{'$and':[{'name':'shreyas'},{'id':1}]}})


# update documents 
x = collection.update_one({'name':"shreyas"},{'$set':{'name':'Shrey'}})


# delete documents
x = collection.delete_one({'name':'shreyas'})
x = collection.delete_many({'name':{'$in':['shreyas','def']}})