def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices #Return empty list
#Passing in list of products and the target product name as argument
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Apple"
result = linear_search_product(products, target)
print("The Target is found at the indices is :",result)