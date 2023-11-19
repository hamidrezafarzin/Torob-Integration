# Import the Torob class
from torob_integration.api import Torob

# Create an instance of the Torob class
torob_instance = Torob()

# Example 1: Fetch product suggestions based on a query
suggestion_result = torob_instance.suggestion("laptop")
print("Product Suggestions:")
print(suggestion_result)
print("\n" + "=" * 50 + "\n")

# Example 2: Perform a search for products based on a query and page number
search_result = torob_instance.search("smartphone", page=1)
print("Search Results:")
print(search_result)
print("\n" + "=" * 50 + "\n")

# Example 3: Get detailed information about a specific product
# Note: Replace 'sample_prk' and 'sample_search_id' with actual values
details_result = torob_instance.details(prk='sample_prk', search_id='sample_search_id')
print("Product Details:")
print(details_result)
print("\n" + "=" * 50 + "\n")

# Example 4: Fetch special offers for products with optional pagination
special_offers_result = torob_instance.special_offers(page=0)
print("Special Offers:")
print(special_offers_result)
print("\n" + "=" * 50 + "\n")

# Example 5: Get the price chart data for a specific product
# Note: Replace 'sample_prk' and 'sample_search_id' with actual values
price_chart_result = torob_instance.price_chart(prk='sample_prk', search_id='sample_search_id')
print("Price Chart:")
print(price_chart_result)
