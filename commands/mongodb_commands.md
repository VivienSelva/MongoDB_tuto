# Basic MongoDB Shell Commands & Collection Usage

This document summarizes essential **MongoDB shell (mongosh)** commands to navigate databases, create collections, and insert or query documents.

---

## 📁 Show Databases
Display all existing databases:
```js
show dbs
```
A database appears **only after** it contains at least one collection **with data**.

---

## 🔄 Switch or Create a Database
```js
use databasename
```
- If the database already exists → switches to it.
- If it does not exist → it will be created **when you insert data**.

---

## 📚 Collections
Collections in MongoDB are similar to SQL tables but more flexible:
- Do **not** require a fixed schema.
- Are created automatically when you insert data.

---

## ✏️ Insert Data Into a Collection
### Insert One Document
**Syntax:**
```js
db.collection_name.insertOne({ key: value, ... })
```

### Example
```js
db.cppcheck.insertOne({
  SAO_8_2: "In function prototype, all parameter identifiers shall be defined and shall have the same name as in the function declaration"
})
```
MongoDB returns an **ObjectId** automatically, which uniquely identifies the inserted document.

---

## 🔍 Find / Display Documents
Retrieve all documents from a collection:
```js
db.collection_name.find()
```
### Example
```js
db.cppcheck.find()
```
This outputs all previously inserted documents.

---

## 🧩 Insert a Document With Multiple Fields
### Example
```js
db.cppcheck.insertOne({
  SAO_8_2: "In function prototype, all parameter identifiers shall be defined and shall have the same name as in the function declaration",
  location: 24
})
```

You can format your insert on multiple lines for readability. In mongosh, use:
- **Shift + Enter** → new line without executing
- **Enter** → execute the command

---

## ✔ Summary
- `show dbs` lists existing databases
- `use dbname` switches or prepares a database
- Collections appear only once they contain data
- `insertOne()` creates a collection if needed
- `find()` retrieves stored documents

MongoDB's shell is flexible and ideal for experimenting with document-based data structures.
