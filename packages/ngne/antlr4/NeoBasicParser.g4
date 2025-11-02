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

options {
    tokenVocab = NeoBasicLexer;
}


// --- STARTING RULES -----------------------------------------------

scriptProgram : shebangInterpreter EOS sourceCodeProgram;

sourceCodeProgram : logicalInstructions;         // from file or eval()

oneLinerProgram : logicalInstruction;            // from interactive REPL

neoBasic : scriptProgram
         | sourceCodeProgram
         | oneLinerProgram
         ;


// --- SOURCE CODE ORGANIZATION OF NEOBASIC PROGRAM -----------------

shebangInterpreter : SHEBANG ABSOLUTE_PATH expression?;

logicalInstructionSuite : EOS INDENT logicalInstructions DEDENT;

logicalInstructions : (logicalInstruction EOS)+;

logicalInstruction : instructionSentence ( ELC instructionSentence )*;

instructionSentence : directive
                    | declaration
                    | statement
                    |                // empty line
                    ;


// --- INSTRUCTION SENTENCE: DIRECTIVE ------------------------------

directive : pragmaDirective
          | canaryTestingDirective
          ; 

// Pragma directive

pragmaDirective : SHEBANG IDENTIFIER expressions?;

// Canary-testing directive

canaryTestingDirective : WOODSTOCK testStatement;

// Test statements

testStatement : assertStatement
              ;

assertStatement : ASSERT expression (EXCLAMATION | EXCLAMATION expression)?;


// --- INSTRUCTION SENTENCE: DECLARATION ----------------------------

declaration : moduleSentence
            | appletSentence
            | notabeneSentence
            | useSentence
            | includeSentence
            | deflagSentence
            | constSentence
            | ivalSentence
            | varSentence
            ;

// Module declaration (translation unit programs)

moduleSentence : moduleClause;

moduleClause: MODULE qualifiedIdentifier;

// Applet declaration (applet programs)

appletSentence : appletClause;

appletClause : APPLET IDENTIFIER;

// Notabene declaration (notebook programs)

notabeneSentence : notabeneClause;

notabeneClause : NOTABENE qualifiedIdentifier;

// Use declaration

useSentence : useClause;

useClause : USE ( useSuite | useDeclare );

useSuite : EOS INDENT useDeclareBlock DEDENT;

useDeclareBlock : useDeclare (EOS useDeclare)*;

useDeclare : useDeclareSingle
           | useDeclareMultiple
           | useDeclareAs
           | useDeclareOf
           ;

useDeclareSingle : qualifiedIdentifier;

useDeclareMultiple : useDeclareSingle (COMMA useDeclareSingle)+;

useDeclareAs : qualifiedIdentifier AS IDENTIFIER;

useDeclareOf : identifiers OF qualifiedIdentifier;

// Include declaration

includeSentence : includeClause;

includeClause : INCLUDE ( includeSuite | includeDeclare );

includeSuite : EOS INDENT includeDeclareBlock DEDENT;

includeDeclareBlock : includeDeclare (EOS includeDeclare)*;

includeDeclare : includeDeclareSingle
               | includeDeclareMultiple
               | includeDeclareAs
               ;

includeDeclareSingle : shellPathLiteral;

includeDeclareMultiple: includeDeclareSingle (COMMA includeDeclareSingle)+;

includeDeclareAs : shellPathLiteral AS typedIdentifier;

// Defined Flag (deflag) declaration

deflagSentence : defineClause
               | undefClause
               ;

defineClause : DEFINE ( defineSuite | defineDeclare );

defineSuite : EOS INDENT defineDeclareBlock DEDENT;

defineDeclareBlock : defineDeclare (EOS defineDeclare)*;

defineDeclare : defineDeclareSingle
              | defineDeclareMultiple
              ;

defineDeclareSingle : IDENTIFIER literal?;

defineDeclareMultiple: defineDeclareSingle (COMMA defineDeclareSingle)+;

undefClause : UNDEF undefDeclare;

undefDeclare : identifiers;


// TOP LEVEL SENTENCES

accessSpecifier : PUBLIC
                | PROTECTED
                | PRIVATE
                ;

// Constant declaration

constSentence : accessSpecifier? constClause;

constClause : constSpecifier* CONST ( constSuite | constDeclare );

constSpecifier : COMPTIME
               | INLINE
               ;

