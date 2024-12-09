import os
import re
import subprocess
from flask import Flask, request, send_file, render_template_string

app = Flask(__name__)

TEX_TEMPLATE = r"""
\documentclass{article}
\begin{document}
%s
\end{document}
"""

dangerous_commands = [
    r'\\openin', r'\\newread', r'\\include', r'\\usepackage', r'\\closein', r'\\newwrite', r'\\openout',
    r'\\write', r'\\closeout', r'\\write18', r'\\url', r'\\read', r'\\input', r'\\def', r'\^', r'\\catcode',
    r'\\immediate', r'\\csname', r'\\makeatletter', r'\\readline', r'\\uccode', r'\\lccode'
]

def check_for_dangerous_commands(latex_input):
    found_commands = []

    for command in dangerous_commands:
        if re.search(command, latex_input, flags=re.IGNORECASE):
            found_commands.append(command)

    if found_commands:
        raise ValueError(f"Dangerous LaTeX commands found: {', '.join(found_commands)}")

    return latex_input

@app.route('/')
def index():
    return render_template_string('''
        <form action="/render" method="post">
            <textarea name="latex" rows="10" cols="50">Enter LaTeX here...</textarea><br>
            <input type="submit" value="Render PDF">
        </form>
    ''')

@app.route('/render', methods=['POST'])
def render_latex():
    try:
        latex_input = request.form['latex']

        check_for_dangerous_commands(latex_input)
        
        tex_file = "output.tex"
        with open(tex_file, "w") as f:
            f.write(TEX_TEMPLATE % latex_input)
        
        subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file])

        pdf_file = "output.pdf"
        if os.path.exists(pdf_file):
            return send_file(pdf_file, mimetype='application/pdf')
        else:
            return "Error in generating PDF"

    except ValueError as e:
        return str(e), 400
  
    finally:
        files = ["output.tex", "output.pdf", "output.log", "output.aux"]
        for file in files:
            if os.path.exists(file):
                os.remove(file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', passthrough_errors=True, threaded=False, debug=False)
