from pymongo import MongoClient

#pymongo - library

#connecting mongodb 
connectionString="mongodb+srv://sangeethasankar474:vmy6NrAP8ql3i3eC@cluster0.paforwb.mongodb.net/?retryWrites=true&w=majority&appName=/inventory"
client=MongoClient(connectionString)

print(client.list_database_names())

#creating a database - automaticaly created when we perform some operations

#create - collection
# collections are similar to table in mysql 
#its also automatically created when you try to insert any documents


# print(db.list_collection_names())  

#insert documents

db=client.get_database("inventory")
collection=db.get_collection("item")

# document={
#     "item":"canvas",
#     "qty":12,
#     "tag":["cotton"],
#     "size":{
#         "h":12,
#         "w":21
#     }

# }

# #insert

# response=collection.insert_one(document)

# #we can get last inserted id
# last_inserted_id=response.inserted_id
# print("Last inserted Id :{}".format(last_inserted_id))

# #bulk multiple documents

# #insert many

# documents=[]
# documents.append({
#     "item":"canvas",
#     "qty":12,
#     "tag":["cotton"],
#     "size":{
#         "h":12,
#         "w":21
#     }
# })

# documents.append({
#     "item":"mat",
#     "qty":11,
#     "tag":["cotton"],
#     "size":{
#         "h":12,
#         "w":21
#     }
# })

# documents.append({
#     "item":"cloth",
#     "qty":11,
#     "tag":["cotton"],
#     "size":{
#         "h":12,
#         "w":21
#     }
# })

# response=collection.insert_many(documents)
# last_inserted_id=response.inserted_ids
# print("Last inserted Id :{}".format(last_inserted_id))


#getting information

#find & find one
#findone= return 
#find = it return object

# document=collection.find_one()
# print(document)

# cursor=collection.find() #getting cursor object
# for each_documents in cursor: #when we want data we have to loop
#     print(each_documents)



#query - when we have large data you want to filter a data 
#filter obj dict as first paramater

#similar to query sql


#filtering  qty as 12
# filter={"qty":12}
# cursor=collection.count_documents(filter)
# print(cursor)

#sort documents
#recently created documents - first 
#late created documents - fisrt 
#we can sort

#firt parameter as field name
#ascening - 1
#decending - -1

# cursor=collection.find().sort("qty",1)
# print(cursor)

# for each in cursor:
#     print(each)


#delete documents

#delete one  - first parameter - query obj 
#bulk delete - dlete many - first parameter as query obj

#delete documents
result=collection.delete_one({"item":" mat"})

print(result)

#delete many 

result=collection.delete_many({"qty":11})
print(result.deleted_count)

#without delete many query - it delete all documents

















