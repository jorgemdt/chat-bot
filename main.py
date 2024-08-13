from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import recursos
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Configurar a API com FastAPI
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir requisições de todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Obter e configurar a chave da API
API_KEY = recursos.api_key()
genai.configure(api_key=API_KEY)

# Definir o modelo generativo
model = genai.GenerativeModel("gemini-1.5-pro")

# Classe que representa o corpo da requisição
class PromptRequest(BaseModel):
    prompt: str

# Rota que processa o prompt e retorna a resposta
@app.post("/chat/")
def chat_with_model(request: PromptRequest):
    prompt = request.prompt
    
    try:
        # Iniciar o chat e enviar o prompt
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        
        # Retornar a resposta gerada
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Iniciar o servidor com Uvicorn (opcional)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
