# Codeword Converter
This is a Python program that can code a sentence and decode a coded sentence back into its original form.

# Installation
Clone or download the repository to your local machine.
Ensure you have Python 3 installed on your machine.

# Usage
To code a sentence, run the program and choose option 1. Enter the sentence you want to code when prompted. The program will code the sentence using a simple algorithm and display the coded sentence.

To decode a coded sentence, run the program and choose option 2. Enter the coded sentence you want to decode when prompted. The program will decode the sentence back into its original form and display the decoded sentence.

# Algorithm
The program uses a simple algorithm to code and decode sentences. For sentences with length less than or equal to 2, the program appends the first character of the sentence to the end and removes the first character. For sentences with length greater than 2, the program appends the first character of the sentence to the end, removes the first character, and adds three random letters from the alphabet to the beginning and end of the sentence.

To decode a sentence that has been coded using this algorithm, the program reverses the steps taken during the coding process. For sentences with length less than or equal to 2, the program appends the first character of the sentence to the end and removes the first character. For sentences with length greater than 2, the program removes the first three and last three characters of the sentence, moves the last character of the remaining sentence to the beginning, and removes the last character.
# Example
Suppose you want to code the sentence "Hello World!". Run the program and choose option 1. Enter the sentence when prompted. The output will be:

Coded Sentence: gkhelloHgkh gxrorld!Wgxr
To decode the coded sentence "gkhelloHgkh gxrorld!Wgxr" back into its original form, run the program and choose option 2. Enter the coded sentence when prompted. The output will be:

DeCoded Sentence: Hello World!

# Notes
This program uses a simple algorithm to code and decode sentences. It is not meant to provide strong encryption, and should not be used for sensitive information.

## 🛠 Skills used in this project
Python
