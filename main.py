# Bloco 1: Importações 
# Bibliotecas padrão do Python
import os
import time

# Bibliotecas de terceiros (instaladas via pip)
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

# Carregar variáveis do .env 
load_dotenv()

SUPABASE_URL      = os.getenv("SUPABASE_URL")
SUPABASE_KEY      = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE     = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN        = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")


# Validação das variáveis de ambiente
def validar_config() -> None:
  """Garante que todas as variáveis de ambiente estão definidas."""
  if not all([SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE, ZAPI_TOKEN, CLIENT_TOKEN]):
      print("❌ Variáveis de ambiente incompletas. Verifique o .env")
      exit(1)


# Função que busca contatos no Supabase
def buscar_contatos() -> list:
  """Busca até 3 contatos da tabela 'contatos'."""
  cliente: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
  resposta = (
      cliente
      .table("contatos")
      .select("*")
      .limit(3)
      .execute()
  )
  return resposta.data


# Função que envia mensagem via Z-API
def enviar_mensagem(telefone: str, nome: str) -> None:
  """Envia a mensagem personalizada para o número recebido."""
  url = (
      f"https://api.z-api.io/instances/{ZAPI_INSTANCE}"
      f"/token/{ZAPI_TOKEN}/send-text"
  )
  headers = {
      "Client-Token": CLIENT_TOKEN,
      "Content-Type": "application/json",
  }
  mensagem = f"Olá, {nome} tudo bem com você?"
  corpo    = {"phone": telefone, "message": mensagem}

  try:
      resposta = requests.post(url, headers=headers, json=corpo)
      if resposta.status_code == 200:
          print(f"✅ Enviado para {nome} ({telefone})")
      else:
          print(f"❌ Erro {resposta.status_code} ao enviar para {nome}")
          print(f"   Detalhe: {resposta.text}")
  except Exception as erro:
      print(f"❌ Falha inesperada ao enviar para {nome}: {erro}")


# Função principal
def main() -> None:
  """Orquestra a busca dos contatos e o envio das mensagens."""
  validar_config()
  print("🚀 Iniciando envio de mensagens...")

  contatos = buscar_contatos()

  if not contatos:
      print("⚠️  Nenhum contato encontrado no banco.")
      return

  print(f"📋 {len(contatos)} contato(s) encontrado(s).")

  for contato in contatos:
      nome     = contato["nome"]
      telefone = contato["telefone"]
      enviar_mensagem(telefone, nome)
      time.sleep(1)

  print("✅ Processo finalizado!")


# Ponto de entrada
if __name__ == "__main__":
  main()