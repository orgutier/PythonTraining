// A small, dependency-free Python syntax highlighter -- no CDN, matching
// this reference's "no build step, no internet required" design. It's a
// regex tokenizer, not a full parser: good enough to color the short
// example snippets in the day-guide and glossary drawers like a VS Code
// dark theme, not meant to handle arbitrary real-world source files.

var PY_KEYWORDS = [
  "def", "return", "if", "elif", "else", "for", "while", "in", "is", "not",
  "and", "or", "class", "import", "from", "as", "try", "except", "finally",
  "raise", "with", "lambda", "yield", "pass", "break", "continue", "global",
  "nonlocal", "async", "await", "None", "True", "False", "del", "assert"
];

var PY_BUILTINS = [
  "print", "len", "range", "isinstance", "sorted", "sum", "list", "dict",
  "set", "tuple", "str", "int", "float", "bool", "type", "super", "getattr",
  "setattr", "enumerate", "zip", "map", "filter", "open", "repr"
];

function _highlightEscapeHtml(str) {
  var div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

function highlightPython(code) {
  var keywordSet = {};
  PY_KEYWORDS.forEach(function (k) { keywordSet[k] = true; });
  var builtinSet = {};
  PY_BUILTINS.forEach(function (b) { builtinSet[b] = true; });

  // Group 1: comment, 2: triple-quoted string, 3: single-line string,
  // 4: number, 5: decorator, 6: identifier immediately before "(",
  // 7: plain identifier, 8: whitespace, 9: everything else (punctuation).
  var re = /(#[^\n]*)|("""[\s\S]*?"""|'''[\s\S]*?''')|(f?"(?:[^"\\\n]|\\.)*"|f?'(?:[^'\\\n]|\\.)*')|(\b\d+\.?\d*\b)|(@[A-Za-z_]\w*)|([A-Za-z_]\w*)(?=\s*\()|([A-Za-z_]\w*)|(\s+)|([^\sA-Za-z0-9_]+)/g;

  var html = "";
  var match;
  while ((match = re.exec(code)) !== null) {
    if (match[1] !== undefined) {
      html += '<span class="tok-com">' + _highlightEscapeHtml(match[1]) + "</span>";
    } else if (match[2] !== undefined) {
      html += '<span class="tok-str">' + _highlightEscapeHtml(match[2]) + "</span>";
    } else if (match[3] !== undefined) {
      html += '<span class="tok-str">' + _highlightEscapeHtml(match[3]) + "</span>";
    } else if (match[4] !== undefined) {
      html += '<span class="tok-num">' + _highlightEscapeHtml(match[4]) + "</span>";
    } else if (match[5] !== undefined) {
      html += '<span class="tok-dec">' + _highlightEscapeHtml(match[5]) + "</span>";
    } else if (match[6] !== undefined) {
      html += '<span class="tok-func">' + _highlightEscapeHtml(match[6]) + "</span>";
    } else if (match[7] !== undefined) {
      var word = match[7];
      if (keywordSet[word]) {
        html += '<span class="tok-kw">' + _highlightEscapeHtml(word) + "</span>";
      } else if (word === "self" || word === "cls") {
        html += '<span class="tok-self">' + _highlightEscapeHtml(word) + "</span>";
      } else if (builtinSet[word]) {
        html += '<span class="tok-builtin">' + _highlightEscapeHtml(word) + "</span>";
      } else {
        html += _highlightEscapeHtml(word);
      }
    } else if (match[8] !== undefined) {
      html += match[8];
    } else if (match[9] !== undefined) {
      html += _highlightEscapeHtml(match[9]);
    }
  }
  return html;
}
