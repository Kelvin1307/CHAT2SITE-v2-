from renderer import render_portfolio_site

manual_json = {
    "business_name": "Kelvin Cakes",
    "tagline": "Fresh cakes made daily",
    "services": ["Birthday Cakes", "Wedding Cakes", "Cupcakes"],
    "city": "Chennai",
    "email": "hello@kelvincakes.in",
    "phone": "+91 9876543210"
}

folder = render_portfolio_site(manual_json)
print("HTML generated in:", folder)
