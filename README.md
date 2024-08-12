
# DFA Minimization Algorithm

## Group Members
- Santiago Salazar Gilchrist

## Environment Information
- **Operating System**: MacOS Sonoma 14.4.1
- **Programming Language**: Python 3.10.6
- **Tools Used**: Visual Studio Code 1.79.2, Python Standard Library

## Instructions for Running the Implementation



1. **Prepare the Input File**:
   - Create an input file containing the description of the DFA as specified in the problem statement.
   - The input file should contain:
     1. The number of cases.
     2. For each case:
        - Number of states (`n`).
        - The alphabet (`alphabet`).
        - The final states (`final_states`).
        - The transition table (`transitions`).

4. **Run the Script**:
   - Navigate to the directory where the script is located.
   - Run the script using the following command:
     ```
     python3 dfa_minimization.py < input.txt
     ```
   - Here, `input.txt` is the file containing the input data.

5. **View the Output**:
   - The output will display pairs of equivalent states in lexicographical order for each case.
   - Each pair will be formatted as `(i,j)` and pairs will be separated by a space.

## Example

Given the following input:

```
1
6
a b
1 4 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
```

The output will be:

```
(3,4) (3,5) (4,5)
```

