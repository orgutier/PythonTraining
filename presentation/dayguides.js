// Day-by-day deep-dive documentation, opened by clicking a Basic/Mid/Advanced
// row in a topic's Week schedule table. Every example below was executed for
// real (see scripts used to generate this file) -- the shown output is not
// hand-typed.

const DAY_GUIDES = {
  "week01-basic": {
    week: 1,
    tierLabel: "Basic tier",
    title: "Week 1 \u2014 Basic tier: variables, types, casting",
    summary: "Get comfortable naming values, telling the five core types apart, and converting between them explicitly.",
    examples: [
      {
        caption: "Variables, types, and casting",
        code: "age = 30\nname = \"Ada\"\nheight = 1.75\nprint(type(age), type(name), type(height))\nprint(f\"{name} is {age} years old and {height}m tall\")\nprint(int(\"42\") + 8)",
        output: "<class 'int'> <class 'str'> <class 'float'>\nAda is 30 years old and 1.75m tall\n50"
      },
      {
        caption: "Comparison operators return bool",
        code: "x = 7\nprint(x == 7, x != 7, x > 10)\nprint(isinstance(x, int))",
        output: "True False False\nTrue"
      },
    ]
  },
  "week01-mid": {
    week: 1,
    tierLabel: "Mid tier",
    title: "Week 1 \u2014 Mid tier: f-strings, walrus, float caveats",
    summary: "Write more compact, idiomatic expressions -- and see the float-imprecision trap firsthand.",
    examples: [
      {
        caption: "f-strings and the walrus operator",
        code: "values = [1, 2, 3, 4, 5]\nif (n := len(values)) > 3:\n    print(f\"list has {n} items, that's more than 3\")",
        output: "list has 5 items, that's more than 3"
      },
      {
        caption: "// vs / and float imprecision",
        code: "print(7 / 2, 7 // 2)\nprint(0.1 + 0.2)\nprint(0.1 + 0.2 == 0.3)",
        output: "3.5 3\n0.30000000000000004\nFalse"
      },
    ]
  },
  "week01-advanced": {
    week: 1,
    tierLabel: "Advanced tier & internals",
    title: "Week 1 \u2014 Advanced tier: big ints, safe float comparison",
    summary: "See arbitrary-precision integers in action, and the correct way to compare floats.",
    examples: [
      {
        caption: "Arbitrary-precision integers",
        code: "big = 2 ** 100\nprint(big)\nprint(type(big))",
        output: "1267650600228229401496703205376\n<class 'int'>"
      },
      {
        caption: "Comparing floats safely",
        code: "import math\na = 0.1 + 0.2\nb = 0.3\nprint(a == b)\nprint(math.isclose(a, b))",
        output: "False\nTrue"
      },
    ]
  },
  "week02-basic": {
    week: 2,
    tierLabel: "Basic tier",
    title: "Week 2 \u2014 Basic tier: loops, break/continue",
    summary: "Practice the core loop constructs and controlling their flow with break/continue.",
    examples: [
      {
        caption: "for + range() with break/continue",
        code: "for i in range(6):\n    if i == 4:\n        break\n    if i % 2 == 0:\n        continue\n    print(i)",
        output: "1\n3"
      },
      {
        caption: "A simple while loop",
        code: "n = 3\nwhile n > 0:\n    print(n)\n    n -= 1\nprint(\"done\")",
        output: "3\n2\n1\ndone"
      },
    ]
  },
  "week02-mid": {
    week: 2,
    tierLabel: "Mid tier",
    title: "Week 2 \u2014 Mid tier: for...else, zip()",
    summary: "Two idioms that come up constantly: the loop else clause, and iterating several sequences in lockstep.",
    examples: [
      {
        caption: "for...else for a search",
        code: "items = [3, 7, 9]\ntarget = 5\nfor x in items:\n    if x == target:\n        print(\"found it\")\n        break\nelse:\n    print(\"not found\")",
        output: "not found"
      },
      {
        caption: "zip() for parallel iteration",
        code: "names = [\"Ada\", \"Grace\"]\nscores = [95, 88]\nfor name, score in zip(names, scores):\n    print(f\"{name}: {score}\")",
        output: "Ada: 95\nGrace: 88"
      },
    ]
  },
  "week02-advanced": {
    week: 2,
    tierLabel: "Advanced tier & internals",
    title: "Week 2 \u2014 Advanced tier: custom iterators, itertools",
    summary: "See the exact iterator protocol that every for loop relies on, plus a itertools building block.",
    examples: [
      {
        caption: "A minimal custom iterator",
        code: "class Countdown:\n    def __init__(self, start):\n        self.n = start\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.n <= 0:\n            raise StopIteration\n        self.n -= 1\n        return self.n + 1\n\nfor x in Countdown(3):\n    print(x)",
        output: "3\n2\n1"
      },
      {
        caption: "itertools.chain for combining iterables",
        code: "import itertools\na = [1, 2]\nb = [3, 4]\nprint(list(itertools.chain(a, b)))",
        output: "[1, 2, 3, 4]"
      },
    ]
  },
  "week03-basic": {
    week: 3,
    tierLabel: "Basic tier",
    title: "Week 3 \u2014 Basic tier: args, kwargs, recursion",
    summary: "Write functions that accept a flexible number of arguments, and your first recursive function.",
    examples: [
      {
        caption: "*args, **kwargs, and default args",
        code: "def total(*args, tax=0.0, **kwargs):\n    subtotal = sum(args)\n    print(\"extras:\", kwargs)\n    return subtotal * (1 + tax)\n\nprint(total(10, 20, tax=0.1, note=\"sale\"))",
        output: "extras: {'note': 'sale'}\n33.0"
      },
      {
        caption: "Recursion with a base case",
        code: "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))",
        output: "120"
      },
    ]
  },
  "week03-mid": {
    week: 3,
    tierLabel: "Mid tier",
    title: "Week 3 \u2014 Mid tier: keyword-only params, closures",
    summary: "Lock down a function's call signature, and see a closure remember state between calls.",
    examples: [
      {
        caption: "Keyword-only parameters",
        code: "def connect(host, *, timeout=5):\n    print(f\"connecting to {host} with timeout={timeout}\")\n\nconnect(\"example.com\", timeout=10)",
        output: "connecting to example.com with timeout=10"
      },
      {
        caption: "A closure that remembers state",
        code: "def make_counter():\n    count = 0\n    def increment():\n        nonlocal count\n        count += 1\n        return count\n    return increment\n\ncounter = make_counter()\nprint(counter(), counter(), counter())",
        output: "1 2 3"
      },
    ]
  },
  "week03-advanced": {
    week: 3,
    tierLabel: "Advanced tier & internals",
    title: "Week 3 \u2014 Advanced tier: lru_cache, generators",
    summary: "Memoize a recursive function in one line, and write a lazy generator instead of building a whole list.",
    examples: [
      {
        caption: "functools.lru_cache speeding up recursion",
        code: "import functools\n\n@functools.lru_cache\ndef fib(n):\n    return n if n < 2 else fib(n - 1) + fib(n - 2)\n\nprint([fib(n) for n in range(10)])",
        output: "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"
      },
      {
        caption: "A generator function",
        code: "def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nprint(list(countdown(4)))",
        output: "[4, 3, 2, 1]"
      },
    ]
  },
  "week04-basic": {
    week: 4,
    tierLabel: "Basic tier",
    title: "Week 4 \u2014 Basic tier: comprehensions, core methods",
    summary: "Build collections with comprehensions instead of append-loops, and use the everyday list/set methods.",
    examples: [
      {
        caption: "List and dict comprehensions",
        code: "squares = [x * x for x in range(6)]\nevens_only = {x: x * x for x in range(6) if x % 2 == 0}\nprint(squares)\nprint(evens_only)",
        output: "[0, 1, 4, 9, 16, 25]\n{0: 0, 2: 4, 4: 16}"
      },
      {
        caption: "Common list/set methods",
        code: "nums = [3, 1, 4, 1, 5]\nnums.append(9)\nprint(sorted(nums))\nprint(set(nums))",
        output: "[1, 1, 3, 4, 5, 9]\n{1, 3, 4, 5, 9}"
      },
    ]
  },
  "week04-mid": {
    week: 4,
    tierLabel: "Mid tier",
    title: "Week 4 \u2014 Mid tier: sorting with key=, set algebra",
    summary: "Sort structured data by a specific field, and compare two collections with set operators.",
    examples: [
      {
        caption: "Sorting with key=",
        code: "people = [(\"Ada\", 36), (\"Grace\", 85), (\"Alan\", 41)]\nby_age = sorted(people, key=lambda p: p[1])\nprint(by_age)",
        output: "[('Ada', 36), ('Alan', 41), ('Grace', 85)]"
      },
      {
        caption: "Set algebra",
        code: "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(a & b, a | b, a - b)",
        output: "{3, 4} {1, 2, 3, 4, 5, 6} {1, 2}"
      },
    ]
  },
  "week04-advanced": {
    week: 4,
    tierLabel: "Advanced tier & internals",
    title: "Week 4 \u2014 Advanced tier: defaultdict, Counter",
    summary: "Two collections-module tools that replace a lot of manual dict bookkeeping.",
    examples: [
      {
        caption: "collections.defaultdict for grouping",
        code: "from collections import defaultdict\n\nwords = [\"bat\", \"cat\", \"ant\", \"car\"]\nby_letter = defaultdict(list)\nfor w in words:\n    by_letter[w[0]].append(w)\nprint(dict(by_letter))",
        output: "{'b': ['bat'], 'c': ['cat', 'car'], 'a': ['ant']}"
      },
      {
        caption: "collections.Counter for frequencies",
        code: "from collections import Counter\n\nvotes = [\"red\", \"blue\", \"red\", \"green\", \"red\", \"blue\"]\ntally = Counter(votes)\nprint(tally)\nprint(tally.most_common(1))",
        output: "Counter({'red': 3, 'blue': 2, 'green': 1})\n[('red', 3)]"
      },
    ]
  },
  "week05-basic": {
    week: 5,
    tierLabel: "Basic tier",
    title: "Week 5 \u2014 Basic tier: try/except, basic regex",
    summary: "Handle a failure without crashing, and pull data out of text with a regex.",
    examples: [
      {
        caption: "try/except/finally",
        code: "def safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\n    finally:\n        print(\"divide attempted\")\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))",
        output: "divide attempted\n5.0\ndivide attempted\nNone"
      },
      {
        caption: "Basic regex search and findall",
        code: "import re\ntext = \"Call 555-1234 or 555-9876\"\nprint(re.search(r\"\\d{3}-\\d{4}\", text).group())\nprint(re.findall(r\"\\d{3}-\\d{4}\", text))",
        output: "555-1234\n['555-1234', '555-9876']"
      },
    ]
  },
  "week05-mid": {
    week: 5,
    tierLabel: "Mid tier",
    title: "Week 5 \u2014 Mid tier: exception chaining, named groups",
    summary: "Preserve the original cause when translating an exception, and name your regex captures.",
    examples: [
      {
        caption: "Exception chaining with raise ... from ...",
        code: "def parse_age(s):\n    try:\n        return int(s)\n    except ValueError as e:\n        raise RuntimeError(f\"invalid age: {s!r}\") from e\n\ntry:\n    parse_age(\"thirty\")\nexcept RuntimeError as e:\n    print(e)\n    print(type(e.__cause__))",
        output: "invalid age: 'thirty'\n<class 'ValueError'>"
      },
      {
        caption: "Named regex groups",
        code: "import re\nm = re.search(r\"(?P<year>\\d{4})-(?P<month>\\d{2})\", \"2024-05\")\nprint(m.group(\"year\"), m.group(\"month\"))",
        output: "2024 05"
      },
    ]
  },
  "week05-advanced": {
    week: 5,
    tierLabel: "Advanced tier & internals",
    title: "Week 5 \u2014 Advanced tier: custom context managers",
    summary: "Build a context manager without a class, and a small exception hierarchy of your own.",
    examples: [
      {
        caption: "A context manager with @contextmanager",
        code: "from contextlib import contextmanager\n\n@contextmanager\ndef timer_block(label):\n    print(f\"start: {label}\")\n    yield\n    print(f\"end: {label}\")\n\nwith timer_block(\"demo\"):\n    print(\"doing work\")",
        output: "start: demo\ndoing work\nend: demo"
      },
      {
        caption: "A custom exception hierarchy",
        code: "class AppError(Exception):\n    pass\n\nclass NotFoundError(AppError):\n    pass\n\ntry:\n    raise NotFoundError(\"user 42 missing\")\nexcept AppError as e:\n    print(f\"caught: {e}\")",
        output: "caught: user 42 missing"
      },
    ]
  },
  "week06-basic": {
    week: 6,
    tierLabel: "Basic tier",
    title: "Week 6 \u2014 Basic tier: classes, @property",
    summary: "Write your first class, then expose a computed value with @property instead of a plain method call.",
    examples: [
      {
        caption: "A class with __init__ and a method",
        code: "class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        return f\"{self.name} says woof\"\n\nd = Dog(\"Rex\")\nprint(d.bark())",
        output: "Rex says woof"
      },
      {
        caption: "@property for a computed attribute",
        code: "class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n    @property\n    def area(self):\n        return 3.14159 * self.radius ** 2\n\nc = Circle(2)\nprint(c.area)",
        output: "12.56636"
      },
    ]
  },
  "week06-mid": {
    week: 6,
    tierLabel: "Mid tier",
    title: "Week 6 \u2014 Mid tier: __slots__, @classmethod",
    summary: "Lock a class down to fixed attributes, and build an alternative constructor.",
    examples: [
      {
        caption: "__slots__ for memory savings",
        code: "class Point:\n    __slots__ = (\"x\", \"y\")\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n\np = Point(1, 2)\nprint(p.x, p.y)\ntry:\n    p.z = 3\nexcept AttributeError as e:\n    print(\"blocked:\", e)",
        output: "1 2\nblocked: 'Point' object has no attribute 'z'"
      },
      {
        caption: "@classmethod as an alternative constructor",
        code: "class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    @classmethod\n    def origin(cls):\n        return cls(0, 0)\n    def __repr__(self):\n        return f\"Point({self.x}, {self.y})\"\n\nprint(Point.origin())",
        output: "Point(0, 0)"
      },
    ]
  },
  "week06-advanced": {
    week: 6,
    tierLabel: "Advanced tier & internals",
    title: "Week 6 \u2014 Advanced tier: descriptors, __init_subclass__",
    summary: "Build the same mechanism @property is made of, and a hook that fires on every subclass.",
    examples: [
      {
        caption: "A simple descriptor",
        code: "class PositiveNumber:\n    def __set_name__(self, owner, name):\n        self.name = \"_\" + name\n    def __get__(self, obj, objtype=None):\n        return getattr(obj, self.name)\n    def __set__(self, obj, value):\n        if value < 0:\n            raise ValueError(\"must be positive\")\n        setattr(obj, self.name, value)\n\nclass Account:\n    balance = PositiveNumber()\n    def __init__(self, balance):\n        self.balance = balance\n\na = Account(100)\nprint(a.balance)",
        output: "100"
      },
      {
        caption: "__init_subclass__ hook",
        code: "class Plugin:\n    registry = []\n    def __init_subclass__(cls, **kwargs):\n        super().__init_subclass__(**kwargs)\n        Plugin.registry.append(cls.__name__)\n\nclass Alpha(Plugin): pass\nclass Beta(Plugin): pass\n\nprint(Plugin.registry)",
        output: "['Alpha', 'Beta']"
      },
    ]
  },
  "week07-basic": {
    week: 7,
    tierLabel: "Basic tier",
    title: "Week 7 \u2014 Basic tier: inheritance, duck typing",
    summary: "Override a parent method, and see Python check behavior instead of type.",
    examples: [
      {
        caption: "Inheritance and super()",
        code: "class Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return \"...\"\n\nclass Dog(Animal):\n    def speak(self):\n        return f\"{self.name} says Woof\"\n\nprint(Dog(\"Rex\").speak())",
        output: "Rex says Woof"
      },
      {
        caption: "Duck typing",
        code: "class Duck:\n    def quack(self):\n        return \"Quack!\"\n\nclass Person:\n    def quack(self):\n        return \"I'm quacking!\"\n\nfor thing in [Duck(), Person()]:\n    print(thing.quack())",
        output: "Quack!\nI'm quacking!"
      },
    ]
  },
  "week07-mid": {
    week: 7,
    tierLabel: "Mid tier",
    title: "Week 7 \u2014 Mid tier: ABCs, composition",
    summary: "Force subclasses to implement a method, and prefer composition over inheritance.",
    examples: [
      {
        caption: "abc.ABC + @abstractmethod",
        code: "from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): ...\n\nclass Square(Shape):\n    def __init__(self, side):\n        self.side = side\n    def area(self):\n        return self.side ** 2\n\nprint(Square(4).area())\ntry:\n    Shape()\nexcept TypeError as e:\n    print(\"blocked:\", e)",
        output: "16\nblocked: Can't instantiate abstract class Shape with abstract method area"
      },
      {
        caption: "Composition instead of inheritance",
        code: "class Engine:\n    def start(self):\n        return \"engine running\"\n\nclass Car:\n    def __init__(self):\n        self.engine = Engine()\n    def start(self):\n        return self.engine.start()\n\nprint(Car().start())",
        output: "engine running"
      },
    ]
  },
  "week07-advanced": {
    week: 7,
    tierLabel: "Advanced tier & internals",
    title: "Week 7 \u2014 Advanced tier: MRO, Protocol",
    summary: "See the actual method resolution order for diamond inheritance, and structural typing with Protocol.",
    examples: [
      {
        caption: "Method Resolution Order with multiple inheritance",
        code: "class A:\n    def who(self): return \"A\"\nclass B(A):\n    def who(self): return \"B\"\nclass C(A):\n    def who(self): return \"C\"\nclass D(B, C):\n    pass\n\nprint(D().who())\nprint([c.__name__ for c in D.__mro__])",
        output: "B\n['D', 'B', 'C', 'A', 'object']"
      },
      {
        caption: "typing.Protocol for structural typing",
        code: "from typing import Protocol\n\nclass Readable(Protocol):\n    def read(self) -> str: ...\n\nclass File:\n    def read(self) -> str:\n        return \"file contents\"\n\ndef show(source: Readable):\n    print(source.read())\n\nshow(File())",
        output: "file contents"
      },
    ]
  },
  "week08-basic": {
    week: 8,
    tierLabel: "Basic tier",
    title: "Week 8 \u2014 Basic tier: __repr__, __str__, __eq__",
    summary: "Give your objects a real debug representation and value-based equality.",
    examples: [
      {
        caption: "__repr__ vs __str__",
        code: "class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __repr__(self):\n        return f\"Point(x={self.x}, y={self.y})\"\n    def __str__(self):\n        return f\"({self.x}, {self.y})\"\n\np = Point(1, 2)\nprint(repr(p))\nprint(str(p))",
        output: "Point(x=1, y=2)\n(1, 2)"
      },
      {
        caption: "__eq__ for value equality",
        code: "class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __eq__(self, other):\n        return (self.x, self.y) == (other.x, other.y)\n\nprint(Point(1, 2) == Point(1, 2))",
        output: "True"
      },
    ]
  },
  "week08-mid": {
    week: 8,
    tierLabel: "Mid tier",
    title: "Week 8 \u2014 Mid tier: __len__/__getitem__, __call__",
    summary: "Make an object work with len()/indexing/for loops, and make an instance callable like a function.",
    examples: [
      {
        caption: "__len__, __getitem__, __iter__ (for-loop for free)",
        code: "class Deck:\n    def __init__(self, cards):\n        self.cards = cards\n    def __len__(self):\n        return len(self.cards)\n    def __getitem__(self, i):\n        return self.cards[i]\n\nd = Deck([\"A\", \"K\", \"Q\"])\nprint(len(d), d[0])\nfor card in d:\n    print(card)",
        output: "3 A\nA\nK\nQ"
      },
      {
        caption: "__call__ makes an instance callable",
        code: "class Multiplier:\n    def __init__(self, factor):\n        self.factor = factor\n    def __call__(self, x):\n        return x * self.factor\n\ndouble = Multiplier(2)\nprint(double(21))",
        output: "42"
      },
    ]
  },
  "week08-advanced": {
    week: 8,
    tierLabel: "Advanced tier & internals",
    title: "Week 8 \u2014 Advanced tier: operator overloading, context managers",
    summary: "Implement + correctly with NotImplemented, and a class-based context manager.",
    examples: [
      {
        caption: "__add__ and __radd__ with NotImplemented",
        code: "class Money:\n    def __init__(self, amount):\n        self.amount = amount\n    def __add__(self, other):\n        if isinstance(other, Money):\n            return Money(self.amount + other.amount)\n        return NotImplemented\n    def __radd__(self, other):\n        return self.__add__(other)\n    def __repr__(self):\n        return f\"Money({self.amount})\"\n\nprint(Money(5) + Money(3))\nprint(sum([Money(1), Money(2), Money(3)], Money(0)))",
        output: "Money(8)\nMoney(6)"
      },
      {
        caption: "__enter__/__exit__ as a context manager",
        code: "class Transaction:\n    def __enter__(self):\n        print(\"BEGIN\")\n        return self\n    def __exit__(self, exc_type, exc, tb):\n        print(\"ROLLBACK\" if exc_type else \"COMMIT\")\n        return False\n\nwith Transaction():\n    print(\"doing work\")",
        output: "BEGIN\ndoing work\nCOMMIT"
      },
    ]
  },
  "week09-basic": {
    week: 9,
    tierLabel: "Basic tier",
    title: "Week 9 \u2014 Basic tier: json round-trip, datetime basics",
    summary: "Serialize and reload Python data as JSON, and format a datetime for display.",
    examples: [
      {
        caption: "json.dumps/loads round-trip",
        code: "import json\ndata = {\"name\": \"Ada\", \"age\": 36}\ntext = json.dumps(data)\nprint(text)\nprint(json.loads(text))",
        output: "{\"name\": \"Ada\", \"age\": 36}\n{'name': 'Ada', 'age': 36}"
      },
      {
        caption: "datetime.now() and isoformat()",
        code: "from datetime import datetime\nnow = datetime(2024, 5, 17, 9, 30)\nprint(now.isoformat())\nprint(now.strftime(\"%A, %B %d %Y\"))",
        output: "2024-05-17T09:30:00\nFriday, May 17 2024"
      },
    ]
  },
  "week09-mid": {
    week: 9,
    tierLabel: "Mid tier",
    title: "Week 9 \u2014 Mid tier: pathlib, ElementTree",
    summary: "Build paths the modern way, and parse a small XML document.",
    examples: [
      {
        caption: "pathlib for path building",
        code: "from pathlib import Path\np = Path(\"data\") / \"reports\" / \"2024.csv\"\nprint(p)\nprint(p.suffix, p.stem)",
        output: "data/reports/2024.csv\n.csv 2024"
      },
      {
        caption: "ElementTree parsing and searching",
        code: "import xml.etree.ElementTree as ET\nxml_text = \"<items><item>Pen</item><item>Cup</item></items>\"\nroot = ET.fromstring(xml_text)\nfor item in root.findall(\"item\"):\n    print(item.text)",
        output: "Pen\nCup"
      },
    ]
  },
  "week09-advanced": {
    week: 9,
    tierLabel: "Advanced tier & internals",
    title: "Week 9 \u2014 Advanced tier: JSON default=, timedelta math",
    summary: "Serialize a non-JSON-native type, and do real calendar arithmetic.",
    examples: [
      {
        caption: "json.dumps with a default= hook",
        code: "import json\nfrom datetime import date\n\ndef default(o):\n    if isinstance(o, date):\n        return o.isoformat()\n    raise TypeError(f\"not serializable: {o!r}\")\n\nprint(json.dumps({\"created\": date(2024, 5, 17)}, default=default))",
        output: "{\"created\": \"2024-05-17\"}"
      },
      {
        caption: "datetime arithmetic with timedelta",
        code: "from datetime import datetime, timedelta\nstart = datetime(2024, 1, 1)\nend = start + timedelta(days=45)\nprint(end.date())\nprint((end - start).days)",
        output: "2024-02-15\n45"
      },
    ]
  },
  "week10-basic": {
    week: 10,
    tierLabel: "Basic tier",
    title: "Week 10 \u2014 Basic tier: DataFrame basics, read_csv",
    summary: "Build a DataFrame directly and from CSV text, then take the standard first look at it.",
    examples: [
      {
        caption: "Build a DataFrame and inspect it",
        code: "import pandas as pd\ndf = pd.DataFrame({\"name\": [\"Ada\", \"Grace\"], \"score\": [95, 88]})\nprint(df.head())\nprint(df[\"score\"].mean())",
        output: "    name  score\n0    Ada     95\n1  Grace     88\n91.5"
      },
      {
        caption: "Read a small CSV",
        code: "import pandas as pd\nfrom io import StringIO\ncsv_text = \"name,score\\nAda,95\\nGrace,88\\n\"\ndf = pd.read_csv(StringIO(csv_text))\nprint(df)",
        output: "    name  score\n0    Ada     95\n1  Grace     88"
      },
    ]
  },
  "week10-mid": {
    week: 10,
    tierLabel: "Mid tier",
    title: "Week 10 \u2014 Mid tier: boolean indexing, groupby",
    summary: "Filter rows with a boolean mask, and aggregate by group.",
    examples: [
      {
        caption: "Boolean indexing",
        code: "import pandas as pd\ndf = pd.DataFrame({\"name\": [\"Ada\", \"Grace\", \"Alan\"], \"score\": [95, 88, 60]})\npassing = df[df[\"score\"] >= 70]\nprint(passing)",
        output: "    name  score\n0    Ada     95\n1  Grace     88"
      },
      {
        caption: "groupby + aggregation",
        code: "import pandas as pd\ndf = pd.DataFrame({\"team\": [\"A\", \"B\", \"A\", \"B\"], \"points\": [10, 20, 30, 5]})\nprint(df.groupby(\"team\")[\"points\"].sum())",
        output: "team\nA    40\nB    25\nName: points, dtype: int64"
      },
    ]
  },
  "week10-advanced": {
    week: 10,
    tierLabel: "Advanced tier & internals",
    title: "Week 10 \u2014 Advanced tier: vectorization, pivot_table",
    summary: "Compare a vectorized column operation to .apply(), and build a two-dimensional summary.",
    examples: [
      {
        caption: "Vectorized operations vs .apply()",
        code: "import pandas as pd\ndf = pd.DataFrame({\"price\": [10, 20, 30]})\ndf[\"with_tax_vectorized\"] = df[\"price\"] * 1.1\ndf[\"with_tax_apply\"] = df[\"price\"].apply(lambda p: p * 1.1)\nprint(df)",
        output: "   price  with_tax_vectorized  with_tax_apply\n0     10                 11.0            11.0\n1     20                 22.0            22.0\n2     30                 33.0            33.0"
      },
      {
        caption: "pivot_table summarizing two dimensions",
        code: "import pandas as pd\ndf = pd.DataFrame({\n    \"region\": [\"East\", \"East\", \"West\", \"West\"],\n    \"month\": [\"Jan\", \"Feb\", \"Jan\", \"Feb\"],\n    \"sales\": [100, 150, 200, 130],\n})\nprint(df.pivot_table(values=\"sales\", index=\"region\", columns=\"month\"))",
        output: "month     Feb    Jan\nregion              \nEast    150.0  100.0\nWest    130.0  200.0"
      },
    ]
  },
  "week11-basic": {
    week: 11,
    tierLabel: "Basic tier",
    title: "Week 11 \u2014 Basic tier: images as arrays, drawing",
    summary: "See that an image is just a NumPy array, and draw directly onto one.",
    examples: [
      {
        caption: "A synthetic image as a NumPy array",
        code: "import numpy as np\nimg = np.zeros((4, 4, 3), dtype=np.uint8)\nimg[:] = (0, 0, 255)  # BGR: pure red\nprint(img.shape)\nprint(img[0, 0])",
        output: "(4, 4, 3)\n[  0   0 255]"
      },
      {
        caption: "Drawing a rectangle",
        code: "import numpy as np\nimport cv2\nimg = np.zeros((5, 5, 3), dtype=np.uint8)\ncv2.rectangle(img, (1, 1), (3, 3), (0, 255, 0), 1)\nprint(img[:, :, 1])  # green channel shows the rectangle outline",
        output: "[[  0   0   0   0   0]\n [  0 255 255 255   0]\n [  0 255   0 255   0]\n [  0 255 255 255   0]\n [  0   0   0   0   0]]"
      },
    ]
  },
  "week11-mid": {
    week: 11,
    tierLabel: "Mid tier",
    title: "Week 11 \u2014 Mid tier: color conversion, cropping",
    summary: "Convert BGR to grayscale, and crop an image with plain array slicing.",
    examples: [
      {
        caption: "Color conversion BGR -> grayscale",
        code: "import numpy as np\nimport cv2\nimg = np.full((2, 2, 3), (10, 20, 30), dtype=np.uint8)\ngray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\nprint(gray)",
        output: "[[22 22]\n [22 22]]"
      },
      {
        caption: "Cropping via array slicing",
        code: "import numpy as np\nimg = np.arange(25).reshape(5, 5).astype(np.uint8)\ncropped = img[1:3, 1:3]\nprint(cropped)",
        output: "[[ 6  7]\n [11 12]]"
      },
    ]
  },
  "week11-advanced": {
    week: 11,
    tierLabel: "Advanced tier & internals",
    title: "Week 11 \u2014 Advanced tier: thresholding, blurring",
    summary: "Convert an image to pure black/white, and smooth it with a convolution.",
    examples: [
      {
        caption: "Thresholding an image",
        code: "import numpy as np\nimport cv2\ngray = np.array([[10, 200], [50, 180]], dtype=np.uint8)\n_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)\nprint(binary)",
        output: "[[  0 255]\n [  0 255]]"
      },
      {
        caption: "Gaussian blur smoothing",
        code: "import numpy as np\nimport cv2\nimg = np.array([[0, 0, 0], [0, 255, 0], [0, 0, 0]], dtype=np.uint8)\nblurred = cv2.GaussianBlur(img, (3, 3), 0)\nprint(blurred)",
        output: "[[64 64 64]\n [64 64 64]\n [64 64 64]]"
      },
    ]
  },
  "week12-basic": {
    week: 12,
    tierLabel: "Basic tier",
    title: "Week 12 \u2014 Basic tier: threads, mocked requests",
    summary: "Start and join several threads, and mock requests.get the same way the graded tests do.",
    examples: [
      {
        caption: "threading.Thread create/start/join",
        code: "import threading\n\ndef worker(n):\n    print(f\"worker {n} running\")\n\nthreads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]\nfor t in threads: t.start()\nfor t in threads: t.join()\nprint(\"all done\")",
        output: "worker 0 running\nworker 1 running\nworker 2 running\nall done"
      },
      {
        caption: "Mocking requests.get (never hit a live endpoint in class)",
        code: "from unittest.mock import patch, Mock\n\nwith patch(\"requests.get\") as mock_get:\n    mock_get.return_value = Mock(status_code=200, json=lambda: {\"id\": 1, \"name\": \"Ada\"})\n    import requests\n    response = requests.get(\"https://api.example.com/users/1\")\n    print(response.status_code, response.json())",
        output: "200 {'id': 1, 'name': 'Ada'}"
      },
    ]
  },
  "week12-mid": {
    week: 12,
    tierLabel: "Mid tier",
    title: "Week 12 \u2014 Mid tier: Lock, raise_for_status",
    summary: "Protect shared state from a race, and handle a failing HTTP response properly.",
    examples: [
      {
        caption: "threading.Lock protecting shared state",
        code: "import threading\n\ncounter = 0\nlock = threading.Lock()\n\ndef increment():\n    global counter\n    for _ in range(1000):\n        with lock:\n            counter += 1\n\nthreads = [threading.Thread(target=increment) for _ in range(4)]\nfor t in threads: t.start()\nfor t in threads: t.join()\nprint(counter)",
        output: "4000"
      },
      {
        caption: "raise_for_status on a mocked failing response",
        code: "from unittest.mock import Mock\nimport requests\n\nresponse = Mock(spec=requests.Response)\nresponse.raise_for_status.side_effect = requests.HTTPError(\"404 Client Error\")\ntry:\n    response.raise_for_status()\nexcept requests.HTTPError as e:\n    print(\"caught:\", e)",
        output: "caught: 404 Client Error"
      },
    ]
  },
  "week12-advanced": {
    week: 12,
    tierLabel: "Advanced tier & internals",
    title: "Week 12 \u2014 Advanced tier: ThreadPoolExecutor, session reuse",
    summary: "Run tasks through a thread pool instead of raw Threads, and reuse one session across calls.",
    examples: [
      {
        caption: "ThreadPoolExecutor running tasks concurrently",
        code: "from concurrent.futures import ThreadPoolExecutor\n\ndef square(n):\n    return n * n\n\nwith ThreadPoolExecutor(max_workers=4) as ex:\n    results = list(ex.map(square, range(6)))\nprint(results)",
        output: "[0, 1, 4, 9, 16, 25]"
      },
      {
        caption: "A reused session making multiple calls",
        code: "from unittest.mock import Mock\n\nclass FakeSession:\n    def __init__(self):\n        self.calls = 0\n    def get(self, url):\n        self.calls += 1\n        return Mock(status_code=200)\n\nsession = FakeSession()\nfor _ in range(3):\n    session.get(\"https://api.example.com/data\")\nprint(f\"made {session.calls} calls on one reused session\")",
        output: "made 3 calls on one reused session"
      },
    ]
  },
  "week13-basic": {
    week: 13,
    tierLabel: "Basic tier",
    title: "Week 13 \u2014 Basic tier: a route, query parameters",
    summary: "Stand up a minimal FastAPI route and call it in-process with TestClient.",
    examples: [
      {
        caption: "A minimal FastAPI route with TestClient",
        code: "from fastapi import FastAPI\nfrom fastapi.testclient import TestClient\n\napp = FastAPI()\n\n@app.get(\"/hello/{name}\")\ndef hello(name: str):\n    return {\"message\": f\"Hello, {name}!\"}\n\nclient = TestClient(app)\nresponse = client.get(\"/hello/Ada\")\nprint(response.status_code, response.json())",
        output: "200 {'message': 'Hello, Ada!'}"
      },
      {
        caption: "Query parameters",
        code: "from fastapi import FastAPI\nfrom fastapi.testclient import TestClient\n\napp = FastAPI()\n\n@app.get(\"/add\")\ndef add(a: int, b: int):\n    return {\"result\": a + b}\n\nclient = TestClient(app)\nresponse = client.get(\"/add\", params={\"a\": 3, \"b\": 4})\nprint(response.json())",
        output: "{'result': 7}"
      },
    ]
  },
  "week13-mid": {
    week: 13,
    tierLabel: "Mid tier",
    title: "Week 13 \u2014 Mid tier: Pydantic validation, Depends()",
    summary: "Validate a request body with a Pydantic model, and share logic across routes with Depends.",
    examples: [
      {
        caption: "Pydantic model validation",
        code: "from fastapi import FastAPI\nfrom fastapi.testclient import TestClient\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass Item(BaseModel):\n    name: str\n    price: float\n\n@app.post(\"/items\")\ndef create_item(item: Item):\n    return item\n\nclient = TestClient(app)\nprint(client.post(\"/items\", json={\"name\": \"Pen\", \"price\": 1.5}).json())\nprint(client.post(\"/items\", json={\"name\": \"Pen\"}).status_code)",
        output: "{'name': 'Pen', 'price': 1.5}\n422"
      },
      {
        caption: "Depends() for shared logic",
        code: "from fastapi import FastAPI, Depends\nfrom fastapi.testclient import TestClient\n\napp = FastAPI()\n\ndef get_greeting():\n    return \"Hi\"\n\n@app.get(\"/greet/{name}\")\ndef greet(name: str, greeting: str = Depends(get_greeting)):\n    return {\"message\": f\"{greeting}, {name}!\"}\n\nclient = TestClient(app)\nprint(client.get(\"/greet/Ada\").json())",
        output: "{'message': 'Hi, Ada!'}"
      },
    ]
  },
  "week13-advanced": {
    week: 13,
    tierLabel: "Advanced tier & internals",
    title: "Week 13 \u2014 Advanced tier: async routes, 404 handling",
    summary: "Write an async def endpoint, and confirm an unknown route returns a real 404.",
    examples: [
      {
        caption: "async def endpoint",
        code: "from fastapi import FastAPI\nfrom fastapi.testclient import TestClient\n\napp = FastAPI()\n\n@app.get(\"/ping\")\nasync def ping():\n    return {\"pong\": True}\n\nclient = TestClient(app)\nprint(client.get(\"/ping\").json())",
        output: "{'pong': True}"
      },
      {
        caption: "TestClient checking a 404 for an unknown route",
        code: "from fastapi import FastAPI\nfrom fastapi.testclient import TestClient\n\napp = FastAPI()\n\n@app.get(\"/exists\")\ndef exists():\n    return {\"ok\": True}\n\nclient = TestClient(app)\nresponse = client.get(\"/does-not-exist\")\nprint(response.status_code)",
        output: "404"
      },
    ]
  },
};
