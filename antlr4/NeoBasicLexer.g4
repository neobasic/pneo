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

lexer grammar NeoBasicLexer;

import NeoBasicKeywords;

options {
//     superClass = NeoBasicLexerBase;
}

/*
 *  Default Lexer Mode
 */

// --- PUNCTUATION --------------------------------------------------

LEFT_PARENTHESIS  : '(';    // 
RIGHT_PARENTHESIS : ')';    // 
LEFT_BRACKET      : '[';    // 
RIGHT_BRACKET     : ']';    // 
LEFT_CURLY        : '{';    // 
RIGHT_CURLY       : '}';    // 
LEFT_ANGLE        : '<';    // Less Than
RIGHT_ANGLE       : '>';    // Greater Than
DOT               : '.';    // Dot
COMMA             : ',';    // Comma
SEMICOLON         : ';';    // 
COLON             : ':';    // Pair mapping
EXCLAMATION       : '!';    // Error
QUESTION          : '?';    // Optional
APOSTROPHE        : '\'';   // Character literal, template string literal
QUOTE             : '"';    // Verbatim String literal
BACKTICK          : '`';    // Backtick
AT                : '@';    // Atoms, Annotations/Decorators
HASH              : '#';    // Comment, Directive (Interpreter, Pragma, Testing)
DOLLAR            : '$';    // 
AMPERSAND         : '&';    // 
ASTERISK          : '*';    // Multiplication
SLASH             : '/';    // Real Division, Regular expression literal
DIVISION          : '÷';    // Integer Division
PERCENT           : '%';    // Modulo, Integer Division, Percentage
BACKSLASH         : '\\';   // 
TILDE             : '~';    // 
CARET             : '^';    // 
PIPE              : '|';    // 
UNDERSCORE        : '_';    // Wildcard, Anonymous variable
EQUAL             : '=';    // Assignment, Equality
PLUS              : '+';    // 
MINUS             : '-';    // 

ELLIPSIS          : '...';  // 
LAMBDA            : '(\\';  // 

DOUBLE_LEFT_BRACKET  : '[[';    // 
DOUBLE_RIGHT_BRACKET : ']]';    // 

DOUBLE_LEFT_CURLY    : '{{';    // 
DOUBLE_RIGHT_CURLY   : '}}';    // 

DOUBLE_LEFT_ANGLE    : '<<';   // 
DOUBLE_RIGHT_ANGLE   : '>>';   // 

DOUBLE_EXCLAMATION   : '!!';   // 
DOUBLE_QUESTION      : '??';   // 

DOUBLE_COLON         : '::';   // 
DOUBLE_SEMICOLON     : ';;';   // 

SPECIAL_ASSIGNMENT   : '~=';   // 


// --- UNARY OPERATORS ----------------------------------------------

// Arithmetic Operators

INCREMENT     : '++';
DECREMENT     : '--';
SQUARE_POWER  : '**';
SQUARE_ROOT   : '*/';
FACTORIAL     : '*!';

// Bitwise Operators

BIT_NEGATION  : '~~';

// Miscellaneous Operators

DEEP_CLONING : '===';

SORTING : '^^';


// --- BINARY OPERATORS ---------------------------------------------

// Arithmetic operators

QUOTIENT : '%%';

// Financial Operators

PERCENTAGE_RATE      : '%/';
PERCENTAGE_AMOUNT    : '%*';
PERCENTAGE_INCREASE  : '%+';
PERCENTAGE_DECREASE  : '%-';
PERCENTAGE_VARIATION : '%^';

// Bitwise Operators

BIT_CLEAR            : '&~';
UNSIGNED_RIGHT_SHIFT : '>>>';

// Conditional Operators

DIVISIBLE_BY          : '?%';
NOT_DIVISIBLE_BY      : '!%';

// Comparison Operators

ELVIS_TEST            : '?:';
THREE_WAY_TEST        : '<=>';

// Relational Operators

STRICT_EQUALITY   : '==';
STRICT_INEQUALITY : '!=';
LOOSE_EQUALITY    : '~==';
LOOSE_INEQUALITY  : '~!=';
LESS_OR_EQUALS    : '<=';
GREATER_OR_EQUALS : '>=';

// Coalescing Operators

ERROR_PROPAGATION_NONE_COALESCING : '!?';

