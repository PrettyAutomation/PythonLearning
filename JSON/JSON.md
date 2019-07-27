#### Understanding JSON
##### Rules
- Its a key value pair
- Key always a String
- Value can be [](Array),{}[Object], Boolean, String, Number/Float, Date
- We can not have any comment in JSON
- there are rules for the key naming
```JSON
{
  "name" : "Pretty"
}
```

Above JSON have `name` is key and its value is string `Pretty`

###### Complex JSON
```JSON
{
  "name": "Pretty",
  "address": {
    "street": "17",
    "houseNumber": 118,
    "phoneNumber": 23423232
  },
  "tags": ["Software Engineer", "Person", "Human being"],
  "isDaughter": true
}
```

Above JSON is having different type of values in complex nature

You can have multilevel of nesting
Accessing deep value using dot operation e.g. name.address.street is value of "17"
Array can be access via indexing
