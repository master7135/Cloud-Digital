# Pixel Forge Render/GitHub Package

This folder is set up for direct deployment on Render as a Python web service.

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

Create a new GitHub repository, upload this folder, and connect it to Render.

Preferred option:

- Use the included `render.yaml` blueprint.
- Render will install dependencies from `requirements.txt`.
- Render will start the app with `waitress-serve --host=0.0.0.0 --port=$PORT app:app`.
- Python is pinned in `render.yaml` with `PYTHON_VERSION=3.11.11`.

Manual option:

- Create a new Render Web Service from the repo.
- Runtime: `Python`
- Build command: `pip install -r requirements.txt`
- Start command: `waitress-serve --host=0.0.0.0 --port=$PORT app:app`

The repo also includes a `Procfile` with the same start command. `waitress` is used instead of `gunicorn` so the app can be started the same way on both Windows and Linux.

## Important

Do not upload `node_modules`, `dist`, `.wrangler`, or `__pycache__`.
