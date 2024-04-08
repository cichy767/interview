1
Lazy loading is the default behavior of most ORM tools, such as Hibernate, SQLAlchemy, or Django ORM. 
It means that the ORM will only fetch the data that you explicitly request from the database, and delay loading any related data until you access them. 
For example, if you have a User model and a Post model, and you query for a user, the ORM will not fetch the user's posts until you call user.posts. 
This can reduce the initial query time and memory usage, but it can also lead to multiple queries and performance issues if you need to access the related data later.


2
Eager loading is the opposite of lazy loading. 
It means that the ORM will fetch all the data that you might need from the database in one query, including the related data. 
For example, if you query for a user, the ORM will also fetch the user's posts in the same query, using a join or a subquery. 
This can improve the performance and avoid the N+1 query problem, which occurs when you need to make one query for each related object. 
However, eager loading can also increase the query complexity and memory usage, and fetch unnecessary data if you don't need them.

3
How to choose
The choice between lazy loading and eager loading depends on your application's needs and trade-offs. 
Generally, lazy loading is more suitable for scenarios where you don't need to access the related data frequently, or where you need to filter or paginate the related data. 
Eager loading is more suitable for scenarios where you need to access the related data often, or where you need to perform calculations or aggregations on the related data. 
You can also use a hybrid approach, where you selectively eager load some data and lazy load others, depending on the context.

**select_related()**
"follows" foreign-key relationships, selecting additional related-object data when it executes its query.
OneToOneField or a ForeignKey


**prefetch_related()**
does a separate lookup for each relationship, and does the "joining" in Python.
reversed OneToMany(ForeignKey) or ManyToMany


Just to clarify what I mean by reverse ForeignKeys, here's an example:
```
{
    class ModelA(models.Model):
        pass
    class ModelB(models.Model):
        a = ForeignKey(ModelA)
}


#Forward ForeignKey relationship**
ModelB.objects.select_related('a').all()

#Reverse ForeignKey relationship**
ModelA.objects.prefetch_related('modelb_set').all() 
```
The difference is that:

select_related does an SQL join and therefore gets the results back as part of the table from the SQL server
prefetch_related on the other hand executes another query and therefore reduces the redundant columns in the original object (ModelA in the above example)
You may use prefetch_related for anything that you can use select_related for.

The tradeoffs are that prefetch_related has to create and send a list of IDs to select back to the server, this can take a while. I'm not sure if there's a nice way of doing this in a transaction, but my understanding is that Django always just sends a list and says SELECT ... WHERE pk IN (...,...,...) basically. In this case if the prefetched data is sparse (let's say U.S. State objects linked to people's addresses) this can be very good, however if it's closer to one-to-one, this can waste a lot of communications. If in doubt, try both and see which performs better.

Everything discussed above is basically about the communications with the database. On the Python side however prefetch_related has the extra benefit that a single object is used to represent each object in the database. With select_related duplicate objects will be created in Python for each "parent" object. Since objects in Python have a decent bit of memory overhead this can also be a consideration.