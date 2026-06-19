<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white"/>
<img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/>
<img src="https://img.shields.io/badge/Z--API-FF6B35?style=for-the-badge&logoColor=white"/>

<br/>
<br/>

# 📲 Envio de Mensagens via WhatsApp

Script que lê contatos de um banco Supabase e envia mensagens  
personalizadas no WhatsApp via Z-API, de ponta a ponta.

</div>

---

## 🗺️ Como funciona

```
┌─────────────┐     lê contatos     ┌─────────────┐     envia mensagem     ┌─────────────┐
│   Supabase  │ ──────────────────► │   main.py   │ ─────────────────────► │    Z-API    │
│  (banco de  │                     │   (Python)  │                        │ (WhatsApp)  │
│    dados)   │                     │             │                        │             │
└─────────────┘                     └─────────────┘                        └─────────────┘
```

Para cada contato encontrado, o programa monta e envia automaticamente:

> *"Olá, \<nome_contato\> tudo bem com você?"*

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Função |
|---|---|---|
| Python | 3.11+ | Linguagem principal |
| Supabase | — | Banco de dados na nuvem (PostgreSQL) |
| Z-API | — | Gateway de envio pelo WhatsApp |
| python-dotenv | — | Leitura segura de variáveis de ambiente |
| requests | — | Chamadas HTTP para a Z-API |

---

## 📁 Estrutura do projeto

```
b2bflow-desafio/
├── main.py            # Programa principal
├── .env               # Variáveis secretas (não sobe pro GitHub)
├── .gitignore         # Arquivos ignorados pelo Git
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação
```

---

## 🗄️ Setup da tabela no Supabase

A tabela foi criada via **SQL Editor** dentro do Supabase.  
Para recriar, execute o SQL abaixo:

```sql
-- Cria a tabela se ainda não existir
CREATE TABLE IF NOT EXISTS public.contatos (
  id       SERIAL PRIMARY KEY,
  nome     TEXT NOT NULL,
  telefone TEXT NOT NULL,
  ativo    BOOLEAN DEFAULT TRUE,
  UNIQUE (telefone)
);

-- Insere contatos de exemplo
INSERT INTO public.contatos (nome, telefone)
VALUES
  ('Contato 1', '5531900000001'),
  ('Contato 2', '5531900000002'),
  ('Contato 3', '5531900000003')
ON CONFLICT (telefone) DO NOTHING;
```

> ⚠️ **Atenção ao RLS:** O Supabase ativa Row Level Security por padrão.
> Sem a policy abaixo, a tabela retorna vazia sem dar erro.

```sql
CREATE POLICY "leitura_publica"
ON public.contatos
FOR SELECT
USING (true);
```

> 📌 **Formato do telefone:** use DDI + DDD + número, sem espaços ou traços.  
> Exemplo: `5531900000001` para (31) 90000-0001.

---

## 🔐 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com os valores abaixo:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua_chave_anonima
ZAPI_INSTANCE=seu_instance_id
ZAPI_TOKEN=seu_token
CLIENT_TOKEN=seu_client_token
```

<details>
<summary>📍 Onde encontrar cada valor</summary>

<br/>

| Variável | Onde encontrar |
|---|---|
| `SUPABASE_URL` | Supabase → Settings → API → **Project URL** |
| `SUPABASE_KEY` | Supabase → Settings → API → **anon public** |
| `ZAPI_INSTANCE` | Z-API → sua instância → **Instance ID** |
| `ZAPI_TOKEN` | Z-API → sua instância → **Token** |
| `CLIENT_TOKEN` | Z-API → sua instância → **Security → Client Token** |

</details>

---

## 🚀 Como rodar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/b2bflow-desafio.git
cd b2bflow-desafio

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o .env com suas credenciais

# 5. Execute
python main.py
```

---

## ✅ Saída esperada

```
🚀 Iniciando envio de mensagens...
📋 3 contato(s) encontrado(s).
✅ Enviado para Contato 1 (5531900000001)
✅ Enviado para Contato 2 (5531900000002)
✅ Enviado para Contato 3 (5531900000003)
✅ Processo finalizado!
```

---

## 🧱 Boas práticas aplicadas

- ✅ Credenciais protegidas via `.env` — nunca expostas no código
- ✅ Funções com responsabilidade única (`buscar_contatos`, `enviar_mensagem`)
- ✅ Validação das variáveis de ambiente antes da execução
- ✅ Tratamento de erros com `try/except` em todas as chamadas de rede
- ✅ Pausa entre envios com `time.sleep()` para respeitar o rate limit da API
- ✅ Type hints e docstrings em todas as funções
- ✅ Organização de imports seguindo PEP 8

<img width="446" height="319" alt="3" src="https://github.com/user-attachments/assets/10998b7e-f4ff-48e1-927e-bc93db1d26e2" />
<img width="450" height="378" alt="2" src="https://github.com/user-attachments/assets/3dc501d2-7207-48f8-ac89-8352c3ade321" />
<img width="445" height="381" alt="1" src="https://github.com/user-attachments/assets/c2f99a0c-3a0f-44d8-aed1-358ac2af5152" />
<div align="center">
