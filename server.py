from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import httpx

app = FastAPI()

# Lista para armazenar conexões WebSocket ativas
active_connections = []

# Função que simula o monitoramento de uma API externa
async def monitor_api(api_url: str, websocket: WebSocket):
    while True:
        # Simula a verificação de uma API (por exemplo, uma verificação a cada 5 segundos)
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            if response.status_code == 200:
                # Envia uma notificação quando a API estiver OK ou retornar algum dado
                await websocket.send_text(f"Notificação: A API {api_url} retornou sucesso.")
        await asyncio.sleep(5)  # Aguarda 5 segundos antes de fazer nova verificação

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Aceita a conexão WebSocket
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        # Aqui você pode passar as APIs que deseja monitorar
        api_urls = [
            "https://api.exemplo1.com/monitor",
            "https://api.exemplo2.com/monitor"
        ]
        
        # Para cada URL de API, cria uma tarefa assíncrona para monitorá-las
        tasks = [monitor_api(api_url, websocket) for api_url in api_urls]
        await asyncio.gather(*tasks)

    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print("Conexão WebSocket fechada.")