constSuite : EOS INDENT constDeclareBlock DEDENT;

constDeclareBlock : constDeclare (EOS constDeclare)*;

constDeclare : constDeclareSingle
             | constDeclareMultiple
             | constDeclareParallel
             ;

constDeclareSingle : typedIdentifier singleAssignmentOperator expression;

constDeclareMultiple : constDeclareSingle (COMMA constDeclareSingle)+;

constDeclareParallel : LEFT_PARENTHESIS typedIdentifiers RIGHT_PARENTHESIS unpackingAssignmentOperator expressions;

// Immutable Value declaration

ivalSentence : accessSpecifier? ivalClause;

ivalClause : ivalSpecifier* IVAL ( ivalSuite | ivalDeclare );

ivalSpecifier : COMPTIME
              | STATIC
              | LINEAR
              | INLINE
              ;

ivalSuite : EOS INDENT ivalDeclareBlock DEDENT;

ivalDeclareBlock : ivalDeclare (EOS ivalDeclare)*;

ivalDeclare : ivalDeclareSingle
            | ivalDeclareMultiple
            | ivalDeclareParallel
            ;

ivalDeclareSingle : typedIdentifier (singleAssignmentOperator expression)?;

ivalDeclareMultiple : ivalDeclareSingle (COMMA ivalDeclareSingle)+;

ivalDeclareParallel : LEFT_PARENTHESIS typedIdentifiers RIGHT_PARENTHESIS unpackingAssignmentOperator expressions;

// Variable declaration

varSentence : accessSpecifier? varClause;

varClause : varSpecifier* VAR ( varSuite | varDeclare );

varSpecifier : COMPTIME
             | STATIC
             | VOLATILE
             | SHARED
             | LOCAL
             | ATOMIC
             | LINEAR
             | INLINE
             ;

varSuite : EOS INDENT varDeclareBlock DEDENT;

varDeclareBlock : varDeclare (EOS varDeclare)*;

varDeclare : varDeclareSingle
           | varDeclareMultiple
           | varDeclareParallel
           ;

varDeclareSingle : typedIdentifier (singleAssignmentOperator expression)?;

varDeclareMultiple : varDeclareSingle (COMMA varDeclareSingle)+;

varDeclareParallel : LEFT_PARENTHESIS typedIdentifiers RIGHT_PARENTHESIS unpackingAssignmentOperator expressions;


// --- INSTRUCTION SENTENCE: STATEMENT ------------------------------

statement : labelIdentifier COLON
          | labelIdentifier COLON statement
          | RUBBERDUCK statement
          | SONGBIRD statement
          | statement executionFlowOperator statement
          | simpleStatement
          | compoundStatement
          ;

// Simple statements

simpleStatement : assignmentStatement
                | consoleStatement
                | expressionStatement
                | emptyStatement
                ;

expressionStatement : expressions;

emptyStatement : ELLIPSIS;

// Assignment statements

assignmentStatement : assignmentSingle
                    | assignmentMultiple
                    | assignmentParallel
                    ;

assignmentSingle : primaryExpression singleAssignmentOperator expression;

assignmentMultiple : assignmentSingle (COMMA assignmentSingle)+;

assignmentParallel : primaryExpressions unpackingAssignmentOperator expressions;

// Console statements

consoleStatement : echoCommand
                 | scanCommand
                 ;

echoCommand : ECHO expression? COMMA?;

scanCommand : SCAN escalarType? expression? COMMA?;

// Compound statements

compoundStatement : controlFlowStatement
                  | conditionalStatement
                  ;

controlFlowStatement : otherwiseSentence
                     ;

conditionalStatement : ifStatement
                     | unlessStatement
                     ;

// Control flow statement otherwise

otherwiseSentence : simpleStatement OTHERWISE statement;

// Conditional statement if

ifStatement : ifThenClause
            ;

ifThenClause : IF expression THEN simpleStatement;

// Conditional statement unless

unlessStatement : unlessClause;

unlessClause : simpleStatement UNLESS expression;


// --- UNARY OPERATORS ----------------------------------------------

prefixUnaryOperator : unaryArithmeticOperator
                    | unaryLogicalOperator
                    | unarySpreadOperator
                    | unaryMetaOperator
                    ;

// Arithmetic Operators (Prefix Notation)

