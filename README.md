In this repository, you would get information on how to build RESTFul APIs with Django Rest Framework.
So what will I do in this prj? -- CRUD
    1. Create a table fo items (name)
    2. create a table for suppliers (name of supplier, contact-info)
    3. create a table for stor inventories, that will have a relationship with items and suppliers foreign key relationship with supplier model
        supplier-name
        --
        description
        list of items
        --
        foreign key relationship with items model
        date the inventories were created
    4. Creare a serializers.py to serialize our models into readable format like json
    5. Create a generics api views capturing CRUD operations
    6. Create the urls endpoints for our different apis
    7. Push github
        Create, Retrieve, Update, Delete
