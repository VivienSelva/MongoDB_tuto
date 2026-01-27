# MongoDB Community Edition Setup (ZIP on Windows)

This document describes how to install and run **MongoDB Community Edition** using the **ZIP packages** (MongoDB + Mongosh) on **Windows**, without installers or services.

---

## 📥 1. Files Downloaded
- **MongoDB Community Edition** (v8.2.3, Windows, ZIP package)
- **MongoDB Shell (mongosh)** as a ZIP file

Both were extracted manually to custom folders.

---

## ⚙️ 2. Environment Variables Setup
Environment variables were configured to include the `bin` folders:
- `mongodbin`
- `mongoshin`

This allows running `mongod` and `mongosh` directly from CMD.

---

## 🚀 3. Initial Launch Test
Running the following command in CMD:
```cmd
mongod
```

**Result:**
- Logs appeared
- Then `mongod` **shut down immediately**

### ❗ Reason:
MongoDB expects a default data directory at:
```
C:\data\db
```
Because the installation was done using ZIP archives and in custom folders, this directory **did not exist**, so MongoDB could not start.

---

## ✅ 4. Solution: Specify a Custom Data Directory
Run `mongod` with a custom `dbpath`:
```cmd
mongod --dbpath "your\custom\data\path"
```

### ✔ After this:
- `mongod` starts correctly
- The process **stays running** in the CMD window
- MongoDB is now operational

*(Optional) MongoDB can be registered as a Windows service later, but this is not required for normal use.*

---

## 🖥️ 5. Using the MongoDB Shell (mongosh)
Open a **new CMD window** (do **not** close the one where `mongod` is running).

In the new window, run:
```cmd
mongosh
```

### ✔ Result:
- Mongosh connects to the localhost database
- Connection info is displayed

You can verify available databases using:
```js
show dbs
```

---

## 🎉 Setup Complete
MongoDB Community Edition is now running from ZIP packages without installers, and you can use `mongod` + `mongosh` normally.