unaryArithmeticOperator : CARET
                        | SQUARE_ROOT
                        | FACTORIAL
                        | INCREMENT
                        | DECREMENT
                        | PLUS
                        | MINUS
                        ;

//  Logical Operators (Prefix Notation)

unaryLogicalOperator : NOT
                     ;

// Meta (Miscellaneous) operators (Prefix Notation)

unarySpreadOperator : ELLIPSIS;

unaryMetaOperator : TYPEOF
                  | SIZEOF
                  ;


// --- BINARY OPERATORS ---------------------------------------------

// Arithmetic Operators (Infix Notation)

binaryExponentialOperator : CARET
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

// Logical Operators (Non-Strict Evaluation = Short-circuit Evaluation) (Infix Notation)

binaryConjunctionOperator : AND
                          | ANDN
                          | NAND
                          ;

binaryExclusiveDisjunctionOperator : XOR
                                   | NXOR
                                   ;

binaryDisjunctionOperator : OR
                          | NOR
                          ;

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

binaryConditionalOperator : ANCESTOROF
                          | INSTANCEOF
                          | IS
                          | IS_NOT
                          | IN
                          | NOT_IN
                          | BETWEEN
                          | NOT_BETWEEN
                          | LIKE
                          | NOT_LIKE
                          | DIVISIBLE_BY
                          | NOT_DIVISIBLE_BY
                          ;

// Flow of Execution Operators

executionFlowOperator : EXECUTE_SEQUENCE
                      | EXECUTE_SEQUENCE_OKAY
                      | EXECUTE_SEQUENCE_FAIL
                      | EXECUTE_BACKGROUND
                      | OUTPUT_REDIRECTION
                      | APPEND_OUTPUT_REDIRECTION
                      | STDOUT_REDIRECTION
                      | APPEND_STDOUT_REDIRECTION
                      | STDERR_REDIRECTION
                      | APPEND_STDERR_REDIRECTION
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
                   | unpackingAssignmentOperator
                   | compoundAssignmentOperator
                   ;

singleAssignmentOperator : EQUAL
                         | DERIVED_ASSIGNMENT
                         | POP_ONE_ASSIGNMENT
                         | PULL_ALL_ASSIGNMENT
                         | PIPE_ASSIGNMENT
                         ;

unpackingAssignmentOperator : EQUAL
                            ;

compoundAssignmentOperator : NTH_POWER_ASSIGNMENT
                           | NTH_ROOT_ASSIGNMENT
                           | MULTIPLICATION_ASSIGNMENT
                           | REAL_DIVISION_ASSIGNMENT
                           | INTEGER_DIVISION_ASSIGNMENT
                           | QUOTIENT_ASSIGNMENT
                           | MODULO_ASSIGNMENT
                           | PERCENTAGE_RATE_ASSIGNMENT
                           | PERCENTAGE_AMOUNT_ASSIGNMENT
                           | PERCENTAGE_INCREASE_ASSIGNMENT
                           | PERCENTAGE_DECREASE_ASSIGNMENT
                           | PERCENTAGE_VARIATION_ASSIGNMENT
                           | ADDITION_ASSIGNMENT
                           | SUBTRACTION_ASSIGNMENT
                           | LEFT_SHIFT_ASSIGNMENT
                           | SIGNED_RIGHT_SHIFT_ASSIGNMENT
                           | UNSIGNED_RIGHT_SHIFT_ASSIGNMENT
                           | NONE_COALESCING_ASSIGNMENT
                           | SHELL_PID_ASSIGNMENT
                           | SHELL_BKG_PID_ASSIGNMENT
                           ;


// --- IDENTIFIERS --------------------------------------------------

// Single identifiers

labelIdentifier : IDENTIFIER;

symbolIdentifier : IDENTIFIER;

typedIdentifier : symbolIdentifier type?;

qualifiedIdentifier : IDENTIFIER (DOT IDENTIFIER)*;

// Identifiers list

identifiers : IDENTIFIER (COMMA IDENTIFIER)*;

symbolIdentifiers : symbolIdentifier (COMMA symbolIdentifier)* ;

typedIdentifiers : typedIdentifier (COMMA typedIdentifier)*;

qualifiedIdentifiers : qualifiedIdentifier (COMMA qualifiedIdentifier)*;


// --- DATA TYPES ---------------------------------------------------

