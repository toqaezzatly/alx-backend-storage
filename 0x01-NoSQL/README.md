

# MongoDB Basics & Usage in Python

## Table of Contents
1. [Introduction to MongoDB](#introduction-to-mongodb)
2. [Key Concepts in MongoDB](#key-concepts-in-mongodb)
    - [Documents](#documents)
    - [Collections](#collections)
    - [Databases](#databases)
    - [CRUD Operations](#crud-operations)
3. [Setting Up MongoDB in Python](#setting-up-mongodb-in-python)
4. [Using MongoDB in Python](#using-mongodb-in-python)
    - [Connecting to MongoDB](#connecting-to-mongodb)
    - [Inserting Documents](#inserting-documents)
    - [Querying Documents](#querying-documents)
    - [Updating Documents](#updating-documents)
    - [Deleting Documents](#deleting-documents)
5. [Conclusion](#conclusion)

---

## Introduction to MongoDB

MongoDB is a popular NoSQL, document-oriented database that stores data in a flexible, JSON-like format known as BSON (Binary JSON). Unlike traditional relational databases, MongoDB does not require a predefined schema, allowing for faster development and greater flexibility.

## Key Concepts in MongoDB

### Documents
- A **document** is a single record in MongoDB, which is a collection of key-value pairs. It is similar to a row in a relational database.
- Example document:
    ```json
    {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }
    ```

### Collections
- A **collection** is a group of documents, similar to a table in a relational database. Collections do not enforce a schema, so documents in the same collection can have different fields.

### Databases
- A **database** is a logical grouping of collections. A MongoDB instance can host multiple databases, each containing its own collections and documents.

### CRUD Operations
CRUD stands for **Create**, **Read**, **Update**, and **Delete**, which are the main operations performed on a database.

---

## Setting Up MongoDB in Python

To use MongoDB with Python, you need the official MongoDB driver, called **`pymongo`**.

### Installation

1. Install MongoDB on your system: [MongoDB Installation Guide](https://www.mongodb.com/try/download/community)
2. Install the `pymongo` library for Python:

   ```bash
   pip install pymongo
   ```

3. Optionally, you can use **MongoDB Atlas** for cloud-based MongoDB hosting.

---

## Using MongoDB in Python

Below are examples of basic MongoDB operations using the `pymongo` library in Python.

### Connecting to MongoDB

```python
from pymongo import MongoClient

# Create a MongoDB client instance and connect to a local MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create or access a database
db = client['mydatabase']
```

### Inserting Documents

```python
# Create or access a collection
collection = db['users']

# Insert a single document
user = {"name": "Alice", "age": 30, "email": "alice@example.com"}
result = collection.insert_one(user)

# Insert multiple documents
users = [
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
    {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
]
result = collection.insert_many(users)
```

### Querying Documents

```python
# Query a single document
user = collection.find_one({"name": "Alice"})
print(user)

# Query multiple documents
users = collection.find({"age": {"$gt": 25}})  # Users older than 25
for user in users:
    print(user)
```

### Updating Documents

```python
# Update a single document
collection.update_one({"name": "Alice"}, {"$set": {"age": 31}})

# Update multiple documents
collection.update_many({"age": {"$gt": 25}}, {"$set": {"status": "active"}})
```

### Deleting Documents

```python
# Delete a single document
collection.delete_one({"name": "Bob"})

# Delete multiple documents
collection.delete_many({"age": {"$lt": 30}})  # Delete users younger than 30
```

---

## Conclusion

MongoDB is a flexible, scalable NoSQL database that pairs well with Python using the `pymongo` library. With its document-oriented data model, MongoDB allows developers to store and manage data efficiently without worrying about schema constraints.

For further learning, check out:
- MongoDB Documentation: [https://docs.mongodb.com](https://docs.mongodb.com)
- PyMongo Documentation: [https://pymongo.readthedocs.io](https://pymongo.readthedocs.io)

