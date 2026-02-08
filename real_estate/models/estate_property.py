from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string = "Name")  # technical name if we dont give a name to this then it use default name
    property_type = fields.Selection([
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa')
    ], string = "Property Type")
    postcode = fields.Char(string = "Postcode")
    available_from = fields.Date(string = "Available From")

    expected_price = fields.Float(string = "Expected Price")
    selling_price = fields.Float(string = "Selling Price")

    bedrooms = fields.Integer(string = "Bedroom")
    living_area = fields.Float(string = "Living Area (sqm)")

    garage = fields.Boolean(string = "Garage")
    garden = fields.Boolean(string = "Garden")

    description = fields.Text(string = "Description")