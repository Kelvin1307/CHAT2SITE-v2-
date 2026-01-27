# renderer.py
import os

def render_portfolio_site(data: dict) -> str:
    output_dir = "site_output"
    os.makedirs(output_dir, exist_ok=True)

    # Explicit traversal
    name = data.get("business_name", "My Business")
    tagline = data.get("tagline", "")
    services = data.get("services", [])
    city = data.get("city", "")
    email = data.get("email", "")
    phone = data.get("phone", "")

    services_html = "".join(f"<li>{s}</li>" for s in services)

    html = f"""
<!DOCTYPE html>
<html>
<head>
  <title>{name}</title>
  <style>
    body {{ font-family: Arial; padding: 40px; }}
  </style>
</head>
<body>
  <h1>{name}</h1>
  <p>{tagline}</p>

  <h2>Services</h2>
  <ul>{services_html}</ul>

  <h3>Contact</h3>
  <p>{city}</p>
  <p>{email}</p>
  <p>{phone}</p>
</body>
</html>
"""

    with open(f"{output_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    return output_dir
