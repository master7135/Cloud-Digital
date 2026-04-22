# Pixel Forge Render/GitHub Package

This is the cleaned deployment folder for GitHub and Render.

## Included

- `app.py`
- `templates/`
- `static/`
- `requirements.txt`
- `render.yaml`
- `.gitignore`
- `.renderignore`

## Local Run

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`

## Render Deploy

Create a new GitHub repository, upload this folder, then deploy it on Render.

- Runtime: `Python`
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

## Important

Do not upload `node_modules`, `dist`, `.wrangler`, or `__pycache__`.
