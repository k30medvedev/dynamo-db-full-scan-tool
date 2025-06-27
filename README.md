# DynamoDB Control Plane Update Tool

## 📓 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history.

The **DynamoDB Control Plane Update Tool** is a Streamlit-based web application for managing DynamoDB tables safely and efficiently.  
It helps you browse, filter, and bulk update records without writing complex scripts or using the AWS CLI.

---

## 🌟 Purpose

This tool is designed to:

- 🔍 Browse and inspect records in DynamoDB tables  
- ➕ Add flexible filters to narrow down data  
- 🛠 Perform safe bulk updates (with dry-run preview)  
- 📊 Count records before running updates  
- ✅ Provide clear feedback and control within the UI  
- 🔎 Run CloudWatch queries by CorrelationId across multiple log groups

It simplifies DynamoDB operations and reduces the risk of errors when modifying data.

---

## 🚀 Main Features and Icons

| Feature                | Icon   | Purpose                                      |
|------------------------|--------|---------------------------------------------|
| AWS connection        | 🔐     | Connect to AWS securely with keys           |
| Fetch Table List      | 🔍     | Retrieve and list available tables          |
| Show Table Content    | 👁️     | Display table records in a DataFrame        |
| Refresh Table         | 🔄     | Reload the latest data from the table       |
| Count Records        | 🔢     | Show total number of records in the table   |
| Additional Filters    | ➕     | Add custom filters by field and value       |
| Delete Filter/Field  | ❌     | Remove a specific filter or update field    |
| Add Update Field     | ➕     | Define which fields to update and how       |
| Run Update          | ▶️ / 🚀 | Start the update process                    |
| Stop Update         | 🛑     | Interrupt the update process safely         |
| CloudWatch Query    | 🔎     | Find blocking executions by CorrelationId   |

---

## 💻 How to use

### 1️⃣ Connect to AWS
- Enter your AWS Access Key ID, Secret Access Key, optional Session Token, and region.
- Click `🔍 Fetch Table List` to load available tables.

### 2️⃣ Select and view a table
- Choose the desired table from the dropdown.
- Click `👁️ Show Table Content` to display its data.
- Use `🔄 Refresh Table` to reload, or `🔢 Count Records` to see how many records are in the table.
