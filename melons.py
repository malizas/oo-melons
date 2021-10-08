"""Classes for melon orders."""
class AbstractMelonOrder():

    def __init__(self, species, qty, order_type):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
    
    def get_total(self):
        if self.species == "christmas melon":
            base_price = 7.5
        else:   
            base_price = 5
            
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    # order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    # order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, order_type, country_code):
        super().__init__(species, qty, order_type) # refers back to the __init__ function from line 4
        self.country_code = country_code

    def get_country_code(self):
        return self.country_code
    
    



# class DomesticMelonOrder():
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder():
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code