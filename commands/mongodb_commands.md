 Basic MongoDB Shell Commands & Collection Usage

This document summarizes the essential **MongoDB Shell (mongosh)** commands to navigate databases, manage collections, and insert, query, update, or delete documents.

---

## 📁 Show Databases

Displays all existing databases:

```js
show dbs
```

A database appears **only after** it contains at least one collection **with data**.

---

## 🔄 Switch or Create a Database

```js
use databasename
```

- If the database exists → switches to it.
- If not → it will be created **only when you insert data**.

---

## 📚 Collections

Collections in MongoDB behave like SQL tables but are more flexible:

- No fixed schema is required.
- A collection is created automatically when you insert data.

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

MongoDB automatically returns an **ObjectId**, which uniquely identifies the document.

---

## 🔍 Find / Display Documents

Retrieve **all documents**:

```js
db.collection_name.find()
```

### Filtering with `find()`

```js
db.collection_name.find({ "file.name": "ro.c" })
```

**Example output:**

```json
[
  {
    "_id": ObjectId("697c8af3ccadfc65d0628ca5"),
    "SAO_6_6": "Symbolic names shall be defined in capital letters",
    "file": { "name": "ro.c", "line": 56 },
    "Status": "Failed"
  },
  {
    "_id": ObjectId("697c8cd8ccadfc65d0628ca7"),
    "SAO_6_6": "Symbolic names shall be defined in capital letters",
    "file": { "name": "ro.c", "line": 56 },
    "Status": "Failed"
  }
]
```

### Find Only One Document

```js
db.collection_name.findOne()
```

With filter:

```js
db.collection_name.findOne({ SAO_6_6: "Symbolic names shall be defined in capital letters" })
```

**Output:**

```json
{
  "_id": ObjectId("697c8af3ccadfc65d0628ca5"),
  "SAO_6_6": "Symbolic names shall be defined in capital letters",
  "file": { "name": "ro.c", "line": 56 },
  "Status": "Failed"
}
```

---

## 🧩 Insert a Document With Multiple Fields

```js
db.cppcheck.insertOne({
  SAO_8_2: "In function prototype, all parameter identifiers shall be defined...",
  location: 24
})
```

### Nested Objects

```js
db.cppcheck.insertOne({
  SAO_8_3: "test",
  line: 252,
  file: {
    "test.c": "a C function",
    cl: 225,
    file: "10"
  }
})
```

---

## 📦 Insert Multiple Documents

Use **insertMany()** when inserting more than one document:

```js
db.collection_name.insertMany([{ key: value }, { key: value }])
```

### Example

```js
db.cppCheck.insertMany([
  {
    SAO_11_4: "In macro definition, parameters and body shall be enclosed in parentheses",
    file: { name: "pb.c", line: 522 },
    Status: "Failed"
  },
  {
    SAO_6_6: "Symbolic names shall be defined in capital letters",
    file: { name: "ro.c", line: 56 },
    Status: "Failed"
  }
])
```

**Output:**

```json
{
  "acknowledged": true,
  "insertedIds": {
    "0": ObjectId("697c8cd8ccadfc65d0628ca6"),
    "1": ObjectId("697c8cd8ccadfc65d0628ca7")
  }
}
```

---

## 🛠 Updating Documents

MongoDB provides two update functions:

### `updateOne()`
Updates the first matching document.

```js
db.collection_name.updateOne(
  { filter_key: filter_value },
  { $set: { field_to_update: new_value } }
)
```

### `updateMany()`
Updates **all** matching documents.

```js
db.collection_name.updateMany(
  { filter_key: filter_value },
  { $set: { field_to_update: new_value } }
)
```

### Example: updateOne

```js
db.cppCheck.updateOne(
  { SAO_6_6: "Symbolic names shall be defined in capital letters" },
  { $set: { "file.name": "test.c" } }
)
```

### Example: updateMany

```js
db.cppCheck.updateMany(
  { SAO_6_6: "Symbolic names shall be defined in capital letters" },
  { $set: { "file.name": "test.c" } }
)
```

---

## 🗑 Delete Data (Documents)

MongoDB provides two delete functions:

### `deleteOne()`
Deletes the **first** matching document.

```js
db.collection_name.deleteOne({ filter_key: filter_value })
```

### `deleteMany()`
Deletes **all** matching documents.

```js
db.collection_name.deleteMany({ filter_key: filter_value })
```

### Examples

```js
db.cppCheck.deleteOne({ SAO_6_6: "Symbolic names shall be defined in capital letters" })
```

```js
db.cppCheck.deleteMany({ SAO_6_6: "Symbolic names shall be defined in capital letters" })
```

---

## 🗑 Delete a Database

```js
db.dropDatabase()
```

### Example

```js
use cppcheck
db.dropDatabase()
```

---

## ✔ Summary

- `show dbs` → list databases
- `use dbname` → switch/create database
- `insertOne()` / `insertMany()` → insert data
- `find()` / `findOne()` → query data
- `updateOne()` / `updateMany()` → update documents
- `deleteOne()` / `deleteMany()` → delete documents
- Supports nested objects and schema‑less structures
