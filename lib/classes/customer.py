from classes.order import Order
class Customer:
    
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Value must be a string between 1 and 15 characters")   
               
    def orders(self):
       from classes.order import Order       
       return [order for order in Order.all if order.customer == self] 
    
    def coffees(self):               
      unique_list = set([order.coffee for order in self.orders()])
      return list(unique_list)
    
    def create_order(self, coffee, price):             
       Order(self, coffee, price)             
       
    
    def __repr__(self):
        return f"<Customer: {self._name} >"