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
    additional_details: Optional[str] = None
) -> None:
    
    """
    Generates a Markdown README.md file for a project using the Gemini API.

    Args:
        project_directory: Path to the project directory containing code files.
        project_name: Name of the project.
        project_description: Brief description of the project.
        additional_details: Optional additional details about the project.
    """

    GOOGLE_API_KEY = "coloque sua api do google ai aqui"
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest')

    # Gather code content from files in the project directory
    code_content = ""
    for root, _, files in os.walk(project_directory):
        for filename in files:
            if not filename.endswith((".py", ".js", ".java", ".cpp", ".c", ".html", ".css", ".rb", ".swift", ".php", ".pl", ".r", ".lua", ".sh", ".scala", ".kt", ".ts", ".dart", ".asm", ".hs")):
                continue  # Process only relevant code files
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                code_content += filename + "\n" + f.read() + "\n\n"

    # Prepare the prompt for the Gemini API
    prompt = str(
        f"""
            Gere uma documentação abrangente em Markdown para o projeto com base nas seguintes informações:

            Nome do Projeto: {project_name}
            Descrição do Projeto: {project_description}
            Detalhes adicionais: {additional_details or 'nenhum'}

            Garanta que a documentação seja bem estruturada, informativa e fácil de entender tanto para um público técnico, quanto para um não técnico.

            Considerações adicionais:

            - Utilize linguagem clara e concisa.
            - Mantenha um estilo e formatação consistentes em todo o documento.
            - Considere as necessidades específicas do público-alvo.
            - Não inclua o código fonte na documentação.
            - Inclua como rodar o backend (se houver um) da aplicação (considere a documentação do framework utilizado) e como acessar a página web (se houver uma) pelo arquivo html.

            Código:

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
