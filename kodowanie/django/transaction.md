# Transactions in Django

## What does `transaction.on_commit()` do in Django?

In Django, `transaction.on_commit()` is a function that allows you to schedule functions or tasks to be executed only after a database transaction has been successfully committed.
This is particularly useful when you have operations that should only occur if the entire transaction completes successfully, without any rollbacks,
such as sending a confirmation email after a user's registration is successfully saved to the database.

## What does `transaction.atomic()` do in Django?

In Django, `transaction.atomic()` is used to ensure that a block of code is executed within a database transaction,
making sure that all database operations within the block are either fully completed or fully rolled back in case of an error.
This is crucial for maintaining data integrity, especially when multiple related operations are dependent on each other to maintain consistency within the database.

---

## Common Interview Questions and Answers

### 1. What does `transaction.atomic()` do in Django?

`transaction.atomic()` ensures that a block of database operations executes completely or not at all. If an exception occurs inside the block, all changes are rolled back to maintain data consistency.

Example:

```python
from django.db import transaction

try:
    with transaction.atomic():
        user = User.objects.create(username='test_user')
        profile = Profile.objects.create(user=user, bio='Test Bio')
except Exception:
    print("Transaction rolled back!")
```
## 2. What is `transaction.on_commit()`, and why is it useful?

`transaction.on_commit()` allows functions to be executed **only after** a successful database commit.  
This prevents operations (e.g., sending emails) from occurring if the transaction fails.

### Example:

```python
from django.db import transaction

def send_email(user_id):
    print(f"Sending email to user {user_id}")

with transaction.atomic():
    user = User.objects.create(username='new_user')
    transaction.on_commit(lambda: send_email(user.id))  # Ensures function runs only after commit
```

## 3. How does `select_for_update()` work, and how does it prevent deadlocks?

`select_for_update()` locks rows at the **database level** to prevent concurrent transactions from modifying the same row at the same time.

- It **ensures that only one transaction can modify a row at a time**.
- Other transactions trying to lock the same row must **wait until the first transaction commits or rolls back**.
- This prevents **race conditions and deadlocks**, ensuring data consistency.

### Example:

```python
from django.db import transaction

with transaction.atomic():
    order = Order.objects.select_for_update().get(id=1)  # Locks this row
    order.status = "Processed"
    order.save()
```

## 4. How Does PostgreSQL Handle `select_for_update()`?

PostgreSQL handles row-level locks using `SELECT ... FOR UPDATE`, ensuring that transactions do not modify the same row concurrently.

### Key Aspects of How PostgreSQL Handles `select_for_update()`:

- PostgreSQL stores lock information in **shared memory** and manages locks using:
  - **`pg_locks` system catalog** → You can check active locks with:
    ```sql
    SELECT * FROM pg_locks;
    ```
  - **Write-Ahead Logging (WAL)** → Ensures transaction recovery in case of crashes.
  - **MVCC (Multiversion Concurrency Control)** → Allows multiple transactions to read data while ensuring exclusive writes.

- If a transaction **holds a lock** on a row:
  - Other transactions **must wait** before modifying it.
  - Prevents dirty reads and inconsistent data updates.

- If a transaction **crashes or is terminated**, PostgreSQL **automatically releases the lock**, ensuring system stability.

## 5. Does `select_for_update()` Work Across Different Django Apps and Pods?

✅ **Yes!** PostgreSQL handles row locks at the **database level**, meaning:

- Multiple **Django instances running in different Kubernetes pods** respect the same row lock.
- **Different Django applications sharing the same database** also honor the row lock.
- If **App A (Order Service)** locks a row, **App B (Inventory Service)** must wait before modifying it.

### Example:

```python
# App 1: Order Service
with transaction.atomic():
    order = Order.objects.select_for_update().get(id=1)  # Lock acquired
    order.status = "Processing"
    order.save()

# App 2: Inventory Service (this query will wait if App 1 is still running)
with transaction.atomic():
    order = Order.objects.select_for_update().get(id=1)  # Waiting for the lock
    order.stock_checked = True
    order.save()
```

How It Ensures Data Consistency Across Applications:

Since locks are enforced at the database level, they apply to any application or process accessing the database.
Even if two separate Django apps try to modify the same row, the first transaction gets the lock, and the second must wait until the first transaction commits or rolls back.

## 6. How does Django handle transactions in different databases?

Django supports transactions differently depending on the database backend. The level of transaction support depends on the capabilities of the underlying database.

### ✅ **Database Transaction Support in Django**

| Database     | Transaction Support | Notes |
|-------------|--------------------|-------|
| **PostgreSQL** | ✅ Full transaction support | Recommended for Django applications needing ACID compliance. |
| **MySQL (InnoDB)** | ✅ Supports transactions | Be cautious with implicit commits, as some MySQL statements force a commit. |
| **MySQL (MyISAM)** | ❌ No transaction support | Each query is auto-committed; not suitable for applications needing atomic operations. |
| **SQLite** | ✅ Supports transactions | Works well for development, but lacks fine-grained concurrency controls. |

### 🔹 **Key Considerations:**
- **PostgreSQL** is the **best choice** for handling complex transactions due to its robust ACID compliance.
- **MySQL (InnoDB)** is reliable but may have **implicit commits** on schema changes or certain SQL operations.
- **MyISAM** (MySQL’s non-transactional engine) does not support `transaction.atomic()`.
- **SQLite** supports transactions but has **limited concurrency support**.

### 🔹 **Example: Using `transaction.atomic()` in PostgreSQL & MySQL (InnoDB)**

```python
from django.db import transaction

try:
    with transaction.atomic():
        order = Order.objects.create(customer="John Doe", total=100)
        payment = Payment.objects.create(order=order, status="Pending")
except Exception as e:
    print(f"Transaction failed: {e}")
    # Any database changes inside `atomic()` will be rolled back
```
This ensures that either both Order and Payment are saved, or neither of them is saved, preserving data consistency.

## 7. What is Django’s default transaction behavior?

By default, Django uses **autocommit mode**, meaning that each database query is immediately committed unless explicitly wrapped in a transaction block.

### 🔹 **Django’s Default Behavior**
- Every database operation is automatically committed unless it is inside `transaction.atomic()`.
- If an error occurs **outside** of `transaction.atomic()`, **only that query fails**, and the database remains unchanged.
- If an error occurs **inside** `transaction.atomic()`, Django **rolls back** all changes within the transaction block.

### ✅ **Example: Default Autocommit Behavior**
```python
# This query is automatically committed to the database
user = User.objects.create(username="autocommit_user")
```

## ✅ Example: Using `transaction.atomic()` to Disable Autocommit

```python
from django.db import transaction

try:
    with transaction.atomic():
        order = Order.objects.create(customer="Alice", total=200)
        payment = Payment.objects.create(order=order, status="Pending")
        # If an exception occurs, both `Order` and `Payment` are rolled back
except Exception as e:
    print(f"Transaction failed: {e}")
```

## 🔹 How to Manually Disable Autocommit?

You can manually disable autocommit using the Django database connection object:

```python
from django.db import connection

connection.set_autocommit(False)
```
**Use this carefully** as it requires manually managing transactions.  
It is **recommended to use `transaction.atomic()` instead**.

---

## 🔹 Key Takeaways

- **Autocommit is enabled by default** – every query is committed immediately.
- Use **`transaction.atomic()`** to ensure multiple queries are executed as a single transaction.
- **Manually disabling autocommit** is possible but **not recommended in most cases**.
