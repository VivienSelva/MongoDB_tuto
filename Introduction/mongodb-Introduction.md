## What are SQL and NoSQL Databases?

**SQL Databases** (like MySQL, PostgreSQL) are relational databases. They store data in tables with rows and columns and use **SQL (Structured Query Language)** to access data.

**NoSQL Databases** (like MongoDB) are non-relational. They store data in flexible structures such as documents, key-value pairs, wide-column stores, or graphs.
MongoDB is a **document-based NoSQL** database.

---

## Main Differences: MongoDB vs MySQL

| Feature | MySQL (SQL) | MongoDB (NoSQL) |
|--------|--------------|------------------|
| **Data Storage** | Tables (rows & columns) | Collections (documents) |
| **Data Format** | Structured, tabular | JSON-like documents (BSON) |
| **Schema** | Fixed, predefined | Flexible, dynamic schema |
| **Joins** | Uses joins | Embeds related data |
| **Transactions** | ACID-compliant | Limited but improving |
| **Scalability** | Vertical | Easy horizontal scaling |

Both can store data for one or multiple databases.

---

## How MongoDB Stores Data

In **MySQL**, data is stored in tables where every row follows the same structure.

In **MongoDB**, data is stored in:
- **Collections** → equivalent to tables
- **Documents** → equivalent to rows

Each document is a JSON-like object encoded as **BSON (Binary JSON)**.

### Example MongoDB Document

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 30,
  "department": "Engineering",
  "skills": ["Python", "MongoDB", "Data Analysis"],
  "isActive": true
}
```

Documents can contain nested objects and arrays.
Documents in the same collection **do not need to share the same structure**.

---

## Why MongoDB?

- **Schema flexibility**: modify structure anytime
- **No complex joins**: embed related data
- **Fast & scalable**: BSON format + horizontal scaling
- **Ideal for JSON workflows**

---

## Summary

**SQL databases** like MySQL use tables, fixed schemas, and normalization.

**NoSQL databases** like MongoDB store JSON-like documents with flexible schemas and embedded data.

This offers more flexibility and simpler data models for many modern applications.