type : nativeType
     | nativeType posfixTypeWrapper
     | nativeType AND type
     | nativeType OR type
     | nativeType XOR type
     ;

nativeType : escalarType
           | compoundType
           | optionalType
           | metaType
           ;

posfixTypeWrapper : EXCLAMATION                    // ResultOption wrapper declaration
                  | QUESTION                       // MaybeOption  wrapper declaration
                  | QUESTION QUESTION              // EitherOption wrapper declaration
                  | PIPE RIGHT_ANGLE               // StreamOption warpper declaration
                  | EXCLAMATION QUESTION           // ResultOption wrapper of MaybeOption wrapper declaration
                  | EXCLAMATION QUESTION QUESTION  // ResultOption wrapper of EitherOption wrapper declaration
                  | EXCLAMATION PIPE RIGHT_ANGLE   // ResultOption wrapper of StreamOption warpper declaration
                  ;

// Escalar data types

escalarType : booleanType
            | numericType
            | temporalType 
            | characterType
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
            | numericDecimal
            | numericRatio
            | numericComplex
            | numericQuaternion
            ;

numericNatural : BYTE
               | NAT8
               | NAT16
               | NAT32
               | NAT64
               | NAT128
               | NAT
               | BIGNAT
               ;

numericInteger : INT8
               | INT16
               | INT32
               | INT64
               | INT128
               | INT
               | BIGINT
               ;

numericDecimal : DECIMAL8
               | DECIMAL16
               | DECIMAL32
               | DECIMAL64
               | DECIMAL128
               | DECIMAL
               | MONEY
               ;

numericReal : REAL8
            | REAL16
            | REAL32
            | REAL64
            | REAL128
            | REAL
            | BIGREAL
            ;

numericRatio : RATIO8
             | RATIO16
             | RATIO32
             | RATIO64
             | RATIO128
             | RATIO
             ;

numericComplex : COMPLEX32
               | COMPLEX64
               | COMPLEX128
               | COMPLEX
               ;

numericQuaternion : QUATERN32
                  | QUATERN64
                  | QUATERN128
                  | QUATERN
                  ;

temporalType : ELAPSE
             | DATE
             ;

characterType : ASCII
              | CHAR8
              | CHAR16
              | CHAR32
              | CHAR
              | WCHAR
              ;

// Compound data types

compoundType : sequenceType
             | compositeType
             | collectionType 
             ;

sequenceType : ANSI
             | STR8
             | STR16
             | STR32
             | STR
             | CSTR
             | WSTR
             | REGEX
             | BINARY
             ;

compositeType : RANGE
              | PAIR
              | TUPLE
              | INET
              | PATH
              | URI
              ;

collectionType : ARRAY
               | LIST
               | MAP
               | CHANNEL
               | VECTOR
               | MATRIX
               | SET
               | QUEUE
               | DEQUE
               | XML
               | TABLE
               | MEMO
               ;

// Optional data types

optionalType : RESULT
             | MAYBE
             | EITHER
             | STREAM
             ;

// Meta data types

metaType : ATOM
         | AUTO
         | SPAN
         | VIEW
         | VOID
         ;


// LITERALS ---------------------------------------------------------

literal : escalarLiteral
        | compoundLiteral
        | optionalLiteral
        ;

// Escalar literals

escalarLiteral : booleanLiteral
               | numericLiteral
               | elapseLiteral
               | dateLiteral
               | characterLiteral
               | sequenceLiteral
               ;

booleanLiteral : TRUE
               | FALSE
               ;

// Numeric literals

numericLiteral : NATURAL_LIT
               | INTEGER_LIT
               | DEC_LIT
               | REAL_LIT
               | RATIO_LIT
               | IMAGINARY_LIT
               | NONZERO parenthesizedExpression
               | ZERO
               | MINVALUE
               | MAXVALUE
               | NAN
               | POSITIVEINFINITY
               | NEGATIVEINFINITY
               ;

// Temporal literals

elapseLiteral : ATOM_DOT_LIT
              | ELAPSE_LIT
              ;  

dateLiteral : ATOM_DOT_LIT
            | LOCALDATE parenthesizedExpression?
            | LOCALDATETIME parenthesizedExpression?
            | OFFSETDATE parenthesizedExpression?
            | OFFSETDATETIME parenthesizedExpression?
            | ZONEDDATE parenthesizedExpression?
            | ZONEDDATETIME parenthesizedExpression?
            | TOMORROW
            | TODAY
            | NOW
            | YESTERDAY
            | EON
            | EPOCH
            ;

