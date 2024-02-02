# SELECT 
#     t1.column1,
#     t1.column2,
#     t2.column3
# FROM
#     Table1 AS t1
# JOIN
#     Table2 AS t2
# ON
#     t1.key = t2.key;


# SELECT 
#     Person.FirstName,
#     Person.LastName,
#     Address.City,
#     Address.State
# FROM
#     Person
# LEFT JOIN
#     Address
# ON
#     Person.PersonId = Address.PersonId;