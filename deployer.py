# deployer.py
import os
import subprocess
import uuid

SITE_ID="44a57d88-e7aa-4ffe-9b50-78897fdf25fb"
NETLIFY_AUTH_TOKEN = "nfp_qXLJNASVvn2SKS7w7DLm6srM97h5YwSE939f"

def deploy_site(folder: str) -> str:
    site_name = f"chat2site-{uuid.uuid4().hex[:6]}"

    subprocess.run([
    r"C:\Users\TIMOTHY KELVIN M\AppData\Roaming\npm\netlify.cmd",
    "deploy",  "--prod", "--dir", folder, "--site", SITE_ID, "--auth", NETLIFY_AUTH_TOKEN], check=True)

    return f"https://{site_name}.netlify.app"
