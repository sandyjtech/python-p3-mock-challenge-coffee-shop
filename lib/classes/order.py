


class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
           
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if type(value) in (int, float) and 1 <= value <= 10:
            self._price = value
        else:
            raise Exception("Price must be a number between 0 and 10")
        
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception
        
    @coffee.setter
    def coffee(self, value):
        from classes.coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Customer must be object Coffee")
        
    def __repr__(self):
        return f"<Order: {self.customer} {self.coffee} ${self.price} >"
    
        
    
