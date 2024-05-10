from fastapi import FastAPI
from fastapi.responses import FileResponse
import google.generativeai as genai
import os
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate-documentation/")
def generate_documentation(
    project_directory: str,
    project_name: str,
    project_description: str,
    project_details: Optional[str] = None
) -> None:
    
    """
    Generates a Markdown README.md file for a project using the Gemini API.

    Args:
        project_directory: Path to the project directory containing code files.
        project_name: Name of the project.
        project_description: Brief description of the project.
        project_details: Optional additional details about the project.
    """

    GOOGLE_API_KEY = "place-your-google-api-key-here"
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest')

    # Gather code content from files in the project directory
    code_content = ""
    for root, _, files in os.walk(project_directory):
        for filename in files:
            if not filename.endswith((".py", ".js", ".java", ".cpp", ".c", ".html", ".css")):
                continue  # Process only relevant code files
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                code_content += filename + "\n" + f.read() + "\n\n"

    # Prepare the prompt for the Gemini API
    prompt = str(
        f"""begin:
Generate comprehensive project documentation based on the following information:

Project Name: {project_name}
Project Description: {project_description}
Additional details: {project_details or ''}


Ensure the documentation is well-structured, informative, and easy to understand for both technical and non-technical audiences.

Additional Considerations:

* Use clear and concise language.
* Include visuals such as diagrams and screenshots where appropriate.
* Maintain a consistent style and formatting throughout the document.
* Consider the specific needs of the target audience.

Code:

{code_content}
"""
    )

    # Send the request to the Gemini API
    response = model.generate_content(prompt)

    # Process the response and create the README.md file

    documentation = response.text
    file_path = "./temp/README.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(documentation)
    return FileResponse(path=file_path)