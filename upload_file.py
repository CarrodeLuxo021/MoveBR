from flask import Flask, request, render_template, redirect, session
from datetime import datetime
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Configuração da conexão com o Azure Blob Storage
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=movebr;AccountKey=zTfue7Cp+hW60myep4Owt8+oTulr/4VVkCybbzXZIOZep0jaNv2nrtqccg3zd4es/0gs97UJJFi1+AStz0ge3w==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "fotos-movebr"
LINK_AZURE = "https://movebr.blob.core.windows.net/"

# Função para upload de arquivo para o Azure Blob Storage
def upload_file(file) -> str:
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)

    if file.filename == '':
        return ""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file.filename = f"{timestamp}_{file.filename}"

    try:
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.filename)
        blob_client.upload_blob(file, overwrite=True)
        return f"{LINK_AZURE}{CONTAINER_NAME}/{file.filename}"
    except Exception as e:
        print(f"Erro ao fazer upload da foto: {e}")
        return ""
