##storefront

**This is a Backend e_commerce project built with **Django and DRF to practice building REST APIs.
**This project is still a work in progress (almost done !)
**I will push The finished VERSION of it Soon !


## Features
- **Products**: and Collections Management : Full CRUD operations for store items (with Viewsets and CBV).
- **Nested Routing**: sub_resource handling Using "drf_nested_routers" . (e.g : reveiws for a specific product :(/products/:id/reviews/) )
- **Modular Architecture**: Clean sepration of concerns with dedicated apps. (e.g :'store' , 'liks' , 'tags' , ... )
- **Custom Delete Validation**: prevents deleting cillections or products with related active records .
- **Calculated Serializers fields**: adding extra Fields dynamically Using 'SerializerMethodField' .

## Tech Stack 
- **Framework** : Django & Django Rest Framework (DRF)
- **Database** : MYSQL 
- **Dependencies**: 'django_rest_farmework' , 'drf_nested_routers'



