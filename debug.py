from customer import Customer
from coffee import Coffee
from order import Order
Cate = Customer("Cate")
Cupchinno= Coffee("Cupchinno")

order = Cate.create_order(Cupchinno,5.0)

print("Customer:", Cate.name) 

print("Coffee:", Cupchinno.name)
print("Orders:", Cate.orders())
print("Coffees ordered by Cate:", [c.name for c in Cate.coffees()])
print("Cupchinno num_orders:", Cupchinno.num_orders())
print("Cupchinno average price:", Cupchinno.average_price())