// Character literal

characterLiteral : ASCII_LIT
                 | CHAR_LIT
                 | WCHAR_LIT
                 | LETTER parenthesizedExpression
                 | DIGIT parenthesizedExpression
                 | PUNCTUATION parenthesizedExpression
                 | SYMBOL parenthesizedExpression
                 | SEPARATOR parenthesizedExpression
                 | NONPRINTABLE parenthesizedExpression
                 | NULL
                 ;

// Compound literals

compoundLiteral : sequenceLiteral
                | shellPathLiteral
                ;

// Sequence literals

sequenceLiteral : HEREDOC_LITERAL
                | REGULAR_EXPRESSION_LIT
                | WSTRING_LIT
                | STRING_LIT
                | ATOM_DOT_LIT
                | BINARY_LIT
                | NONBLANK parenthesizedExpression
                | BLANK
                ;

// Shell literals

shellPathLiteral : SHELL_PATH
                 | SHELL_STRING_PATH
                 ;

// Wrappers data types

optionalLiteral : resultLiteral
                | maybeLiteral
                | eitherLiteral
                | streamLiteral
                ;

resultLiteral : OKAY parenthesizedExpression
              | FAIL parenthesizedExpression
              ;

maybeLiteral : SOME parenthesizedExpression
             | NONE
             ;

eitherLiteral : YEA parenthesizedExpression
              | NAY parenthesizedExpression
              ;

streamLiteral : DATUM parenthesizedExpression
              | EOT
              ;

// Pre-declared values

predeclaredValue : THIS
                 | IOTA
                 ;


// --- EXPRESSION ---------------------------------------------------

operand : literal
        | predeclaredValue
        | qualifiedIdentifier
        ;

primaryExpression : operand
                  | LEFT_PARENTHESIS primaryExpression RIGHT_PARENTHESIS
                  | primaryExpression LEFT_BRACKET expressions RIGHT_BRACKET
                  | primaryExpression LEFT_BRACKET slicingRange RIGHT_BRACKET
                  | primaryExpression DOT primaryExpression
                  | primaryExpression SEMICOLON primaryExpression
                  | prefixUnaryOperator primaryExpression
                  | qualifiedIdentifier expression
                  | factScope FUNCTOR qualifiedIdentifier expressions
                  ;

slicingRange : intervalExpression
             | sliceExpression
             ;

intervalExpression : expression INTERVAL expression
                   | INTERVAL_RIGHT expression
                   | expression INTERVAL_LEFT
                   | intervalExpression INTERVAL_INCLUSIVE expression
                   ;

sliceExpression : expression COLON expression
                | COLON expression
                | expression COLON
                | sliceExpression COLON expression
                ;

factScope : ALL
          | ANY
          | LOT
          | NIL
          | ONE
          | TWO
          ;

expression : primaryExpression
           | parenthesizedExpression
           | expression binaryExponentialOperator expression
           | expression binaryMultiplicativeOperator expression
           | expression binaryAdditiveOperator expression
           | expression bitShiftOperator expression
           | expression binaryComparisonOperator expression
           | expression binaryRelationalOperator expression
           | expression binaryConditionalOperator expression
           | expression binaryConjunctionOperator expression
           | expression binaryExclusiveDisjunctionOperator expression
           | expression binaryDisjunctionOperator expression
           | expression binaryCoalescingOperator expression?
           | assignmentExpression
           | condicionalExpression
           | macroExpression
           | sos_Expression
           ;

sos_Expression : LEFT_PARENTHESIS statement RIGHT_PARENTHESIS;

assignmentExpression : primaryExpression assignmentOperator expression;

condicionalExpression : guardsExpression;

guardsExpression : guardClause+ guardDefault?;

guardClause : PIPE expression COLON expression;

guardDefault : PIPE expression;

macroExpression : macroCall+;

macroCall : qualifiedIdentifier expression*;

parenthesizedExpression : LEFT_PARENTHESIS expression RIGHT_PARENTHESIS;

primaryExpressions : primaryExpression (COMMA primaryExpression)*;

expressions : expression (COMMA expression)*;
