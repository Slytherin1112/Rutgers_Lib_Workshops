import cbpro
public_client = cbpro.PublicClient()
#Get Products
#print(public_client.get_products())
# Get the order book at the default level.
#print(public_client.get_product_order_book('BTC-USD'))
# Get the order book at a specific level.
#print(public_client.get_product_order_book('BTC-USD', level=2))
print(public_client.get_currencies())