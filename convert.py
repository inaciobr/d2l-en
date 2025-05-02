import os
import subprocess

def convert_md_to_ipynb(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                ipynb_path = os.path.splitext(md_path)[0] + ".ipynb"
                
                print(f"Converting: {md_path} -> {ipynb_path}")
                with open(ipynb_path, "w") as outfile:
                    subprocess.run(["notedown", md_path], stdout=outfile)

# Example usage:
convert_md_to_ipynb(".")
