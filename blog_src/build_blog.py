import os
import json
import glob
from datetime import datetime
import markdown
from jinja2 import Environment, FileSystemLoader

# Configuration
POSTS_DIR = 'posts'
TEMPLATES_DIR = 'templates'
OUTPUT_DIR = '../blog'

def build():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    post_template = env.get_template('post.html')
    list_template = env.get_template('list.html')
    
    md = markdown.Markdown(extensions=['meta'])

    posts = []

    # Read markdown files
    for filepath in glob.glob(os.path.join(POSTS_DIR, '*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        html_content = md.convert(content)
        meta = md.Meta
        
        # md.Meta values are lists, so we take the first item
        post_data = {
            'id': os.path.splitext(os.path.basename(filepath))[0],
            'title': meta.get('title', [''])[0],
            'author': meta.get('author', [''])[0],
            'date': meta.get('date', [''])[0],
            'description': meta.get('description', [''])[0],
            'keywords': meta.get('keywords', [''])[0],
            'image': meta.get('image', [''])[0],
            'content': html_content
        }
        
        posts.append(post_data)

    # Sort posts by date descending
    posts.sort(key=lambda x: x['date'], reverse=True)

    # Generate individual post pages
    for post in posts:
        output_html = post_template.render(post=post)
        output_path = os.path.join(OUTPUT_DIR, f"{post['id']}.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_html)
        print(f"Generated {output_path}")

    # Generate blog index page
    index_html = list_template.render(posts=posts)
    index_path = os.path.join(OUTPUT_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"Generated {index_path}")

if __name__ == "__main__":
    build()
