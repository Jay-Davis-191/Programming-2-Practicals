"""CP1404 Practical - User to use the ProgrammingLanguage class"""

from programming_language import ProgrammingLanguage
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print("\nThe dynamically typed languages are: ")
ruby.determine_dynamic()
python.determine_dynamic()
visual_basic.determine_dynamic()
