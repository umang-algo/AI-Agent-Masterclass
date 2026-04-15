import glob
import os
import subprocess

directory = "/Users/umang/Desktop/Umang/AI-Agent-SDK/Course"
output_md = os.path.join(directory, "AI_Agent_Course.md")

# Ensure order: README -> Chapter 1 -> 2 -> ... -> 6
files = [
    "README.md",
    "Chapter_1_Microsoft_Ecosystem.md",
    "Chapter_2_LangChain_Ecosystem.md",
    "Chapter_3_OpenAI_and_Google.md",
    "Chapter_4_Specialized_Open_Source_Frameworks.md",
    "Chapter_5_Enterprise_and_Low_Code_Platforms.md",
    "Chapter_6_Observability_and_Tracing.md"
]

content = ""
for f in files:
    path = os.path.join(directory, f)
    if os.path.exists(path):
        with open(path, "r") as fh:
            content += fh.read() + "\n\n"

with open(output_md, "w") as fh:
    fh.write(content)

print("Concatenated MD successfully!")

# Attempt to build the PDF via npx
try:
    print("Compiling PDF... (this may take a minute if downloading chromium)")
    process = subprocess.run(["npx", "-y", "md-to-pdf", "AI_Agent_Course.md"], cwd=directory, capture_output=True, text=True)
    if process.returncode == 0:
        print("PDF Compilation Successful!")
    else:
        print(f"PDF Compiler Warning (You can safely ignore if you read the .md): {process.stderr}")
except Exception as e:
    print(f"Error accessing npx md-to-pdf: {e}")
