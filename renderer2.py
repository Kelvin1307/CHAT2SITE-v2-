import os

def render_store(data: dict) -> str:
    output_dir = "site_output"
    os.makedirs(output_dir, exist_ok=True)

    name = data.get("store_name", "Fresh Market")
    tagline = data.get("tagline", "Quality groceries delivered fast")
    categories = data.get("categories", ["Fruits", "Vegetables", "Dairy"])
    products = data.get("products", [])
    contact = data.get("contact", {})

    category_html = "".join(
        f"<div class='category'>{c}</div>" for c in categories
    )

    if not products:
        products = [
            {"name": "Sample Item", "price": "$5", "img": "https://via.placeholder.com/200"}
            for _ in range(6)
        ]

    product_html = "".join(
        f"""
        <div class="product">
            <img src="{p.get('img')}" />
            <h3>{p.get('name')}</h3>
            <p class="price">{p.get('price')}</p>
            <button onclick="addCart()">Add to cart</button>
        </div>
        """ for p in products
    )

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<link rel="stylesheet" href="style.css">
<script src="script.js" defer></script>
</head>

<body>

<header class="header">
  <div class="logo">{name}</div>
  <nav>
    <a href="#">Home</a>
    <a href="#">Shop</a>
    <a href="#">Deals</a>
    <a href="#">Contact</a>
  </nav>
</header>

<section class="hero">
  <h1>{tagline}</h1>
  <button>Shop Now</button>
</section>

<section class="categories">
  <h2>Shop by Category</h2>
  <div class="category-grid">
    {category_html}
  </div>
</section>

<section class="products">
  <h2>Featured Products</h2>
  <div class="product-grid">
    {product_html}
  </div>
</section>

<section class="promo">
  <h2>Weekly Deals</h2>
  <p>Save up to 40% on selected items</p>
</section>

<footer>
  <p>{contact.get("email","contact@store.com")}</p>
  <p>{contact.get("phone","+000000000")}</p>
  <p>{contact.get("city","Your City")}</p>
  <p>© 2026 {name}</p>
</footer>

</body>
</html>
"""

    with open(f"{output_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    return output_dir