// Single Assignment Operators

POP_ONE_ASSIGNMENT       : '<-';
PULL_ALL_ASSIGNMENT      : '<<-'; 
PIPE_ASSIGNMENT          : '<|'; 
DESTRUCTURING_ASSIGNMENT : ':=';

// Compound Assignment Operators

ADDITION_ASSIGNMENT             : '+=';
SUBTRACTION_ASSIGNMENT          : '-=';
MULTIPLICATION_ASSIGNMENT       : '*=';
REAL_DIVISION_ASSIGNMENT        : '/=';
INTEGER_DIVISION_ASSIGNMENT     : '÷=';
QUOTIENT_ASSIGNMENT             : '%%=';
MODULO_ASSIGNMENT               : '%=';
NTH_POWER_ASSIGNMENT            : '**=';
NTH_ROOT_ASSIGNMENT             : '*/=';
PERCENTAGE_RATE_ASSIGNMENT      : '%/=';
PERCENTAGE_AMOUNT_ASSIGNMENT    : '%*=';
PERCENTAGE_INCREASE_ASSIGNMENT  : '%+=';
PERCENTAGE_DECREASE_ASSIGNMENT  : '%-=';
PERCENTAGE_VARIATION_ASSIGNMENT : '%^⁼';
BIT_AND_ASSIGNMENT              : '&=';
BIT_OR_ASSIGNMENT               : '|=';
BIT_XOR_ASSIGNMENT              : '^=';
BIT_CLEAR_ASSIGNMENT            : '&^=';
LEFT_SHIFT_ASSIGNMENT           : '<<=';
SIGNED_RIGHT_SHIFT_ASSIGNMENT   : '>>=';
UNSIGNED_RIGHT_SHIFT_ASSIGNMENT : '>>>=';
NONE_COALESCING_ASSIGNMENT      : '??=';
SHELL_PID_ASSIGNMENT            : '&&=';
SHELL_BKG_PID_ASSIGNMENT        : '||=';

// Range Operators

INTERVAL_INCLUSIVE       : '..';
INTERVAL_LEFT_EXCLUSIVE  : '>..';
INTERVAL_RIGHT_EXCLUSIVE : '..<';
INTERVAL_EXCLUSIVE       : '>..<';

INTERVAL
    : INTERVAL_INCLUSIVE
    | INTERVAL_LEFT_EXCLUSIVE
    | INTERVAL_RIGHT_EXCLUSIVE
    | INTERVAL_EXCLUSIVE
    ;

INTERVAL_LEFT
    : INTERVAL_INCLUSIVE
    | INTERVAL_LEFT_EXCLUSIVE
    ;

INTERVAL_RIGHT
    : INTERVAL_INCLUSIVE
    | INTERVAL_RIGHT_EXCLUSIVE
    ;

// Composite Operators

MIXIN   : '<>';
EXTENDS : '->';

// Imply Operators

NECK_RULE : ':-';

MAPPING_ARROW : '=>';

MONAD_BIND : '=>>';

// Pipeline Operator

PIPELINE : '|>';

// Command Execution Operators

COMMAND_SEQUENCE : '&&';

COMMAND_SEQUENCE_OKAY : '?&';
COMMAND_SEQUENCE_FAIL : '!&';

COMMAND_BACKGROUND : '||';

// Input/Output Redirection Operators

OUTPUT_REDIRECTION : '&>';
APPEND_OUTPUT_REDIRECTION : '&>>';

STDOUT_REDIRECTION : '&1>';
APPEND_STDOUT_REDIRECTION : '&1>>';

STDERR_REDIRECTION : '&2>';
APPEND_STDERR_REDIRECTION : '&2>>';


// --- LITERALS -----------------------------------------------------

// Real literals (Floating Point Numbers)

REAL_LIT : [+-] REAL_NUMBER;

fragment REAL_NUMBER
    : DEC_REAL
    | HEX_REAL
    ; 

DEC_REAL : DEC_DECIMAL DEC_EXPONENT?;
fragment DEC_EXPONENT : [eE] [+-]? DEC_GROUPS;

HEX_REAL : HEX_DECIMAL HEX_EXPONENT?;
fragment HEX_EXPONENT : [pP] [+-]? DEC_GROUPS;

