import glob
import os

for dr in ["Course", "AI-Agent-Masterclass"]:
    path_pattern = f"/Users/umang/Desktop/Umang/AI-Agent-SDK/{dr}/Chapter_*.md"
    for file in glob.glob(path_pattern):
        with open(file, 'r') as f:
            content = f.read()
        
        # Repair the broken file extensions in the markdown links
        content = content.replace('.py)', '.ipynb)')
        content = content.replace('.py](', '.ipynb](')
        
        with open(file, 'w') as f:
            f.write(content)
            
    print(f"Repaired markdown links for {dr}")
