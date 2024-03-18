import sys
import inspect
from scalene import scalene_profiler

# Using Python Settrace
scalene_profiler.start()


def my_tracer2(frame, event, arg):
    function_code = frame.f_code
    function_name = function_code.co_name
    lineno = frame.f_lineno
    vars = frame.f_locals
    source_lines, starting_line_no = inspect.getsourcelines(frame.f_code)
    loc = f"{function_name}:{lineno} {source_lines[lineno - starting_line_no].rstrip()}"
    vars = ", ".join(f"{name} = {vars[name]}" for name in vars)
    print(f"{loc:50} ({vars})")
    return my_tracer


def my_tracer(frame, event, arg=None):
    code = frame.f_code
    func_name = code.co_name
    line_no = frame.f_lineno
    print(f"A {event} encountered in \
    {func_name}() at line number {line_no} ")

    return my_tracer


def fun(a, b):
    c = a + b
    return c

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def check():
    return fibonacci(20)


# sys.settrace(my_tracer)
sys.settrace(my_tracer2)

print(check())
sys.settrace(None)


scalene_profiler.stop()


