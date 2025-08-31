# this file changes jupyter theme to match my website + look like default vscode blocks
# jupyter nbconvert --execute --format basic --to html runes-domain.ipynb
import re



r = """.highlight .nb { color: var(--vscode-lightgreen) } 
.hl-ipython3 {background-color: var(--card-color); color: var(--text-color); line-height: 1.5; padding: 10px;}"""
#.highlight .n { color: var(--vscode-lightblue)} /* base funcs */

"""
    --vscode-yellow: #CFD9AF; /* function names, base funcs */
    --vscode-darkyellow: #EDC952; /* bracket, paren*/
    --vscode-pink: #B188B6; /*try if except return for in if*/
    --vscode-orange: #B88557; /* strings */
    --vscode-blue: #6995C8; /*function def */
    --vscode-lightblue: #B0D6F5; /*args in function */
    --vscode-lightgreen: #BACA9E;/* numbers */
    --vscode-darkgreen: #799461; /* comments */
"""

replace = {
    ".highlight .o { color: var\(--jp-mirror-editor-operator-color\); font-weight: bold }" : ".highlight .o { color: var(--text-color) }",
    ".highlight .ow { color: var\(--jp-mirror-editor-operator-color\); font-weight: bold }" : ".highlight .ow { color: var(--vscode-pink); }",
    ".highlight .kc { color: var\(--jp-mirror-editor-keyword-color\); font-weight: bold }" : ".highlight .kc { color: var(--vscode-blue); }",
    "</style>" : r + "</style>",
    ".jp-OutputArea-output {\n.+display: table-cell;" : ".jp-OutputArea-output {\n display: table-cell; margin-top: 2rem; margin-bottom: 2rem;\n",
    ".jp-Cell-outputWrapper {\n.+display: flex;" : ".jp-Cell-outputWrapper {\ndisplay: flex;margin-top:1rem;\nmargin-bottom:1rem;",
    # table
    "var\(--jp-layout-color0\)": "var(--card-color)",
    "var\(--jp-rendermime-table-row-background\)": "var(--ligthter-card-color)",
    ".jp-MarkdownOutput {": ".jp-MarkdownOutput {color: var(--text-color);\n"
}

numbers= "var\(--jp-mirror-editor-number-color\)"
punctuation = "var\(--jp-mirror-editor-punctuation-color\)"
strings = "var\(--jp-mirror-editor-string-color\)"
keywords = "var\(--jp-mirror-editor-keyword-color\).+" #get rid of bold
codeBorder = "var\(--jp-cell-editor-border-color\)"
comment = "var\(--jp-mirror-editor-comment-color\).+" #get rid of italics
code = "var\(--jp-code-font-family\)"

a = open("../templates/swrlly/runes-domain.html", "r").read()
for i in replace:
    a = re.sub(i, replace[i], a)
a = re.sub(numbers, "var(--vscode-lightgreen)", a)
a = re.sub(strings, "var(--vscode-orange)", a)
a = re.sub(keywords, "var(--vscode-pink)}", a)
a = re.sub(punctuation, "var(--vscode-darkyellow)", a)
a = re.sub(comment, "var(--vscode-darkgreen)}", a)
a = re.sub(codeBorder, "var(--card-color)", a)
#a = re.sub(code, "\"Source Code Pro, monospace\"", a)

b = open("../templates/swrlly/runes-domain.html", "w")
b.write(a)
b.close()
