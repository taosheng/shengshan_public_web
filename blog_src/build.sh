#!/bin/bash
cd "$(dirname "$0")"

# Create a temporary virtual environment if dependencies are missing
if ! python3 -c "import markdown, jinja2" 2>/dev/null; then
    echo "Installing build dependencies..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install markdown jinja2
else
    # if they are installed globally, just run
    echo "Dependencies found."
fi

python3 build_blog.py

if [ -d ".venv" ]; then
    deactivate
fi
