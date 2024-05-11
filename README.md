# Gerador de Readme

## Descrição do Projeto
Este projeto consiste em um Gerador de Documentação Automática para arquivos README.md. Utilizando a API do Google Gemini, a ferramenta analisa código fonte fornecido pelo usuário e gera um arquivo README.md completo e bem estruturado, facilitando a documentação de projetos de software.

## Funcionalidades
- Geração automática de arquivos README.md a partir de código fonte.
- Análise de código em diversas linguagens de programação (Python, JavaScript, Java, C++, C, HTML, CSS).
- Interface web amigável para interação com o usuário.
- Documentação abrangente, informativa e de fácil compreensão para públicos técnicos e não técnicos.

## Como Usar

1. **Acesse a interface web:** Abra o arquivo `index.html` em seu navegador.
2. **Preencha as informações do projeto:**
   - **Nome do Projeto:** Insira o nome do seu projeto.
   - **Breve Descrição:** Forneça uma descrição concisa do projeto.
   - **Diretório do Projeto:** Indique o caminho para o diretório raiz do seu projeto, onde se encontram os arquivos de código fonte.
   - **Detalhes Adicionais (opcional):** Acrescente informações extras relevantes, como dependências, tecnologias utilizadas, autores, etc.
3. **Clique em "Enviar"**:  A ferramenta enviará as informações para a API do Gemini, que processará o código e gerará a documentação.
4. **Faça o download do arquivo README.md:** Após a geração da documentação, clique no botão "Download README" para baixar o arquivo README.md gerado.

## Estrutura do Projeto

O projeto consiste nos seguintes arquivos:
- `main.py`: Contém o código da API FastAPI que recebe as informações do projeto e interage com a API do Google Gemini para gerar a documentação.
- `index.html`: Define a interface web do gerador de Readme.
- `style.css`: Define os estilos visuais da interface web.
- `script.js`: Contém a lógica JavaScript da interface web, incluindo o envio das informações para a API e o download do arquivo README.md.

## Dependências

- Python 3.7 ou superior
- FastAPI
- Uvicorn
- Google Gemini API 

Certifique-se de ter as dependências instaladas em seu ambiente antes de executar o projeto.

## Instalação e Execução

1. **Clone o repositório:**
```
git clone https://github.com/seu-usuario/gerador-readme.git
```
2. **Instale as dependências:**
```
pip install -r requirements.txt
```
3. **Configure a API Key do Google Gemini:**
    - Insira sua API Key no arquivo `main.py` na variável `GOOGLE_API_KEY`.
4. **Execute a aplicação:**
```
uvicorn main:app --reload
```

## Observações
- É fundamental ter uma API Key válida do Google Gemini para que o gerador funcione corretamente.
- A qualidade da documentação gerada depende da qualidade e organização do código fonte fornecido.
- É recomendável revisar o arquivo README.md gerado e realizar ajustes manuais para garantir a precisão e completude da documentação.
- Este projeto é um ponto de partida para a geração de documentação automatizada e pode ser expandido com novas funcionalidades e recursos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias para o projeto.