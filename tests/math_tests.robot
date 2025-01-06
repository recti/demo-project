*** Settings ***
Library    ../MyMathLibrary.py

*** Test Cases ***

Test Addition
    ${result}=    Add    2    3
    Should Be Equal As Numbers    ${result}    5

Test Subtraction
    ${result}=    Subtract    3    2
    Should Be Equal As Numbers    ${result}    1

Test Multiplication
    ${result}=    Multiply    3    2
    Should Be Equal As Numbers    ${result}    6