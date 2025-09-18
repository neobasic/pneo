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

lexer grammar NeoBasicKeywords;

// --- KEYWORDS -----------------------------------------------------

// IDENTIFICATION DIVISION


// ENVIRONMENT DIVISION


// TOP LEVEL SENTENCES

CONST : 'const';
VAL : 'val';
VAR : 'var';

// ACCESS SPECIFIERS


// DECLARATION SPECIFIERS

COMPTIME : 'comptime';
INLINE : 'inline';
STATIC : 'static';

// STATEMENTS AND BLOCKS


// PREDECLARED VALUES AND VARIABLES

IOTA : 'iota';

// FACT SCOPES


// EXPRESSIONS


// META OPERATORS

TYPEOF : 'typeof';
SIZEOF : 'sizeof';
INSTANCEOF : 'instanceof';

// CONDITIONAL OPERATORS

IS : 'is';
IN : 'in';
BETWEEN : 'between';
LIKE : 'like';

// LOGICAL OPERATORS

NOT : 'not';
AND : 'and';
OR : 'or';
XOR : 'xor';
NAND : 'nand';
NOR : 'nor';
NXOR : 'nxor';

// ARRAY OPERATORS


// META DATA TYPES


// BOOLEAN DATA TYPES

BOOL8 : 'bool8';
BOOL16 : 'bool16';
BOOL32 : 'bool32';
BOOL64 : 'bool64';
BOOL128 : 'bool128';
BOOL : 'bool';

// NUMERIC DIGITS


// NATURAL NUMBERS

NAT8 : 'nat8';
NAT16 : 'nat16';
NAT32 : 'nat32';
NAT64 : 'nat64';
NAT128 : 'nat128';
BYTE : 'byte';
NAT : 'nat';

// NUMERIC INTEGERS

INT8 : 'int8';
INT16 : 'int16';
INT32 : 'int32';
INT64 : 'int64';
INT128 : 'int128';
INT : 'int';

// NUMERIC REALS

REAL8 : 'real8';
REAL16 : 'real16';
REAL32 : 'real32';
REAL64 : 'real64';
REAL128 : 'real128';
REAL : 'real';

// NUMERIC DECIMALS


// NUMERIC RATIOS


// NUMERIC COMPLEXES


// NUMERIC QUATERNIONS


// TEMPORAL DATA TYPES


// CHARACTER DATA TYPES


// SEQUENCE DATA TYPES


// SHELL DATA TYPES


// COMPOSITE DATA TYPES


// ARRAY DATA TYPES


// MONAD LOGIC VALUE CONSTRUCTORS

TRUE : 'True';
FALSE : 'False';

// MONAD NUMERIC VALUE CONSTRUCTORS

NONZERO : 'Nonzero';
ZERO : 'Zero';
MINVALUE : 'MinValue';
MAXVALUE : 'MaxValue';
NAN : 'NaN';
POSITIVEINFINITY : 'PositiveInfinity';
NEGATIVEINFINITY : 'NegativeInfinity';

// MONAD TEMPORAL VALUE CONSTRUCTORS


// MONAD CHARACTER VALUE CONSTRUCTORS


// MONAD SEQUENCE VALUE CONSTRUCTORS


// MONAD PATH VALUE CONSTRUCTORS


// MONAD URI VALUE CONSTRUCTORS


// MONAD INET VALUE CONSTRUCTORS


// MONAD RESULT ! VALUE CONSTRUCTORS


// MONAD MAYBE ? VALUE CONSTRUCTORS


// MONAD EITHER ?? VALUE CONSTRUCTORS


// MONAD STREAM |> VALUE CONSTRUCTORS


// -------------------------------------------------------------------------

// BUILT-IN CONSOLE MACROS

SCAN  : 'scan';
ECHO  : 'echo';

// BUILT-IN SHELL MACROS


// BUILT-IN ERROR-HANDLING MACROS


// MAGIC COMMENT: TEST


// MAGIC STATEMENT: TRACING

