from renderer2 import render_store

manual_json = {
  "store_name": "Green Basket",
  "tagline": "Fresh groceries delivered daily",
  "categories": ["Fruits", "Vegetables", "Dairy", "Snacks"],
  "banners": [
    { "title": "Weekend Sale", "desc": "Up to 40% off" },
    { "title": "Organic Picks", "desc": "Healthy & fresh" }
  ],
  "products": [
    { "name": "Apples", "price": "$4", "img": "apple.jpg" },
    { "name": "Milk", "price": "$2", "img": "milk.jpg" }
  ],
  "contact": {
    "email": "shop@greenbasket.com",
    "phone": "+123456789",
    "city": "New York"
  }
}


folder = render_store(manual_json)
print("HTML generated in:", folder)
