# this file changes jupyter theme to match my website + look like default vscode blocks
# jupyter nbconvert --execute --format basic --to html runes-domain.ipynb
import re



r = """.highlight .nb { color: var(--vscode-lightgreen); } 
.hl-ipython3 {background-color: var(--card-color); color: var(--text-color); line-height: 1.5; padding: 10px; overflow: scroll; font-family: "Source Code Pro, monospace"}
.pre {color: var(--text-color); }
.modifyImg {width: 80%; margin: 0 auto; display: flex;}
.modifyPrintText {color: var(--text-color);}
@media (min-width: 1200px) {
    h1 {
        font-size: 2.5rem;
    }
    h2  {
        font-size: 2rem;
    }
    h3 {
        font-size: 1.75rem;
    }
    h4 {
        font-size: 1.5rem;
    }
    .page-title {
        font-size: 4rem;
    }
    .index-title {
        font-size: 4rem;
    }
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
    "var\(--jp-rendermime-table-row-background\)": "var(--ligthter-card-color)",
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
    """<div class="jp-OutputArea-child jp-OutputArea-executeResult">.+(\r\n|\r|\n)*.+<div class="jp-OutputPrompt jp-OutputArea-prompt">.*</div>.*(\r\n|\r|\n)*.*<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex=".*">.*(\r\n|\r|\n)*.*<pre>.+</pre>.*(\r\n|\r|\n)*.*</div>.*(\r\n|\r|\n)*.*</div>""": "",
    "<div class=\"jp-OutputPrompt jp-OutputArea-prompt\"></div>": "",
    #don't do this it screws up svgs which screws up mathjax
    #".jp-RenderedSVG svg {": ".jp-RenderedSVG svg {width: 80%; margin: 0 auto; display: flex;",
    #inline code
    "--jp-content-font-color1: rgba\(0, 0, 0, 0.87\);": "--jp-content-font-color1: var(--text-color);",
    "--jp-layout-color2: var\(--md-grey-200\);": "--jp-layout-color: var(--lighter-card-color);",
    "<img.+class=\"\"": "<img class=\"modifyImg\"",
    # print statement font
    "<div class=\"jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult\" data-mime-type=\"text/plain\".+>\n*<pre>": "<div class=\"jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult\" data-mime-type=\"text/plain\" tabindex=\"0\">\n*<pre class=\"modifyPrintText\">",
    # time to change headers and paragraph decls
    #"--jp-content-heading-line-height: 1;": 
    # Base font size 
    "--jp-content-font-size1: 14px;":  "--jp-content-font-size1: var(--h5-size);, 
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
