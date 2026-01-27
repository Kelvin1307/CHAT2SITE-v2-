# deployer.py
import os
import subprocess
import uuid

SITE_ID = os.getenv("SITE_ID")
NETLIFY_AUTH_TOKEN = os.getenv("NETLIFY_AUTH_TOKEN")

def deploy_site(folder: str) -> str:
    site_name = f"chat2site-{uuid.uuid4().hex[:6]}"

    subprocess.run([
    r"C:\Users\TIMOTHY KELVIN M\AppData\Roaming\npm\netlify.cmd",
    "deploy",  "--prod", "--dir", folder, "--site", SITE_ID, "--auth", NETLIFY_AUTH_TOKEN], check=True)

    return f"https://{site_name}.netlify.app"
