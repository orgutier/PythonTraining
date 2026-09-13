// Data for the Python Training reference. One entry per week/topic.
// Mirrors the "Study Reference - All Topics" sheet in the planning workbook.

const TOPICS = [
{
  n: 1, title: "Python Fundamentals", sub: "variables, types, operators",
  basic: {
    text: "Variables & assignment; int/float/str/bool/None; arithmetic & comparison operators; print()/input(); basic type casting; type hints for variables (x: int = 5).",
    ref: "Book — Python Distilled, §1.1–1.6"
  },
  mid: {
    text: "Operator precedence & chained comparisons; f-strings; // vs / and float imprecision; the walrus operator (:=); augmented assignment.",
    ref: "Book — Python Distilled, Ch2 (Operators, Expressions, and Data Manipulation)"
  },
  advanced: {
    text: "Arbitrary-precision integers; IEEE-754 float caveats (0.1 + 0.2 != 0.3); string interning; identity (is) vs equality (==); Decimal/Fraction for precision-sensitive work.",
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
  basic: {
    text: "if/elif/else; while; for + range(); break/continue/pass; nested loops.",
    ref: "Book — Python Distilled, §1.5, 1.12; Ch3"
  },
  mid: {
    text: "for...else / while...else; short-circuit and/or; ternary expressions (a if cond else b); zip() for parallel iteration.",
    ref: "Book — Python Distilled, Ch3 (continued)"
  },
  advanced: {
    text: "Writing a custom iterable/iterator class; itertools for advanced iteration patterns; loop-style performance differences.",
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
  basic: {
    text: "def, parameters, return, default args, *args/**kwargs, return type hints (->), basic recursion, lambda.",
    ref: "Book — Python Distilled, §1.13; Ch5"
  },
  mid: {
    text: "Keyword-only arguments (after *); positional-only parameters (before /); docstrings & introspection; closures; writing a simple decorator.",
    ref: "Book — Fluent Python, Ch9 (Decorators and Closures)"
  },
  advanced: {
    text: "functools (wraps, lru_cache, partial); generator functions (yield); recursion limits — Python has no tail-call optimization.",
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
  basic: {
    text: "list/tuple/dict/set — creation, indexing, slicing, common methods; list & dict comprehensions.",
    ref: "Book — Python Distilled, §1.8–1.11"
  },
  mid: {
    text: "Nested structures; sorting with key=; set operations (union/intersection/difference); namedtuple/dataclasses as lightweight records.",
    ref: "Book — Fluent Python, Ch2 (An Array of Sequences) & Ch3 (Dictionaries and Sets)"
  },
  advanced: {
    text: "collections (defaultdict, Counter, deque, OrderedDict); array/deque vs list performance; frozenset/tuple as hashable composite keys.",
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
  basic: {
    text: "open/with/read/write; try/except/finally/raise; custom exception classes; re.search/match/findall/sub.",
    ref: "Book — Python Distilled, §1.7, 1.14; Ch9"
  },
  mid: {
    text: "Exception chaining (raise ... from ...); exception hierarchies; contextlib beyond files; regex groups, named groups, re.compile.",
    ref: "Book — Fluent Python, Ch18 (with, match, and else Blocks)"
  },
  advanced: {
    text: "Custom context managers (__enter__/__exit__ or @contextmanager); regex lookahead/lookbehind; catastrophic-backtracking performance traps.",
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
  basic: {
    text: "class/__init__/self; instance vs class attributes; _protected/__private convention; @property/@staticmethod/@classmethod.",
    ref: "Book — Python Distilled, Ch7 §7.1–7.4, 7.15–7.17"
  },
  mid: {
    text: "__slots__ for memory savings; property with computed/cached values; cls vs self in practice.",
    ref: "Book — Fluent Python, Ch11 (A Pythonic Object)"
  },
  advanced: {
    text: "Writing a custom descriptor, not just using @property; metaclass basics (what `type` does); __init_subclass__ hook.",
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
  basic: {
    text: "class Child(Parent), super(), method overriding, duck typing.",
    ref: "Book — Python Distilled, Ch7 §7.7"
  },
  mid: {
    text: "Multiple inheritance basics; composition-vs-inheritance judgment; the abc module, @abstractmethod.",
    ref: "Book — Fluent Python, Ch13 (Interfaces, Protocols, and ABCs)"
  },
  advanced: {
    text: "Method Resolution Order & diamond inheritance; mixins; typing.Protocol for structural typing.",
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
  basic: {
    text: "__init__, __repr__, __str__, __eq__.",
    ref: "Book — Fluent Python, Ch1 (The Python Data Model)"
  },
  mid: {
    text: "__add__ and other operator dunders; __len__/__getitem__/__iter__/__contains__; __call__; __bool__.",
    ref: "Book — Fluent Python, Ch12 (Special Methods for Sequences)"
  },
  advanced: {
    text: "__enter__/__exit__ (context managers); reflected operators (__radd__) and NotImplemented; __hash__'s relationship to __eq__; __slots__ interaction with dunders.",
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
  basic: {
    text: "os.listdir/os.path; json.load/dump; datetime.now(); basic XML parsing with ElementTree.",
    ref: "Web — Python docs: os, json, datetime, xml.etree.ElementTree — neither priority book covers these stdlib modules in depth"
  },
  mid: {
    text: "pathlib as the modern os.path alternative; json custom encoders (default= for non-serializable objects); timezone-aware vs naive datetimes; ElementTree .findall() searching.",
    ref: "Web — Python docs, pathlib (docs.python.org/3/library/pathlib.html)"
  },
  advanced: {
    text: "os.walk for recursive traversal; datetime arithmetic & timedelta/DST edge cases; building/modifying XML trees, not just reading them.",
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
  basic: {
    text: "DataFrame/Series basics; read_csv; .head()/.info()/.describe().",
    ref: "Web — pandas docs, \u201c10 minutes to pandas\u201d (pandas.pydata.org/docs/user_guide/10min.html)"
  },
  mid: {
    text: "Boolean-indexing filters; groupby + aggregation; sorting; merging/joining DataFrames.",
    ref: "Web — pandas User Guide, Group By (pandas.pydata.org/docs/user_guide/groupby.html)"
  },
  advanced: {
    text: "Vectorized operations vs .apply() performance; multi-indexing; dtype-based memory optimization; pivot tables.",
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
  basic: {
    text: "cv2.imread/imwrite; cv2.cvtColor (color conversion); cv2.resize; basic drawing (rectangle/circle/line).",
    ref: "Web — OpenCV-Python official tutorials, \u201cGetting Started with Images\u201d (docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)"
  },
  mid: {
    text: "Thresholding; simple edge detection (Canny); cropping via array slicing; video capture from a file/webcam.",
    ref: "Web — OpenCV-Python tutorials, Image Processing section"
  },
  advanced: {
    text: "Contour detection; blur/sharpen filtering (convolution); Haar cascades for simple face/object detection.",
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
  basic: {
    text: "requests.get/post; response.json()/.status_code; threading.Thread — create/start/join.",
    ref: "Web — requests Quickstart + Python docs threading (docs.python.org/3/library/threading.html)"
  },
  mid: {
    text: "Headers/auth/query params/timeouts; raise_for_status(); Lock for protecting shared state between threads.",
    ref: "Web — requests \u201cAdvanced Usage\u201d (sessions, timeouts, retries)"
  },
  advanced: {
    text: "requests.Session for connection reuse; retry/backoff strategies; ThreadPoolExecutor instead of raw Thread objects; race conditions and deadlocks.",
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
  basic: {
    text: "FastAPI app instance; @app.get()/@app.post() routes; path & query parameters; returning a dict (auto-serialized to JSON).",
    ref: "Web — FastAPI Tutorial, \u201cFirst Steps\u201d (fastapi.tiangolo.com/tutorial/first-steps)"
  },
  mid: {
    text: "Pydantic models for request/response validation; automatic interactive docs (/docs); status codes; basic dependency injection (Depends).",
    ref: "Web — FastAPI Tutorial, \u201cRequest Body\u201d and \u201cPath Parameters\u201d sections"
  },
  advanced: {
    text: "async def endpoints; middleware; background tasks; testing with TestClient.",
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
  basic: { text: "Synthesis of Topics 1-13 into one small project. No new knowledge tier here — this week is applied review.", ref: "" },
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
  internals: "cli.py and gui.py are both thin presentation layers over the same core.py functions (run_week_tests/run_all_tests) — neither talks to pytest directly, which is what keeps their behavior identical. subprocess.run() forks a child process, waits for it to exit, and hands back a CompletedProcess with .stdout/.stderr/.returncode; sys.exit(result.returncode) then makes the CLI's own exit code mirror pytest's, so shell `&&` chains and git hooks can react to it. Tkinter runs a single-threaded event loop (mainloop()) — blocking it with a slow subprocess call would freeze the window, which is exactly why gui.py hands the subprocess call to a background thread and marshals the result back with self.after(0, ...).",
  keywords: ["argparse.ArgumentParser","add_subparsers()","sys.exit()","if __name__ == \"__main__\":"],
  dunders: ["__main__"],
  modules: ["argparse","subprocess","tkinter","threading","venv"],
  methods: ["subprocess.run()","result.returncode","result.stdout / result.stderr","tkinter.Tk()","ttk.Button()","ttk.Combobox()","scrolledtext.ScrolledText()","threading.Thread()"],
  concepts: ["separating shared logic from each frontend","non-blocking GUI via background threads","exit codes as pass/fail signals","git hooks gating commits on tests"],
  theory: ["ANSI escape codes & isatty() terminal detection","Tkinter's single-threaded event loop model"],
  note: "This topic documents how this repo's own test runner (tools/cli.py, tools/gui.py, tools/core.py) is built — read it end to end and you have everything needed to rebuild a CLI+GUI test runner like this one from scratch."
}
];
