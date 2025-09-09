import requests
import os
from urllib.parse import urlparse
import hashlib

def generate_filename(url, content):
    """
    Generate a filename from the URL if possible.
    If no filename is available, generate one using a hash of the content.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or '.' not in filename:  # no filename or no extension
        # Generate a unique filename based on hash of content
        hash_digest = hashlib.md5(content).hexdigest()[:10]
        filename = f"downloaded_image_{hash_digest}.jpg"

    return filename

def download_image(url):
    """
    Download an image from the given URL and save it into Fetched_Images directory.
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error for bad HTTP codes

        # Validate content type
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print(f"✗ The URL does not point to an image: {url}")
            return

        # Extract/generate filename
        filename = generate_filename(url, response.content)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicates
        if os.path.exists(filepath):
            print(f"⚠ Image already exists: {filename}, skipping download.")
            return

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Accept multiple URLs separated by commas
    urls = input("Please enter one or more image URLs (comma separated): ")
    urls = [u.strip() for u in urls.split(",") if u.strip()]

    for url in urls:
        download_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
