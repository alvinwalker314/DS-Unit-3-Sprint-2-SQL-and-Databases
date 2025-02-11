import sqlite3
connection = sqlite3.connect('northwind_small.sqlite3')
c = connection.cursor()
c.execute("SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10")
c.fetchall()
'''[('Côte de Blaye', 263.5),
 ('Thüringer Rostbratwurst', 123.79),
 ('Mishi Kobe Niku', 97),
 ("Sir Rodney's Marmalade", 81),
 ('Carnarvon Tigers', 62.5),
 ('Raclette Courdavault', 55),
 ('Manjimup Dried Apples', 53),
 ('Tarte au sucre', 49.3),
 ('Ipoh Coffee', 46),
 ('Rössle Sauerkraut', 45.6)]
'''
c.execute("SELECT AVG(HireDate-BirthDate) FROM Employee")
c.fetchone()
# (37.22222222222222,)

##Part 2
c.execute("SELECT ProductName, Product.UnitPrice, Supplier.CompanyName FROM Product INNER JOIN Supplier ON Product.SupplierId = Supplier.Id ORDER BY UnitPrice DESC LIMIT 10")
c.fetchall()

'''[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
 ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
 ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
 ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
 ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
 ('Raclette Courdavault', 55, 'Gai pâturage'),
 ('Manjimup Dried Apples', 53, "G'day, Mate"),
 ('Tarte au sucre', 49.3, "Forêts d'érables"),
 ('Ipoh Coffee', 46, 'Leka Trading'),
 ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
 '''

c.execute("SELECT DISTINCT COUNT(ProductName) FROM Product GROUP BY CategoryId")
c.fetchall()

# [(12,), (13,), (10,), (7,), (6,), (5,)]

#Stretch
c.execute("SELECT City, AVG(HireDate-BirthDate) FROM Employee GROUP BY City")
'''[('Kirkland', 29.0),
 ('London', 32.5),
 ('Redmond', 56.0),
 ('Seattle', 40.0),
 ('Tacoma', 40.0)]
 '''
#2nd stretch
c.execute("SELECT EmployeeId, COUNT(TerritoryId) as total FROM EmployeeTerritory GROUP BY EmployeeId ORDER BY total DESC LIMIT 1")
c.fetchone()
#(7, 10)
