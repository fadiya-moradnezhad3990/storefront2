# storefront

**This is a Backend E_Commerce project built with **Django and DRF to practice building REST APIs.
**This project is still a work in progress (almost done !)



## Features

- **Products : and Collections Management**: Full CRUD operations for store items (with Viewsets and CBV).
- **Nested Routing**: sub_resource handling Using "drf_nested_routers" . (e.g : reviews for a specific product :(/products/:id/reviews/) )
- **Modular Architecture**: Clean separation of concerns with dedicated apps. (e.g :'store' , 'likes' , 'tags' , ... )
- **Custom Delete Validation**: prevents deleting collections or products with related active records .
- **Calculated Serializers fields**: adding extra Fields dynamically Using 'SerializerMethodField' .

### SHOPPING CART API

#### What i did in this section :

- **Database Performance & Optimization:**
  - Resolved the classic **$N+1$ query issue** by utilizing `select_related('product')`, reducing round-trip database queries to a single efficient SQL `JOIN`.
  
- **API Security & Resource Protection:**
  - Used non-sequential **UUIDs** instead of standard auto-incrementing integers for Cart IDs, preventing URL enumeration and ID scraping attacks.
  - Enforced strict authorization and resource boundaries using scoped querysets in ViewSets (`get_queryset`).

- **RESTful Hierarchy & Clean Routing:**
  - Designed the API structure using `drf-nested-routers`, ensuring that child resources cannot exist without their parent container (e.g., `/carts/{cart_pk}/items/`).

- **Data Integrity & Upsert Logic:**
  - Implemented custom business logic inside `CartItemSerializer.save()`: handles atomic updates by automatically incrementing item `quantity` for existing products instead of generating duplicate entries or returning database constraint errors.
  - Added custom field-level validation (`validate_product_id`) to verify product existence prior to persistence.



## Tech Stack 
- **Framework** : Django & Django Rest Framework (DRF)
- **Database** : MYSQL 
- **Dependencies**: 'django_rest_framework' , 'drf_nested_routers'
