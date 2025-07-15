# this loads the template and fills user data
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def render_pdf(data, output_path="outputs/resume.pdf"):
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("resume_template.html")

    # Render the template with user data
    rendered_html = template.render(data=data)

    # Output PDF with CSS styling
    css_path = os.path.join("static", "style.css")
    HTML(string=rendered_html).write_pdf(output_path, stylesheets=[css_path])
    
    return output_path
