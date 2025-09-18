/*
The MIT License (MIT)
Copyright (c) 2025 [WE THE DEVS].

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

/*
 * Project      : ANTLR4 lexer grammar for NeoBASIC programming language.
 *                https://github.com/neobasic
 * Developed by : Raul Bras, @teknolista.
 */

parser grammar NeoBasicParser;

// Insert here @header.

options {
    tokenVocab = NeoBasicLexer;
    // superClass = NeoBasicParserBase;
}

// --- SOURCE CODE ORGANIZATION OF NEO PROGRAM ----------------------

neoProgram : (instructionSentence EOS)+;

instructionSentence : declaration;


// --- INSTRUCTION SENTENCE: DECLARATION ----------------------------

declaration : constSentence
            | valSentence
            | varSentence
            ;

// Constant declaration

constSentence : constSpecifier* constClause;

constSpecifier : COMPTIME
               | INLINE
               ;

constClause : CONST constDeclare;

constDeclare : constDeclareSingle
             | constDeclareMultiple
             | constDeclareParallel
             ;

constDeclareSingle : symbolIdentifier type? singleAssignmentOperator expression;

constDeclareMultiple : constDeclareSingle (COMMA constDeclareSingle)+;

constDeclareParallel : symbolIdentifiers multipleAssignmentOperator expressions;

// Value declaration

valSentence : valSpecifier* valClause;

valSpecifier : COMPTIME
             | STATIC
             | INLINE
             ;

valClause : VAL varDeclare;

valDeclare : valDeclareSingle
           | valDeclareMultiple
           | valDeclareParallel
           ;

valDeclareSingle : symbolIdentifier type? (singleAssignmentOperator expression)?;

valDeclareMultiple : valDeclareSingle (COMMA valDeclareSingle)+;

valDeclareParallel : symbolIdentifiers multipleAssignmentOperator expressions;

// Variable declaration

varSentence : varSpecifier* varClause;

varSpecifier : COMPTIME
             | STATIC
             | INLINE
             ;

varClause : VAR varDeclare;

varDeclare : varDeclareSingle
           | varDeclareMultiple
           | varDeclareParallel
           ;

varDeclareSingle : symbolIdentifier type? (singleAssignmentOperator expression)?;

varDeclareMultiple : varDeclareSingle (COMMA varDeclareSingle)+;

varDeclareParallel : symbolIdentifiers multipleAssignmentOperator expressions;


// --- UNARY OPERATORS ----------------------------------------------

prefixUnaryOperator : unaryArithmeticOperator
                    | unaryBitwiseOperator
                    | unaryLogicalOperator
                    | unarySpreadOperator
                    | unarySortOperator
                    | unaryMetaOperator
                    ;

posfixUnaryOperator : unarySortOperator
                    | unaryCloneOperator
                    ;

// Arithmetic Operators (Prefix Notation)

unaryArithmeticOperator : PLUS
                        | MINUS
                        | INCREMENT
                        | DECREMENT
                        | SQUARE_POWER
                        | SQUARE_ROOT
                        | FACTORIAL
                        ;

//  Bitwise and Logical Operators

unaryBitwiseOperator : TILDE
                     | BIT_NEGATION
                     ;

unaryLogicalOperator : NOT;

// Miscellaneous operators

unarySpreadOperator : ELLIPSIS;

unarySortOperator : CARET    // Sort ascending or descending a data structure
                  | SORTING  // Sort ascending or descending a var
                  ;

unaryCloneOperator : EQUAL         // Shallow copy
                   | DEEP_CLONING  // Deepp copy
                   ;

unaryMetaOperator : TYPEOF
                  | SIZEOF
                  ;

// --- BINARY OPERATORS ---------------------------------------------

// Arithmetic Operators (Infix Notation)

binaryExponentialOperator : SQUARE_POWER
                          | SQUARE_ROOT
                          ;

binaryMultiplicativeOperator : ASTERISK
                             | SLASH
                             | DIVISION
                             | QUOTIENT
                             | PERCENT
                             | PERCENTAGE_RATE
                             | PERCENTAGE_AMOUNT
                             | PERCENTAGE_INCREASE
                             | PERCENTAGE_DECREASE
                             | PERCENTAGE_VARIATION
                             ;

binaryAdditiveOperator : PLUS
                       | MINUS
                       ;

// Bitwise Operators (Non-Strict Evaluation = Short-circuit Evaluation)

bitShiftOperator : DOUBLE_LEFT_ANGLE
                 | DOUBLE_RIGHT_ANGLE
                 | UNSIGNED_RIGHT_SHIFT
                 ;

bitConjunctionOperator : AMPERSAND
                       | BIT_CLEAR
                       ;

bitExclusiveDisjunctionOperator : CARET;

bitDisjunctionOperator : PIPE;

// Comparison Operators

binaryComparisonOperator : ELVIS_TEST
                         | THREE_WAY_TEST
                         ;

// Relational Operators

binaryRelationalOperator : STRICT_EQUALITY
                         | STRICT_INEQUALITY
                         | LOOSE_EQUALITY
                         | LOOSE_INEQUALITY
                         | LEFT_ANGLE
                         | LESS_OR_EQUALS
                         | RIGHT_ANGLE
                         | GREATER_OR_EQUALS
                         ;

// Conditional operators

binaryConditionalOperator : IS
                          | IS NOT
                          | IN
                          | NOT IN
                          | BETWEEN
                          | NOT BETWEEN
                          | LIKE
                          | NOT LIKE
                          | DIVISIBLE_BY
                          | NOT_DIVISIBLE_BY
                          ;

// Logical Operators (Non-Strict Evaluation = Short-circuit Evaluation)

