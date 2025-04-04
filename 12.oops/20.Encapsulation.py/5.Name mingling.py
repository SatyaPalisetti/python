############# Name Mingling #######
'''In Python, private variables are typically declared by prefixing them with an underscore (e.g., _variable), or more conventionally with two underscores (e.g., __variable). However, Python does not enforce strict access restrictions like some other languages (such as Java or C++). Instead, it relies on name mangling to "protect" variables with double underscores.

Here are a few methods you can use to access private variables outside the class:

1. Using Name Mangling (For Double Underscore Variables)
Python "mangles" the names of private variables by internally renaming them to include the class name. This makes it harder (but not impossible) to access them from outside.
'''
