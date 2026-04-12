from jinja2 import Environment, FileSystemLoader
import os

def render_page(data: dict):
    output_dir = "site_output"
    os.makedirs(output_dir, exist_ok=True)

    # Load HTML template
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")

    # Render HTML
    output = template.render(data=data)

    # Save output file
    with open(f"{output_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(output)

    print("✅ HTML generated → site_output/index.html")
    return output_dir