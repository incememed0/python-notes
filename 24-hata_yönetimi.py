# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# hataların tümüne https://docs.python.org/3/library/exceptions.html buradan ulaşabilirsin.
#
# Hatalar
# print(a)        ---> NameError
# int('5b2')      ---> ValueName
# print(10/0)     ---> ZeroDivisionError
# print('denem'e) ---> SyntaxError
#
# Hata Yönetimi

try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except Exception as hata : # programda oluşabilicek hatalar yazılır
    print("bir hata oluştu. sebebi: ",hata)
else: # program hatasız çalıştırılırsa;
    print("program çalıştı")
finally: # program hatalı veya hatasız çalışsada çalıştırılır
    print("try ve except çalıştırıldı")

"""
---> TÜM HATALAR <---
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""