binaryConjunctionOperator : AND
                          | NAND
                          ;

binaryExclusiveDisjunctionOperator : XOR
                                   | NXOR
                                   ;

binaryDisjunctionOperator : OR
                          | NOR
                          ;

// Coalescing Operators

binaryCoalescingOperator : EXCLAMATION
                         | DOUBLE_EXCLAMATION
                         | ERROR_PROPAGATION_NONE_COALESCING
                         | QUESTION
                         | DOUBLE_QUESTION
                         ; 


// --- ASSIGNMENT OPERATORS -----------------------------------------

assignmentOperator : singleAssignmentOperator
                   | multipleAssignmentOperator
                   | compoundAssignmentOperator
                   ;

singleAssignmentOperator : EQUAL
                         | POP_ONE_ASSIGNMENT
                         | PULL_ALL_ASSIGNMENT
                         | PIPE_ASSIGNMENT
                         ;

multipleAssignmentOperator : EQUAL
                           | DESTRUCTURING_ASSIGNMENT
                           ;

compoundAssignmentOperator : ADDITION_ASSIGNMENT
                           | SUBTRACTION_ASSIGNMENT
                           | MULTIPLICATION_ASSIGNMENT
                           | REAL_DIVISION_ASSIGNMENT
                           | INTEGER_DIVISION_ASSIGNMENT
                           | MODULO_ASSIGNMENT
                           | NTH_POWER_ASSIGNMENT
                           | NTH_ROOT_ASSIGNMENT
                           | PERCENTAGE_RATE_ASSIGNMENT
                           | PERCENTAGE_AMOUNT_ASSIGNMENT
                           | PERCENTAGE_INCREASE_ASSIGNMENT
                           | PERCENTAGE_DECREASE_ASSIGNMENT
                           | PERCENTAGE_VARIATION_ASSIGNMENT
                           | BIT_AND_ASSIGNMENT
                           | BIT_CLEAR_ASSIGNMENT
                           | BIT_XOR_ASSIGNMENT
                           | BIT_OR_ASSIGNMENT
                           | LEFT_SHIFT_ASSIGNMENT
                           | SIGNED_RIGHT_SHIFT_ASSIGNMENT
                           | UNSIGNED_RIGHT_SHIFT_ASSIGNMENT
                           | NONE_COALESCING_ASSIGNMENT
                           ;


// --- IDENTIFIERS --------------------------------------------------

// Single identifiers

symbolIdentifier : IDENTIFIER;

qualifiedIdentifier : IDENTIFIER (DOT IDENTIFIER)*;

// Identifiers list

identifiers : IDENTIFIER (COMMA IDENTIFIER)*;

symbolIdentifiers : symbolIdentifier (COMMA symbolIdentifier)*;

qualifiedIdentifiers : qualifiedIdentifier (COMMA qualifiedIdentifier)*;


// LITERALS ---------------------------------------------------------

predeclaredValue : IOTA;

literal : escalarLiteral
        ;

// Escalar literals

escalarLiteral : booleanLiteral
               | numericLiteral
               ;

booleanLiteral : TRUE
               | FALSE
               ;

// Numeric literals

numericLiteral : NATURAL_LIT
               | INTEGER_LIT
               | REAL_LIT
               | NONZERO expression
               | ZERO
               | MINVALUE
               | MAXVALUE
               | NAN
               | POSITIVEINFINITY
               | NEGATIVEINFINITY
               ;


// --- DATA TYPES ---------------------------------------------------

type : nativeType
     ;

nativeType : escalarType
           ;

// Escalar data types

escalarType : booleanType
            | numericType
            ;

booleanType : BOOL8
            | BOOL16
            | BOOL32
            | BOOL64
            | BOOL128
            | BOOL
            ;

numericType : numericNatural
            | numericInteger
            | numericReal
            ;

numericNatural : NAT8
               | NAT16
               | NAT32
               | NAT64
               | NAT128
               | BYTE
               | NAT
               ;

numericInteger : INT8
               | INT16
               | INT32
               | INT64
               | INT128
               | INT
               ;

numericReal : REAL8
            | REAL16
            | REAL32
            | REAL64
            | REAL128
            | REAL
            ;


// --- EXPRESSION ---------------------------------------------------

expressions : expression (COMMA expression)*;

primaryExpressions : primaryExpression (COMMA primaryExpression)*;

primaryExpression : operand
                  | parenthesizedExpression
                  | primaryExpression DOT primaryExpression
                  | primaryExpression LEFT_PARENTHESIS expressions RIGHT_PARENTHESIS
                  | primaryExpression SEMICOLON primaryExpression
                  | primaryExpression posfixUnaryOperator
                  | prefixUnaryOperator primaryExpression
                  | qualifiedIdentifier expression
                  ;

operand : literal
        | predeclaredValue
        | qualifiedIdentifier
        ;

parenthesizedExpression : LEFT_PARENTHESIS expression RIGHT_PARENTHESIS;

expression : primaryExpression
           | expression binaryExponentialOperator expression
           | expression binaryMultiplicativeOperator expression
           | expression binaryAdditiveOperator expression
           | expression bitShiftOperator expression
           | expression bitConjunctionOperator expression
           | expression bitExclusiveDisjunctionOperator expression
           | expression bitDisjunctionOperator expression
           | expression binaryComparisonOperator expression
           | expression binaryRelationalOperator expression
           | expression binaryConditionalOperator expression
           | expression binaryConjunctionOperator expression
           | expression binaryExclusiveDisjunctionOperator expression
           | expression binaryDisjunctionOperator expression
           | expression binaryCoalescingOperator expression?
           | assignmentExpression
           ;

assignmentExpression : primaryExpression assignmentOperator expression;
