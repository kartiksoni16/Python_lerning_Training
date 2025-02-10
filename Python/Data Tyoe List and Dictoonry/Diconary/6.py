def manage_pricelist():
    pricelist = {}

    while True:
        product = input("Enter product (or press Enter to finish): ").strip()
        
        if not product:
            break
        
        try:
            price = float(input(f"Enter price for {product}: "))
        except ValueError:
            print("Invalid price, please enter a numeric value.")
            continue
        
        pricelist[product] = price

    if pricelist:
        print("\nProduct Pricelist:")
        print(f"{'Product':<20} {'Price':<10}")
        print("-" * 30)
        for product, price in pricelist.items():
            print(f"{product:<20} {price:<10.2f}")
    else:
        print("No products added.")

manage_pricelist()
