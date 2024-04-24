# What does transaction.on_commit() do in Django?

In Django, transaction.on_commit() is a function that allows you to schedule functions or tasks to be executed only after a database transaction has been successfully committed. 
This is particularly useful when you have operations that should only occur if the entire transaction completes successfully, without any rollbacks, 
such as sending a confirmation email after a user's registration is successfully saved to the database.


# What does transaction.atomic() do in Django?

In Django, transaction.atomic() is used to ensure that a block of code is executed within a database transaction, 
making sure that all database operations within the block are either fully completed or fully rolled back in case of an error. 
This is crucial for maintaining data integrity, especially when multiple related operations are dependent on each other to maintain consistency within the database.