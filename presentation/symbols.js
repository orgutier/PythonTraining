// Shared trilingual (Python / English / Spanish) reference for every
// operator and punctuation symbol used across the course, plus a
// Stage-1-scoped operators summary. Loaded by BOTH presentation/index.html
// and presentation-review/index.html (the latter via a relative path) so
// this content is written once and never drifts between the two sites.

const SYMBOLS_REFERENCE = {
  groups: [
    {
      heading: "Arithmetic operators",
      headingEs: "Operadores aritm\u00e9ticos",
      rows: [
        { symbol: "+", english: "Plus sign \u2014 addition", spanish: "M\u00e1s \u2014 suma (adici\u00f3n)", example: "3 + 2  # 5" },
        { symbol: "-", english: "Minus sign \u2014 subtraction", spanish: "Menos \u2014 resta (sustracci\u00f3n)", example: "3 - 2  # 1" },
        { symbol: "*", english: "Asterisk \u2014 multiplication", spanish: "Asterisco \u2014 multiplicaci\u00f3n", example: "3 * 2  # 6" },
        { symbol: "/", english: "Slash \u2014 division (true division)", spanish: "Barra \u2014 divisi\u00f3n (divisi\u00f3n real)", example: "7 / 2  # 3.5" },
        { symbol: "//", english: "Double slash \u2014 floor division", spanish: "Doble barra \u2014 divisi\u00f3n entera", example: "7 // 2  # 3" },
        { symbol: "%", english: "Percent sign \u2014 modulo (remainder)", spanish: "Signo de porcentaje \u2014 m\u00f3dulo (resto)", example: "7 % 2  # 1" },
        { symbol: "**", english: "Double asterisk \u2014 exponentiation (power)", spanish: "Doble asterisco \u2014 potenciaci\u00f3n (exponente)", example: "2 ** 3  # 8" }
      ]
    },
    {
      heading: "Comparison operators",
      headingEs: "Operadores de comparaci\u00f3n",
      rows: [
        { symbol: "==", english: "Double equals \u2014 equal to", spanish: "Doble igual \u2014 igual a", example: "3 == 3  # True" },
        { symbol: "!=", english: "Not-equals \u2014 not equal to", spanish: "Distinto de \u2014 no igual a", example: "3 != 4  # True" },
        { symbol: "<", english: "Less-than sign", spanish: "Signo de menor que", example: "3 < 4  # True" },
        { symbol: ">", english: "Greater-than sign", spanish: "Signo de mayor que", example: "4 > 3  # True" },
        { symbol: "<=", english: "Less-than-or-equal sign", spanish: "Menor o igual que", example: "3 <= 3  # True" },
        { symbol: ">=", english: "Greater-than-or-equal sign", spanish: "Mayor o igual que", example: "3 >= 4  # False" }
      ]
    },
    {
      heading: "Assignment operators",
      headingEs: "Operadores de asignaci\u00f3n",
      rows: [
        { symbol: "=", english: "Equals sign \u2014 assignment", spanish: "Igual \u2014 asignaci\u00f3n", example: "x = 5" },
        { symbol: "+=", english: "Plus-equals \u2014 add and assign", spanish: "Asignaci\u00f3n con suma", example: "x += 1  # x = x + 1" },
        { symbol: "-=", english: "Minus-equals \u2014 subtract and assign", spanish: "Asignaci\u00f3n con resta", example: "x -= 1  # x = x - 1" },
        { symbol: "*=", english: "Star-equals \u2014 multiply and assign", spanish: "Asignaci\u00f3n con multiplicaci\u00f3n", example: "x *= 2  # x = x * 2" },
        { symbol: "/=", english: "Slash-equals \u2014 divide and assign", spanish: "Asignaci\u00f3n con divisi\u00f3n", example: "x /= 2  # x = x / 2" },
        { symbol: "//=", english: "Double-slash-equals \u2014 floor-divide and assign", spanish: "Asignaci\u00f3n con divisi\u00f3n entera", example: "x //= 2" },
        { symbol: "%=", english: "Percent-equals \u2014 modulo and assign", spanish: "Asignaci\u00f3n con m\u00f3dulo", example: "x %= 2" },
        { symbol: "**=", english: "Double-star-equals \u2014 exponentiate and assign", spanish: "Asignaci\u00f3n con potenciaci\u00f3n", example: "x **= 2" },
        { symbol: ":=", english: "Walrus operator \u2014 assignment expression", spanish: "Operador morsa \u2014 expresi\u00f3n de asignaci\u00f3n", example: "if (n := len(data)) > 10:" }
      ]
    },
    {
      heading: "Logical operators",
      headingEs: "Operadores l\u00f3gicos",
      rows: [
        { symbol: "and", english: "Logical AND", spanish: "Y l\u00f3gico (conjunci\u00f3n)", example: "True and False  # False" },
        { symbol: "or", english: "Logical OR", spanish: "O l\u00f3gico (disyunci\u00f3n)", example: "True or False  # True" },
        { symbol: "not", english: "Logical NOT", spanish: "Negaci\u00f3n l\u00f3gica", example: "not True  # False" }
      ]
    },
    {
      heading: "Identity & membership operators",
      headingEs: "Operadores de identidad y pertenencia",
      rows: [
        { symbol: "is", english: "Identity operator \u2014 same object?", spanish: "Operador de identidad \u2014 \u00bfmismo objeto?", example: "x is None" },
        { symbol: "is not", english: "Negated identity operator", spanish: "Identidad negada", example: "x is not None" },
        { symbol: "in", english: "Membership operator \u2014 contains?", spanish: "Operador de pertenencia \u2014 \u00bfcontiene?", example: "3 in [1, 2, 3]  # True" },
        { symbol: "not in", english: "Negated membership operator", spanish: "Pertenencia negada", example: "4 not in [1, 2, 3]  # True" }
      ]
    },
    {
      heading: "Grouping & punctuation",
      headingEs: "Agrupaci\u00f3n y puntuaci\u00f3n",
      rows: [
        { symbol: "()", english: "Parentheses \u2014 grouping, function calls, tuples", spanish: "Par\u00e9ntesis \u2014 agrupaci\u00f3n, llamadas a funci\u00f3n, tuplas", example: "print(\"hi\")" },
        { symbol: "[]", english: "Square brackets \u2014 lists, indexing/slicing", spanish: "Corchetes \u2014 listas, indexaci\u00f3n/rebanado", example: "nums[0]" },
        { symbol: "{}", english: "Curly braces \u2014 dicts, sets", spanish: "Llaves \u2014 diccionarios, conjuntos", example: "{\"a\": 1}" },
        { symbol: ":", english: "Colon \u2014 starts a block / dict key-value separator", spanish: "Dos puntos \u2014 inicia un bloque / separador clave-valor", example: "if x:\n    pass" },
        { symbol: ",", english: "Comma \u2014 separator", spanish: "Coma \u2014 separador", example: "f(a, b, c)" },
        { symbol: ".", english: "Dot \u2014 attribute/method access", spanish: "Punto \u2014 acceso a atributo/m\u00e9todo", example: "obj.value" },
        { symbol: ";", english: "Semicolon \u2014 statement separator (rare in Python)", spanish: "Punto y coma \u2014 separador de instrucciones (poco usado)", example: "x = 1; y = 2" },
        { symbol: "...", english: "Ellipsis \u2014 placeholder value/stub", spanish: "Puntos suspensivos \u2014 valor marcador/relleno", example: "def todo(): ..." }
      ]
    },
    {
      heading: "Function & unpacking symbols",
      headingEs: "S\u00edmbolos de funciones y desempaquetado",
      rows: [
        { symbol: "->", english: "Arrow \u2014 return type annotation", spanish: "Flecha \u2014 anotaci\u00f3n de tipo de retorno", example: "def f() -> int:" },
        { symbol: "*args", english: "Star \u2014 collect/unpack positional arguments", spanish: "Asterisco \u2014 empaquetar/desempaquetar argumentos posicionales", example: "def f(*args):" },
        { symbol: "**kwargs", english: "Double star \u2014 collect/unpack keyword arguments", spanish: "Doble asterisco \u2014 empaquetar/desempaquetar argumentos con nombre", example: "def f(**kwargs):" },
        { symbol: "@", english: "At sign \u2014 decorator", spanish: "Arroba \u2014 decorador", example: "@property" },
        { symbol: "_", english: "Underscore \u2014 throwaway name / placeholder", spanish: "Gui\u00f3n bajo \u2014 nombre desechable/marcador", example: "for _ in range(3):" }
      ]
    },
    {
      heading: "Comments & strings",
      headingEs: "Comentarios y cadenas de texto",
      rows: [
        { symbol: "#", english: "Hash / pound sign \u2014 starts a comment", spanish: "Almohadilla / numeral \u2014 inicia un comentario", example: "# this is a comment" },
        { symbol: "'' / \"\"", english: "Quotes \u2014 string literal", spanish: "Comillas \u2014 cadena de texto (literal)", example: "\"hello\"" },
        { symbol: "f\"\"", english: "f-string prefix \u2014 formatted string literal", spanish: "Prefijo f \u2014 cadena formateada (f-string)", example: "f\"{name}\"" },
        { symbol: "\\", english: "Backslash \u2014 escape character / line continuation", spanish: "Barra invertida \u2014 car\u00e1cter de escape / continuaci\u00f3n de l\u00ednea", example: "\"line1\\nline2\"" }
      ]
    }
  ]
};

// Stage 1 (Python Fundamentals) operators summary -- the subset of
// SYMBOLS_REFERENCE that Stage 1 itself actually teaches (arithmetic,
// comparison, logical/identity/membership from its Basic tier, plus
// assignment/augmented-assignment/walrus from its Mid tier).
const STAGE01_OPERATORS = {
  groups: [
    SYMBOLS_REFERENCE.groups[0], // Arithmetic
    SYMBOLS_REFERENCE.groups[1], // Comparison
    {
      heading: "Assignment operators",
      headingEs: "Operadores de asignaci\u00f3n",
      rows: [
        SYMBOLS_REFERENCE.groups[2].rows[0], // =
        SYMBOLS_REFERENCE.groups[2].rows[1], // +=
        SYMBOLS_REFERENCE.groups[2].rows[8]  // :=
      ]
    },
    SYMBOLS_REFERENCE.groups[3], // Logical
    SYMBOLS_REFERENCE.groups[4]  // Identity & membership
  ]
};
