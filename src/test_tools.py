from tools import tools

# Access the actual function from the StructuredTool
request_price_func = tools["request_price"].func

# Call it with a product name
product_name = "laptop"
result = request_price_func(product_name)

print("Response API Tool:", result)

# Access the actual function from the StructuredTool
calculate_func = tools["calculate"].func

print("Response Calculate Tool:", calculate_func("3*12"))