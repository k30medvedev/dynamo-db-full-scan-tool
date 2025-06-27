# DynamoDB Tool

![Image](https://raw.githubusercontent.com/k30medvedev/dynamo-db-full-scan-tool/master/images/image.jpg)


## 📓 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history.

The **DynamoDB Tool** is a Streamlit-based web application for managing DynamoDB tables safely and efficiently.  
It helps you browse all records of aws DynamoDb

---

## 🌟 Purpose

This tool is designed to:

- 🔍 Browse and inspect records in DynamoDB tables  
- ➕ Add flexible filters to narrow down data  
- 📊 Count records before running updates  

---

## 🚀 Main Features and Icons

| Feature                | Icon   | Purpose                                      |
|------------------------|--------|---------------------------------------------|
| AWS connection        | 🔐     | Connect to AWS securely with keys           |
| Fetch Table List      | 🔍     | Retrieve and list available tables          |
| Show Table Content    | 👁️     | Display table records in a DataFrame        |
| Refresh Table         | 🔄     | Reload the latest data from the table       |
| Count Records        | 🔢     | Show total number of records in the table   |
---

## 💻 How to use

### 1️⃣ Connect to AWS
- Enter your AWS Access Key ID, Secret Access Key, optional Session Token, and region.
- Click `🔍 Fetch Table List` to load available tables.

### 2️⃣ Select and view a table
- Choose the desired table from the dropdown.
- Click `👁️ Show Table Content` to display its data.
- Use `🔄 Refresh Table` to reload, or `🔢 Count Records` to see how many records are in the table.
