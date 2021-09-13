from shop.models import Product
from shop.recommender import Recommender

black_tea = Product.objects.get(translations__name='Black Tea')
red_tea = Product.objects.get(translations__name='Red Tea')
green_tea = Product.objects.get(translations__name='Green Tea')
tea_powder = Product.objects.get(translations__name='Tea Powder')

# Then, add some test purchases to the recommendation engine:
r = Recommender()
r.products_bought([black_tea, red_tea])
r.products_bought([black_tea, green_tea])
r.products_bought([red_tea, black_tea, tea_powder])
r.products_bought([green_tea, tea_powder])
r.products_bought([black_tea, tea_powder])
r.products_bought([red_tea, green_tea])

# Let's activate a language to retrieve translated products and get product
# recommendations to buy together with a given single product:
from django.utils.translation import activate
activate('en')

r.suggest_products_for([black_tea])
# >>> [<Product: Tea powder>, <Product: Red tea>, <Product: Green tea>]

r.suggest_products_for([red_tea])
# >>> [<Product: Black tea>, <Product: Tea powder>, <Product: Green tea>]

r.suggest_products_for([green_tea])
# >>> [<Product: Black tea>, <Product: Tea powder>, <Product: Red tea>]

r.suggest_products_for([tea_powder])
# >>> [<Product: Black tea>, <Product: Red tea>, <Product: Green tea>]

# You can see that the order for recommended products is based on their score. Let's
# get recommendations for multiple products with aggregated scores:

r.suggest_products_for([black_tea, red_tea])
# >>> [<Product: Tea powder>, <Product: Green tea>]

r.suggest_products_for([green_tea, red_tea])
# >>> [<Product: Black tea>, <Product: Tea powder>]

r.suggest_products_for([tea_powder, black_tea])
# >>> [<Product: Red tea>, <Product: Green tea>]