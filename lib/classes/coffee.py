from classes.order import Order

class Coffee:
    def __init__(self, name):
        self.name = name        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, 'name'):
            self._name = value
        else:
            raise Exception("Invalid operation")        
        
    def orders(self):              
       return [order for order in Order.all if order.coffee == self]               
  
    def customers(self):
        #converting into unique list
        return [*set([order.customer for order in self.orders()])]      
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):        
        order = [order.price for order in self.orders()]
        return sum(order) / self.num_orders()
    
    def __repr__(self):
        return f"<Coffee: {self._name} >"
    
    