# Trust-First Agentic Web Explainer

A LangChain-powered FastAPI service wrapped for the [NANDA adapter](https://github.com/projnanda/adapter). The agent focuses on MCP, A2A, and trust-first agentic web concepts, and can optionally fetch and summarize external URLs.

## Project layout

```
nanda-agent/
├─ adapter/                         # clone https://github.com/projnanda/adapter
├─ app/
│  ├─ main.py                       # FastAPI server (NANDA adapter wrapper)
│  ├─ agent.py                      # LangChain agent logic
│  ├─ tools.py                      # URL fetch/extract helper
│  ├─ config.py                     # environment configuration
│  ├─ prompts.py                    # system prompt definition
│  └─ __init__.py
├─ requirements.txt
├─ .env.example
└─ README.md
```

## Prerequisites

* Python 3.10+
* An OpenAI API key with access to `gpt-4o-mini` (or override `MODEL`)
* (Optional) NANDA adapter cloned alongside the project

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # update with your secrets
```

## Running locally

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Check health:

```bash
curl -s http://127.0.0.1:8080/health
```

Test chat endpoint:

```bash
curl -X POST http://127.0.0.1:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"In 3 bullets, what is MCP?"}]}'
```

## NANDA adapter integration

1. Clone the adapter as a sibling directory inside `nanda-agent/adapter/`:

   ```bash
   git clone https://github.com/projnanda/adapter.git adapter
   ```

2. Follow the adapter README to configure its environment variables. Point the adapter at the FastAPI endpoint, e.g. `ADAPTER_TARGET_URL=http://127.0.0.1:8080/chat`.

3. Start the adapter (for example via `uvicorn`, Docker, or the method specified by the repo) and obtain the NANDA chat URL it exposes.

4. (Optional) Set `NANDA_SHARED_SECRET` in both the adapter and this service to enforce shared-secret auth on `/chat`.

## Deployment to Ubuntu 22.04 (EC2 example)

```bash
sudo apt update && sudo apt -y install git python3.10-venv python3-pip nginx

# clone repo
cd /home/ubuntu
git clone https://github.com/youruser/nanda-agent.git
cd nanda-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add real secrets
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Create `/etc/systemd/system/nanda-agent.service`:

```
[Unit]
Description=Nanda Agent (Uvicorn)
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/nanda-agent
Environment="PATH=/home/ubuntu/nanda-agent/.venv/bin"
ExecStart=/home/ubuntu/nanda-agent/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8080
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now nanda-agent
sudo systemctl status nanda-agent
```

(Optional) Reverse proxy with Nginx:

```
server {
  listen 80;
  server_name _;

  location / {
    proxy_pass http://127.0.0.1:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```

Link and reload:

```bash
sudo ln -s /etc/nginx/sites-available/nanda /etc/nginx/sites-enabled/nanda
sudo nginx -t
sudo systemctl restart nginx
```

## Demo

Record a short (~1 minute) screen capture that:

1. Shows the FastAPI server running (either locally or on EC2).
2. Demonstrates a `/chat` request, ideally via the NANDA adapter URL.
3. Highlights URL ingestion by pasting a link and letting the agent summarize it with trust/interop insights.
