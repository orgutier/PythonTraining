# Hello, World! (Environment Check)

The very first program you'll run in this course. It exists purely to prove your Python install, virtual environment, and this repo's test runner (`python tools/cli.py test stage01_hello_world`) all actually work, before we get into any real content.

Write two lines of code, in order, right in `solution.py` (no function -- just plain statements):

1. Assign a variable `greeting` set to exactly `"Hello, World!"`, then `print(greeting)`.
2. Assign a variable `author_name` to your own name as a non-empty string (e.g. `"Ada"`), then print a second line built with string **concatenation** (not an f-string -- those aren't introduced until the Mid tier): `print("This is " + author_name + "'s first Python program.")`.

That's it. If `python tools/cli.py test stage01_hello_world` passes, your setup is good and you're ready for the Basic tier.
