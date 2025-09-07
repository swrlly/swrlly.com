# this file changes jupyter theme to match my website + look like default vscode blocks
# jupyter nbconvert --execute --format basic --to html runes-domain.ipynb
import re

# .modifyImg {width: 80%; margin: 0 auto; display: flex;}

r = """.highlight .nb { color: var(--vscode-lightgreen); } 
.hl-ipython3 {
    background-color: var(--card-color); 
    color: var(--text-color); 
    padding: 10px; 
    overflow: scroll; 
    font-family: "Source Code Pro, monospace"; 
    font-size: 10px; 
    letter-spacing: -0.2px;
}
.pre { color: var(--text-color); }
.modifyImg { margin: 1.5rem auto; 
    display: flex; 
    border: 1px var(--card-color) solid; 
    box-shadow: 0px 0px 10px 5px black;
    padding: 0.5rem;
    border-radius: 15px;
}
.modifyPrintText {color: var(--text-color); overflow: auto; }
.ol, ul {
    line-height: var(--list-line-height);
}
.h2, .h3, .h4, .h5 {
    line-height: var(--line-height);
    }
"""
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
    # remove keywords/operator bold
    ".highlight .o { color: var\(--jp-mirror-editor-operator-color\); font-weight: bold }" : ".highlight .o { color: var(--text-color) }",
    ".highlight .ow { color: var\(--jp-mirror-editor-operator-color\); font-weight: bold }" : ".highlight .ow { color: var(--vscode-pink); }",
    ".highlight .kc { color: var\(--jp-mirror-editor-keyword-color\); font-weight: bold }" : ".highlight .kc { color: var(--vscode-blue); }",
    # inject css
    "</style>\n.+text/css.+>" : r + "</style>\n<style type=\"text/css\">",
    # change df table print
    ".jp-OutputArea-output {\n.+display: table-cell;" : ".jp-OutputArea-output {\n display: table-cell; margin-top: 2rem; margin-bottom: 2rem;\n",
    ".jp-Cell-outputWrapper {\n.+display: flex;" : ".jp-Cell-outputWrapper {\ndisplay: flex;margin-top:1rem;\nmargin-bottom:1rem;",
    "var\(--jp-rendermime-table-row-background\)": "var(--lighter-card-color)",
    "--jp-rendermime-table-row-hover-background: var\(--md-light-blue-50\);": "--jp-rendermime-table-row-hover-background: var(--lighter-card-color);",
    # forgot
    "var\(--jp-layout-color0\)": "var(--card-color)",
    # md font color
    ".jp-MarkdownOutput {": ".jp-MarkdownOutput {color: var(--text-color);\n",
    #"a {\n.+\n.+\n}" : "a {text-decoration: unset; color: var(--link-color);}",
    "a:hover {\n.+\n.+\n}" : "a:hover {text-decoration: unset; color: var(--link-hover-color);}",
    "--jp-content-link-color: var\(--md-blue-900\);" : "--jp-content-link-color: var(--link-color);",
    # remove code blocks
    "<div class=\"jp-OutputPrompt jp-OutputArea-prompt\">.*</div>": "",
    "<div class=\"jp-InputPrompt jp-InputArea-prompt\">.*(\r\n|\r|\n)*.*</div>": "",
    #"""<div class="jp-OutputArea-child jp-OutputArea-executeResult">.+(\r\n|\r|\n)*.+<div class="jp-OutputPrompt jp-OutputArea-prompt">.*</div>.*(\r\n|\r|\n)*.*<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex=".*">.*(\r\n|\r|\n)*.*<pre>.+</pre>.*(\r\n|\r|\n)*.*</div>.*(\r\n|\r|\n)*.*</div>""": "",
    "<div class=\"jp-OutputPrompt jp-OutputArea-prompt\"></div>": "",
    #don't do this it screws up svgs which screws up mathjax
    #".jp-RenderedSVG svg {": ".jp-RenderedSVG svg {width: 80%; margin: 0 auto; display: flex;",
    """.jp-RenderedHTMLCommon img,\n.*.jp-RenderedImage img,\n.*.jp-RenderedHTMLCommon svg,\n.*.jp-RenderedSVG svg {\n.*max-width: 100%;\n.*height: auto;\n}""": """jp-RenderedHTMLCommon svg, .jp-RenderedSVG svg {max-width: 100%; height: auto;}\n .jp-RenderedHTMLCommon img, .jp-RenderedImage img {max-width: 90%; height: auto;}""",
    #inline code
    "--jp-content-font-color1: rgba\(0, 0, 0, 0.87\);": "--jp-content-font-color1: var(--text-color);",
    "--jp-layout-color2: var\(--md-grey-200\);": "--jp-layout-color: var(--lighter-card-color);",
    "<img.+class=\"\"": "<img class=\"modifyImg\"",
    # print statement font
    "<div class=\"jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult\" data-mime-type=\"text/plain\".+>\n*<pre>": "<div class=\"jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult\" data-mime-type=\"text/plain\" tabindex=\"0\">\n<pre class=\"modifyPrintText\">",
    # embedded in markdown code background
    """.jp-RenderedHTMLCommon :not\(pre\) > code {\n.*background-color: var\(--jp-layout-color2\);\n.*padding: 1px 5px;\n}""" : """.jp-RenderedHTMLCommon :not(pre) > code {background-color: var(--lighter-card-color); padding: 2px 2px; border-radius: 2.5px;}""",
    # mobile allow overflow for print statements
    """.jp-OutputArea-output pre {\n.*border: none;\n.*margin: 0;\n.*padding: 0;\n.*overflow-x: auto;\n.*overflow-y: auto;\n.*word-break: break-all;\n.*word-wrap: break-word;\n.*white-space: pre-wrap;\n} """ : """.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
}""",
    # allow overflow on mobile
    "word-break: break-all;": "",
    "word-wrap: break-word;": "",
    "white-space: pre-wrap;": "",
    # center overflow mjax
    "<mjx-container class=\"MathJax CtxtMenu_Attached_0\" jax=\"SVG\" display=\"true\" style=\"position: relative;\"": "<mjx-container class=\"MathJax CtxtMenu_Attached_0\" jax=\"SVG\" display=\"true\" style=\"position: relative;\"overflow: auto;",
    # allow dataframe to overflow
    "<div>\n.*<style scoped=\"\">": "<div style=\"overflow: auto;\">\n<style scoped=\"\" >",
    # time to change headers and paragraph decls
    #"--jp-content-heading-line-height: 1;": 
    # Base font size 
    "--jp-content-font-size1: 14px;":  "--jp-content-font-size1: var(--h5-size);",
    "--jp-content-font-size2: 1.2em;": "--jp-content-font-size2: var(--h4-size);",
    "--jp-content-font-size3: 1.44em;":  "--jp-content-font-size3: var(--h3-size);",
    "--jp-content-font-size4: 1.728em;": "--jp-content-font-size4: var(--h2-size);",
    "--jp-content-font-size5: 2.0736em;" :  "--jp-content-font-size5: var(--h1-size);"

}

numbers= "var\(--jp-mirror-editor-number-color\)"
punctuation = "var\(--jp-mirror-editor-punctuation-color\)"
strings = "var\(--jp-mirror-editor-string-color\)"
keywords = "var\(--jp-mirror-editor-keyword-color\).+" #get rid of bold
codeBorder = "var\(--jp-cell-editor-border-color\)"
comment = "var\(--jp-mirror-editor-comment-color\).+" #get rid of italics
code = "var\(--jp-code-font-family\)"

a = open("../templates/swrlly/runes-domain.html", "r", encoding = "utf-8").read()
for i in replace:
    a = re.sub(i, replace[i], a)
a = re.sub(numbers, "var(--vscode-lightgreen);", a)
a = re.sub(strings, "var(--vscode-orange);", a)
a = re.sub(keywords, "var(--vscode-pink);}", a)
a = re.sub(punctuation, "var(--vscode-darkyellow);", a)
a = re.sub(comment, "var(--vscode-darkgreen);}", a)
a = re.sub(codeBorder, "var(--card-color);", a)
#a = re.sub(code, "\"Source Code Pro, monospace\"", a)

b = open("../templates/swrlly/runes-domain.html", "wb")
b.write(a.encode("utf-8"))
b.close()
