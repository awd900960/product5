import os
def read_file(filename):
	    products = []
	    with open (filename, 'r' encoding='utf-8') as f :
	    	for line in f:
	    		if 'product,price' in line:
	    			   contiune
	    			   name, price = line.strip().split(',')
	    			   products.append([name,price])
	    return.products
	    


def user_input(products):
	while Ture:
	         name = input('please input product name')	
	         if name == 'q':
	           	      break
            price = input('please input product price')
            price = int(price)
            products.append([name,price])
        print(products)
        return products
def print_products(products):
    for p in products:
             print(p[0], 'the price is',p[1])

def write_file(filename, products):
	with open('products.csv','w',encoding = 'utf-8') as f:
		     f.write('products,price\n')
		for p in products:
		          f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
		 filename = 'products.csv'
	if os.path.isfile('products.csv'):
	         print('yeah!,have file')
	     products = read_file(filename)
	else:
	       print("can't find file" )
	products = user_input(products)
	print_products(products)
	write_file('products.csv',products) 

main()

refactor
	            
