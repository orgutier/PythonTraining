// Data for the Python Training reference. One entry per stage/topic.
// Mirrors the "Study Reference - All Topics" sheet in the planning workbook.

const TOPICS = [
{
  n: 1, title: "Python Fundamentals", sub: "variables, types, operators",
  challenges: [
    {
      id: "challenge01",
      title: "Typed Config Loader",
      blurb: "Parse KEY=value config lines into properly typed int/float/bool/None/str values by hand -- no try/except numeric-detection shortcuts, isinstance()/type() used explicitly, and the result is always a brand-new dict.",
      path: "challenges/challenge01/"
    },
    {
      id: "challenge02",
      title: "Identity, Equality, and a Login Prompt",
      blurb: "A pairwise identity-vs-equality auditor plus a None-safe login prompt -- is/is not used explicitly throughout, and a bare is-None check instead of truthiness so an empty string is never mistaken for a missing one.",
      path: "challenges/challenge02/"
    }
  ],
  schedule: [
    { step: "1", title: "Setup", details: "Install Python 3.11+, create and activate a virtual environment (python -m venv .venv), pip install -r requirements.txt, and open the repo in VS Code. Run python tools/cli.py list and python tools/cli.py test stage01 to see the starter tests fail, try tools/gui.py, and do a git basics pass (status/add/commit). Tour exercises/, reference_solutions/, tests/, and open presentation/index.html to keep alongside the editor all course long." },
    { step: "2", title: "Learn", details: "Variables, Python's five foundational types, and operators, building up through precedence, f-strings, and the walrus operator to arbitrary-precision integers and IEEE-754 float internals.", tiers: [
      { label: "Basic tier", guideKey: "stage01-basic", keywords: ["int", "float", "str", "bool", "None", "True", "False", "print()", "input()", "type()", "isinstance()", "and", "or", "not", "is", "in", "x: int = 5"], concepts: ["type hints"] },
      { label: "Mid tier", guideKey: "stage01-mid" },
      { label: "Advanced tier & internals", guideKey: "stage01-advanced", concepts: ["mutability vs immutability", "identity vs equality"], theory: ["small-integer caching", "string interning", "IEEE-754 floating point"] }
    ] },
    { step: "3", title: "Practice", details: "Work through the exercises in exercises/stage01/ (see its README for the full list), running \`python tools/cli.py test stage01\` as you go." },
    { step: "4", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage01\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "Python variables are just names bound to objects — assignment (x = 5) creates that binding, it doesn't copy a value into a box. The five foundational built-in types are int, float, str, bool, and None: integers are whole numbers with no size limit, floats are decimal numbers stored in IEEE-754 double precision, strings are immutable text, booleans are True/False, and None represents \"no value\". Arithmetic operators (+ - * / // % **) and comparison operators (== != < > <= >=) work across these types, with / always returning a float and // performing integer (floor) division. print() writes to the console and input() reads a line of text (always as a str, so cast it with int()/float() when you need a number). Basic type casting (int(\"5\"), str(5), float(\"3.14\")) converts between these types explicitly, and a variable annotation like x: int = 5 documents the intended type for readers and tools without Python enforcing it at runtime.",
    ref: "Book — Python Distilled, §1.1–1.6"
  },
  mid: {
    text: "Operators follow a precedence order (like math: ** before * / before + -), and comparisons can be chained (0 < x < 10 really means 0 < x and x < 10, evaluated once). f-strings (f\"{name} is {age}\") are the modern, preferred way to build strings from variables, supporting inline expressions and format specs (f\"{pi:.2f}\"). // (floor division) and / (true division) behave differently and both are subject to float imprecision — 0.1 + 0.2 != 0.3 because binary floats can't represent most decimal fractions exactly. The walrus operator := lets you assign inside an expression (if (n := len(data)) > 10:), useful for avoiding a repeated computation. Augmented assignment (x += 1, x *= 2) is shorthand for \"compute and reassign\" and, for mutable objects, can mutate in place rather than rebinding.",
    ref: "Book — Python Distilled, Ch2 (Operators, Expressions, and Data Manipulation)"
  },
  advanced: {
    text: "Python integers have arbitrary precision — they grow as large as memory allows and never silently overflow, unlike fixed-width integers in C or Java. Floats, by contrast, are IEEE-754 doubles with finite precision, so 0.1 + 0.2 != 0.3 and comparisons should use math.isclose() instead of ==. Small integers (-5 to 256) and some string literals are cached/interned by CPython, meaning is comparisons on them can appear to work even though is should only ever be used for identity checks like x is None. Decimal (exact base-10 arithmetic) and Fraction (exact rational numbers) exist in the standard library for precision-sensitive work like currency, where float imprecision is unacceptable.",
    ref: "Web — Python docs, \u201cFloating Point Arithmetic: Issues and Limitations\u201d (docs.python.org/3/tutorial/floatingpoint.html)"
  },
  internals: "Everything is a PyObject; a variable is a name bound to an object, not a box holding a value. Small-int caching (-5..256) and string interning explain surprising `is` results. The mutable/immutable distinction here underlies hashability and the mutable-default-argument bug in Topic 3.",
  keywords: ["int","float","str","bool","None","True","False","print()","input()","type()","isinstance()","and","or","not","is","in","x: int = 5"],
  dunders: [],
  modules: [],
  methods: [],
  concepts: ["type hints","mutability vs immutability","identity vs equality"],
  theory: ["small-integer caching","string interning","IEEE-754 floating point"]
},
{
  n: 2, title: "Control Flow", sub: "conditionals, loops",
  challenges: [
    {
      id: "challenge03",
      title: "Log Stream Parser and Scanner",
      blurb: "Parse and scan a stream of log lines using a for...else search, enumerate()/zip() for labeling and pairing, and one and/not expression for a health check -- most of Stage 2's control-flow toolkit in one pipeline.",
      path: "challenges/challenge03/"
    },
    {
      id: "challenge04",
      title: "Batch Retry Simulator",
      blurb: "A batch-retry simulator built around a while...else loop, itertools.chain + islice for flattening batches, and a chained ternary for status labels.",
      path: "challenges/challenge04/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Conditionals and loops, building up through for...else, ternaries, and zip() to writing a custom iterator and the iterator protocol.", tiers: [
      { label: "Basic tier", guideKey: "stage02-basic", keywords: ["if", "elif", "else", "while", "for", "in", "range()", "break", "continue", "pass"], methods: ["enumerate()"] },
      { label: "Mid tier", guideKey: "stage02-mid", methods: ["zip()"], concepts: ["short-circuit evaluation", "ternary expression", "for...else / while...else"] },
      { label: "Advanced tier & internals", guideKey: "stage02-advanced", modules: ["itertools"], concepts: ["truthiness"], theory: ["iterator protocol (iter/next)", "StopIteration"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage02/ (see its README for the full list), running \`python tools/cli.py test stage02\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage02\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "if/elif/else branch on truthy conditions, with elif chaining as many additional conditions as needed and else catching everything unhandled. while repeats its block as long as its condition stays true — use it when the number of iterations isn't known ahead of time. for x in iterable: is the idiomatic way to loop in Python, most often paired with range(stop) / range(start, stop, step) to iterate a fixed number of times without building an actual list. break exits a loop immediately, continue skips to the next iteration, and pass is a no-op placeholder wherever a statement is syntactically required. Loops can nest freely, but watch for quadratic (O(n*n)) behavior when a loop runs inside another loop over the same size of data.",
    ref: "Book — Python Distilled, §1.5, 1.12; Ch3"
  },
  mid: {
    text: "A for/while loop can carry an else clause that runs only if the loop finished without hitting break — the classic use is a search loop where the else branch means \"not found\". and/or short-circuit: they stop evaluating as soon as the result is known and return one of the actual operands rather than a plain boolean, which is why x or default is a common one-line fallback idiom. Ternary expressions (value_if_true if condition else value_if_false) let you write a simple conditional assignment on one line instead of a full if/else block. zip(a, b) pairs up two (or more) iterables element-by-element into tuples, stopping at the shortest one — the standard way to loop over several sequences in lockstep instead of indexing manually.",
    ref: "Book — Python Distilled, Ch3 (continued)"
  },
  advanced: {
    text: "Writing a custom iterable means implementing __iter__ (returning an iterator) and a custom iterator means implementing __next__ (returning the next value or raising StopIteration when exhausted) — this is the exact protocol that powers every for loop in Python. The itertools module provides fast, memory-efficient building blocks (chain, product, groupby, islice, and more) for iteration patterns that would otherwise need hand-written loops. Loop-style choices have real performance implications: a list comprehension is typically faster than an equivalent explicit for-append loop because the comprehension's iteration runs in a tighter, more optimized bytecode path.",
    ref: "Book — Fluent Python, Ch17 (Iterators, Generators, and Classic Coroutines)"
  },
  internals: "`for` desugars to calling iter() then repeated next() until StopIteration. Truthiness resolves via `__bool__` then `__len__`. `and`/`or` return an operand, not a boolean — that's the actual mechanism behind short-circuiting.",
  keywords: ["if","elif","else","while","for","in","range()","break","continue","pass"],
  dunders: [],
  modules: ["itertools"],
  methods: ["zip()","enumerate()"],
  concepts: ["short-circuit evaluation","truthiness","ternary expression","for...else / while...else"],
  theory: ["iterator protocol (iter/next)","StopIteration"]
},
{
  n: 3, title: "Functions", sub: "parameters, scope, recursion",
  challenges: [
    {
      id: "challenge05",
      title: "Pluggable Event Pipeline",
      blurb: "A closure-based plugin registry, plus two flavors of caching decorator -- a hand-rolled memoize() and functools.lru_cache with a keyword-only parameter -- every decorator preserving metadata via functools.wraps.",
      path: "challenges/challenge05/"
    },
    {
      id: "challenge06",
      title: "Streaming Metrics Aggregator",
      blurb: "A streaming batch processor combining a real generator (yield), positional-only AND keyword-only parameters in the same signature, module state via global, and functools.partial for a reusable transform.",
      path: "challenges/challenge06/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Defining and calling functions, building up through closures and decorators to generator functions and Python's LEGB scoping rules.", tiers: [
      { label: "Basic tier", guideKey: "stage03-basic", keywords: ["def", "return", "->", "*args", "**kwargs", "lambda"] },
      { label: "Mid tier", guideKey: "stage03-mid", keywords: ["nonlocal"], concepts: ["decorators", "keyword-only arguments", "positional-only parameters"] },
      { label: "Advanced tier & internals", guideKey: "stage03-advanced", keywords: ["global", "yield"], methods: ["functools.wraps()", "functools.lru_cache()", "functools.partial()"], modules: ["functools"], concepts: ["closures"], theory: ["LEGB scope resolution", "mutable default argument bug", "no tail-call optimization"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage03/ (see its README for the full list), running \`python tools/cli.py test stage03\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage03\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "def name(params): defines a function; return value sends a result back to the caller (a function with no return, or a bare return, implicitly returns None). Default arguments (def f(x=10):) make a parameter optional, *args collects any extra positional arguments into a tuple, and **kwargs collects any extra keyword arguments into a dict — both are used when a function needs to accept a variable number of inputs. A return type hint (def f() -> int:) documents what the function produces, purely for readers and tools; Python does not enforce it. Recursion (a function calling itself) needs a base case to terminate, and lambda args: expr creates a small anonymous function limited to a single expression, most useful as a short inline callback like a sort key.",
    ref: "Book — Python Distilled, §1.13; Ch5"
  },
  mid: {
    text: "Keyword-only arguments (declared after a bare * in the parameter list) must be passed by name, which forces clarity at the call site for parameters that would be confusing as bare positional values; positional-only parameters (declared before a bare /) can only be passed positionally, which locks down a function's call signature so the parameter names can be changed freely later without breaking callers. Docstrings (a string literal right after def) document what a function does and are readable at runtime via introspection (help(f), f.__doc__). A closure is a nested function that remembers variables from its enclosing function's scope even after that outer function has returned — this is the mechanism behind both function factories and simple decorators, a decorator being a function that takes a function and returns a (usually wrapped) replacement, applied with @decorator syntax.",
    ref: "Book — Fluent Python, Ch9 (Decorators and Closures)"
  },
  advanced: {
    text: "functools.wraps should be applied inside any decorator you write so the wrapped function keeps its original name and docstring for debugging tools; functools.lru_cache memoizes a function's results by its arguments, which is a fast, one-line way to speed up expensive pure functions like recursive Fibonacci; functools.partial builds a new callable with some arguments pre-filled. A generator function (one containing yield) produces a lazy sequence of values one at a time instead of building a whole list in memory, pausing at each yield and resuming on the next call to next(). Recursion has a limit in Python (sys.getrecursionlimit(), usually 1000) because CPython does not perform tail-call optimization — deep or unbounded recursion should usually be rewritten as an iterative loop instead of raising the limit.",
    ref: "Book — Fluent Python, Ch7 (Functions as First-Class Objects)"
  },
  internals: "Functions are objects with `__code__`/`__defaults__`/`__closure__`. Name resolution follows LEGB (Local, Enclosing, Global, Built-in). Closures capture variables via cell objects, not values — which is also why default arguments are evaluated once at def-time, the classic mutable-default-argument bug.",
  keywords: ["def","return","->","*args","**kwargs","lambda","global","nonlocal","yield"],
  dunders: [],
  modules: ["functools"],
  methods: ["functools.wraps()","functools.lru_cache()","functools.partial()"],
  concepts: ["closures","decorators","keyword-only arguments","positional-only parameters"],
  theory: ["LEGB scope resolution","mutable default argument bug","no tail-call optimization"]
},
{
  n: 4, title: "Data Structures", sub: "lists, tuples, dicts, sets",
  challenges: [
    {
      id: "challenge07",
      title: "Anagram Groups with Records",
      blurb: "Group Anagrams (LeetCode #49), rebuilt around collections.defaultdict and a frozen, hashable dataclass record for each group -- plus set operations and enumerate() for the derived reports.",
      path: "challenges/challenge07/"
    },
    {
      id: "challenge08",
      title: "Longest Consecutive Run of Records",
      blurb: "Longest Consecutive Sequence (LeetCode #128), returning every run (not just the longest) as collections.namedtuple records, found in O(n) via a set -- no sorting the raw input.",
      path: "challenges/challenge08/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "The four built-in collections and comprehensions, building up through sorting and set operations to collections' specialized containers and the hash-table/dynamic-array internals behind them.", tiers: [
      { label: "Basic tier", guideKey: "stage04-basic", keywords: ["list", "tuple", "dict", "set", "append()", "sort()/sorted()", "len()", "zip()", "enumerate()", "[x for x in ...]", "{k:v for ...}"] },
      { label: "Mid tier", guideKey: "stage04-mid", methods: ["dataclasses.dataclass"], dunders: ["__eq__"], modules: ["collections", "dataclasses"], concepts: ["namedtuple / dataclass records", "set operations (union/intersection/difference)"] },
      { label: "Advanced tier & internals", guideKey: "stage04-advanced", methods: ["collections.defaultdict()", "collections.Counter()", "collections.deque()"], dunders: ["__hash__"], concepts: ["hashability"], theory: ["dynamic array amortized growth", "hash table internals", "insertion-ordered dicts (3.7+)"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage04/ (see its README for the full list), running \`python tools/cli.py test stage04\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage04\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "list (ordered, mutable), tuple (ordered, immutable), dict (key→value mapping, insertion-ordered since 3.7), and set (unordered, unique elements) are Python's four core built-in containers. All of them support indexing/slicing where applicable (seq[0], seq[1:3]) and each has its own common methods (list.append(), dict.get(), set.add(), and so on). List and dict comprehensions ([x*x for x in range(5)], {k: v for k, v in pairs}) build a new collection from an existing iterable in a single, usually faster and more readable expression than an equivalent append-loop.",
    ref: "Book — Python Distilled, §1.8–1.11"
  },
  mid: {
    text: "Containers can nest arbitrarily (a list of dicts, a dict of lists, and so on) to model more complex data. sorted(items, key=...) and list.sort(key=...) accept a key= function that controls what gets compared, which is how you sort a list of objects or tuples by a specific field. Sets support algebraic operators — | (union), & (intersection), - (difference), ^ (symmetric difference) — for comparing two collections of unique items without manual loops. collections.namedtuple and @dataclasses.dataclass are two lightweight ways to define a small, named record type without writing a full class by hand; use namedtuple for an immutable tuple-like record and @dataclass when you also want mutability or more generated behavior (__init__, __repr__, __eq__).",
    ref: "Book — Fluent Python, Ch2 (An Array of Sequences) & Ch3 (Dictionaries and Sets)"
  },
  advanced: {
    text: "collections provides specialized containers beyond the built-ins: defaultdict auto-creates a default value for missing keys (great for grouping without an if key not in dict check), Counter is built for counting hashable items and exposes .most_common(), and deque gives O(1) appends/pops from both ends (a plain list's pop(0) is O(n), so deque is the right choice for a queue). frozenset and tuple are the hashable, immutable counterparts of set and list, which is what makes them usable as dict keys or set members. Under the hood, lists are dynamic arrays that over-allocate extra capacity so most appends are amortized O(1), while dicts and sets are hash tables — average O(1) lookup, but only for keys that are properly hashable (implement a stable __hash__ and consistent __eq__).",
    ref: "Web — Python docs, collections module (docs.python.org/3/library/collections.html)"
  },
  internals: "Lists are dynamic arrays with amortized O(1) append via over-allocation. Dicts are hash tables keyed by `__hash__`/`__eq__`, insertion-ordered since 3.7. Tuples are fixed-size immutable arrays, hashable only if every element is hashable.",
  keywords: ["list","tuple","dict","set","append()","sort()/sorted()","len()","zip()","enumerate()","[x for x in ...]","{k:v for ...}"],
  dunders: ["__hash__","__eq__"],
  modules: ["collections","dataclasses"],
  methods: ["collections.defaultdict()","collections.Counter()","collections.deque()","dataclasses.dataclass"],
  concepts: ["hashability","namedtuple / dataclass records","set operations (union/intersection/difference)"],
  theory: ["dynamic array amortized growth","hash table internals","insertion-ordered dicts (3.7+)"]
},
{
  n: 5, title: "Files, Exceptions, Regex", sub: "I/O, error handling, pattern matching",
  challenges: [
    {
      id: "challenge09",
      title: "Log File Parser with a Custom Exception Chain",
      blurb: "Parse a real log file with a two-level custom exception hierarchy, a compiled regex with named groups, and raise ... from ... chaining when a bad line is found.",
      path: "challenges/challenge09/"
    },
    {
      id: "challenge10",
      title: "Log Text Utilities with a Custom Context Manager",
      blurb: "Text-processing utilities plus the same \"suppress and count\" context manager built two ways -- a class with __enter__/__exit__, and the @contextlib.contextmanager generator equivalent -- alongside re.findall()/re.sub()/re.search().",
      path: "challenges/challenge10/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Reading/writing files, exceptions, and regex basics, building up through exception chaining and named groups to custom context managers and the regex engine's backtracking behavior.", tiers: [
      { label: "Basic tier", guideKey: "stage05-basic", keywords: ["open()", "with", "as", "try", "except", "finally", "raise", "Exception", "re.search()", "re.findall()"], methods: ["re.match()", "re.sub()"], modules: ["re"] },
      { label: "Mid tier", guideKey: "stage05-mid", keywords: ["re.compile()"], modules: ["contextlib"], concepts: ["exception chaining (raise ... from ...)", "exception hierarchies", "regex named groups"] },
      { label: "Advanced tier & internals", guideKey: "stage05-advanced", methods: ["contextlib.contextmanager"], dunders: ["__enter__", "__exit__"], concepts: ["custom context managers"], theory: ["traceback propagation up the call stack", "backtracking regex engine", "catastrophic backtracking"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage05/ (see its README for the full list), running \`python tools/cli.py test stage05\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage05\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "open(path, mode) opens a file and returns a file object; always pair it with a with block (with open(path) as f:) so the file is closed automatically even if an error occurs partway through. try/except/finally/raise are Python's error-handling primitives: code that might fail goes in try, except ExceptionType: catches and handles a specific failure, finally always runs for cleanup, and raise SomeError(\"message\") throws an exception (write your own exception classes by subclassing Exception when the built-in types don't fit). The re module handles pattern matching over text: re.search() finds the first match anywhere in a string, re.match() only matches at the start, re.findall() returns every match, and re.sub() performs regex-based find-and-replace.",
    ref: "Book — Python Distilled, §1.7, 1.14; Ch9"
  },
  mid: {
    text: "raise NewError(...) from original_error chains an exception to its underlying cause, preserving the original traceback context — useful when translating a low-level failure into a more meaningful one without losing the reason it happened. Exception classes form an inheritance hierarchy (ValueError and TypeError both descend from Exception), so catching a shared base class handles a whole family of related errors at once. contextlib has tools beyond file handling for building your own context managers (see the advanced tier). Regex patterns can group parts of a match with (...) and name a group with (?P<name>...) for retrieval by name instead of position; re.compile() pre-compiles a pattern for reuse when the same pattern is applied many times.",
    ref: "Book — Fluent Python, Ch18 (with, match, and else Blocks)"
  },
  advanced: {
    text: "Any object implementing __enter__/__exit__ — or a generator wrapped in @contextlib.contextmanager (write setup code, yield, then teardown code) — can be used in a with block, which is how you guarantee cleanup for a resource that isn't a plain file, like a lock or a temporary directory. Regex lookahead ((?=...)) and lookbehind ((?<=...)) assert that a pattern exists nearby without consuming it as part of the match, useful for conditions like \"a digit not preceded by a letter\". Nested, ambiguous quantifiers in a regex (like (a+)+) can trigger catastrophic backtracking — the matching engine tries exponentially many paths on certain inputs — so patterns applied to untrusted input should be kept simple and bounded.",
    ref: "Web — Python docs, Regular Expression HOWTO (docs.python.org/3/howto/regex.html)"
  },
  internals: "Exceptions are objects that propagate up the call stack carrying a traceback. `with` desugars to `__enter__`/`__exit__` calls (Topic 8 covers this properly). The `re` engine compiles a pattern into a backtracking state machine, which is why some patterns can go exponentially slow.",
  keywords: ["open()","with","as","try","except","finally","raise","Exception","re.search()","re.findall()","re.compile()"],
  dunders: ["__enter__","__exit__"],
  modules: ["re","contextlib"],
  methods: ["re.match()","re.sub()","contextlib.contextmanager"],
  concepts: ["exception chaining (raise ... from ...)","exception hierarchies","custom context managers","regex named groups"],
  theory: ["traceback propagation up the call stack","backtracking regex engine","catastrophic backtracking"]
},
{
  n: 6, title: "OOP I", sub: "classes, encapsulation, properties",
  challenges: [
    {
      id: "challenge11",
      title: "LRU Cache with a Descriptor and Class-Level Stats",
      blurb: "LRU Cache (LeetCode #146) with O(1) get/put via a hand-built doubly linked list, __slots__, a validating descriptor for capacity, a computed @property, and a @classmethod alternate constructor.",
      path: "challenges/challenge11/"
    },
    {
      id: "challenge12",
      title: "Min Stack with Class-Level Push Stats",
      blurb: "Min Stack (LeetCode #155) with O(1) minimum() and no min() call, wrapped in a __slots__ class that tracks total pushes across every instance via a class attribute.",
      path: "challenges/challenge12/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Classes, __init__, and encapsulation conventions, building up through __slots__ and computed properties to writing a custom descriptor and Python's attribute lookup order.", tiers: [
      { label: "Basic tier", guideKey: "stage06-basic", keywords: ["class", "self", "__init__", "@property", "@x.setter", "@staticmethod", "@classmethod", "cls"], dunders: ["__init__"], concepts: ["encapsulation", "instance vs class attributes"] },
      { label: "Mid tier", guideKey: "stage06-mid", concepts: ["__slots__ memory savings"] },
      { label: "Advanced tier & internals", guideKey: "stage06-advanced", dunders: ["__get__/__set__ (preview)"], concepts: ["descriptors"], theory: ["attribute lookup order (instance \u2192 class \u2192 MRO)", "descriptor protocol (__get__/__set__)"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage06/ (see its README for the full list), running \`python tools/cli.py test stage06\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage06\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "class Name: defines a class; __init__(self, ...) is the initializer that runs automatically right after a new instance is created, typically used to set up instance attributes on self. Instance attributes (self.x = ...) belong to one object; class attributes (defined directly in the class body) are shared by every instance unless an instance attribute of the same name shadows them. A leading underscore (_protected) is Python's convention for \"internal use, please don't touch\" and a leading double-underscore (__private) triggers name mangling to discourage accidental access from subclasses — neither is true enforced privacy. @property turns a method into a read-only computed attribute (accessed without parentheses); @staticmethod marks a method that needs neither self nor cls (just a function namespaced inside the class); @classmethod marks a method that receives the class itself as cls, commonly used for alternative constructors.",
    ref: "Book — Python Distilled, Ch7 §7.1–7.4, 7.15–7.17"
  },
  mid: {
    text: "Declaring __slots__ = (\"x\", \"y\") on a class replaces each instance's normal __dict__ with fixed, fixed-size storage for exactly those named attributes, which meaningfully cuts memory use for classes instantiated in large numbers — the tradeoff is that instances can no longer have arbitrary new attributes added later. A @property can compute or cache a value on access rather than just exposing a stored field directly, letting you change the internal representation later without breaking the public obj.value interface. In practice, self refers to the specific instance a method was called on, while cls (inside a @classmethod) refers to the class itself — cls(...) inside a classmethod constructs an instance in a way that still works correctly for subclasses.",
    ref: "Book — Fluent Python, Ch11 (A Pythonic Object)"
  },
  advanced: {
    text: "A descriptor is any object implementing __get__ (and optionally __set__/__delete__) placed on a class to customize attribute access — @property, @staticmethod, and @classmethod are all themselves built on the descriptor protocol, which is why understanding descriptors explains how those three decorators actually work. Metaclasses control how classes themselves are constructed (the default metaclass is type); writing a custom metaclass lets you hook into or modify class creation, though it's rarely needed outside of framework code. __init_subclass__ is a lighter-weight hook (available since Python 3.6) that runs automatically whenever a class is subclassed, useful for validation or registration without the full complexity of a metaclass.",
    ref: "Book — Fluent Python, Ch22 (Dynamic Attributes and Properties) & Ch23 (Attribute Descriptors)"
  },
  internals: "Instances store attributes in a per-instance `__dict__` unless `__slots__` is used. Attribute lookup checks the instance dict, then the class dict, then the MRO. `@property`/`@staticmethod`/`@classmethod` are themselves descriptor objects implementing `__get__`/`__set__` — this is also where decorators get explained properly for the first time.",
  keywords: ["class","self","__init__","@property","@x.setter","@staticmethod","@classmethod","cls"],
  dunders: ["__init__","__get__/__set__ (preview)"],
  modules: [],
  methods: [],
  concepts: ["encapsulation","instance vs class attributes","__slots__ memory savings","descriptors"],
  theory: ["attribute lookup order (instance → class → MRO)","descriptor protocol (__get__/__set__)"]
},
{
  n: 7, title: "OOP II", sub: "inheritance, polymorphism, abstraction",
  challenges: [
    {
      id: "challenge13",
      title: "Notification System with Mixins and ABCs",
      blurb: "A notification dispatcher built from an abc.ABC base, mixins combined via multiple inheritance, super() cooperating through the chain, and isinstance()/duck typing in the broadcaster.",
      path: "challenges/challenge13/"
    },
    {
      id: "challenge14",
      title: "Shape Library with Protocols and Composition",
      blurb: "A shape library where Circle and Rectangle share no base class at all -- only a runtime_checkable typing.Protocol -- plus a CompositeShape built by composition, not inheritance.",
      path: "challenges/challenge14/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Inheritance, super(), and duck typing, building up through multiple inheritance and the abc module to Method Resolution Order, mixins, and structural typing with Protocol.", tiers: [
      { label: "Basic tier", guideKey: "stage07-basic", keywords: ["class Child(Parent)", "super()", "isinstance()"], modules: ["typing"], concepts: ["polymorphism", "duck typing"] },
      { label: "Mid tier", guideKey: "stage07-mid", keywords: ["abc", "ABC", "@abstractmethod"], modules: ["abc"], concepts: ["composition vs inheritance"] },
      { label: "Advanced tier & internals", guideKey: "stage07-advanced", concepts: ["mixins", "Protocol structural typing"], theory: ["Method Resolution Order (C3 linearization)", "diamond inheritance"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage07/ (see its README for the full list), running \`python tools/cli.py test stage07\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage07\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "class Child(Parent): makes Child inherit every attribute and method Parent defines; use inheritance when Child genuinely \"is a\" Parent, not just for code reuse. super() returns a proxy that forwards calls to the parent class, most commonly used inside __init__ to run the parent's setup before adding the child's own. Overriding a method means redefining it in the child class with the same name — Python resolves which version runs based on the actual object's type, not the variable's declared type. Duck typing (\"if it walks like a duck and quacks like a duck\") means Python cares about what methods/attributes an object actually has, not its declared type or class hierarchy — this is why explicit interfaces are optional in everyday Python code.",
    ref: "Book — Python Distilled, Ch7 §7.7"
  },
  mid: {
    text: "A class can inherit from more than one parent (class C(A, B):), which works but needs judgment about which parent \"wins\" when both define the same method — see the advanced tier's Method Resolution Order. Composition (\"has-a\", holding another object as an attribute) is often a better fit than inheritance (\"is-a\") when the relationship isn't a true specialization — it avoids fragile, deep class hierarchies that are hard to change later. The abc module's ABC base class and @abstractmethod decorator let you define a formal interface: a class inheriting from an ABC with abstract methods cannot be instantiated until every abstract method is overridden by a concrete subclass.",
    ref: "Book — Fluent Python, Ch13 (Interfaces, Protocols, and ABCs)"
  },
  advanced: {
    text: "When a class has multiple parents, Python decides which one's method actually runs using the Method Resolution Order (MRO) — a deterministic order computed by the C3 linearization algorithm and visible as SomeClass.__mro__. Diamond inheritance (two parents sharing a common ancestor) is resolved consistently by this MRO, unlike in some other languages where it's ambiguous. Mixins are small classes designed to be combined via multiple inheritance to add one specific, orthogonal capability (like a LoggingMixin), rather than building one large monolithic base class. typing.Protocol lets you define an interface by the shape an object must have (its methods/attributes) for static type checkers, without requiring the object to explicitly inherit from anything — a formalization of duck typing for tools like mypy.",
    ref: "Book — Fluent Python, Ch14 (Inheritance: For Better or For Worse)"
  },
  internals: "MRO is computed via C3 linearization, visible as `__mro__`. `super()` isn't \u201ccall my parent\u201d — it follows the MRO chain, which matters once multiple inheritance is involved. ABCs use `__subclasshook__` to allow duck-typed \u201cvirtual\u201d subclassing without explicit inheritance.",
  keywords: ["class Child(Parent)","super()","isinstance()","abc","ABC","@abstractmethod"],
  dunders: [],
  modules: ["abc","typing"],
  methods: [],
  concepts: ["polymorphism","duck typing","composition vs inheritance","mixins","Protocol structural typing"],
  theory: ["Method Resolution Order (C3 linearization)","diamond inheritance"]
},
{
  n: 8, title: "The Python Data Model", sub: "special methods, protocols",
  challenges: [
    {
      id: "challenge15",
      title: "Matrix: A Rich Numeric Type",
      blurb: "A Matrix class implementing ten dunders at once -- __repr__/__str__/__eq__/__hash__/__add__/__radd__/__len__/__getitem__/__iter__/__contains__/__bool__ -- with NotImplemented used correctly so + fails cleanly on a shape mismatch.",
      path: "challenges/challenge15/"
    },
    {
      id: "challenge16",
      title: "Transaction Ledger: Callable and Context Manager",
      blurb: "A transaction ledger that's directly callable (__call__) and a context manager (__enter__/__exit__) with commit-or-rollback batching -- no inheritance from any special base required for either to work.",
      path: "challenges/challenge16/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "The core object dunders (__init__/__repr__/__eq__), building up through operator overloading and container/callable protocols to context managers and how dunder lookup actually happens on the type.", tiers: [
      { label: "Basic tier", guideKey: "stage08-basic", dunders: ["__repr__", "__str__", "__eq__"] },
      { label: "Mid tier", guideKey: "stage08-mid", dunders: ["__add__", "__len__", "__getitem__", "__iter__", "__contains__", "__call__", "__bool__"], concepts: ["operator overloading", "protocols vs explicit inheritance"] },
      { label: "Advanced tier & internals", guideKey: "stage08-advanced", dunders: ["__enter__", "__exit__", "__hash__", "__radd__"], theory: ["dunder lookup happens on the type, not the instance", "reflected operators & NotImplemented", "iterator protocol requires StopIteration"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage08/ (see its README for the full list), running \`python tools/cli.py test stage08\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage08\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "__init__ initializes a new instance; __repr__ should return an unambiguous, developer-facing string (ideally one that could recreate the object, e.g. Point(x=1, y=2)) and is what you see in the REPL or in repr(obj); __str__ returns a more human-readable string for print(obj)/str(obj) and falls back to __repr__ if not defined; __eq__ defines what == means for your objects (by default, objects compare by identity, not by their contents).",
    ref: "Book — Fluent Python, Ch1 (The Python Data Model)"
  },
  mid: {
    text: "__add__ (and its siblings __sub__, __mul__, and so on) define what the corresponding operator does for your objects — this is called operator overloading. __len__ powers len(obj), __getitem__ powers obj[key] (indexing and slicing), __iter__ makes an object usable in a for loop, and __contains__ powers the in operator. __call__ makes instances callable like a function (obj(...)) — handy for an object that wraps a single configurable operation. __bool__ controls an object's truthiness in conditions (if obj:); if it's not defined, Python falls back to len(obj) != 0.",
    ref: "Book — Fluent Python, Ch12 (Special Methods for Sequences)"
  },
  advanced: {
    text: "__enter__/__exit__ make an object usable as a context manager in a with block (see Topic 5's context-manager coverage). When a + b is evaluated and a.__add__(b) returns NotImplemented (not an exception — an actual sentinel value), Python retries with b.__radd__(a) before finally raising TypeError; returning NotImplemented rather than raising is how you correctly signal \"I don't support this operand type\" from an operator dunder. If you define __eq__, you should also define __hash__ consistently (equal objects must have equal hashes) or explicitly set __hash__ = None to mark instances unhashable — otherwise a class silently becomes both \"equal by value\" and \"unusable as a dict key\" in surprising combinations. __slots__ (Topic 6) also affects which dunders and attributes an instance can carry, since it removes the per-instance __dict__.",
    ref: "Book — Fluent Python, Ch16 (Operator Overloading)"
  },
  internals: "Special methods are looked up on the TYPE, not the instance — `len(x)` really calls `type(x).__len__(x)`, which is why patching an instance's `__len__` directly doesn't work. Operator dispatch falls back to the reflected method if the left operand returns `NotImplemented`. The iterator protocol requires `__next__` to raise `StopIteration` when exhausted.",
  keywords: [],
  dunders: ["__repr__","__str__","__eq__","__add__","__len__","__getitem__","__iter__","__contains__","__call__","__bool__","__enter__","__exit__","__hash__","__radd__"],
  modules: [],
  methods: [],
  concepts: ["operator overloading","protocols vs explicit inheritance"],
  theory: ["dunder lookup happens on the type, not the instance","reflected operators & NotImplemented","iterator protocol requires StopIteration"]
},
{
  n: 9, title: "OS, JSON, Datetime, XML", sub: "everyday stdlib modules",
  challenges: [
    {
      id: "challenge17",
      title: "Directory Report Builder",
      blurb: "A directory report builder combining os.walk(), pathlib's rglob() as the modern alternative, and json.dumps(default=...) to serialize the real datetime objects it collects.",
      path: "challenges/challenge17/"
    },
    {
      id: "challenge18",
      title: "XML Feed to Timezone-Aware Digest",
      blurb: "Parse an XML event feed (ElementTree, findall()), explicitly attach UTC to its naive timestamps, and rebuild a fresh XML document from the result.",
      path: "challenges/challenge18/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Everyday stdlib modules for files, JSON, dates, and XML, building up through pathlib and timezone-aware datetimes to recursive directory walks and building XML trees from scratch.", tiers: [
      { label: "Basic tier", guideKey: "stage09-basic", keywords: ["os.listdir", "os.path", "json.load/dump", "datetime.now/isoformat", "ElementTree.parse/findall"], modules: ["os", "json", "datetime", "xml.etree.ElementTree"] },
      { label: "Mid tier", guideKey: "stage09-mid", methods: ["pathlib.Path", "json.dumps(default=...)"], modules: ["pathlib"], concepts: ["pathlib as the modern os.path alternative", "timezone-aware vs naive datetimes"] },
      { label: "Advanced tier & internals", guideKey: "stage09-advanced", methods: ["os.walk()"], theory: ["JSON recursive-descent parsing", "DOM-style (ElementTree) vs streaming (SAX) XML parsing"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage09/ (see its README for the full list), running \`python tools/cli.py test stage09\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage09\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "os.listdir(path) returns the entry names in a directory, and os.path provides functions like os.path.join()/os.path.exists() for building and checking paths as plain strings. json.load(file)/json.dump(obj, file) read and write JSON to/from an open file (use the s-suffixed loads/dumps for strings instead of files) — JSON objects map directly onto Python dicts, arrays onto lists, and so on. datetime.now() gets the current local date and time as a datetime object. xml.etree.ElementTree provides basic XML parsing: ET.parse(file) reads a file into an in-memory element tree you can then search.",
    ref: "Web — Python docs: os, json, datetime, xml.etree.ElementTree — neither priority book covers these stdlib modules in depth"
  },
  mid: {
    text: "pathlib.Path is the modern, object-oriented replacement for most os.path string functions — build paths with the / operator (Path(\"data\") / \"file.txt\") and call methods like .exists()/.read_text() directly on the path object. json.dumps(obj, default=fn) lets you serialize objects JSON doesn't know how to handle natively (like a custom class or a date) by providing a conversion callback. A \"naive\" datetime carries no timezone information; an \"aware\" one does, and can be safely compared and converted across timezones — prefer aware datetimes for anything that crosses timezone boundaries. ElementTree's .findall(path) searches the parsed tree for matching child elements using an XPath-like path string.",
    ref: "Web — Python docs, pathlib (docs.python.org/3/library/pathlib.html)"
  },
  advanced: {
    text: "os.walk(path) recursively walks an entire directory tree, yielding (dirpath, dirnames, filenames) for every directory it visits, which is how you process a whole tree instead of one level at a time. datetime supports arithmetic with timedelta objects (some_date + timedelta(days=7)), but daylight-saving-time transitions and other calendar edge cases can make naive date math subtly wrong — this is another reason to prefer timezone-aware datetimes for anything date-sensitive. ElementTree can build and modify XML trees, not just read them, using Element()/SubElement() and then writing the tree back out.",
    ref: "Web — Python docs, os and xml.etree.ElementTree advanced sections"
  },
  internals: "`os` is a thin wrapper over OS system calls. `json` implements a recursive-descent parser mapping JSON types to Python types — the reason arbitrary objects need a `default=` hook to serialize. `ElementTree` builds a full in-memory tree (DOM-like), unlike a streaming parser (SAX) that never holds the whole document at once.",
  keywords: ["os.listdir","os.path","json.load/dump","datetime.now/isoformat","ElementTree.parse/findall"],
  dunders: [],
  modules: ["os","json","pathlib","datetime","xml.etree.ElementTree"],
  methods: ["os.walk()","pathlib.Path","json.dumps(default=...)"],
  concepts: ["pathlib as the modern os.path alternative","timezone-aware vs naive datetimes"],
  theory: ["JSON recursive-descent parsing","DOM-style (ElementTree) vs streaming (SAX) XML parsing"]
},
{
  n: 10, title: "Pandas", sub: "data analysis",
  challenges: [
    {
      id: "challenge19",
      title: "Sales Data Analyzer",
      blurb: "A sales data analyzer using nothing but groupby()/sort_values()/boolean indexing/pivot_table() -- zero explicit row loops -- plus category-dtype memory optimization.",
      path: "challenges/challenge19/"
    },
    {
      id: "challenge20",
      title: "Two Sum, Pandas-Style, with Joins and Diagnostics",
      blurb: "Two Sum (LeetCode #1) solved as a vectorized pandas.Series operation, alongside df.merge(), df.apply(), a two-key groupby (MultiIndex), and a df.head()/info()/describe() diagnostics bundle.",
      path: "challenges/challenge20/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "DataFrame/Series basics and reading data, building up through filtering, grouping, and merging to vectorized operations, multi-indexing, and pandas' columnar NumPy-backed storage.", tiers: [
      { label: "Basic tier", guideKey: "stage10-basic", keywords: ["pd.read_csv", "df.head()"], methods: ["df.describe()"], modules: ["pandas"] },
      { label: "Mid tier", guideKey: "stage10-mid", keywords: ["df.groupby()", "df.sort_values()", "df.merge()"], concepts: ["boolean indexing"] },
      { label: "Advanced tier & internals", guideKey: "stage10-advanced", methods: ["df.info()", "df.apply()", "df.pivot_table()"], concepts: ["multi-indexing", "dtype-based memory optimization"], theory: ["columnar storage backed by NumPy arrays", "vectorization vs per-row Python loops"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage10/ (see its README for the full list), running \`python tools/cli.py test stage10\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage10\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "A DataFrame is pandas' 2-D labeled table (rows and named columns); a Series is a single labeled column. pd.read_csv(path) loads a CSV file straight into a DataFrame. .head(n) shows the first n rows for a quick sanity check, .info() summarizes column names/dtypes/non-null counts, and .describe() gives summary statistics for numeric columns — run all three immediately after loading any new dataset.",
    ref: "Web — pandas docs, \u201c10 minutes to pandas\u201d (pandas.pydata.org/docs/user_guide/10min.html)"
  },
  mid: {
    text: "Boolean indexing (df[df[\"age\"] > 18]) is the idiomatic way to filter rows in pandas, using a boolean array (usually from a comparison) instead of a manual loop. df.groupby(col) splits a DataFrame into groups by a column's values so you can chain an aggregation like .sum()/.mean()/.count() per group. df.sort_values(col) returns rows sorted by one or more columns (ascending=False for descending). df.merge(other, on=key, how=...) joins two DataFrames together like a SQL join, with how controlling \"inner\"/\"left\"/\"right\"/\"outer\" join behavior.",
    ref: "Web — pandas User Guide, Group By (pandas.pydata.org/docs/user_guide/groupby.html)"
  },
  advanced: {
    text: "Vectorized pandas operations (arithmetic, .str methods, boolean masks) run in compiled C over an entire column at once; .apply() and manual row loops fall back to slow, per-element Python bytecode, so always look for a vectorized equivalent before reaching for .apply(). A DataFrame can have a hierarchical multi-index (made of tuples instead of a single flat index) to represent grouped or nested data, often the natural result of a groupby() on multiple columns. Choosing narrower or more specific dtypes — smaller integer types, or \"category\" for low-cardinality string columns — can drastically cut a DataFrame's memory footprint; check with df.info(memory_usage=\"deep\"). df.pivot_table() reshapes data into a spreadsheet-style pivot summarizing values across two categorical dimensions at once.",
    ref: "Web — pandas User Guide, \u201cEnhancing Performance\u201d (pandas.pydata.org/docs/user_guide/enhancingperf.html)"
  },
  internals: "A DataFrame's columns are backed by contiguous NumPy arrays (columnar storage). Vectorized operations run in compiled C code instead of per-element Python bytecode — the entire reason pandas is fast when used idiomatically and slow the moment you loop over rows.",
  keywords: ["pd.read_csv","df.head()","df.groupby()","df.sort_values()","df.merge()"],
  dunders: [],
  modules: ["pandas"],
  methods: ["df.info()","df.describe()","df.apply()","df.pivot_table()"],
  concepts: ["boolean indexing","multi-indexing","dtype-based memory optimization"],
  theory: ["columnar storage backed by NumPy arrays","vectorization vs per-row Python loops"],
  note: "Optional deeper book (not required): \u201cPython for Data Analysis\u201d by Wes McKinney — see repo README for why this is optional."
},
{
  n: 11, title: "OpenCV", sub: "images as arrays",
  challenges: [
    {
      id: "challenge21",
      title: "Document Scanner Preprocessing Pipeline",
      blurb: "A document-scanner preprocessing pipeline: grayscale -> Gaussian blur -> Canny edges -> the largest-contour trick -> an aspect-ratio-preserving resize.",
      path: "challenges/challenge21/"
    },
    {
      id: "challenge22",
      title: "Face-Region Redactor",
      blurb: "A face-region redactor built on cv2.CascadeClassifier, with box-clipping via image.shape, adaptive thresholding, and cv2.imread()/imwrite() file I/O.",
      path: "challenges/challenge22/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Reading, writing, and transforming images, building up through thresholding and edge detection to contour detection and how images are represented as NumPy arrays.", tiers: [
      { label: "Basic tier", guideKey: "stage11-basic", keywords: ["cv2.imread", "cv2.imwrite", "cv2.cvtColor", "cv2.resize", "cv2.rectangle", "image.shape"], modules: ["opencv-python (cv2)", "numpy"] },
      { label: "Mid tier", guideKey: "stage11-mid", methods: ["cv2.Canny()"], concepts: ["thresholding"] },
      { label: "Advanced tier & internals", guideKey: "stage11-advanced", methods: ["cv2.findContours()", "cv2.GaussianBlur()", "cv2.CascadeClassifier"], concepts: ["convolution filtering"], theory: ["images as NumPy arrays (height \u00d7 width \u00d7 channels)", "BGR vs RGB channel order"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage11/ (see its README for the full list), running \`python tools/cli.py test stage11\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage11\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "cv2.imread(path) reads an image file into a NumPy array in BGR channel order (not RGB — a very common source of bugs) and cv2.imwrite(path, img) writes an array back out, inferring the format from the file extension; cv2.imread fails silently by returning None on a bad path, so always check the result. cv2.cvtColor(img, code) converts between color spaces, most often BGR↔grayscale or BGR↔RGB. cv2.resize(img, (w, h)) resizes an image. Basic drawing functions (cv2.rectangle, cv2.circle, cv2.line) draw shapes directly onto an image array in place.",
    ref: "Web — OpenCV-Python official tutorials, \u201cGetting Started with Images\u201d (docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)"
  },
  mid: {
    text: "Thresholding converts a grayscale image to pure black/white by classifying each pixel above or below a cutoff value — commonly the first step before contour detection. cv2.Canny(gray, t1, t2) detects edges using the Canny algorithm, typically run on a grayscale image with two threshold values controlling sensitivity. Because an OpenCV image is just a NumPy array, cropping is plain array slicing (img[y1:y2, x1:x2]) — no special OpenCV function needed. Video (from a file or a webcam) is read frame-by-frame as a sequence of these same image arrays via cv2.VideoCapture.",
    ref: "Web — OpenCV-Python tutorials, Image Processing section"
  },
  advanced: {
    text: "cv2.findContours() finds the outlines of connected white regions in a binary (thresholded/edge-detected) image, letting you locate distinct shapes or objects. Blurring and sharpening (cv2.GaussianBlur and friends) are both implemented as convolution — sliding a small kernel matrix over the image and combining nearby pixel values — the same underlying operation that powers edge detection. Haar cascades (cv2.CascadeClassifier) are pre-trained models for detecting objects like faces: load a .xml cascade file, then call .detectMultiScale() on a grayscale image to get bounding boxes.",
    ref: "Web — OpenCV-Python tutorials, Contours + Cascade Classifier sections"
  },
  internals: "An OpenCV image is just a NumPy array (height \u00d7 width \u00d7 channels). OpenCV defaults to BGR channel order, not RGB — a very common source of bugs. Most operations are implemented in C++ under a thin Python binding for speed.",
  keywords: ["cv2.imread","cv2.imwrite","cv2.cvtColor","cv2.resize","cv2.rectangle","image.shape"],
  dunders: [],
  modules: ["opencv-python (cv2)","numpy"],
  methods: ["cv2.Canny()","cv2.findContours()","cv2.GaussianBlur()","cv2.CascadeClassifier"],
  concepts: ["thresholding","convolution filtering"],
  theory: ["images as NumPy arrays (height × width × channels)","BGR vs RGB channel order"],
  note: "Optional deeper book (not required): \u201cPractical Python and OpenCV\u201d by Adrian Rosebrock — see repo README for why this is optional."
},
{
  n: 12, title: "Requests + Threading", sub: "HTTP clients, concurrency",
  challenges: [
    {
      id: "challenge23",
      title: "Rate-Limited HTTP Client",
      blurb: "A thread-safe token-bucket rate limiter wired into an actual requests.Session-based HTTP client -- fetched concurrently from raw threading.Thread workers, results returned in the original order.",
      path: "challenges/challenge23/"
    },
    {
      id: "challenge24",
      title: "Bounded Job Queue with Retry and ThreadPoolExecutor",
      blurb: "A retrying job submitter (requests.post + exponential backoff) driven by concurrent.futures.ThreadPoolExecutor, with a threading.Lock-protected counter proving exact correctness under real concurrency.",
      path: "challenges/challenge24/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Making HTTP requests and basic threading, building up through auth/timeouts and locking shared state to connection pooling, ThreadPoolExecutor, and the GIL.", tiers: [
      { label: "Basic tier", guideKey: "stage12-basic", keywords: ["requests.get()", "response.json()", "threading.Thread", ".start()", ".join()"], methods: ["requests.post()"], modules: ["requests", "threading"] },
      { label: "Mid tier", guideKey: "stage12-mid", keywords: ["threading.Lock"], methods: ["response.raise_for_status()"] },
      { label: "Advanced tier & internals", guideKey: "stage12-advanced", methods: ["requests.Session()", "concurrent.futures.ThreadPoolExecutor"], concepts: ["sessions & connection reuse", "retry/backoff strategies", "race conditions & deadlocks"], theory: ["Global Interpreter Lock (GIL)", "I/O-bound vs CPU-bound concurrency"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage12/ (see its README for the full list), running \`python tools/cli.py test stage12\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage12\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "requests.get(url)/requests.post(url, ...) send HTTP requests and return a Response object; response.json() parses the body as JSON and response.status_code gives the numeric HTTP status. threading.Thread(target=fn) represents a separate thread of execution: construct it, call .start() to begin running the target function concurrently, and call .join() to block until that thread finishes — useful when the main program needs to wait for background work to complete.",
    ref: "Web — requests Quickstart + Python docs threading (docs.python.org/3/library/threading.html)"
  },
  mid: {
    text: "Pass headers=, auth=, params= (query string), and always a timeout= to requests.get/post to avoid a request hanging forever on a slow or dead server. response.raise_for_status() raises an exception if the response's status code indicates a client or server error (4xx/5xx), so call it immediately after a request instead of letting failures pass silently. threading.Lock is a mutual-exclusion lock: acquire it (ideally with a with lock: block) around any code that reads or modifies state shared between threads, to prevent one thread's changes from interleaving unsafely with another's.",
    ref: "Web — requests \u201cAdvanced Usage\u201d (sessions, timeouts, retries)"
  },
  advanced: {
    text: "requests.Session() persists settings (headers, cookies) and reuses the underlying TCP connection across multiple requests to the same host — faster and more convenient than repeated standalone requests.get() calls. Retry/backoff strategies (configured via requests' HTTPAdapter + urllib3's Retry) automatically retry a failed request with increasing delays, to ride out transient network failures rather than hand-rolling a retry loop. concurrent.futures.ThreadPoolExecutor manages a pool of worker threads and is generally preferable to constructing raw Thread objects for running many similar concurrent tasks. A race condition is a bug from unsynchronized concurrent access to shared state (fixed with a Lock); a deadlock is threads permanently blocked waiting on each other's locks (avoided by always acquiring multiple locks in the same order).",
    ref: "Book — Fluent Python, Ch19 (Concurrency Models in Python)"
  },
  internals: "`requests` wraps urllib3, which implements HTTP over a TCP socket (request line, headers, body). Python threads map to real OS threads, but the GIL (Global Interpreter Lock) means only one thread executes Python bytecode at a time — threading helps I/O-bound waits (the GIL releases during them) but gives no speedup for CPU-bound work. That's exactly why these two modules are taught together: threads sit idle waiting on network calls.",
  keywords: ["requests.get()","response.json()","threading.Thread",".start()",".join()","threading.Lock"],
  dunders: [],
  modules: ["requests","threading"],
  methods: ["requests.post()","response.raise_for_status()","requests.Session()","concurrent.futures.ThreadPoolExecutor"],
  concepts: ["sessions & connection reuse","retry/backoff strategies","race conditions & deadlocks"],
  theory: ["Global Interpreter Lock (GIL)","I/O-bound vs CPU-bound concurrency"]
},
{
  n: 13, title: "Local API Endpoints", sub: "FastAPI",
  challenges: [
    {
      id: "challenge25",
      title: "URL Shortener API with Dependency-Injected Auth",
      blurb: "A URL shortener API with an API-key check injected via Depends(), Pydantic request/response models, an async def route, and Query() validation on a search endpoint.",
      path: "challenges/challenge25/"
    },
    {
      id: "challenge26",
      title: "Underground System API with Live Diagnostics",
      blurb: "Design Underground System (LeetCode #1396), with its storage injected via Depends() instead of touched directly in the routes, plus a TestClient()-based diagnostics utility and a mocked uvicorn.run().",
      path: "challenges/challenge26/"
    }
  ],
  schedule: [
    { step: "1", title: "Learn", details: "Building routes that return JSON, building up through Pydantic validation and dependency injection to async endpoints, middleware, and ASGI.", tiers: [
      { label: "Basic tier", guideKey: "stage13-basic", keywords: ["FastAPI()", "@app.get", "@app.post", "uvicorn.run"], modules: ["fastapi", "uvicorn"], concepts: ["path & query parameters"] },
      { label: "Mid tier", guideKey: "stage13-mid", keywords: ["Depends"], methods: ["BaseModel (pydantic)"], modules: ["pydantic"], concepts: ["dependency injection", "automatic interactive docs (/docs)"] },
      { label: "Advanced tier & internals", guideKey: "stage13-advanced", methods: ["TestClient()"], concepts: ["async def endpoints"], theory: ["ASGI vs WSGI", "type-hint-driven runtime validation"] }
    ] },
    { step: "2", title: "Practice", details: "Work through the exercises in exercises/stage13/ (see its README for the full list), running \`python tools/cli.py test stage13\` as you go." },
    { step: "3", title: "Review", details: "Finish any remaining exercises, get \`python tools/cli.py test stage13\` fully green, and review anything the group is still shaky on before moving on." }
  ],
  basic: {
    text: "app = FastAPI() creates the application instance that routes are registered on. @app.get(\"/path\")/@app.post(\"/path\") register a function as the handler for GET/POST requests to that path; path parameters ({item_id}) and query parameters are declared simply as ordinary Python function parameters with type hints. Returning a plain dict from a route handler is automatically serialized to a JSON response — no manual serialization step needed.",
    ref: "Web — FastAPI Tutorial, \u201cFirst Steps\u201d (fastapi.tiangolo.com/tutorial/first-steps)"
  },
  mid: {
    text: "A Pydantic BaseModel subclass describes the shape of a request or response body with typed fields; FastAPI uses it to validate incoming data automatically and reject malformed requests before your code even runs. FastAPI auto-generates interactive documentation at /docs (Swagger UI) and /redoc from your route signatures and Pydantic models — invaluable during development for trying out endpoints without writing a separate HTTP client. Depends(fn) declares a dependency FastAPI resolves and injects automatically before calling the route function, useful for shared logic like auth checks or a database session without repeating it in every route.",
    ref: "Web — FastAPI Tutorial, \u201cRequest Body\u201d and \u201cPath Parameters\u201d sections"
  },
  advanced: {
    text: "Route handlers can be declared async def to use non-blocking I/O (await) inside them, appropriate when a route needs to await other async calls like an async database driver — a plain def route still works fine for synchronous code. Middleware runs code before/after every request (logging, CORS, auth) without touching individual route functions. Background tasks let a route return a response immediately while continuing work afterward (e.g. sending a confirmation email). fastapi.testclient.TestClient calls the app in-process for testing, without needing a real running server or open port.",
    ref: "Web — FastAPI Advanced User Guide"
  },
  internals: "FastAPI is built on Starlette, an ASGI framework — contrasted with older WSGI frameworks like Flask. Routing matches an incoming URL against registered path patterns. FastAPI inspects your function's type hints at runtime (via Pydantic) to validate incoming data — a direct callback to the type hints taught in Topic 1.",
  keywords: ["FastAPI()","@app.get","@app.post","Depends","uvicorn.run"],
  dunders: [],
  modules: ["fastapi","pydantic","uvicorn"],
  methods: ["TestClient()","BaseModel (pydantic)"],
  concepts: ["path & query parameters","dependency injection","async def endpoints","automatic interactive docs (/docs)"],
  theory: ["ASGI vs WSGI","type-hint-driven runtime validation"]
},
{
  n: 14, title: "Capstone", sub: "putting it all together",
  schedule: [
    { step: "1", title: "Kickoff", details: "Pick a capstone idea that combines two or more earlier topics (e.g. pandas + requests, or OpenCV + FastAPI); scope it down to something finishable in the time available and sketch a short plan." },
    { step: "2", title: "Build", details: "Implement the core data handling/processing logic first, then wire in the second module (API, GUI, file I/O, etc.) and start adding basic tests or sanity checks." },
    { step: "3", title: "Polish", details: "Add error handling, write a short README for the capstone, and run python tools/cli.py test --all as a full sanity check across every stage." },
    { step: "4", title: "Demo & Review", details: "Present the capstone to the group, retro on the course, and point interested trainees at the optional deeper books noted in the main README." }
  ],
  basic: { text: "This stage has no new material — it is a synthesis stage. Pick a small project that combines two or more of Topics 1-13 (for example: pull data with requests, analyze it with pandas, and serve results through a small FastAPI app), scope it down to something finishable in the days available, and apply everything learned so far: clean functions, appropriate data structures, error handling, and a few classes where they genuinely help. Treat it as the first real test of whether the pieces fit together, not just whether each piece works in isolation.", ref: "" },
  mid: { text: "", ref: "" },
  advanced: { text: "", ref: "" },
  internals: "",
  keywords: [],
  dunders: [],
  modules: ["json + your choice of pandas/requests/opencv/FastAPI"],
  methods: [],
  concepts: ["synthesizing multiple modules into one project"],
  theory: []
},
{
  n: 15, title: "Appendix: The Tooling Itself", sub: "how cli.py / gui.py / core.py are built",
  basic: {
    text: "argparse.ArgumentParser with subparsers (list/test); subprocess.run() to launch pytest as a child process and capture its output; a virtual environment (python -m venv) plus pip install -r requirements.txt to isolate dependencies; tkinter's Tk()/ttk widgets for a basic window with a button.",
    ref: "Web — Python docs: argparse, subprocess, venv (docs.python.org/3/library/argparse.html)"
  },
  mid: {
    text: "ANSI escape codes to color terminal text, gated on sys.stdout.isatty() so piped output stays plain; running the tested subprocess in a background threading.Thread so a Tkinter GUI doesn't freeze while pytest runs; scrolledtext + tag_config for colored output panes; a shared core.py imported by both frontends so CLI and GUI can never drift apart.",
    ref: "Web — Python docs: threading, tkinter (docs.python.org/3/library/tkinter.html)"
  },
  advanced: {
    text: "Gating a git commit on a test's exit code via a pre-commit hook; structuring a repo so pytest can discover tests via conftest.py without installing the project as a package; propagating a subprocess's returncode out through sys.exit() so shell scripts and CI can check success/failure.",
    ref: "Web — Python docs, pytest docs “Good Integration Practices” (docs.pytest.org/en/stable/explanation/goodpractices.html)"
  },
  internals: "cli.py and gui.py are both thin presentation layers over the same core.py functions (run_stage_tests/run_all_tests) — neither talks to pytest directly, which is what keeps their behavior identical. subprocess.run() forks a child process, waits for it to exit, and hands back a CompletedProcess with .stdout/.stderr/.returncode; sys.exit(result.returncode) then makes the CLI's own exit code mirror pytest's, so shell `&&` chains and git hooks can react to it. Tkinter runs a single-threaded event loop (mainloop()) — blocking it with a slow subprocess call would freeze the window, which is exactly why gui.py hands the subprocess call to a background thread and marshals the result back with self.after(0, ...).",
  keywords: ["argparse.ArgumentParser","add_subparsers()","sys.exit()","if __name__ == \"__main__\":"],
  dunders: ["__main__"],
  modules: ["argparse","subprocess","tkinter","threading","venv"],
  methods: ["subprocess.run()","result.returncode","result.stdout / result.stderr","tkinter.Tk()","ttk.Button()","ttk.Combobox()","scrolledtext.ScrolledText()","threading.Thread()"],
  concepts: ["separating shared logic from each frontend","non-blocking GUI via background threads","exit codes as pass/fail signals","git hooks gating commits on tests"],
  theory: ["ANSI escape codes & isatty() terminal detection","Tkinter's single-threaded event loop model"],
  note: "This topic documents how this repo's own test runner (tools/cli.py, tools/gui.py, tools/core.py) is built — read it end to end and you have everything needed to rebuild a CLI+GUI test runner like this one from scratch."
}
];
