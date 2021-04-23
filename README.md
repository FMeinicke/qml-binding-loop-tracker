# QML Binding Loop Tracker
This is a slightly modified version of [Dave's QML Binding Loop Backtrace Printer](https://blog.davidedmundson.co.uk/blog/daves-qml-binding-loop-backtrace-printer/).

You can read more about this tool in the blog post linked above.  
Essentially, what it does is to start a GDB debugging session for the application that you call this script with.
The script registers a breakpoint with a corresponding handler that simply prints a backtrace of the bindings being updated when a binding loop occurs.

## Usage
In order to use this script you need to have the `gdb` executable in your `PATH` environment variable.

The you can simply call it like this:
```console
$ /path/to/binding-loop-tracker.py yourAppName
```
if you're on Linux  
**or** 
```cmd
> python C:\path\to\binding-loop-tracker.py yourAppName.exe
```
if you're on Windows.


## Credits
As I said, full credit goes to [David Edmundson](https://blog.davidedmundson.co.uk/) for providing this tool in the first place.  
I just built on his work to improve the tool for my personal use case.

## License 
This tool is licensed under the [MIT License](#LICENSE).
