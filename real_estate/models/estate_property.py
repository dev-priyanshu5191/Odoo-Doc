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
    facades = fields.Integer(string ="Facades")
    bedrooms = fields.Integer(string = "Bedroom")
    living_area = fields.Float(string = "Living Area (sqm)")

    garage = fields.Boolean(string = "Garage")
    garden = fields.Boolean(string = "Garden")
    garden_area = fields.Integer(string ="Garden Area")

    garden_orientation = fields.Selection([
        ('east', 'East'), ('west', 'West'), ('north', 'North'), ('south', 'South')
    ], string = "Garden Orientation")

    description = fields.Text(string = "Description")