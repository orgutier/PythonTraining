// Auto-generated -- see tools/review_data_extract.py + tools/review_data_build.js.
// Regenerate rather than hand-edit if exercises/challenges/exams/data.js change:
//   python tools/review_data_extract.py /tmp/review_extract
//   node tools/review_data_build.js /tmp/review_extract
const REVIEW_DATA = {
 "stages": [
  {
   "n": 1,
   "title": "Python Fundamentals",
   "sub": "variables, types, operators",
   "tiers": [
    {
     "label": "Setup",
     "ref": "Book — Python Distilled, §1.1–1.3 (a first program, variables, strings)",
     "newItems": {
      "keywords": [
       "print()"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "variable assignment",
       "string concatenation"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage01_tier0_hello_world",
       "name": "tier0_hello_world",
       "title": "Hello, World! (Environment Check)",
       "summary": "print(), variable assignment, string concatenation -- confirms your environment and this repo's test runner both work",
       "newItems": {
        "keywords": [
         "print()"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Basic tier",
     "ref": "Book — Python Distilled, §1.1–1.6",
     "newItems": {
      "keywords": [
       "int",
       "float",
       "str",
       "bool",
       "None",
       "True",
       "False",
       "input()",
       "type()",
       "isinstance()",
       "and",
       "or",
       "not",
       "is",
       "in",
       "x: int = 5"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "type hints"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [
       "print()"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [
       "bool",
       "None",
       "input()",
       "type()",
       "and",
       "or",
       "not",
       "is",
       "in",
       "x: int = 5"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage01_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Road Trip Fuel Ledger",
       "summary": "explicit int()/float() casting, arithmetic operators, isinstance(), no f-strings yet",
       "newItems": {
        "keywords": [
         "int",
         "float",
         "str",
         "isinstance()"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage01_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Digital Clock Decoder",
       "summary": "// and % chained together, explicit bool-from-string casting (avoiding the bool(str) trap)",
       "newItems": {
        "keywords": [
         "int",
         "str",
         "True",
         "False"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage01_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Precision Price Comparator",
       "summary": "operator precedence, chained comparisons, the walrus operator, f-strings, augmented assignment",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage01_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Marathon Pace Report",
       "summary": "more precedence/walrus/chained-comparison/augmented-assignment practice, a different scenario",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Web — Python docs, “Floating Point Arithmetic: Issues and Limitations” (docs.python.org/3/tutorial/floatingpoint.html)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "mutability vs immutability",
       "identity vs equality"
      ],
      "theory": [
       "small-integer caching",
       "string interning",
       "IEEE-754 floating point"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage01_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Exact Ledger vs. Float Drift",
       "summary": "Decimal built from string (not float), math.isclose() vs ==, the classic 0.1+0.2 case",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage01_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Big Numbers and String Identity",
       "summary": "arbitrary-precision integers, small-int caching, string interning (and its limits)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Testing tier",
     "ref": "Web — Python docs, unittest module overview (docs.python.org/3/library/unittest.html) -- read for how a real framework formalizes exactly the checks you just wrote by hand",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "manual test verification (no framework)",
       "expected-vs-actual comparison",
       "test oracle"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage01_tier4_testing",
       "name": "tier4_testing",
       "title": "Testing Without a Framework: Catch the Bug",
       "summary": "manual, framework-free verification -- plain comparisons, no assert, no pytest",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 2,
   "title": "Control Flow",
   "sub": "conditionals, loops",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Book — Python Distilled, §1.5, 1.12; Ch3",
     "newItems": {
      "keywords": [
       "if",
       "elif",
       "else",
       "while",
       "for",
       "range()",
       "break",
       "continue",
       "pass"
      ],
      "dunders": [],
      "modules": [],
      "methods": [
       "enumerate()"
      ],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [
       "in"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "enumerate()"
      ],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage02_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Warehouse Grid Scanner",
       "summary": "nested for + range(), if/elif/else, continue, pass, while + break",
       "newItems": {
        "keywords": [
         "if",
         "elif",
         "else",
         "while",
         "for",
         "range()",
         "break",
         "continue",
         "pass"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage02_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Bus Route Ticket Counter",
       "summary": "while as the main loop, if/elif/else, break, continue, pass, nested for",
       "newItems": {
        "keywords": [
         "if",
         "elif",
         "else",
         "while",
         "for",
         "range()",
         "break",
         "continue",
         "pass"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Book — Python Distilled, Ch3 (continued)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "zip()"
      ],
      "concepts": [
       "short-circuit evaluation",
       "ternary expression",
       "for...else / while...else"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage02_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Shift Coverage Checker",
       "summary": "for...else, a short-circuit guard, a ternary, zip()",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "zip()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage02_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Inventory Restock Matcher",
       "summary": "while...else, a short-circuit guard, a ternary, zip() -- a different combination",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "zip()"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Book — Fluent Python, Ch17 (Iterators, Generators, and Classic Coroutines)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [
       "itertools"
      ],
      "methods": [],
      "concepts": [
       "truthiness"
      ],
      "theory": [
       "iterator protocol (iter/next)",
       "StopIteration"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage02_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Custom Iterator: CountdownTimer",
       "summary": "a class implementing the iterator protocol (__iter__/__next__/StopIteration) by hand",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage02_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Round-Robin Task Scheduler",
       "summary": "itertools.chain + itertools.cycle + itertools.islice, combined",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [
         "itertools"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Testing tier",
     "ref": "",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "manual test verification (no framework)",
       "expected-vs-actual comparison",
       "test oracle"
      ],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage02_tier4_testing",
       "name": "tier4_testing",
       "title": "Testing Without a Framework: Catch the Bug",
       "summary": "manual, framework-free verification -- plain comparisons, no assert, no pytest",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 3,
   "title": "Functions",
   "sub": "parameters, scope, recursion",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Book — Python Distilled, §1.13; Ch5",
     "newItems": {
      "keywords": [
       "def",
       "return",
       "->",
       "*args",
       "**kwargs",
       "lambda"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [
       "*args",
       "**kwargs"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage03_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Order Total Calculator",
       "summary": "def, return, ->, default args, *args, **kwargs",
       "newItems": {
        "keywords": [
         "def",
         "return",
         "->"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage03_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Digit & List Utilities",
       "summary": "basic recursion, lambda, return type hints",
       "newItems": {
        "keywords": [
         "def",
         "return",
         "->",
         "lambda"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Book — Fluent Python, Ch9 (Decorators and Closures)",
     "newItems": {
      "keywords": [
       "nonlocal"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "decorators",
       "keyword-only arguments",
       "positional-only parameters"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [
       "nonlocal"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage03_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Rate-Limited Logger Factory + Clamp",
       "summary": "closures, keyword-only args, positional-only params, docstrings & introspection",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage03_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Call-Counting Decorator + Validated Config",
       "summary": "a simple decorator, closures, keyword-only args (a different scenario)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Book — Fluent Python, Ch7 (Functions as First-Class Objects)",
     "newItems": {
      "keywords": [
       "global",
       "yield"
      ],
      "dunders": [],
      "modules": [
       "functools"
      ],
      "methods": [
       "functools.wraps()",
       "functools.lru_cache()",
       "functools.partial()"
      ],
      "concepts": [
       "closures"
      ],
      "theory": [
       "LEGB scope resolution",
       "mutable default argument bug",
       "no tail-call optimization"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage03_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "functools Toolkit",
       "summary": "functools.wraps, functools.lru_cache, functools.partial",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [
         "functools"
        ],
        "methods": [
         "functools.wraps()",
         "functools.lru_cache()",
         "functools.partial()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage03_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Generators, Scope & the Mutable-Default Trap",
       "summary": "yield / generator functions, global + LEGB scoping, the mutable-default-argument bug",
       "newItems": {
        "keywords": [
         "global",
         "yield"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Testing tier",
     "ref": "",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "manual test verification (no framework)",
       "expected-vs-actual comparison",
       "test oracle"
      ],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage03_tier4_testing",
       "name": "tier4_testing",
       "title": "Testing Without a Framework: Catch the Bug",
       "summary": "manual, framework-free verification -- your own check() helper, no assert, no pytest",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 4,
   "title": "Data Structures",
   "sub": "lists, tuples, dicts, sets",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Book — Python Distilled, §1.8–1.11",
     "newItems": {
      "keywords": [
       "list",
       "tuple",
       "dict",
       "set",
       "append()",
       "sort()/sorted()",
       "len()",
       "[x for x in ...]",
       "{k:v for ...}"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [
       "zip()",
       "enumerate()"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage04_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Race Results Ledger",
       "summary": "list, tuple, append(), sort()/sorted(), zip(), enumerate(), len()",
       "newItems": {
        "keywords": [
         "list",
         "tuple",
         "append()",
         "sort()/sorted()",
         "len()",
         "[x for x in ...]"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage04_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Inventory Category Summary",
       "summary": "dict, set, dict comprehension, list comprehension, zip(), len()",
       "newItems": {
        "keywords": [
         "list",
         "dict",
         "set",
         "len()",
         "[x for x in ...]",
         "{k:v for ...}"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Book — Fluent Python, Ch2 (An Array of Sequences) & Ch3 (Dictionaries and Sets)",
     "newItems": {
      "keywords": [],
      "dunders": [
       "__eq__"
      ],
      "modules": [
       "collections",
       "dataclasses"
      ],
      "methods": [
       "dataclasses.dataclass"
      ],
      "concepts": [
       "namedtuple / dataclass records",
       "set operations (union/intersection/difference)"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [
       "__eq__"
      ],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage04_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Player Records: Dataclass vs. namedtuple",
       "summary": "dataclasses.dataclass, __eq__, collections module (namedtuple), dataclasses module, records",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [
         "collections",
         "dataclasses"
        ],
        "methods": [
         "dataclasses.dataclass"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage04_tier2_mid02",
       "name": "tier2_mid02",
       "title": "League Membership Analyzer",
       "summary": "set operations: union, intersection, difference",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Web — Python docs, collections module (docs.python.org/3/library/collections.html)",
     "newItems": {
      "keywords": [],
      "dunders": [
       "__hash__"
      ],
      "modules": [],
      "methods": [
       "collections.defaultdict()",
       "collections.Counter()",
       "collections.deque()"
      ],
      "concepts": [
       "hashability"
      ],
      "theory": [
       "dynamic array amortized growth",
       "hash table internals",
       "insertion-ordered dicts (3.7+)"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage04_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Log Aggregator",
       "summary": "collections.defaultdict(), collections.Counter() x2, collections.deque() x2",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "collections.defaultdict()",
         "collections.Counter()",
         "collections.deque()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage04_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Hashable Records: Frozen Dataclasses and Manual __hash__",
       "summary": "__hash__, hashability -- automatic (frozen dataclass) and manual (__eq__ + __hash__ pair)",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__hash__"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Testing tier",
     "ref": "",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "manual test verification (no framework)",
       "expected-vs-actual comparison",
       "test oracle"
      ],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage04_tier4_testing",
       "name": "tier4_testing",
       "title": "Testing Without a Framework: Catch the Bug",
       "summary": "manual, framework-free verification -- your own check() helper, no assert, no pytest",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 5,
   "title": "Files, Exceptions, Regex",
   "sub": "I/O, error handling, pattern matching",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Book — Python Distilled, §1.7, 1.14; Ch9",
     "newItems": {
      "keywords": [
       "open()",
       "with",
       "as",
       "try",
       "except",
       "finally",
       "raise",
       "Exception",
       "re.search()",
       "re.findall()"
      ],
      "dunders": [],
      "modules": [
       "re"
      ],
      "methods": [
       "re.match()",
       "re.sub()"
      ],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage05_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Session Log Files",
       "summary": "open(), with, as",
       "newItems": {
        "keywords": [
         "open()",
         "with",
         "as"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage05_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Support Ticket Intake",
       "summary": "try, except, finally, raise, Exception, re.search(), re.findall(), re.match(), re.sub()",
       "newItems": {
        "keywords": [
         "try",
         "except",
         "finally",
         "raise",
         "Exception",
         "re.search()",
         "re.findall()"
        ],
        "dunders": [],
        "modules": [
         "re"
        ],
        "methods": [
         "re.match()",
         "re.sub()"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Book — Fluent Python, Ch18 (with, match, and else Blocks)",
     "newItems": {
      "keywords": [
       "re.compile()"
      ],
      "dunders": [],
      "modules": [
       "contextlib"
      ],
      "methods": [],
      "concepts": [
       "exception chaining (raise ... from ...)",
       "exception hierarchies",
       "regex named groups"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [
       "contextlib"
      ],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage05_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Order Validation Pipeline",
       "summary": "exception hierarchies, exception chaining (raise ... from ...)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage05_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Config and Log Parsers",
       "summary": "re.compile(), regex named groups",
       "newItems": {
        "keywords": [
         "re.compile()"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Web — Python docs, Regular Expression HOWTO (docs.python.org/3/howto/regex.html)",
     "newItems": {
      "keywords": [],
      "dunders": [
       "__enter__",
       "__exit__"
      ],
      "modules": [],
      "methods": [
       "contextlib.contextmanager"
      ],
      "concepts": [
       "custom context managers"
      ],
      "theory": [
       "traceback propagation up the call stack",
       "backtracking regex engine",
       "catastrophic backtracking"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage05_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Class-Based Context Managers",
       "summary": "__enter__/__exit__",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__enter__",
         "__exit__"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage05_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Generator-Based Context Managers",
       "summary": "@contextlib.contextmanager",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "contextlib.contextmanager"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Testing tier",
     "ref": "",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "manual test verification (no framework)",
       "expected-vs-actual comparison",
       "test oracle"
      ],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage05_tier4_testing",
       "name": "tier4_testing",
       "title": "Testing Without a Framework: Catch the Bug",
       "summary": "manual, framework-free verification -- your own check() helper, no assert, no pytest",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 6,
   "title": "OOP I",
   "sub": "classes, encapsulation, properties",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Book — Python Distilled, Ch7 §7.1–7.4, 7.15–7.17",
     "newItems": {
      "keywords": [
       "class",
       "self",
       "__init__",
       "@property",
       "@x.setter",
       "@staticmethod",
       "@classmethod",
       "cls"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "encapsulation",
       "instance vs class attributes"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [
       "__init__"
      ],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage06_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Bank Account",
       "summary": "class, self, __init__, @property, @x.setter, @staticmethod, encapsulation",
       "newItems": {
        "keywords": [
         "class",
         "self",
         "__init__",
         "@property",
         "@x.setter",
         "@staticmethod"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage06_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Employee Registry",
       "summary": "instance vs class attributes, @classmethod, cls, @staticmethod, @property (read-only)",
       "newItems": {
        "keywords": [
         "class",
         "self",
         "__init__",
         "@property",
         "@staticmethod",
         "@classmethod",
         "cls"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Book — Fluent Python, Ch11 (A Pythonic Object)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "__slots__ memory savings"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage06_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Slotted Geometry",
       "summary": "__slots__",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage06_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Slotted Records",
       "summary": "__slots__ (two more classes)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Book — Fluent Python, Ch22 (Dynamic Attributes and Properties) & Ch23 (Attribute Descriptors)",
     "newItems": {
      "keywords": [],
      "dunders": [
       "__get__/__set__ (preview)"
      ],
      "modules": [],
      "methods": [],
      "concepts": [
       "descriptors"
      ],
      "theory": [
       "attribute lookup order (instance → class → MRO)",
       "descriptor protocol (__get__/__set__)"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage06_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Descriptors Preview: PositiveNumber",
       "summary": "__get__/__set__, descriptors",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__get__/__set__ (preview)"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage06_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Descriptors Preview: Typed",
       "summary": "__get__/__set__, descriptors (type-checking variant)",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__get__/__set__ (preview)"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Testing tier",
     "ref": "",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "manual test verification (no framework)",
       "expected-vs-actual comparison",
       "test oracle"
      ],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage06_tier4_testing",
       "name": "tier4_testing",
       "title": "Testing Without a Framework: Catch the Bug",
       "summary": "manual, framework-free verification -- your own check() helper, no assert, no pytest",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 7,
   "title": "OOP II",
   "sub": "inheritance, polymorphism, abstraction",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Book — Python Distilled, Ch7 §7.7",
     "newItems": {
      "keywords": [
       "class Child(Parent)",
       "super()"
      ],
      "dunders": [],
      "modules": [
       "typing"
      ],
      "methods": [],
      "concepts": [
       "polymorphism",
       "duck typing"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [
       "isinstance()"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage07_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Animal Sounds: Inheritance and Duck Typing",
       "summary": "class Child(Parent), super(), polymorphism, duck typing (side by side)",
       "newItems": {
        "keywords": [
         "class Child(Parent)",
         "super()"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage07_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Vehicle Fleet",
       "summary": "super() (three-level chain), isinstance(), typing module, polymorphism",
       "newItems": {
        "keywords": [
         "class Child(Parent)",
         "super()"
        ],
        "dunders": [],
        "modules": [
         "typing"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Book — Fluent Python, Ch13 (Interfaces, Protocols, and ABCs)",
     "newItems": {
      "keywords": [
       "abc",
       "ABC",
       "@abstractmethod"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "composition vs inheritance"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [
       "abc"
      ],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage07_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Abstract Base Classes",
       "summary": "abc module, ABC, @abstractmethod",
       "newItems": {
        "keywords": [
         "abc",
         "ABC",
         "@abstractmethod"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage07_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Composition and Swappable Engines",
       "summary": "composition vs inheritance",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Book — Fluent Python, Ch14 (Inheritance: For Better or For Worse)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "mixins",
       "Protocol structural typing"
      ],
      "theory": [
       "Method Resolution Order (C3 linearization)",
       "diamond inheritance"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage07_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Mixins",
       "summary": "mixins (multiple inheritance for composed-in behavior)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage07_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Protocol Structural Typing",
       "summary": "typing.Protocol, @runtime_checkable, isinstance() (structural)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Testing tier",
     "ref": "",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "manual test verification (no framework)",
       "expected-vs-actual comparison",
       "test oracle"
      ],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage07_tier4_testing",
       "name": "tier4_testing",
       "title": "Testing Without a Framework: Catch the Bug",
       "summary": "manual, framework-free verification -- your own check() helper, no assert, no pytest",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 8,
   "title": "The Python Data Model",
   "sub": "special methods, protocols",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Book — Fluent Python, Ch1 (The Python Data Model)",
     "newItems": {
      "keywords": [],
      "dunders": [
       "__repr__",
       "__str__"
      ],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [
       "__eq__"
      ],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage08_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Point: repr, str, eq",
       "summary": "__repr__, __str__, __eq__",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__repr__",
         "__str__"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage08_tier1_basic02",
       "name": "tier1_basic02",
       "title": "PlayingCard: repr, str, eq",
       "summary": "__repr__, __str__, __eq__ (a second scenario)",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__repr__",
         "__str__"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Book — Fluent Python, Ch12 (Special Methods for Sequences)",
     "newItems": {
      "keywords": [],
      "dunders": [
       "__add__",
       "__len__",
       "__getitem__",
       "__iter__",
       "__contains__",
       "__call__",
       "__bool__"
      ],
      "modules": [],
      "methods": [],
      "concepts": [
       "operator overloading",
       "protocols vs explicit inheritance"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage08_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Deck: A Collection Protocol",
       "summary": "__len__, __getitem__, __iter__, __contains__, __add__, operator overloading, protocols",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__add__",
         "__len__",
         "__getitem__",
         "__iter__",
         "__contains__"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage08_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Inventory and Callables",
       "summary": "__contains__, __iter__, __bool__ (reinforced), __call__",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__iter__",
         "__contains__",
         "__call__",
         "__bool__"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Book — Fluent Python, Ch16 (Operator Overloading)",
     "newItems": {
      "keywords": [],
      "dunders": [
       "__radd__"
      ],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": [
       "dunder lookup happens on the type, not the instance",
       "reflected operators & NotImplemented",
       "iterator protocol requires StopIteration"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [
       "__enter__",
       "__exit__",
       "__hash__"
      ],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage08_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Money and Score: Operator Overloading",
       "summary": "__repr__/__eq__ (reinforced), __add__, __radd__, __hash__",
       "newItems": {
        "keywords": [],
        "dunders": [
         "__radd__"
        ],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage08_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Context Managers as a Protocol",
       "summary": "__enter__, __exit__",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 9,
   "title": "OS, JSON, Datetime, XML",
   "sub": "everyday stdlib modules",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Web — Python docs: os, json, datetime, xml.etree.ElementTree — neither priority book covers these stdlib modules in depth",
     "newItems": {
      "keywords": [
       "os.listdir",
       "os.path",
       "json.load/dump",
       "datetime.now/isoformat",
       "ElementTree.parse/findall"
      ],
      "dunders": [],
      "modules": [
       "os",
       "json",
       "datetime",
       "xml.etree.ElementTree"
      ],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage09_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Config File Manager",
       "summary": "os.listdir, os.path, json.load/dump",
       "newItems": {
        "keywords": [
         "os.listdir",
         "os.path",
         "json.load/dump"
        ],
        "dunders": [],
        "modules": [
         "os",
         "json"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage09_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Library Catalog: Dates and XML",
       "summary": "datetime.now/isoformat, ElementTree.parse/findall",
       "newItems": {
        "keywords": [
         "datetime.now/isoformat",
         "ElementTree.parse/findall"
        ],
        "dunders": [],
        "modules": [
         "datetime",
         "xml.etree.ElementTree"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Web — Python docs, pathlib (docs.python.org/3/library/pathlib.html)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [
       "pathlib"
      ],
      "methods": [
       "pathlib.Path",
       "json.dumps(default=...)"
      ],
      "concepts": [
       "pathlib as the modern os.path alternative",
       "timezone-aware vs naive datetimes"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "json.dumps(default=...)"
      ],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage09_tier2_mid01",
       "name": "tier2_mid01",
       "title": "pathlib: The Modern os.path Alternative",
       "summary": "pathlib.Path, pathlib as the modern os.path alternative",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [
         "pathlib"
        ],
        "methods": [
         "pathlib.Path"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage09_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Timezone-Aware Timestamps in JSON",
       "summary": "json.dumps(default=...), timezone-aware vs naive datetimes",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Web — Python docs, os and xml.etree.ElementTree advanced sections",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "os.walk()"
      ],
      "concepts": [],
      "theory": [
       "JSON recursive-descent parsing",
       "DOM-style (ElementTree) vs streaming (SAX) XML parsing"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage09_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Recursing with os.walk: File Discovery",
       "summary": "os.walk()",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "os.walk()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage09_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Recursing with os.walk: Size and Depth",
       "summary": "os.walk() (two more scenarios)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "os.walk()"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 10,
   "title": "Pandas",
   "sub": "data analysis",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Web — pandas docs, “10 minutes to pandas” (pandas.pydata.org/docs/user_guide/10min.html)",
     "newItems": {
      "keywords": [
       "pd.read_csv",
       "df.head()"
      ],
      "dunders": [],
      "modules": [
       "pandas"
      ],
      "methods": [
       "df.describe()"
      ],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage10_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Reading and Inspecting Sales Data",
       "summary": "pd.read_csv, df.head(), df.describe()",
       "newItems": {
        "keywords": [
         "pd.read_csv",
         "df.head()"
        ],
        "dunders": [],
        "modules": [
         "pandas"
        ],
        "methods": [
         "df.describe()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage10_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Reading and Inspecting Employee Data",
       "summary": "pd.read_csv, df.head(), df.describe() (a second dataset)",
       "newItems": {
        "keywords": [
         "pd.read_csv",
         "df.head()"
        ],
        "dunders": [],
        "modules": [
         "pandas"
        ],
        "methods": [
         "df.describe()"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Web — pandas User Guide, Group By (pandas.pydata.org/docs/user_guide/groupby.html)",
     "newItems": {
      "keywords": [
       "df.groupby()",
       "df.sort_values()",
       "df.merge()"
      ],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [
       "boolean indexing"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage10_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Boolean Indexing",
       "summary": "boolean indexing",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage10_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Sorting, Grouping, and Merging",
       "summary": "df.sort_values(), df.groupby(), df.merge()",
       "newItems": {
        "keywords": [
         "df.groupby()",
         "df.sort_values()",
         "df.merge()"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Web — pandas User Guide, “Enhancing Performance” (pandas.pydata.org/docs/user_guide/enhancingperf.html)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "df.info()",
       "df.apply()",
       "df.pivot_table()"
      ],
      "concepts": [
       "multi-indexing",
       "dtype-based memory optimization"
      ],
      "theory": [
       "columnar storage backed by NumPy arrays",
       "vectorization vs per-row Python loops"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage10_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Inspecting, Pivoting, and Multi-Indexing",
       "summary": "df.info(), df.pivot_table(), multi-indexing (via groupby)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "df.info()",
         "df.pivot_table()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage10_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Apply and Dtype Optimization",
       "summary": "df.apply(), dtype-based memory optimization, multi-indexing (via set_index)",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "df.apply()"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 11,
   "title": "OpenCV",
   "sub": "hand posture & face gesture recognition",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Web — OpenCV-Python official tutorials, “Getting Started with Images” (docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)",
     "newItems": {
      "keywords": [
       "cv2.imread",
       "cv2.imwrite",
       "cv2.cvtColor",
       "cv2.resize",
       "cv2.rectangle",
       "image.shape"
      ],
      "dunders": [],
      "modules": [
       "opencv-python (cv2)",
       "numpy"
      ],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [
       "opencv-python (cv2)"
      ],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage11_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Loading and Inspecting Camera Frames",
       "summary": "cv2.imread, cv2.imwrite, image.shape, numpy",
       "newItems": {
        "keywords": [
         "cv2.imread",
         "cv2.imwrite",
         "image.shape"
        ],
        "dunders": [],
        "modules": [
         "numpy"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage11_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Preparing Frames for Detection",
       "summary": "cv2.cvtColor, cv2.resize, cv2.rectangle",
       "newItems": {
        "keywords": [
         "cv2.cvtColor",
         "cv2.resize",
         "cv2.rectangle"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Web — OpenCV-Python tutorials, Image Processing section",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "cv2.Canny()"
      ],
      "concepts": [
       "thresholding"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage11_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Skin-Tone Thresholding for Hand Segmentation",
       "summary": "thresholding",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage11_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Edge Detection on the Hand Silhouette",
       "summary": "cv2.Canny()",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "cv2.Canny()"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Web — OpenCV-Python tutorials, Contours + Cascade Classifier sections",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "cv2.findContours()",
       "cv2.GaussianBlur()",
       "cv2.CascadeClassifier"
      ],
      "concepts": [
       "convolution filtering"
      ],
      "theory": [
       "images as NumPy arrays (height × width × channels)",
       "BGR vs RGB channel order"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage11_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Hand Posture via Contours and Convexity Defects",
       "summary": "cv2.findContours(), cv2.GaussianBlur(), convolution filtering",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "cv2.findContours()",
         "cv2.GaussianBlur()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage11_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Face Gesture and Gaze Direction (Driver-Camera Style)",
       "summary": "cv2.CascadeClassifier",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "cv2.CascadeClassifier"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 12,
   "title": "Requests + Threading",
   "sub": "HTTP clients, concurrency",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Web — requests Quickstart + Python docs threading (docs.python.org/3/library/threading.html)",
     "newItems": {
      "keywords": [
       "requests.get()",
       "response.json()",
       "threading.Thread",
       ".start()",
       ".join()"
      ],
      "dunders": [],
      "modules": [
       "requests",
       "threading"
      ],
      "methods": [
       "requests.post()"
      ],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage12_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Requests Basics",
       "summary": "requests.get(), response.json(), requests.post()",
       "newItems": {
        "keywords": [
         "requests.get()",
         "response.json()"
        ],
        "dunders": [],
        "modules": [
         "requests"
        ],
        "methods": [
         "requests.post()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage12_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Threading Basics",
       "summary": "threading.Thread, .start(), .join()",
       "newItems": {
        "keywords": [
         "threading.Thread",
         ".start()",
         ".join()"
        ],
        "dunders": [],
        "modules": [
         "threading"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Web — requests “Advanced Usage” (sessions, timeouts, retries)",
     "newItems": {
      "keywords": [
       "threading.Lock"
      ],
      "dunders": [],
      "modules": [],
      "methods": [
       "response.raise_for_status()"
      ],
      "concepts": [],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage12_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Raising on HTTP Errors",
       "summary": "response.raise_for_status()",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "response.raise_for_status()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage12_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Locks Guarding Shared State",
       "summary": "threading.Lock",
       "newItems": {
        "keywords": [
         "threading.Lock"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Book — Fluent Python, Ch19 (Concurrency Models in Python)",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "requests.Session()",
       "concurrent.futures.ThreadPoolExecutor"
      ],
      "concepts": [
       "sessions & connection reuse",
       "retry/backoff strategies",
       "race conditions & deadlocks"
      ],
      "theory": [
       "Global Interpreter Lock (GIL)",
       "I/O-bound vs CPU-bound concurrency"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage12_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Sessions and Retry/Backoff",
       "summary": "requests.Session(), connection reuse, retry/backoff strategies",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "requests.Session()"
        ],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage12_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "ThreadPoolExecutor",
       "summary": "concurrent.futures.ThreadPoolExecutor",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "concurrent.futures.ThreadPoolExecutor"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 13,
   "title": "Local API Endpoints",
   "sub": "FastAPI",
   "tiers": [
    {
     "label": "Basic tier",
     "ref": "Web — FastAPI Tutorial, “First Steps” (fastapi.tiangolo.com/tutorial/first-steps)",
     "newItems": {
      "keywords": [
       "FastAPI()",
       "@app.get",
       "@app.post",
       "uvicorn.run"
      ],
      "dunders": [],
      "modules": [
       "fastapi",
       "uvicorn"
      ],
      "methods": [],
      "concepts": [
       "path & query parameters"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage13_tier1_basic01",
       "name": "tier1_basic01",
       "title": "Basic Routes",
       "summary": "FastAPI(), @app.get, @app.post, path & query parameters",
       "newItems": {
        "keywords": [
         "FastAPI()",
         "@app.get",
         "@app.post"
        ],
        "dunders": [],
        "modules": [
         "fastapi"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage13_tier1_basic02",
       "name": "tier1_basic02",
       "title": "Running the App",
       "summary": "FastAPI(), @app.get, @app.post, uvicorn.run",
       "newItems": {
        "keywords": [
         "FastAPI()",
         "@app.get",
         "@app.post",
         "uvicorn.run"
        ],
        "dunders": [],
        "modules": [
         "fastapi",
         "uvicorn"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Mid tier",
     "ref": "Web — FastAPI Tutorial, “Request Body” and “Path Parameters” sections",
     "newItems": {
      "keywords": [
       "Depends"
      ],
      "dunders": [],
      "modules": [
       "pydantic"
      ],
      "methods": [
       "BaseModel (pydantic)"
      ],
      "concepts": [
       "dependency injection",
       "automatic interactive docs (/docs)"
      ],
      "theory": []
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "BaseModel (pydantic)"
      ],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage13_tier2_mid01",
       "name": "tier2_mid01",
       "title": "Pydantic Models",
       "summary": "pydantic.BaseModel",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [
         "pydantic"
        ],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage13_tier2_mid02",
       "name": "tier2_mid02",
       "title": "Dependency Injection and Automatic Docs",
       "summary": "Depends, dependency injection, automatic interactive docs (/docs)",
       "newItems": {
        "keywords": [
         "Depends"
        ],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      }
     ]
    },
    {
     "label": "Advanced tier & internals",
     "ref": "Web — FastAPI Advanced User Guide",
     "newItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [
       "TestClient()"
      ],
      "concepts": [
       "async def endpoints"
      ],
      "theory": [
       "ASGI vs WSGI",
       "type-hint-driven runtime validation"
      ]
     },
     "refreshItems": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "tierOnlyNew": {
      "keywords": [],
      "dunders": [],
      "modules": [],
      "methods": [],
      "concepts": [],
      "theory": []
     },
     "exercises": [
      {
       "id": "stage13_tier3_advanced01",
       "name": "tier3_advanced01",
       "title": "Async Endpoints",
       "summary": "async def endpoints",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [],
        "concepts": [],
        "theory": []
       }
      },
      {
       "id": "stage13_tier3_advanced02",
       "name": "tier3_advanced02",
       "title": "Testing Apps with TestClient",
       "summary": "TestClient()",
       "newItems": {
        "keywords": [],
        "dunders": [],
        "modules": [],
        "methods": [
         "TestClient()"
        ],
        "concepts": [],
        "theory": []
       }
      }
     ]
    }
   ]
  },
  {
   "n": 14,
   "title": "Capstone",
   "sub": "putting it all together",
   "isCapstone": true,
   "newConcepts": [
    "synthesizing multiple modules into one project"
   ],
   "note": "This stage has no new material — it is a synthesis stage. Pick a small project that combines two or more of Topics 1-13 (for example: pull data with requests, analyze it with pandas, and serve results through a small FastAPI app), scope it down to something finishable in the days available, and apply everything learned so far: clean functions, appropriate data structures, error handling, and a few classes where they genuinely help. Treat it as the first real test of whether the pieces fit together, not just whether each piece works in isolation."
  }
 ],
 "challenges": {
  "challenge01": {
   "id": "challenge01",
   "title": "Typed Config Loader",
   "blurb": "Parse KEY=value config lines into properly typed int/float/bool/None/str values by hand -- no try/except numeric-detection shortcuts, isinstance()/type() used explicitly, and the result is always a brand-new dict.",
   "stage": "stage01",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "str",
     "bool",
     "None",
     "False",
     "type()",
     "and",
     "or",
     "not",
     "in",
     "x: int = 5",
     "if",
     "for",
     "continue",
     "def",
     "return",
     "->",
     "list",
     "tuple",
     "dict",
     "len()",
     "{k:v for ...}",
     "with",
     "raise",
     ".start()"
    ],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge02": {
   "id": "challenge02",
   "title": "Identity, Equality, and a Login Prompt",
   "blurb": "A pairwise identity-vs-equality auditor plus a None-safe login prompt -- is/is not used explicitly throughout, and a bare is-None check instead of truthiness so an empty string is never mistaken for a missing one.",
   "stage": "stage01",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "print()",
     "str",
     "None",
     "True",
     "False",
     "input()",
     "or",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "elif",
     "else",
     "for",
     "range()",
     "break",
     "def",
     "return",
     "->",
     "list",
     "dict",
     "append()",
     "len()"
    ],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge03": {
   "id": "challenge03",
   "title": "Log Stream Parser and Scanner",
   "blurb": "Parse and scan a stream of log lines using a for...else search, enumerate()/zip() for labeling and pairing, and one and/not expression for a health check -- most of Stage 2's control-flow toolkit in one pipeline.",
   "stage": "stage02",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "bool",
     "input()",
     "and",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "else",
     "for",
     "break",
     "continue",
     "enumerate()",
     "zip()",
     "def",
     "return",
     "->",
     "list",
     "tuple",
     "append()",
     "[x for x in ...]",
     "with",
     "as"
    ],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge04": {
   "id": "challenge04",
   "title": "Batch Retry Simulator",
   "blurb": "A batch-retry simulator built around a while...else loop, itertools.chain + islice for flattening batches, and a chained ternary for status labels.",
   "stage": "stage02",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "else",
     "while",
     "for",
     "range()",
     "break",
     "continue",
     "def",
     "return",
     "->",
     "list",
     "tuple",
     "append()",
     "len()",
     "raise"
    ],
    "dunders": [],
    "modules": [
     "itertools"
    ],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge05": {
   "id": "challenge05",
   "title": "Pluggable Event Pipeline",
   "blurb": "A closure-based plugin registry, plus two flavors of caching decorator -- a hand-rolled memoize() and functools.lru_cache with a keyword-only parameter -- every decorator preserving metadata via functools.wraps.",
   "stage": "stage03",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "None",
     "not",
     "in",
     "x: int = 5",
     "if",
     "for",
     "def",
     "return",
     "->",
     "*args",
     "**kwargs",
     "nonlocal",
     "tuple",
     "sort()/sorted()",
     "raise"
    ],
    "dunders": [],
    "modules": [
     "functools"
    ],
    "methods": [
     "functools.wraps()",
     "functools.lru_cache()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge06": {
   "id": "challenge06",
   "title": "Streaming Metrics Aggregator",
   "blurb": "A streaming batch processor combining a real generator (yield), positional-only AND keyword-only parameters in the same signature, module state via global, and functools.partial for a reusable transform.",
   "stage": "stage03",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "None",
     "not",
     "is",
     "in",
     "for",
     "range()",
     "def",
     "return",
     "->",
     "lambda",
     "global",
     "yield",
     "list",
     "len()",
     "[x for x in ...]"
    ],
    "dunders": [],
    "modules": [
     "functools"
    ],
    "methods": [
     "functools.partial()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge07": {
   "id": "challenge07",
   "title": "Anagram Groups with Records",
   "blurb": "Group Anagrams (LeetCode #49), rebuilt around collections.defaultdict and a frozen, hashable dataclass record for each group -- plus set operations and enumerate() for the derived reports.",
   "stage": "stage04",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "True",
     "input()",
     "is",
     "in",
     "for",
     "enumerate()",
     "def",
     "return",
     "->",
     "lambda",
     "list",
     "tuple",
     "set",
     "append()",
     "sort()/sorted()",
     "len()",
     "[x for x in ...]",
     "class",
     "self",
     ".join()"
    ],
    "dunders": [
     "__len__"
    ],
    "modules": [
     "collections",
     "dataclasses"
    ],
    "methods": [
     "dataclasses.dataclass",
     "collections.defaultdict()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge08": {
   "id": "challenge08",
   "title": "Longest Consecutive Run of Records",
   "blurb": "Longest Consecutive Sequence (LeetCode #128), returning every run (not just the longest) as collections.namedtuple records, found in O(n) via a set -- no sorting the raw input.",
   "stage": "stage04",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "bool",
     "and",
     "not",
     "in",
     "x: int = 5",
     "if",
     "for",
     "range()",
     "def",
     "return",
     "->",
     "lambda",
     "list",
     "set",
     "append()",
     "sort()/sorted()",
     "as",
     "raise",
     ".start()"
    ],
    "dunders": [],
    "modules": [
     "collections"
    ],
    "methods": [
     "json.dumps(default=...)"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge09": {
   "id": "challenge09",
   "title": "Log File Parser with a Custom Exception Chain",
   "blurb": "Parse a real log file with a two-level custom exception hierarchy, a compiled regex with named groups, and raise ... from ... chaining when a bad line is found.",
   "stage": "stage05",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "None",
     "or",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "for",
     "continue",
     "pass",
     "enumerate()",
     "def",
     "return",
     "->",
     "list",
     "tuple",
     "dict",
     "append()",
     "open()",
     "with",
     "as",
     "try",
     "except",
     "raise",
     "Exception",
     "re.compile()",
     "class",
     "class Child(Parent)"
    ],
    "dunders": [],
    "modules": [
     "re"
    ],
    "methods": [
     "re.match()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge10": {
   "id": "challenge10",
   "title": "Log Text Utilities with a Custom Context Manager",
   "blurb": "Text-processing utilities plus the same \"suppress and count\" context manager built two ways -- a class with __enter__/__exit__, and the @contextlib.contextmanager generator equivalent -- alongside re.findall()/re.sub()/re.search().",
   "stage": "stage05",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "str",
     "bool",
     "None",
     "True",
     "False",
     "and",
     "not",
     "is",
     "if",
     "def",
     "return",
     "->",
     "yield",
     "list",
     "try",
     "except",
     "re.search()",
     "re.findall()",
     "class",
     "self",
     "ElementTree.parse/findall"
    ],
    "dunders": [
     "__enter__",
     "__exit__",
     "__init__"
    ],
    "modules": [
     "re",
     "contextlib"
    ],
    "methods": [
     "re.sub()",
     "contextlib.contextmanager"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge11": {
   "id": "challenge11",
   "title": "LRU Cache with a Descriptor and Class-Level Stats",
   "blurb": "LRU Cache (LeetCode #146) with O(1) get/put via a hand-built doubly linked list, __slots__, a validating descriptor for capacity, a computed @property, and a @classmethod alternate constructor.",
   "stage": "stage06",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "bool",
     "None",
     "isinstance()",
     "and",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "else",
     "for",
     "def",
     "return",
     "->",
     "dict",
     "len()",
     "raise",
     "class",
     "self",
     "@property",
     "@staticmethod",
     "@classmethod",
     "cls"
    ],
    "dunders": [
     "__init__",
     "__get__/__set__ (preview)"
    ],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge12": {
   "id": "challenge12",
   "title": "Min Stack with Class-Level Push Stats",
   "blurb": "Min Stack (LeetCode #155) with O(1) minimum() and no min() call, wrapped in a __slots__ class that tracks total pushes across every instance via a class attribute.",
   "stage": "stage06",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "bool",
     "None",
     "isinstance()",
     "and",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "else",
     "for",
     "def",
     "return",
     "->",
     "append()",
     "as",
     "raise",
     "class",
     "self",
     "@property",
     "@staticmethod",
     "@classmethod",
     "cls"
    ],
    "dunders": [
     "__init__"
    ],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge13": {
   "id": "challenge13",
   "title": "Notification System with Mixins and ABCs",
   "blurb": "A notification dispatcher built from an abc.ABC base, mixins combined via multiple inheritance, super() cooperating through the chain, and isinstance()/duck typing in the broadcaster.",
   "stage": "stage07",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "None",
     "isinstance()",
     "not",
     "in",
     "x: int = 5",
     "if",
     "else",
     "for",
     "range()",
     "continue",
     "def",
     "return",
     "->",
     "list",
     "append()",
     "as",
     "try",
     "except",
     "raise",
     "class",
     "self",
     "class Child(Parent)",
     "super()",
     "ABC",
     "@abstractmethod"
    ],
    "dunders": [
     "__init__"
    ],
    "modules": [
     "abc"
    ],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge14": {
   "id": "challenge14",
   "title": "Shape Library with Protocols and Composition",
   "blurb": "A shape library where Circle and Rectangle share no base class at all -- only a runtime_checkable typing.Protocol -- plus a CompositeShape built by composition, not inheritance.",
   "stage": "stage07",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "float",
     "None",
     "isinstance()",
     "not",
     "in",
     "if",
     "for",
     "def",
     "return",
     "->",
     "lambda",
     "list",
     "with",
     "class",
     "self",
     "class Child(Parent)",
     "image.shape"
    ],
    "dunders": [
     "__init__"
    ],
    "modules": [
     "typing"
    ],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge15": {
   "id": "challenge15",
   "title": "Matrix: A Rich Numeric Type",
   "blurb": "A Matrix class implementing ten dunders at once -- __repr__/__str__/__eq__/__hash__/__add__/__radd__/__len__/__getitem__/__iter__/__contains__/__bool__ -- with NotImplemented used correctly so + fails cleanly on a shape mismatch.",
   "stage": "stage08",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "bool",
     "None",
     "isinstance()",
     "and",
     "or",
     "not",
     "in",
     "if",
     "for",
     "zip()",
     "def",
     "return",
     "->",
     "list",
     "tuple",
     "len()",
     "[x for x in ...]",
     "{k:v for ...}",
     "as",
     "class",
     "self",
     ".join()"
    ],
    "dunders": [
     "__eq__",
     "__hash__",
     "__init__",
     "__repr__",
     "__str__",
     "__add__",
     "__len__",
     "__getitem__",
     "__iter__",
     "__contains__",
     "__bool__",
     "__radd__"
    ],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge16": {
   "id": "challenge16",
   "title": "Transaction Ledger: Callable and Context Manager",
   "blurb": "A transaction ledger that's directly callable (__call__) and a context manager (__enter__/__exit__) with commit-or-rollback batching -- no inheritance from any special base required for either to work.",
   "stage": "stage08",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "str",
     "bool",
     "None",
     "False",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "else",
     "for",
     "def",
     "return",
     "->",
     "append()",
     "len()",
     "with",
     "class",
     "self",
     "@property"
    ],
    "dunders": [
     "__enter__",
     "__exit__",
     "__init__",
     "__repr__",
     "__len__",
     "__call__"
    ],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge17": {
   "id": "challenge17",
   "title": "Directory Report Builder",
   "blurb": "A directory report builder combining os.walk(), pathlib's rglob() as the modern alternative, and json.dumps(default=...) to serialize the real datetime objects it collects.",
   "stage": "stage09",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "str",
     "None",
     "isinstance()",
     "and",
     "not",
     "in",
     "x: int = 5",
     "if",
     "for",
     "def",
     "return",
     "->",
     "lambda",
     "list",
     "dict",
     "append()",
     "sort()/sorted()",
     "len()",
     "{k:v for ...}",
     "open()",
     "with",
     "as",
     "raise",
     "os.path",
     "json.load/dump",
     "datetime.now/isoformat",
     "requests.get()",
     ".join()",
     "@app.get"
    ],
    "dunders": [],
    "modules": [
     "os",
     "json",
     "datetime",
     "pathlib"
    ],
    "methods": [
     "pathlib.Path",
     "os.walk()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge18": {
   "id": "challenge18",
   "title": "XML Feed to Timezone-Aware Digest",
   "blurb": "Parse an XML event feed (ElementTree, findall()), explicitly attach UTC to its naive timestamps, and rebuild a fresh XML document from the result.",
   "stage": "stage09",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "str",
     "bool",
     "None",
     "input()",
     "is",
     "in",
     "x: int = 5",
     "if",
     "for",
     "def",
     "return",
     "->",
     "lambda",
     "list",
     "append()",
     "sort()/sorted()",
     "as",
     "re.findall()",
     "datetime.now/isoformat",
     "ElementTree.parse/findall",
     "requests.get()",
     "@app.get"
    ],
    "dunders": [],
    "modules": [
     "datetime",
     "xml.etree.ElementTree"
    ],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "challenge19": {
   "id": "challenge19",
   "title": "Sales Data Analyzer",
   "blurb": "A sales data analyzer using nothing but groupby()/sort_values()/boolean indexing/pivot_table() -- zero explicit row loops -- plus category-dtype memory optimization.",
   "stage": "stage10",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "str",
     "False",
     "not",
     "is",
     "for",
     "def",
     "return",
     "->",
     "with",
     "as",
     "pd.read_csv",
     "df.head()",
     "df.groupby()",
     "df.sort_values()"
    ],
    "dunders": [],
    "modules": [
     "pandas"
    ],
    "methods": [
     "df.pivot_table()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge20": {
   "id": "challenge20",
   "title": "Two Sum, Pandas-Style, with Joins and Diagnostics",
   "blurb": "Two Sum (LeetCode #1) solved as a vectorized pandas.Series operation, alongside df.merge(), df.apply(), a two-key groupby (MultiIndex), and a df.head()/info()/describe() diagnostics bundle.",
   "stage": "stage10",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "None",
     "or",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "for",
     "def",
     "return",
     "->",
     "dict",
     "with",
     "as",
     "df.head()",
     "df.groupby()",
     "df.merge()",
     "requests.get()",
     "@app.get"
    ],
    "dunders": [],
    "modules": [
     "pandas"
    ],
    "methods": [
     "df.describe()",
     "df.info()",
     "df.apply()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge21": {
   "id": "challenge21",
   "title": "Document Scanner Preprocessing Pipeline",
   "blurb": "A document-scanner preprocessing pipeline: grayscale -> Gaussian blur -> Canny edges -> the largest-contour trick -> an aspect-ratio-preserving resize.",
   "stage": "stage11",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "None",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "def",
     "return",
     "->",
     "tuple",
     "dict",
     "cv2.cvtColor",
     "cv2.resize",
     "cv2.rectangle",
     "image.shape"
    ],
    "dunders": [],
    "modules": [],
    "methods": [
     "cv2.Canny()",
     "cv2.findContours()",
     "cv2.GaussianBlur()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge22": {
   "id": "challenge22",
   "title": "Face-Region Redactor",
   "blurb": "A face-region redactor built on cv2.CascadeClassifier, with box-clipping via image.shape, adaptive thresholding, and cv2.imread()/imwrite() file I/O.",
   "stage": "stage11",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "str",
     "bool",
     "type()",
     "not",
     "is",
     "in",
     "x: int = 5",
     "for",
     "def",
     "return",
     "->",
     "list",
     "tuple",
     "[x for x in ...]",
     "cv2.imread",
     "cv2.imwrite",
     "cv2.rectangle",
     "image.shape"
    ],
    "dunders": [],
    "modules": [],
    "methods": [
     "cv2.CascadeClassifier"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge23": {
   "id": "challenge23",
   "title": "Rate-Limited HTTP Client",
   "blurb": "A thread-safe token-bucket rate limiter wired into an actual requests.Session-based HTTP client -- fetched concurrently from raw threading.Thread workers, results returned in the original order.",
   "stage": "stage12",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "str",
     "bool",
     "None",
     "True",
     "False",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "while",
     "for",
     "enumerate()",
     "def",
     "return",
     "->",
     "list",
     "dict",
     "len()",
     "[x for x in ...]",
     "with",
     "class",
     "self",
     "requests.get()",
     "response.json()",
     "threading.Thread",
     ".start()",
     ".join()",
     "threading.Lock",
     "@app.get"
    ],
    "dunders": [
     "__init__"
    ],
    "modules": [
     "json",
     "requests",
     "threading"
    ],
    "methods": [
     "response.raise_for_status()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge24": {
   "id": "challenge24",
   "title": "Bounded Job Queue with Retry and ThreadPoolExecutor",
   "blurb": "A retrying job submitter (requests.post + exponential backoff) driven by concurrent.futures.ThreadPoolExecutor, with a threading.Lock-protected counter proving exact correctness under real concurrency.",
   "stage": "stage12",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "None",
     "not",
     "in",
     "x: int = 5",
     "if",
     "for",
     "range()",
     "def",
     "return",
     "->",
     "lambda",
     "list",
     "dict",
     "with",
     "as",
     "try",
     "except",
     "raise",
     "class",
     "self",
     "@property",
     "response.json()",
     "threading.Thread",
     "threading.Lock",
     "@app.post"
    ],
    "dunders": [
     "__init__"
    ],
    "modules": [
     "json",
     "requests",
     "threading"
    ],
    "methods": [
     "re.sub()",
     "requests.post()",
     "response.raise_for_status()",
     "concurrent.futures.ThreadPoolExecutor"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge25": {
   "id": "challenge25",
   "title": "URL Shortener API with Dependency-Injected Auth",
   "blurb": "A URL shortener API with an API-key check injected via Depends(), Pydantic request/response models, an async def route, and Query() validation on a search endpoint.",
   "stage": "stage13",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "None",
     "not",
     "in",
     "x: int = 5",
     "if",
     "while",
     "for",
     "def",
     "return",
     "->",
     "[x for x in ...]",
     "raise",
     "class",
     "class Child(Parent)",
     "requests.get()",
     ".start()",
     "FastAPI()",
     "@app.get",
     "@app.post",
     "Depends"
    ],
    "dunders": [],
    "modules": [
     "fastapi",
     "pydantic"
    ],
    "methods": [
     "requests.post()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "challenge26": {
   "id": "challenge26",
   "title": "Underground System API with Live Diagnostics",
   "blurb": "Design Underground System (LeetCode #1396), with its storage injected via Depends() instead of touched directly in the routes, plus a TestClient()-based diagnostics utility and a mocked uvicorn.run().",
   "stage": "stage13",
   "newItems": {
    "keywords": [],
    "dunders": [],
    "modules": [],
    "methods": [],
    "concepts": [],
    "theory": []
   },
   "refreshItems": {
    "keywords": [
     "int",
     "str",
     "None",
     "True",
     "not",
     "in",
     "x: int = 5",
     "if",
     "for",
     "def",
     "return",
     "->",
     "dict",
     "sort()/sorted()",
     "raise",
     "class",
     "class Child(Parent)",
     "requests.get()",
     "response.json()",
     "FastAPI()",
     "@app.get",
     "@app.post",
     "uvicorn.run",
     "Depends"
    ],
    "dunders": [],
    "modules": [
     "json",
     "fastapi",
     "uvicorn",
     "pydantic"
    ],
    "methods": [
     "requests.post()",
     "TestClient()"
    ],
    "concepts": [],
    "theory": []
   }
  }
 },
 "exams": {
  "exam01": {
   "id": "exam01",
   "lo": 1,
   "hi": 4,
   "refreshItems": {
    "keywords": [
     "int",
     "float",
     "str",
     "bool",
     "None",
     "True",
     "and",
     "or",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "else",
     "while",
     "for",
     "break",
     "enumerate()",
     "zip()",
     "def",
     "return",
     "->",
     "*args",
     "lambda",
     "list",
     "dict",
     "set",
     "append()",
     "sort()/sorted()",
     "len()",
     "{k:v for ...}",
     "raise",
     "class",
     ".start()"
    ],
    "dunders": [],
    "modules": [
     "functools",
     "collections",
     "dataclasses"
    ],
    "methods": [],
    "concepts": [],
    "theory": []
   }
  },
  "exam02": {
   "id": "exam02",
   "lo": 5,
   "hi": 9,
   "refreshItems": {
    "keywords": [
     "str",
     "None",
     "True",
     "False",
     "isinstance()",
     "and",
     "or",
     "not",
     "is",
     "in",
     "x: int = 5",
     "if",
     "elif",
     "else",
     "for",
     "pass",
     "def",
     "return",
     "->",
     "list",
     "tuple",
     "dict",
     "set",
     "append()",
     "sort()/sorted()",
     "len()",
     "[x for x in ...]",
     "with",
     "as",
     "try",
     "except",
     "raise",
     "Exception",
     "re.findall()",
     "re.compile()",
     "class",
     "self",
     "@property",
     "@classmethod",
     "cls",
     "class Child(Parent)",
     "super()",
     "ABC",
     "@abstractmethod",
     "datetime.now/isoformat",
     "ElementTree.parse/findall",
     "requests.get()",
     "@app.get"
    ],
    "dunders": [
     "__eq__",
     "__hash__",
     "__enter__",
     "__exit__",
     "__init__",
     "__get__/__set__ (preview)",
     "__repr__",
     "__len__",
     "__iter__",
     "__contains__"
    ],
    "modules": [
     "re",
     "abc",
     "json",
     "datetime",
     "pathlib"
    ],
    "methods": [
     "re.match()"
    ],
    "concepts": [],
    "theory": []
   }
  },
  "exam03": {
   "id": "exam03",
   "lo": 10,
   "hi": 13,
   "refreshItems": {
    "keywords": [
     "float",
     "str",
     "True",
     "False",
     "not",
     "x: int = 5",
     "if",
     "def",
     "return",
     "->",
     "list",
     "dict",
     "with",
     "as",
     "class",
     "self",
     "@property",
     "class Child(Parent)",
     "df.groupby()",
     "df.sort_values()",
     "df.merge()",
     "cv2.cvtColor",
     "requests.get()",
     "response.json()",
     "threading.Thread",
     "threading.Lock",
     "FastAPI()",
     "@app.get",
     "Depends"
    ],
    "dunders": [
     "__init__"
    ],
    "modules": [
     "json",
     "pandas",
     "numpy",
     "threading",
     "fastapi",
     "pydantic"
    ],
    "methods": [
     "df.pivot_table()",
     "cv2.findContours()",
     "cv2.GaussianBlur()",
     "response.raise_for_status()",
     "concurrent.futures.ThreadPoolExecutor"
    ],
    "concepts": [],
    "theory": []
   }
  }
 }
};
