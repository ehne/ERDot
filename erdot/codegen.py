from b import template as t
from phi.api import *

_="Int(10)"

a = lambda p: f"Char({int(p*140)})"

tables ={
    "Customer":{
        "*CustomerID":_,
        "FullName":a(0.5)
    },
    "CustomerAddress":{
        "+*CustomerID":_,
        "+*AddressID":_
    },
    "Address":{
        "*AddressID": _,
        "AddressLine1":a(1),
        "AddressLine2":a(1),
        "City":a(1),
        "Postcode": "Char(4)",
        "State":a(0.5),
        "Country":a(0.5)
    },
    "PhoneNumber":{
        "*PhoneNumber":"Char(10)",
        "+CustomerID":_,
        "Description":a(0.5)
    },
    "Venue":{
        "*VenueID":_,
        "+AddressID":_,
        "PhoneNumber":"Char(10)",
        "Name":a(0.5)
        # figure out date ranges?
    },
    "Room": {
        "*RoomID":_,
        "+VenueID":_,
        "Name":a(0.5),
        "Description":a(2),
        "PricePerDay":"Float()",
        "NumberOfBeds":"Int()"
    },
    # "DateRange":{
    #     "*DateRangeID":_,
    #     "RangeStartDate":"DateTime()",
    #     "RangeEndDate":"DateTime()"
    # },
    # "RoomDateRange":{
    #     "+*DateRangeID":_,
    #     "+*RoomID":_,
    # }
    "Booking":{
        "*BookingID":_,
        "+CustomerID":_,
        "+RoomID":_

    },
    "BookingDate":{
        "*+BookingID":_,
        "*+DateID":_
    },
    "Date":{
        "*DateID":_,
        "Date":"Date()"
    },
    "Facility":{
        "*FacilityID":_,
        "+VenueID":_,
        "FacilityName":a(0.5),
        "Description":a(1),
    }
}


relations =[
    "Customer:CustomerID 1--* PhoneNumber:CustomerID",
    "Venue:AddressID 1--1 Address:AddressID",
    "Customer:CustomerID 1--+ CustomerAddress:CustomerID",
    "Address:AddressID 1--1 CustomerAddress:AddressID",
    "Room:VenueID +--1 Venue:VenueID",
    #"Room:RoomID 1--* RoomDateRange:RoomID",
    #"DateRange:DateRangeID 1--* RoomDateRange:DateRangeID "
    "Room:RoomID 1--* Booking:RoomID",
    "Customer:CustomerID 1--* Booking:CustomerID",
    "Booking:BookingID 1--+ BookingDate:BookingID",
    "BookingDate:DateID +--1 Date:DateID",
    "Venue:VenueID 1--* Facility:VenueID"
]

rankAdjustments = "" 
"""
{ rank=min; Address PhoneNumber };
{ rank=same; Member };
{ rank=max; Pet };
"""

graphExtras="""
labeljust=r,
"""
label = ""


file = open("eh.dot","w+")
stringGen = t("relations", tables=tables, relations=relations,ra=rankAdjustments,gs=graphExtras,lbl=label)

file.write(stringGen)

