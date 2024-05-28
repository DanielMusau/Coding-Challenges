# ccwc: Custom Count Words and Characters
## Overview
ccwc is a Python script that mimics some functionalities of the Unix `wc` (word count) command. It can count the number of lines, words, characters, and bytes in a given file. Additionally, it supports reading input from standard input (stdin) if no filename is specified, making it versatile for use in pipelines.

## Features
- Count lines in a file or from stdin.
- Count words in a file or from stdin.
- Count characters in a file or from stdin.
- Count bytes in a file.
- Display a summary of lines, words, and bytes for a file or stdin.

## Usage
```
./ccwc -option [<filename>]
Options
-c: Count bytes.
-l: Count lines.
-w: Count words.
-m: Count characters.
No option: Display a summary (lines, words, and bytes).
```
### Examples
```
Count lines in a file:
./ccwc -l example.txt

Count words from stdin:
cat example.txt | ./ccwc -w

Display summary of a file:
./ccwc example.txt

Display summary from stdin:
cat example.txt | ./ccwc
```

## Installation
To use ccwc, you need to have Python 3 installed on your system. You can download and install Python 3 from python.org.

## Implementation Details
The script is implemented in Python 3 and uses standard libraries: sys and os. Here’s a breakdown of the functions:

- `print_usage()`: Prints the usage instructions and exits the program.
- `count_bytes(file_path)`: Counts and prints the number of bytes in a file. Reads from stdin if file_path is None.
- `count_lines(file_path)`: Counts and prints the number of lines in a file. Reads from stdin if file_path is None.
- `count_words(file_path)`: Counts and prints the number of words in a file. Reads from stdin if file_path is None.
- `count_chars(file_path)`: Counts and prints the number of characters in a file. Reads from stdin if file_path is None.
- `count_all(file_path)`: Prints a summary of the number of lines, words, and bytes in a file. Reads from stdin if file_path is None.
- `main()`: The main function that processes command-line arguments and invokes the appropriate counting function.