DEC_DECIMAL : DEC_MANTISSA;
fragment DEC_MANTISSA
    : DEC_GROUPS
    | DEC_GROUPS '.' DEC_GROUPS?
    | '.' DEC_GROUPS
    ;

HEX_DECIMAL : '0' [xX] HEX_MANTISSA;
fragment HEX_MANTISSA
    : HEX_GROUPS
    | HEX_GROUPS '.' HEX_GROUPS?
    | '.' HEX_GROUPS
    ;

// Integer literals

NATURAL_LIT : INTEGER_NUMBER 'N'?;

INTEGER_LIT : [+-] INTEGER_NUMBER;

INTEGER_NUMBER
    : DEC_VALUE
    | HEX_VALUE
    | OCT_VALUE
    | BIN_VALUE
    | ROM_VALUE
    ;

DEC_VALUE  : '0' | DEC_GROUPS;
fragment DEC_GROUPS : DEC_DIGIT ('_'? DEC_DIGIT)*;

HEX_VALUE  : HEX_UNIT HEX_GROUPS;
fragment HEX_UNIT   : '0' [xX];
fragment HEX_GROUPS : HEX_DIGIT ('_'? HEX_DIGIT)*;

OCT_VALUE  : OCT_UNIT OCT_GROUPS;
fragment OCT_UNIT   : '0' [oO];
fragment OCT_GROUPS : OCT_DIGIT ('_'? OCT_DIGIT)*;

BIN_VALUE  : BIN_UNIT BIN_GROUPS;
fragment BIN_UNIT   : '0' [bB];
fragment BIN_GROUPS : BIN_DIGIT ('_'? BIN_DIGIT)*;

ROM_VALUE  : ROM_UNIT ROM_GROUPS;
fragment ROM_UNIT   : '0' [rR];
fragment ROM_GROUPS : ROM_DIGIT ('_'? ROM_DIGIT)*;

// Computer number formats

fragment DEC_DIGIT : UNICODE_DIGIT;
fragment HEX_DIGIT : [0-9a-fA-F];
fragment OCT_DIGIT : [0-7];
fragment BIN_DIGIT : [01];
fragment ROM_DIGIT : [IVXLCDM];


// --- MAGIC STATEMENTS ---------------------------------------------


// --- SYMBOLS ------------------------------------------------------

// Identifier Names

IDENTIFIER : ALPHA ALPHANUMERIC*;


// --- MAGIC COMMENTS -----------------------------------------------


// --- SPECIAL TOKENS -----------------------------------------------

// End of Sentence (EOS): Emit an EOS token for any newlines, semicolon, 
// multiline comments or the EOF and return to normal lexing.

EOS : EOL
    // | LINE_COMMENT
    | EOF
    ;

// End of Line (EOL) characters

EOL : '\n'       // Unix, Linux, macOS
    | '\r' '\n'  // Windows, DOS
    | '\r'       // Classic Mac OS (pre-OS X)
    | '\u0085'   // IBM Mainframes (EBCDIC)
    | '\u2028'   // Unicode Line Separator
    | '\u2029'   // Unicode Paragraph Separator
    ;


// --- UNICODE CHARACTERS -------------------------------------------

fragment ALPHA: UNICODE_LETTER | '_';

fragment ALPHANUMERIC : UNICODE_ALPHANUMERIC | '_';

fragment UNICODE_ALPHANUMERIC
    : UNICODE_LETTER
    | UNICODE_DIGIT
    | [\p{Mn}]   // Unicode category for Nonspacing Mark
    | [\p{Pc}]   // Unicode category for Connector Punctuation
    ;

// Any unicode code points that are categorized as (L) Letter.
//[\p{L}] matches any kind of letter from any language.
fragment UNICODE_LETTER: [\p{L}];

// Any unicode code points that are categorized as (Nd) Decimal Number.
//[\p{Nd}] matches a digit zero through nine in any script except ideographic scripts
fragment UNICODE_DIGIT: [\p{Nd}];


// --- COMMENTS -----------------------------------------------------


// --- HIDDEN TOKENS ------------------------------------------------

// White Spaces (WSP) characters

WSP : [\u0009\u000B\u000C\u0020\u00A0\p{Zs}]+ -> channel(HIDDEN);


// --- ERROR HANDLING -----------------------------------------------
