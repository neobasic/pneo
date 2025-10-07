// Generated from /home/dever/workspace/neobasic/ngne/antlr4/NeoBasicParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class NeoBasicParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LEFT_PARENTHESIS=1, RIGHT_PARENTHESIS=2, LEFT_BRACKET=3, RIGHT_BRACKET=4, 
		LEFT_CURLY=5, RIGHT_CURLY=6, LEFT_ANGLE=7, RIGHT_ANGLE=8, DOT=9, COMMA=10, 
		SEMICOLON=11, COLON=12, EXCLAMATION=13, QUESTION=14, APOSTROPHE=15, QUOTE=16, 
		BACKTICK=17, AT=18, HASH=19, DOLLAR=20, AMPERSAND=21, ASTERISK=22, SLASH=23, 
		DIVISION=24, PERCENT=25, BACKSLASH=26, TILDE=27, CARET=28, PIPE=29, UNDERSCORE=30, 
		EQUAL=31, PLUS=32, MINUS=33, ELLIPSIS=34, LAMBDA=35, DOUBLE_LEFT_BRACKET=36, 
		DOUBLE_RIGHT_BRACKET=37, DOUBLE_LEFT_CURLY=38, DOUBLE_RIGHT_CURLY=39, 
		DOUBLE_LEFT_ANGLE=40, DOUBLE_RIGHT_ANGLE=41, DOUBLE_EXCLAMATION=42, DOUBLE_QUESTION=43, 
		DOUBLE_COLON=44, DOUBLE_SEMICOLON=45, SPECIAL_ASSIGNMENT=46, INCREMENT=47, 
		DECREMENT=48, SQUARE_POWER=49, SQUARE_ROOT=50, FACTORIAL=51, BIT_NEGATION=52, 
		DEEP_CLONING=53, SORTING=54, QUOTIENT=55, PERCENTAGE_RATE=56, PERCENTAGE_AMOUNT=57, 
		PERCENTAGE_INCREASE=58, PERCENTAGE_DECREASE=59, PERCENTAGE_VARIATION=60, 
		BIT_CLEAR=61, UNSIGNED_RIGHT_SHIFT=62, DIVISIBLE_BY=63, NOT_DIVISIBLE_BY=64, 
		ELVIS_TEST=65, THREE_WAY_TEST=66, STRICT_EQUALITY=67, STRICT_INEQUALITY=68, 
		LOOSE_EQUALITY=69, LOOSE_INEQUALITY=70, LESS_OR_EQUALS=71, GREATER_OR_EQUALS=72, 
		ERROR_PROPAGATION_NONE_COALESCING=73, POP_ONE_ASSIGNMENT=74, PULL_ALL_ASSIGNMENT=75, 
		PIPE_ASSIGNMENT=76, DESTRUCTURING_ASSIGNMENT=77, ADDITION_ASSIGNMENT=78, 
		SUBTRACTION_ASSIGNMENT=79, MULTIPLICATION_ASSIGNMENT=80, REAL_DIVISION_ASSIGNMENT=81, 
		INTEGER_DIVISION_ASSIGNMENT=82, QUOTIENT_ASSIGNMENT=83, MODULO_ASSIGNMENT=84, 
		NTH_POWER_ASSIGNMENT=85, NTH_ROOT_ASSIGNMENT=86, PERCENTAGE_RATE_ASSIGNMENT=87, 
		PERCENTAGE_AMOUNT_ASSIGNMENT=88, PERCENTAGE_INCREASE_ASSIGNMENT=89, PERCENTAGE_DECREASE_ASSIGNMENT=90, 
		PERCENTAGE_VARIATION_ASSIGNMENT=91, BIT_AND_ASSIGNMENT=92, BIT_OR_ASSIGNMENT=93, 
		BIT_XOR_ASSIGNMENT=94, BIT_CLEAR_ASSIGNMENT=95, LEFT_SHIFT_ASSIGNMENT=96, 
		SIGNED_RIGHT_SHIFT_ASSIGNMENT=97, UNSIGNED_RIGHT_SHIFT_ASSIGNMENT=98, 
		NONE_COALESCING_ASSIGNMENT=99, SHELL_PID_ASSIGNMENT=100, SHELL_BKG_PID_ASSIGNMENT=101, 
		INTERVAL_INCLUSIVE=102, INTERVAL_LEFT_EXCLUSIVE=103, INTERVAL_RIGHT_EXCLUSIVE=104, 
		INTERVAL_EXCLUSIVE=105, INTERVAL=106, INTERVAL_LEFT=107, INTERVAL_RIGHT=108, 
		MIXIN=109, EXTENDS=110, NECK_RULE=111, MAPPING_ARROW=112, MONAD_BIND=113, 
		PIPELINE=114, COMMAND_SEQUENCE=115, COMMAND_SEQUENCE_OKAY=116, COMMAND_SEQUENCE_FAIL=117, 
		COMMAND_BACKGROUND=118, OUTPUT_REDIRECTION=119, APPEND_OUTPUT_REDIRECTION=120, 
		STDOUT_REDIRECTION=121, APPEND_STDOUT_REDIRECTION=122, STDERR_REDIRECTION=123, 
		APPEND_STDERR_REDIRECTION=124, REAL_LIT=125, DEC_REAL=126, HEX_REAL=127, 
		DEC_DECIMAL=128, HEX_DECIMAL=129, NATURAL_LIT=130, INTEGER_LIT=131, INTEGER_NUMBER=132, 
		DEC_VALUE=133, HEX_VALUE=134, OCT_VALUE=135, BIN_VALUE=136, ROM_VALUE=137, 
		IDENTIFIER=138, EOS=139, EOL=140, WSP=141, CONST=142, VAL=143, VAR=144, 
		COMPTIME=145, INLINE=146, STATIC=147, IOTA=148, TYPEOF=149, SIZEOF=150, 
		INSTANCEOF=151, IS=152, IN=153, BETWEEN=154, LIKE=155, NOT=156, AND=157, 
		OR=158, XOR=159, NAND=160, NOR=161, NXOR=162, BOOL8=163, BOOL16=164, BOOL32=165, 
		BOOL64=166, BOOL128=167, BOOL=168, NAT8=169, NAT16=170, NAT32=171, NAT64=172, 
		NAT128=173, BYTE=174, NAT=175, INT8=176, INT16=177, INT32=178, INT64=179, 
		INT128=180, INT=181, REAL8=182, REAL16=183, REAL32=184, REAL64=185, REAL128=186, 
		REAL=187, TRUE=188, FALSE=189, NONZERO=190, ZERO=191, MINVALUE=192, MAXVALUE=193, 
		NAN=194, POSITIVEINFINITY=195, NEGATIVEINFINITY=196, SCAN=197, ECHO=198;
	public static final int
		RULE_neoProgram = 0, RULE_instructionSentence = 1, RULE_declaration = 2, 
		RULE_constSentence = 3, RULE_constSpecifier = 4, RULE_constClause = 5, 
		RULE_constDeclare = 6, RULE_constDeclareSingle = 7, RULE_constDeclareMultiple = 8, 
		RULE_constDeclareParallel = 9, RULE_valSentence = 10, RULE_valSpecifier = 11, 
		RULE_valClause = 12, RULE_valDeclare = 13, RULE_valDeclareSingle = 14, 
		RULE_valDeclareMultiple = 15, RULE_valDeclareParallel = 16, RULE_varSentence = 17, 
		RULE_varSpecifier = 18, RULE_varClause = 19, RULE_varDeclare = 20, RULE_varDeclareSingle = 21, 
		RULE_varDeclareMultiple = 22, RULE_varDeclareParallel = 23, RULE_prefixUnaryOperator = 24, 
		RULE_posfixUnaryOperator = 25, RULE_unaryArithmeticOperator = 26, RULE_unaryBitwiseOperator = 27, 
		RULE_unaryLogicalOperator = 28, RULE_unarySpreadOperator = 29, RULE_unarySortOperator = 30, 
		RULE_unaryCloneOperator = 31, RULE_unaryMetaOperator = 32, RULE_binaryExponentialOperator = 33, 
		RULE_binaryMultiplicativeOperator = 34, RULE_binaryAdditiveOperator = 35, 
		RULE_bitShiftOperator = 36, RULE_bitConjunctionOperator = 37, RULE_bitExclusiveDisjunctionOperator = 38, 
		RULE_bitDisjunctionOperator = 39, RULE_binaryComparisonOperator = 40, 
		RULE_binaryRelationalOperator = 41, RULE_binaryConditionalOperator = 42, 
		RULE_binaryConjunctionOperator = 43, RULE_binaryExclusiveDisjunctionOperator = 44, 
		RULE_binaryDisjunctionOperator = 45, RULE_binaryCoalescingOperator = 46, 
		RULE_assignmentOperator = 47, RULE_singleAssignmentOperator = 48, RULE_multipleAssignmentOperator = 49, 
		RULE_compoundAssignmentOperator = 50, RULE_symbolIdentifier = 51, RULE_qualifiedIdentifier = 52, 
		RULE_identifiers = 53, RULE_symbolIdentifiers = 54, RULE_qualifiedIdentifiers = 55, 
		RULE_predeclaredValue = 56, RULE_literal = 57, RULE_escalarLiteral = 58, 
		RULE_booleanLiteral = 59, RULE_numericLiteral = 60, RULE_type = 61, RULE_nativeType = 62, 
		RULE_escalarType = 63, RULE_booleanType = 64, RULE_numericType = 65, RULE_numericNatural = 66, 
		RULE_numericInteger = 67, RULE_numericReal = 68, RULE_expressions = 69, 
		RULE_primaryExpressions = 70, RULE_primaryExpression = 71, RULE_operand = 72, 
		RULE_parenthesizedExpression = 73, RULE_expression = 74, RULE_assignmentExpression = 75;
	private static String[] makeRuleNames() {
		return new String[] {
			"neoProgram", "instructionSentence", "declaration", "constSentence", 
			"constSpecifier", "constClause", "constDeclare", "constDeclareSingle", 
			"constDeclareMultiple", "constDeclareParallel", "valSentence", "valSpecifier", 
			"valClause", "valDeclare", "valDeclareSingle", "valDeclareMultiple", 
			"valDeclareParallel", "varSentence", "varSpecifier", "varClause", "varDeclare", 
			"varDeclareSingle", "varDeclareMultiple", "varDeclareParallel", "prefixUnaryOperator", 
			"posfixUnaryOperator", "unaryArithmeticOperator", "unaryBitwiseOperator", 
			"unaryLogicalOperator", "unarySpreadOperator", "unarySortOperator", "unaryCloneOperator", 
			"unaryMetaOperator", "binaryExponentialOperator", "binaryMultiplicativeOperator", 
			"binaryAdditiveOperator", "bitShiftOperator", "bitConjunctionOperator", 
			"bitExclusiveDisjunctionOperator", "bitDisjunctionOperator", "binaryComparisonOperator", 
			"binaryRelationalOperator", "binaryConditionalOperator", "binaryConjunctionOperator", 
			"binaryExclusiveDisjunctionOperator", "binaryDisjunctionOperator", "binaryCoalescingOperator", 
			"assignmentOperator", "singleAssignmentOperator", "multipleAssignmentOperator", 
			"compoundAssignmentOperator", "symbolIdentifier", "qualifiedIdentifier", 
			"identifiers", "symbolIdentifiers", "qualifiedIdentifiers", "predeclaredValue", 
			"literal", "escalarLiteral", "booleanLiteral", "numericLiteral", "type", 
			"nativeType", "escalarType", "booleanType", "numericType", "numericNatural", 
			"numericInteger", "numericReal", "expressions", "primaryExpressions", 
			"primaryExpression", "operand", "parenthesizedExpression", "expression", 
			"assignmentExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'['", "']'", "'{'", "'}'", "'<'", "'>'", "'.'", 
			"','", "';'", "':'", "'!'", "'?'", "'''", "'\"'", "'`'", "'@'", "'#'", 
			"'$'", "'&'", "'*'", "'/'", "'\\u00F7'", "'%'", "'\\'", "'~'", "'^'", 
			"'|'", "'_'", "'='", "'+'", "'-'", "'...'", "'(\\'", "'[['", "']]'", 
			"'{{'", "'}}'", "'<<'", "'>>'", "'!!'", "'??'", "'::'", "';;'", "'~='", 
			"'++'", "'--'", "'**'", "'*/'", "'*!'", "'~~'", "'==='", "'^^'", "'%%'", 
			"'%/'", "'%*'", "'%+'", "'%-'", "'%^'", "'&~'", "'>>>'", "'?%'", "'!%'", 
			"'?:'", "'<=>'", "'=='", "'!='", "'~=='", "'~!='", "'<='", "'>='", "'!?'", 
			"'<-'", "'<<-'", "'<|'", "':='", "'+='", "'-='", "'*='", "'/='", "'\\u00F7='", 
			"'%%='", "'%='", "'**='", "'*/='", "'%/='", "'%*='", "'%+='", "'%-='", 
			"'%^\\u207C'", "'&='", "'|='", "'^='", "'&^='", "'<<='", "'>>='", "'>>>='", 
			"'??='", "'&&='", "'||='", "'..'", "'>..'", "'..<'", "'>..<'", null, 
			null, null, "'<>'", "'->'", "':-'", "'=>'", "'=>>'", "'|>'", "'&&'", 
			"'?&'", "'!&'", "'||'", "'&>'", "'&>>'", "'&1>'", "'&1>>'", "'&2>'", 
			"'&2>>'", null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "'const'", "'val'", "'var'", 
			"'comptime'", "'inline'", "'static'", "'iota'", "'typeof'", "'sizeof'", 
			"'instanceof'", "'is'", "'in'", "'between'", "'like'", "'not'", "'and'", 
			"'or'", "'xor'", "'nand'", "'nor'", "'nxor'", "'bool8'", "'bool16'", 
			"'bool32'", "'bool64'", "'bool128'", "'bool'", "'nat8'", "'nat16'", "'nat32'", 
			"'nat64'", "'nat128'", "'byte'", "'nat'", "'int8'", "'int16'", "'int32'", 
			"'int64'", "'int128'", "'int'", "'real8'", "'real16'", "'real32'", "'real64'", 
			"'real128'", "'real'", "'True'", "'False'", "'Nonzero'", "'Zero'", "'MinValue'", 
			"'MaxValue'", "'NaN'", "'PositiveInfinity'", "'NegativeInfinity'", "'scan'", 
			"'echo'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET", 
			"LEFT_CURLY", "RIGHT_CURLY", "LEFT_ANGLE", "RIGHT_ANGLE", "DOT", "COMMA", 
			"SEMICOLON", "COLON", "EXCLAMATION", "QUESTION", "APOSTROPHE", "QUOTE", 
			"BACKTICK", "AT", "HASH", "DOLLAR", "AMPERSAND", "ASTERISK", "SLASH", 
			"DIVISION", "PERCENT", "BACKSLASH", "TILDE", "CARET", "PIPE", "UNDERSCORE", 
			"EQUAL", "PLUS", "MINUS", "ELLIPSIS", "LAMBDA", "DOUBLE_LEFT_BRACKET", 
			"DOUBLE_RIGHT_BRACKET", "DOUBLE_LEFT_CURLY", "DOUBLE_RIGHT_CURLY", "DOUBLE_LEFT_ANGLE", 
			"DOUBLE_RIGHT_ANGLE", "DOUBLE_EXCLAMATION", "DOUBLE_QUESTION", "DOUBLE_COLON", 
			"DOUBLE_SEMICOLON", "SPECIAL_ASSIGNMENT", "INCREMENT", "DECREMENT", "SQUARE_POWER", 
			"SQUARE_ROOT", "FACTORIAL", "BIT_NEGATION", "DEEP_CLONING", "SORTING", 
			"QUOTIENT", "PERCENTAGE_RATE", "PERCENTAGE_AMOUNT", "PERCENTAGE_INCREASE", 
			"PERCENTAGE_DECREASE", "PERCENTAGE_VARIATION", "BIT_CLEAR", "UNSIGNED_RIGHT_SHIFT", 
			"DIVISIBLE_BY", "NOT_DIVISIBLE_BY", "ELVIS_TEST", "THREE_WAY_TEST", "STRICT_EQUALITY", 
			"STRICT_INEQUALITY", "LOOSE_EQUALITY", "LOOSE_INEQUALITY", "LESS_OR_EQUALS", 
			"GREATER_OR_EQUALS", "ERROR_PROPAGATION_NONE_COALESCING", "POP_ONE_ASSIGNMENT", 
			"PULL_ALL_ASSIGNMENT", "PIPE_ASSIGNMENT", "DESTRUCTURING_ASSIGNMENT", 
			"ADDITION_ASSIGNMENT", "SUBTRACTION_ASSIGNMENT", "MULTIPLICATION_ASSIGNMENT", 
			"REAL_DIVISION_ASSIGNMENT", "INTEGER_DIVISION_ASSIGNMENT", "QUOTIENT_ASSIGNMENT", 
			"MODULO_ASSIGNMENT", "NTH_POWER_ASSIGNMENT", "NTH_ROOT_ASSIGNMENT", "PERCENTAGE_RATE_ASSIGNMENT", 
			"PERCENTAGE_AMOUNT_ASSIGNMENT", "PERCENTAGE_INCREASE_ASSIGNMENT", "PERCENTAGE_DECREASE_ASSIGNMENT", 
			"PERCENTAGE_VARIATION_ASSIGNMENT", "BIT_AND_ASSIGNMENT", "BIT_OR_ASSIGNMENT", 
			"BIT_XOR_ASSIGNMENT", "BIT_CLEAR_ASSIGNMENT", "LEFT_SHIFT_ASSIGNMENT", 
			"SIGNED_RIGHT_SHIFT_ASSIGNMENT", "UNSIGNED_RIGHT_SHIFT_ASSIGNMENT", "NONE_COALESCING_ASSIGNMENT", 
			"SHELL_PID_ASSIGNMENT", "SHELL_BKG_PID_ASSIGNMENT", "INTERVAL_INCLUSIVE", 
			"INTERVAL_LEFT_EXCLUSIVE", "INTERVAL_RIGHT_EXCLUSIVE", "INTERVAL_EXCLUSIVE", 
			"INTERVAL", "INTERVAL_LEFT", "INTERVAL_RIGHT", "MIXIN", "EXTENDS", "NECK_RULE", 
			"MAPPING_ARROW", "MONAD_BIND", "PIPELINE", "COMMAND_SEQUENCE", "COMMAND_SEQUENCE_OKAY", 
			"COMMAND_SEQUENCE_FAIL", "COMMAND_BACKGROUND", "OUTPUT_REDIRECTION", 
			"APPEND_OUTPUT_REDIRECTION", "STDOUT_REDIRECTION", "APPEND_STDOUT_REDIRECTION", 
			"STDERR_REDIRECTION", "APPEND_STDERR_REDIRECTION", "REAL_LIT", "DEC_REAL", 
			"HEX_REAL", "DEC_DECIMAL", "HEX_DECIMAL", "NATURAL_LIT", "INTEGER_LIT", 
			"INTEGER_NUMBER", "DEC_VALUE", "HEX_VALUE", "OCT_VALUE", "BIN_VALUE", 
			"ROM_VALUE", "IDENTIFIER", "EOS", "EOL", "WSP", "CONST", "VAL", "VAR", 
			"COMPTIME", "INLINE", "STATIC", "IOTA", "TYPEOF", "SIZEOF", "INSTANCEOF", 
			"IS", "IN", "BETWEEN", "LIKE", "NOT", "AND", "OR", "XOR", "NAND", "NOR", 
			"NXOR", "BOOL8", "BOOL16", "BOOL32", "BOOL64", "BOOL128", "BOOL", "NAT8", 
			"NAT16", "NAT32", "NAT64", "NAT128", "BYTE", "NAT", "INT8", "INT16", 
			"INT32", "INT64", "INT128", "INT", "REAL8", "REAL16", "REAL32", "REAL64", 
			"REAL128", "REAL", "TRUE", "FALSE", "NONZERO", "ZERO", "MINVALUE", "MAXVALUE", 
			"NAN", "POSITIVEINFINITY", "NEGATIVEINFINITY", "SCAN", "ECHO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "NeoBasicParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public NeoBasicParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NeoProgramContext extends ParserRuleContext {
		public List<InstructionSentenceContext> instructionSentence() {
			return getRuleContexts(InstructionSentenceContext.class);
		}
		public InstructionSentenceContext instructionSentence(int i) {
			return getRuleContext(InstructionSentenceContext.class,i);
		}
		public List<TerminalNode> EOS() { return getTokens(NeoBasicParser.EOS); }
		public TerminalNode EOS(int i) {
			return getToken(NeoBasicParser.EOS, i);
		}
		public NeoProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_neoProgram; }
	}

	public final NeoProgramContext neoProgram() throws RecognitionException {
		NeoProgramContext _localctx = new NeoProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_neoProgram);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(152);
				instructionSentence();
				setState(153);
				match(EOS);
				}
				}
				setState(157); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( ((((_la - 142)) & ~0x3f) == 0 && ((1L << (_la - 142)) & 63L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstructionSentenceContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public InstructionSentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instructionSentence; }
	}

	public final InstructionSentenceContext instructionSentence() throws RecognitionException {
		InstructionSentenceContext _localctx = new InstructionSentenceContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instructionSentence);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			declaration();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public ConstSentenceContext constSentence() {
			return getRuleContext(ConstSentenceContext.class,0);
		}
		public ValSentenceContext valSentence() {
			return getRuleContext(ValSentenceContext.class,0);
		}
		public VarSentenceContext varSentence() {
			return getRuleContext(VarSentenceContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		try {
			setState(164);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(161);
				constSentence();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(162);
				valSentence();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(163);
				varSentence();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstSentenceContext extends ParserRuleContext {
		public ConstClauseContext constClause() {
			return getRuleContext(ConstClauseContext.class,0);
		}
		public List<ConstSpecifierContext> constSpecifier() {
			return getRuleContexts(ConstSpecifierContext.class);
		}
		public ConstSpecifierContext constSpecifier(int i) {
			return getRuleContext(ConstSpecifierContext.class,i);
		}
		public ConstSentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constSentence; }
	}

	public final ConstSentenceContext constSentence() throws RecognitionException {
		ConstSentenceContext _localctx = new ConstSentenceContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_constSentence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMPTIME || _la==INLINE) {
				{
				{
				setState(166);
				constSpecifier();
				}
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(172);
			constClause();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstSpecifierContext extends ParserRuleContext {
		public TerminalNode COMPTIME() { return getToken(NeoBasicParser.COMPTIME, 0); }
		public TerminalNode INLINE() { return getToken(NeoBasicParser.INLINE, 0); }
		public ConstSpecifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constSpecifier; }
	}

	public final ConstSpecifierContext constSpecifier() throws RecognitionException {
		ConstSpecifierContext _localctx = new ConstSpecifierContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_constSpecifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			_la = _input.LA(1);
			if ( !(_la==COMPTIME || _la==INLINE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstClauseContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(NeoBasicParser.CONST, 0); }
		public ConstDeclareContext constDeclare() {
			return getRuleContext(ConstDeclareContext.class,0);
		}
		public ConstClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constClause; }
	}

	public final ConstClauseContext constClause() throws RecognitionException {
		ConstClauseContext _localctx = new ConstClauseContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_constClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(CONST);
			setState(177);
			constDeclare();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstDeclareContext extends ParserRuleContext {
		public ConstDeclareSingleContext constDeclareSingle() {
			return getRuleContext(ConstDeclareSingleContext.class,0);
		}
		public ConstDeclareMultipleContext constDeclareMultiple() {
			return getRuleContext(ConstDeclareMultipleContext.class,0);
		}
		public ConstDeclareParallelContext constDeclareParallel() {
			return getRuleContext(ConstDeclareParallelContext.class,0);
		}
		public ConstDeclareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constDeclare; }
	}

	public final ConstDeclareContext constDeclare() throws RecognitionException {
		ConstDeclareContext _localctx = new ConstDeclareContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_constDeclare);
		try {
			setState(182);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(179);
				constDeclareSingle();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
				constDeclareMultiple();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(181);
				constDeclareParallel();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstDeclareSingleContext extends ParserRuleContext {
		public SymbolIdentifierContext symbolIdentifier() {
			return getRuleContext(SymbolIdentifierContext.class,0);
		}
		public SingleAssignmentOperatorContext singleAssignmentOperator() {
			return getRuleContext(SingleAssignmentOperatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ConstDeclareSingleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constDeclareSingle; }
	}

	public final ConstDeclareSingleContext constDeclareSingle() throws RecognitionException {
		ConstDeclareSingleContext _localctx = new ConstDeclareSingleContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_constDeclareSingle);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			symbolIdentifier();
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 163)) & ~0x3f) == 0 && ((1L << (_la - 163)) & 33554431L) != 0)) {
				{
				setState(185);
				type();
				}
			}

			setState(188);
			singleAssignmentOperator();
			setState(189);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstDeclareMultipleContext extends ParserRuleContext {
		public List<ConstDeclareSingleContext> constDeclareSingle() {
			return getRuleContexts(ConstDeclareSingleContext.class);
		}
		public ConstDeclareSingleContext constDeclareSingle(int i) {
			return getRuleContext(ConstDeclareSingleContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public ConstDeclareMultipleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constDeclareMultiple; }
	}

	public final ConstDeclareMultipleContext constDeclareMultiple() throws RecognitionException {
		ConstDeclareMultipleContext _localctx = new ConstDeclareMultipleContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_constDeclareMultiple);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			constDeclareSingle();
			setState(194); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(192);
				match(COMMA);
				setState(193);
				constDeclareSingle();
				}
				}
				setState(196); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstDeclareParallelContext extends ParserRuleContext {
		public SymbolIdentifiersContext symbolIdentifiers() {
			return getRuleContext(SymbolIdentifiersContext.class,0);
		}
		public MultipleAssignmentOperatorContext multipleAssignmentOperator() {
			return getRuleContext(MultipleAssignmentOperatorContext.class,0);
		}
		public ExpressionsContext expressions() {
			return getRuleContext(ExpressionsContext.class,0);
		}
		public ConstDeclareParallelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constDeclareParallel; }
	}

	public final ConstDeclareParallelContext constDeclareParallel() throws RecognitionException {
		ConstDeclareParallelContext _localctx = new ConstDeclareParallelContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_constDeclareParallel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			symbolIdentifiers();
			setState(199);
			multipleAssignmentOperator();
			setState(200);
			expressions();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValSentenceContext extends ParserRuleContext {
		public ValClauseContext valClause() {
			return getRuleContext(ValClauseContext.class,0);
		}
		public List<ValSpecifierContext> valSpecifier() {
			return getRuleContexts(ValSpecifierContext.class);
		}
		public ValSpecifierContext valSpecifier(int i) {
			return getRuleContext(ValSpecifierContext.class,i);
		}
		public ValSentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valSentence; }
	}

	public final ValSentenceContext valSentence() throws RecognitionException {
		ValSentenceContext _localctx = new ValSentenceContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_valSentence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 145)) & ~0x3f) == 0 && ((1L << (_la - 145)) & 7L) != 0)) {
				{
				{
				setState(202);
				valSpecifier();
				}
				}
				setState(207);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(208);
			valClause();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValSpecifierContext extends ParserRuleContext {
		public TerminalNode COMPTIME() { return getToken(NeoBasicParser.COMPTIME, 0); }
		public TerminalNode STATIC() { return getToken(NeoBasicParser.STATIC, 0); }
		public TerminalNode INLINE() { return getToken(NeoBasicParser.INLINE, 0); }
		public ValSpecifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valSpecifier; }
	}

	public final ValSpecifierContext valSpecifier() throws RecognitionException {
		ValSpecifierContext _localctx = new ValSpecifierContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_valSpecifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			_la = _input.LA(1);
			if ( !(((((_la - 145)) & ~0x3f) == 0 && ((1L << (_la - 145)) & 7L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValClauseContext extends ParserRuleContext {
		public TerminalNode VAL() { return getToken(NeoBasicParser.VAL, 0); }
		public VarDeclareContext varDeclare() {
			return getRuleContext(VarDeclareContext.class,0);
		}
		public ValClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valClause; }
	}

	public final ValClauseContext valClause() throws RecognitionException {
		ValClauseContext _localctx = new ValClauseContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_valClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(VAL);
			setState(213);
			varDeclare();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValDeclareContext extends ParserRuleContext {
		public ValDeclareSingleContext valDeclareSingle() {
			return getRuleContext(ValDeclareSingleContext.class,0);
		}
		public ValDeclareMultipleContext valDeclareMultiple() {
			return getRuleContext(ValDeclareMultipleContext.class,0);
		}
		public ValDeclareParallelContext valDeclareParallel() {
			return getRuleContext(ValDeclareParallelContext.class,0);
		}
		public ValDeclareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valDeclare; }
	}

	public final ValDeclareContext valDeclare() throws RecognitionException {
		ValDeclareContext _localctx = new ValDeclareContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_valDeclare);
		try {
			setState(218);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				valDeclareSingle();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(216);
				valDeclareMultiple();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(217);
				valDeclareParallel();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValDeclareSingleContext extends ParserRuleContext {
		public SymbolIdentifierContext symbolIdentifier() {
			return getRuleContext(SymbolIdentifierContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public SingleAssignmentOperatorContext singleAssignmentOperator() {
			return getRuleContext(SingleAssignmentOperatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ValDeclareSingleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valDeclareSingle; }
	}

	public final ValDeclareSingleContext valDeclareSingle() throws RecognitionException {
		ValDeclareSingleContext _localctx = new ValDeclareSingleContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_valDeclareSingle);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			symbolIdentifier();
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 163)) & ~0x3f) == 0 && ((1L << (_la - 163)) & 33554431L) != 0)) {
				{
				setState(221);
				type();
				}
			}

			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 31)) & ~0x3f) == 0 && ((1L << (_la - 31)) & 61572651155457L) != 0)) {
				{
				setState(224);
				singleAssignmentOperator();
				setState(225);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValDeclareMultipleContext extends ParserRuleContext {
		public List<ValDeclareSingleContext> valDeclareSingle() {
			return getRuleContexts(ValDeclareSingleContext.class);
		}
		public ValDeclareSingleContext valDeclareSingle(int i) {
			return getRuleContext(ValDeclareSingleContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public ValDeclareMultipleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valDeclareMultiple; }
	}

	public final ValDeclareMultipleContext valDeclareMultiple() throws RecognitionException {
		ValDeclareMultipleContext _localctx = new ValDeclareMultipleContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_valDeclareMultiple);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			valDeclareSingle();
			setState(232); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(230);
				match(COMMA);
				setState(231);
				valDeclareSingle();
				}
				}
				setState(234); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValDeclareParallelContext extends ParserRuleContext {
		public SymbolIdentifiersContext symbolIdentifiers() {
			return getRuleContext(SymbolIdentifiersContext.class,0);
		}
		public MultipleAssignmentOperatorContext multipleAssignmentOperator() {
			return getRuleContext(MultipleAssignmentOperatorContext.class,0);
		}
		public ExpressionsContext expressions() {
			return getRuleContext(ExpressionsContext.class,0);
		}
		public ValDeclareParallelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valDeclareParallel; }
	}

	public final ValDeclareParallelContext valDeclareParallel() throws RecognitionException {
		ValDeclareParallelContext _localctx = new ValDeclareParallelContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_valDeclareParallel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			symbolIdentifiers();
			setState(237);
			multipleAssignmentOperator();
			setState(238);
			expressions();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarSentenceContext extends ParserRuleContext {
		public VarClauseContext varClause() {
			return getRuleContext(VarClauseContext.class,0);
		}
		public List<VarSpecifierContext> varSpecifier() {
			return getRuleContexts(VarSpecifierContext.class);
		}
		public VarSpecifierContext varSpecifier(int i) {
			return getRuleContext(VarSpecifierContext.class,i);
		}
		public VarSentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varSentence; }
	}

	public final VarSentenceContext varSentence() throws RecognitionException {
		VarSentenceContext _localctx = new VarSentenceContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_varSentence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 145)) & ~0x3f) == 0 && ((1L << (_la - 145)) & 7L) != 0)) {
				{
				{
				setState(240);
				varSpecifier();
				}
				}
				setState(245);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(246);
			varClause();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarSpecifierContext extends ParserRuleContext {
		public TerminalNode COMPTIME() { return getToken(NeoBasicParser.COMPTIME, 0); }
		public TerminalNode STATIC() { return getToken(NeoBasicParser.STATIC, 0); }
		public TerminalNode INLINE() { return getToken(NeoBasicParser.INLINE, 0); }
		public VarSpecifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varSpecifier; }
	}

	public final VarSpecifierContext varSpecifier() throws RecognitionException {
		VarSpecifierContext _localctx = new VarSpecifierContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_varSpecifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_la = _input.LA(1);
			if ( !(((((_la - 145)) & ~0x3f) == 0 && ((1L << (_la - 145)) & 7L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarClauseContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(NeoBasicParser.VAR, 0); }
		public VarDeclareContext varDeclare() {
			return getRuleContext(VarDeclareContext.class,0);
		}
		public VarClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varClause; }
	}

	public final VarClauseContext varClause() throws RecognitionException {
		VarClauseContext _localctx = new VarClauseContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_varClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(VAR);
			setState(251);
			varDeclare();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclareContext extends ParserRuleContext {
		public VarDeclareSingleContext varDeclareSingle() {
			return getRuleContext(VarDeclareSingleContext.class,0);
		}
		public VarDeclareMultipleContext varDeclareMultiple() {
			return getRuleContext(VarDeclareMultipleContext.class,0);
		}
		public VarDeclareParallelContext varDeclareParallel() {
			return getRuleContext(VarDeclareParallelContext.class,0);
		}
		public VarDeclareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclare; }
	}

	public final VarDeclareContext varDeclare() throws RecognitionException {
		VarDeclareContext _localctx = new VarDeclareContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_varDeclare);
		try {
			setState(256);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(253);
				varDeclareSingle();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(254);
				varDeclareMultiple();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(255);
				varDeclareParallel();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclareSingleContext extends ParserRuleContext {
		public SymbolIdentifierContext symbolIdentifier() {
			return getRuleContext(SymbolIdentifierContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public SingleAssignmentOperatorContext singleAssignmentOperator() {
			return getRuleContext(SingleAssignmentOperatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public VarDeclareSingleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclareSingle; }
	}

	public final VarDeclareSingleContext varDeclareSingle() throws RecognitionException {
		VarDeclareSingleContext _localctx = new VarDeclareSingleContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_varDeclareSingle);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			symbolIdentifier();
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 163)) & ~0x3f) == 0 && ((1L << (_la - 163)) & 33554431L) != 0)) {
				{
				setState(259);
				type();
				}
			}

			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 31)) & ~0x3f) == 0 && ((1L << (_la - 31)) & 61572651155457L) != 0)) {
				{
				setState(262);
				singleAssignmentOperator();
				setState(263);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclareMultipleContext extends ParserRuleContext {
		public List<VarDeclareSingleContext> varDeclareSingle() {
			return getRuleContexts(VarDeclareSingleContext.class);
		}
		public VarDeclareSingleContext varDeclareSingle(int i) {
			return getRuleContext(VarDeclareSingleContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public VarDeclareMultipleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclareMultiple; }
	}

	public final VarDeclareMultipleContext varDeclareMultiple() throws RecognitionException {
		VarDeclareMultipleContext _localctx = new VarDeclareMultipleContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_varDeclareMultiple);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			varDeclareSingle();
			setState(270); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(268);
				match(COMMA);
				setState(269);
				varDeclareSingle();
				}
				}
				setState(272); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclareParallelContext extends ParserRuleContext {
		public SymbolIdentifiersContext symbolIdentifiers() {
			return getRuleContext(SymbolIdentifiersContext.class,0);
		}
		public MultipleAssignmentOperatorContext multipleAssignmentOperator() {
			return getRuleContext(MultipleAssignmentOperatorContext.class,0);
		}
		public ExpressionsContext expressions() {
			return getRuleContext(ExpressionsContext.class,0);
		}
		public VarDeclareParallelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclareParallel; }
	}

	public final VarDeclareParallelContext varDeclareParallel() throws RecognitionException {
		VarDeclareParallelContext _localctx = new VarDeclareParallelContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_varDeclareParallel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			symbolIdentifiers();
			setState(275);
			multipleAssignmentOperator();
			setState(276);
			expressions();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrefixUnaryOperatorContext extends ParserRuleContext {
		public UnaryArithmeticOperatorContext unaryArithmeticOperator() {
			return getRuleContext(UnaryArithmeticOperatorContext.class,0);
		}
		public UnaryBitwiseOperatorContext unaryBitwiseOperator() {
			return getRuleContext(UnaryBitwiseOperatorContext.class,0);
		}
		public UnaryLogicalOperatorContext unaryLogicalOperator() {
			return getRuleContext(UnaryLogicalOperatorContext.class,0);
		}
		public UnarySpreadOperatorContext unarySpreadOperator() {
			return getRuleContext(UnarySpreadOperatorContext.class,0);
		}
		public UnarySortOperatorContext unarySortOperator() {
			return getRuleContext(UnarySortOperatorContext.class,0);
		}
		public UnaryMetaOperatorContext unaryMetaOperator() {
			return getRuleContext(UnaryMetaOperatorContext.class,0);
		}
		public PrefixUnaryOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prefixUnaryOperator; }
	}

	public final PrefixUnaryOperatorContext prefixUnaryOperator() throws RecognitionException {
		PrefixUnaryOperatorContext _localctx = new PrefixUnaryOperatorContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_prefixUnaryOperator);
		try {
			setState(284);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case INCREMENT:
			case DECREMENT:
			case SQUARE_POWER:
			case SQUARE_ROOT:
			case FACTORIAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(278);
				unaryArithmeticOperator();
				}
				break;
			case TILDE:
			case BIT_NEGATION:
				enterOuterAlt(_localctx, 2);
				{
				setState(279);
				unaryBitwiseOperator();
				}
				break;
			case NOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(280);
				unaryLogicalOperator();
				}
				break;
			case ELLIPSIS:
				enterOuterAlt(_localctx, 4);
				{
				setState(281);
				unarySpreadOperator();
				}
				break;
			case CARET:
			case SORTING:
				enterOuterAlt(_localctx, 5);
				{
				setState(282);
				unarySortOperator();
				}
				break;
			case TYPEOF:
			case SIZEOF:
				enterOuterAlt(_localctx, 6);
				{
				setState(283);
				unaryMetaOperator();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PosfixUnaryOperatorContext extends ParserRuleContext {
		public UnarySortOperatorContext unarySortOperator() {
			return getRuleContext(UnarySortOperatorContext.class,0);
		}
		public UnaryCloneOperatorContext unaryCloneOperator() {
			return getRuleContext(UnaryCloneOperatorContext.class,0);
		}
		public PosfixUnaryOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_posfixUnaryOperator; }
	}

	public final PosfixUnaryOperatorContext posfixUnaryOperator() throws RecognitionException {
		PosfixUnaryOperatorContext _localctx = new PosfixUnaryOperatorContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_posfixUnaryOperator);
		try {
			setState(288);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CARET:
			case SORTING:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				unarySortOperator();
				}
				break;
			case EQUAL:
			case DEEP_CLONING:
				enterOuterAlt(_localctx, 2);
				{
				setState(287);
				unaryCloneOperator();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryArithmeticOperatorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(NeoBasicParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(NeoBasicParser.MINUS, 0); }
		public TerminalNode INCREMENT() { return getToken(NeoBasicParser.INCREMENT, 0); }
		public TerminalNode DECREMENT() { return getToken(NeoBasicParser.DECREMENT, 0); }
		public TerminalNode SQUARE_POWER() { return getToken(NeoBasicParser.SQUARE_POWER, 0); }
		public TerminalNode SQUARE_ROOT() { return getToken(NeoBasicParser.SQUARE_ROOT, 0); }
		public TerminalNode FACTORIAL() { return getToken(NeoBasicParser.FACTORIAL, 0); }
		public UnaryArithmeticOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryArithmeticOperator; }
	}

	public final UnaryArithmeticOperatorContext unaryArithmeticOperator() throws RecognitionException {
		UnaryArithmeticOperatorContext _localctx = new UnaryArithmeticOperatorContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_unaryArithmeticOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4362875023917056L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryBitwiseOperatorContext extends ParserRuleContext {
		public TerminalNode TILDE() { return getToken(NeoBasicParser.TILDE, 0); }
		public TerminalNode BIT_NEGATION() { return getToken(NeoBasicParser.BIT_NEGATION, 0); }
		public UnaryBitwiseOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryBitwiseOperator; }
	}

	public final UnaryBitwiseOperatorContext unaryBitwiseOperator() throws RecognitionException {
		UnaryBitwiseOperatorContext _localctx = new UnaryBitwiseOperatorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_unaryBitwiseOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			_la = _input.LA(1);
			if ( !(_la==TILDE || _la==BIT_NEGATION) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryLogicalOperatorContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(NeoBasicParser.NOT, 0); }
		public UnaryLogicalOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryLogicalOperator; }
	}

	public final UnaryLogicalOperatorContext unaryLogicalOperator() throws RecognitionException {
		UnaryLogicalOperatorContext _localctx = new UnaryLogicalOperatorContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_unaryLogicalOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			match(NOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnarySpreadOperatorContext extends ParserRuleContext {
		public TerminalNode ELLIPSIS() { return getToken(NeoBasicParser.ELLIPSIS, 0); }
		public UnarySpreadOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unarySpreadOperator; }
	}

	public final UnarySpreadOperatorContext unarySpreadOperator() throws RecognitionException {
		UnarySpreadOperatorContext _localctx = new UnarySpreadOperatorContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_unarySpreadOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			match(ELLIPSIS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnarySortOperatorContext extends ParserRuleContext {
		public TerminalNode CARET() { return getToken(NeoBasicParser.CARET, 0); }
		public TerminalNode SORTING() { return getToken(NeoBasicParser.SORTING, 0); }
		public UnarySortOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unarySortOperator; }
	}

	public final UnarySortOperatorContext unarySortOperator() throws RecognitionException {
		UnarySortOperatorContext _localctx = new UnarySortOperatorContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_unarySortOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			_la = _input.LA(1);
			if ( !(_la==CARET || _la==SORTING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryCloneOperatorContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(NeoBasicParser.EQUAL, 0); }
		public TerminalNode DEEP_CLONING() { return getToken(NeoBasicParser.DEEP_CLONING, 0); }
		public UnaryCloneOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryCloneOperator; }
	}

	public final UnaryCloneOperatorContext unaryCloneOperator() throws RecognitionException {
		UnaryCloneOperatorContext _localctx = new UnaryCloneOperatorContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_unaryCloneOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			_la = _input.LA(1);
			if ( !(_la==EQUAL || _la==DEEP_CLONING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryMetaOperatorContext extends ParserRuleContext {
		public TerminalNode TYPEOF() { return getToken(NeoBasicParser.TYPEOF, 0); }
		public TerminalNode SIZEOF() { return getToken(NeoBasicParser.SIZEOF, 0); }
		public UnaryMetaOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryMetaOperator; }
	}

	public final UnaryMetaOperatorContext unaryMetaOperator() throws RecognitionException {
		UnaryMetaOperatorContext _localctx = new UnaryMetaOperatorContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_unaryMetaOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			_la = _input.LA(1);
			if ( !(_la==TYPEOF || _la==SIZEOF) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryExponentialOperatorContext extends ParserRuleContext {
		public TerminalNode SQUARE_POWER() { return getToken(NeoBasicParser.SQUARE_POWER, 0); }
		public TerminalNode SQUARE_ROOT() { return getToken(NeoBasicParser.SQUARE_ROOT, 0); }
		public BinaryExponentialOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryExponentialOperator; }
	}

	public final BinaryExponentialOperatorContext binaryExponentialOperator() throws RecognitionException {
		BinaryExponentialOperatorContext _localctx = new BinaryExponentialOperatorContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_binaryExponentialOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			_la = _input.LA(1);
			if ( !(_la==SQUARE_POWER || _la==SQUARE_ROOT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryMultiplicativeOperatorContext extends ParserRuleContext {
		public TerminalNode ASTERISK() { return getToken(NeoBasicParser.ASTERISK, 0); }
		public TerminalNode SLASH() { return getToken(NeoBasicParser.SLASH, 0); }
		public TerminalNode DIVISION() { return getToken(NeoBasicParser.DIVISION, 0); }
		public TerminalNode QUOTIENT() { return getToken(NeoBasicParser.QUOTIENT, 0); }
		public TerminalNode PERCENT() { return getToken(NeoBasicParser.PERCENT, 0); }
		public TerminalNode PERCENTAGE_RATE() { return getToken(NeoBasicParser.PERCENTAGE_RATE, 0); }
		public TerminalNode PERCENTAGE_AMOUNT() { return getToken(NeoBasicParser.PERCENTAGE_AMOUNT, 0); }
		public TerminalNode PERCENTAGE_INCREASE() { return getToken(NeoBasicParser.PERCENTAGE_INCREASE, 0); }
		public TerminalNode PERCENTAGE_DECREASE() { return getToken(NeoBasicParser.PERCENTAGE_DECREASE, 0); }
		public TerminalNode PERCENTAGE_VARIATION() { return getToken(NeoBasicParser.PERCENTAGE_VARIATION, 0); }
		public BinaryMultiplicativeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryMultiplicativeOperator; }
	}

	public final BinaryMultiplicativeOperatorContext binaryMultiplicativeOperator() throws RecognitionException {
		BinaryMultiplicativeOperatorContext _localctx = new BinaryMultiplicativeOperatorContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_binaryMultiplicativeOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2269814212257644544L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryAdditiveOperatorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(NeoBasicParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(NeoBasicParser.MINUS, 0); }
		public BinaryAdditiveOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryAdditiveOperator; }
	}

	public final BinaryAdditiveOperatorContext binaryAdditiveOperator() throws RecognitionException {
		BinaryAdditiveOperatorContext _localctx = new BinaryAdditiveOperatorContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_binaryAdditiveOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitShiftOperatorContext extends ParserRuleContext {
		public TerminalNode DOUBLE_LEFT_ANGLE() { return getToken(NeoBasicParser.DOUBLE_LEFT_ANGLE, 0); }
		public TerminalNode DOUBLE_RIGHT_ANGLE() { return getToken(NeoBasicParser.DOUBLE_RIGHT_ANGLE, 0); }
		public TerminalNode UNSIGNED_RIGHT_SHIFT() { return getToken(NeoBasicParser.UNSIGNED_RIGHT_SHIFT, 0); }
		public BitShiftOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitShiftOperator; }
	}

	public final BitShiftOperatorContext bitShiftOperator() throws RecognitionException {
		BitShiftOperatorContext _localctx = new BitShiftOperatorContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_bitShiftOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4611689316962271232L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitConjunctionOperatorContext extends ParserRuleContext {
		public TerminalNode AMPERSAND() { return getToken(NeoBasicParser.AMPERSAND, 0); }
		public TerminalNode BIT_CLEAR() { return getToken(NeoBasicParser.BIT_CLEAR, 0); }
		public BitConjunctionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitConjunctionOperator; }
	}

	public final BitConjunctionOperatorContext bitConjunctionOperator() throws RecognitionException {
		BitConjunctionOperatorContext _localctx = new BitConjunctionOperatorContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_bitConjunctionOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			_la = _input.LA(1);
			if ( !(_la==AMPERSAND || _la==BIT_CLEAR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitExclusiveDisjunctionOperatorContext extends ParserRuleContext {
		public TerminalNode CARET() { return getToken(NeoBasicParser.CARET, 0); }
		public BitExclusiveDisjunctionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitExclusiveDisjunctionOperator; }
	}

	public final BitExclusiveDisjunctionOperatorContext bitExclusiveDisjunctionOperator() throws RecognitionException {
		BitExclusiveDisjunctionOperatorContext _localctx = new BitExclusiveDisjunctionOperatorContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_bitExclusiveDisjunctionOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(CARET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitDisjunctionOperatorContext extends ParserRuleContext {
		public TerminalNode PIPE() { return getToken(NeoBasicParser.PIPE, 0); }
		public BitDisjunctionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitDisjunctionOperator; }
	}

	public final BitDisjunctionOperatorContext bitDisjunctionOperator() throws RecognitionException {
		BitDisjunctionOperatorContext _localctx = new BitDisjunctionOperatorContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_bitDisjunctionOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(316);
			match(PIPE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryComparisonOperatorContext extends ParserRuleContext {
		public TerminalNode ELVIS_TEST() { return getToken(NeoBasicParser.ELVIS_TEST, 0); }
		public TerminalNode THREE_WAY_TEST() { return getToken(NeoBasicParser.THREE_WAY_TEST, 0); }
		public BinaryComparisonOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryComparisonOperator; }
	}

	public final BinaryComparisonOperatorContext binaryComparisonOperator() throws RecognitionException {
		BinaryComparisonOperatorContext _localctx = new BinaryComparisonOperatorContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_binaryComparisonOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			_la = _input.LA(1);
			if ( !(_la==ELVIS_TEST || _la==THREE_WAY_TEST) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryRelationalOperatorContext extends ParserRuleContext {
		public TerminalNode STRICT_EQUALITY() { return getToken(NeoBasicParser.STRICT_EQUALITY, 0); }
		public TerminalNode STRICT_INEQUALITY() { return getToken(NeoBasicParser.STRICT_INEQUALITY, 0); }
		public TerminalNode LOOSE_EQUALITY() { return getToken(NeoBasicParser.LOOSE_EQUALITY, 0); }
		public TerminalNode LOOSE_INEQUALITY() { return getToken(NeoBasicParser.LOOSE_INEQUALITY, 0); }
		public TerminalNode LEFT_ANGLE() { return getToken(NeoBasicParser.LEFT_ANGLE, 0); }
		public TerminalNode LESS_OR_EQUALS() { return getToken(NeoBasicParser.LESS_OR_EQUALS, 0); }
		public TerminalNode RIGHT_ANGLE() { return getToken(NeoBasicParser.RIGHT_ANGLE, 0); }
		public TerminalNode GREATER_OR_EQUALS() { return getToken(NeoBasicParser.GREATER_OR_EQUALS, 0); }
		public BinaryRelationalOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryRelationalOperator; }
	}

	public final BinaryRelationalOperatorContext binaryRelationalOperator() throws RecognitionException {
		BinaryRelationalOperatorContext _localctx = new BinaryRelationalOperatorContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_binaryRelationalOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
			_la = _input.LA(1);
			if ( !(_la==LEFT_ANGLE || _la==RIGHT_ANGLE || ((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & 63L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryConditionalOperatorContext extends ParserRuleContext {
		public TerminalNode IS() { return getToken(NeoBasicParser.IS, 0); }
		public TerminalNode NOT() { return getToken(NeoBasicParser.NOT, 0); }
		public TerminalNode IN() { return getToken(NeoBasicParser.IN, 0); }
		public TerminalNode BETWEEN() { return getToken(NeoBasicParser.BETWEEN, 0); }
		public TerminalNode LIKE() { return getToken(NeoBasicParser.LIKE, 0); }
		public TerminalNode DIVISIBLE_BY() { return getToken(NeoBasicParser.DIVISIBLE_BY, 0); }
		public TerminalNode NOT_DIVISIBLE_BY() { return getToken(NeoBasicParser.NOT_DIVISIBLE_BY, 0); }
		public BinaryConditionalOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryConditionalOperator; }
	}

	public final BinaryConditionalOperatorContext binaryConditionalOperator() throws RecognitionException {
		BinaryConditionalOperatorContext _localctx = new BinaryConditionalOperatorContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_binaryConditionalOperator);
		try {
			setState(336);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(322);
				match(IS);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(323);
				match(IS);
				setState(324);
				match(NOT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(325);
				match(IN);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(326);
				match(NOT);
				setState(327);
				match(IN);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(328);
				match(BETWEEN);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(329);
				match(NOT);
				setState(330);
				match(BETWEEN);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(331);
				match(LIKE);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(332);
				match(NOT);
				setState(333);
				match(LIKE);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(334);
				match(DIVISIBLE_BY);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(335);
				match(NOT_DIVISIBLE_BY);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryConjunctionOperatorContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(NeoBasicParser.AND, 0); }
		public TerminalNode NAND() { return getToken(NeoBasicParser.NAND, 0); }
		public BinaryConjunctionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryConjunctionOperator; }
	}

	public final BinaryConjunctionOperatorContext binaryConjunctionOperator() throws RecognitionException {
		BinaryConjunctionOperatorContext _localctx = new BinaryConjunctionOperatorContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_binaryConjunctionOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(338);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==NAND) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryExclusiveDisjunctionOperatorContext extends ParserRuleContext {
		public TerminalNode XOR() { return getToken(NeoBasicParser.XOR, 0); }
		public TerminalNode NXOR() { return getToken(NeoBasicParser.NXOR, 0); }
		public BinaryExclusiveDisjunctionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryExclusiveDisjunctionOperator; }
	}

	public final BinaryExclusiveDisjunctionOperatorContext binaryExclusiveDisjunctionOperator() throws RecognitionException {
		BinaryExclusiveDisjunctionOperatorContext _localctx = new BinaryExclusiveDisjunctionOperatorContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_binaryExclusiveDisjunctionOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(340);
			_la = _input.LA(1);
			if ( !(_la==XOR || _la==NXOR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryDisjunctionOperatorContext extends ParserRuleContext {
		public TerminalNode OR() { return getToken(NeoBasicParser.OR, 0); }
		public TerminalNode NOR() { return getToken(NeoBasicParser.NOR, 0); }
		public BinaryDisjunctionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryDisjunctionOperator; }
	}

	public final BinaryDisjunctionOperatorContext binaryDisjunctionOperator() throws RecognitionException {
		BinaryDisjunctionOperatorContext _localctx = new BinaryDisjunctionOperatorContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_binaryDisjunctionOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(342);
			_la = _input.LA(1);
			if ( !(_la==OR || _la==NOR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryCoalescingOperatorContext extends ParserRuleContext {
		public TerminalNode EXCLAMATION() { return getToken(NeoBasicParser.EXCLAMATION, 0); }
		public TerminalNode DOUBLE_EXCLAMATION() { return getToken(NeoBasicParser.DOUBLE_EXCLAMATION, 0); }
		public TerminalNode ERROR_PROPAGATION_NONE_COALESCING() { return getToken(NeoBasicParser.ERROR_PROPAGATION_NONE_COALESCING, 0); }
		public TerminalNode QUESTION() { return getToken(NeoBasicParser.QUESTION, 0); }
		public TerminalNode DOUBLE_QUESTION() { return getToken(NeoBasicParser.DOUBLE_QUESTION, 0); }
		public BinaryCoalescingOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryCoalescingOperator; }
	}

	public final BinaryCoalescingOperatorContext binaryCoalescingOperator() throws RecognitionException {
		BinaryCoalescingOperatorContext _localctx = new BinaryCoalescingOperatorContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_binaryCoalescingOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(344);
			_la = _input.LA(1);
			if ( !(((((_la - 13)) & ~0x3f) == 0 && ((1L << (_la - 13)) & 1152921506217459715L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentOperatorContext extends ParserRuleContext {
		public SingleAssignmentOperatorContext singleAssignmentOperator() {
			return getRuleContext(SingleAssignmentOperatorContext.class,0);
		}
		public MultipleAssignmentOperatorContext multipleAssignmentOperator() {
			return getRuleContext(MultipleAssignmentOperatorContext.class,0);
		}
		public CompoundAssignmentOperatorContext compoundAssignmentOperator() {
			return getRuleContext(CompoundAssignmentOperatorContext.class,0);
		}
		public AssignmentOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentOperator; }
	}

	public final AssignmentOperatorContext assignmentOperator() throws RecognitionException {
		AssignmentOperatorContext _localctx = new AssignmentOperatorContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_assignmentOperator);
		try {
			setState(349);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(346);
				singleAssignmentOperator();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(347);
				multipleAssignmentOperator();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(348);
				compoundAssignmentOperator();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SingleAssignmentOperatorContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(NeoBasicParser.EQUAL, 0); }
		public TerminalNode POP_ONE_ASSIGNMENT() { return getToken(NeoBasicParser.POP_ONE_ASSIGNMENT, 0); }
		public TerminalNode PULL_ALL_ASSIGNMENT() { return getToken(NeoBasicParser.PULL_ALL_ASSIGNMENT, 0); }
		public TerminalNode PIPE_ASSIGNMENT() { return getToken(NeoBasicParser.PIPE_ASSIGNMENT, 0); }
		public SingleAssignmentOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleAssignmentOperator; }
	}

	public final SingleAssignmentOperatorContext singleAssignmentOperator() throws RecognitionException {
		SingleAssignmentOperatorContext _localctx = new SingleAssignmentOperatorContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_singleAssignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			_la = _input.LA(1);
			if ( !(((((_la - 31)) & ~0x3f) == 0 && ((1L << (_la - 31)) & 61572651155457L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultipleAssignmentOperatorContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(NeoBasicParser.EQUAL, 0); }
		public TerminalNode DESTRUCTURING_ASSIGNMENT() { return getToken(NeoBasicParser.DESTRUCTURING_ASSIGNMENT, 0); }
		public MultipleAssignmentOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multipleAssignmentOperator; }
	}

	public final MultipleAssignmentOperatorContext multipleAssignmentOperator() throws RecognitionException {
		MultipleAssignmentOperatorContext _localctx = new MultipleAssignmentOperatorContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_multipleAssignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			_la = _input.LA(1);
			if ( !(_la==EQUAL || _la==DESTRUCTURING_ASSIGNMENT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompoundAssignmentOperatorContext extends ParserRuleContext {
		public TerminalNode ADDITION_ASSIGNMENT() { return getToken(NeoBasicParser.ADDITION_ASSIGNMENT, 0); }
		public TerminalNode SUBTRACTION_ASSIGNMENT() { return getToken(NeoBasicParser.SUBTRACTION_ASSIGNMENT, 0); }
		public TerminalNode MULTIPLICATION_ASSIGNMENT() { return getToken(NeoBasicParser.MULTIPLICATION_ASSIGNMENT, 0); }
		public TerminalNode REAL_DIVISION_ASSIGNMENT() { return getToken(NeoBasicParser.REAL_DIVISION_ASSIGNMENT, 0); }
		public TerminalNode INTEGER_DIVISION_ASSIGNMENT() { return getToken(NeoBasicParser.INTEGER_DIVISION_ASSIGNMENT, 0); }
		public TerminalNode MODULO_ASSIGNMENT() { return getToken(NeoBasicParser.MODULO_ASSIGNMENT, 0); }
		public TerminalNode NTH_POWER_ASSIGNMENT() { return getToken(NeoBasicParser.NTH_POWER_ASSIGNMENT, 0); }
		public TerminalNode NTH_ROOT_ASSIGNMENT() { return getToken(NeoBasicParser.NTH_ROOT_ASSIGNMENT, 0); }
		public TerminalNode PERCENTAGE_RATE_ASSIGNMENT() { return getToken(NeoBasicParser.PERCENTAGE_RATE_ASSIGNMENT, 0); }
		public TerminalNode PERCENTAGE_AMOUNT_ASSIGNMENT() { return getToken(NeoBasicParser.PERCENTAGE_AMOUNT_ASSIGNMENT, 0); }
		public TerminalNode PERCENTAGE_INCREASE_ASSIGNMENT() { return getToken(NeoBasicParser.PERCENTAGE_INCREASE_ASSIGNMENT, 0); }
		public TerminalNode PERCENTAGE_DECREASE_ASSIGNMENT() { return getToken(NeoBasicParser.PERCENTAGE_DECREASE_ASSIGNMENT, 0); }
		public TerminalNode PERCENTAGE_VARIATION_ASSIGNMENT() { return getToken(NeoBasicParser.PERCENTAGE_VARIATION_ASSIGNMENT, 0); }
		public TerminalNode BIT_AND_ASSIGNMENT() { return getToken(NeoBasicParser.BIT_AND_ASSIGNMENT, 0); }
		public TerminalNode BIT_CLEAR_ASSIGNMENT() { return getToken(NeoBasicParser.BIT_CLEAR_ASSIGNMENT, 0); }
		public TerminalNode BIT_XOR_ASSIGNMENT() { return getToken(NeoBasicParser.BIT_XOR_ASSIGNMENT, 0); }
		public TerminalNode BIT_OR_ASSIGNMENT() { return getToken(NeoBasicParser.BIT_OR_ASSIGNMENT, 0); }
		public TerminalNode LEFT_SHIFT_ASSIGNMENT() { return getToken(NeoBasicParser.LEFT_SHIFT_ASSIGNMENT, 0); }
		public TerminalNode SIGNED_RIGHT_SHIFT_ASSIGNMENT() { return getToken(NeoBasicParser.SIGNED_RIGHT_SHIFT_ASSIGNMENT, 0); }
		public TerminalNode UNSIGNED_RIGHT_SHIFT_ASSIGNMENT() { return getToken(NeoBasicParser.UNSIGNED_RIGHT_SHIFT_ASSIGNMENT, 0); }
		public TerminalNode NONE_COALESCING_ASSIGNMENT() { return getToken(NeoBasicParser.NONE_COALESCING_ASSIGNMENT, 0); }
		public CompoundAssignmentOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundAssignmentOperator; }
	}

	public final CompoundAssignmentOperatorContext compoundAssignmentOperator() throws RecognitionException {
		CompoundAssignmentOperatorContext _localctx = new CompoundAssignmentOperatorContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_compoundAssignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			_la = _input.LA(1);
			if ( !(((((_la - 78)) & ~0x3f) == 0 && ((1L << (_la - 78)) & 4194271L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SymbolIdentifierContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(NeoBasicParser.IDENTIFIER, 0); }
		public SymbolIdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_symbolIdentifier; }
	}

	public final SymbolIdentifierContext symbolIdentifier() throws RecognitionException {
		SymbolIdentifierContext _localctx = new SymbolIdentifierContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_symbolIdentifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(357);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QualifiedIdentifierContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(NeoBasicParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(NeoBasicParser.IDENTIFIER, i);
		}
		public List<TerminalNode> DOT() { return getTokens(NeoBasicParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(NeoBasicParser.DOT, i);
		}
		public QualifiedIdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifiedIdentifier; }
	}

	public final QualifiedIdentifierContext qualifiedIdentifier() throws RecognitionException {
		QualifiedIdentifierContext _localctx = new QualifiedIdentifierContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_qualifiedIdentifier);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			match(IDENTIFIER);
			setState(364);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(360);
					match(DOT);
					setState(361);
					match(IDENTIFIER);
					}
					} 
				}
				setState(366);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifiersContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(NeoBasicParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(NeoBasicParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public IdentifiersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifiers; }
	}

	public final IdentifiersContext identifiers() throws RecognitionException {
		IdentifiersContext _localctx = new IdentifiersContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_identifiers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(367);
			match(IDENTIFIER);
			setState(372);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(368);
				match(COMMA);
				setState(369);
				match(IDENTIFIER);
				}
				}
				setState(374);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SymbolIdentifiersContext extends ParserRuleContext {
		public List<SymbolIdentifierContext> symbolIdentifier() {
			return getRuleContexts(SymbolIdentifierContext.class);
		}
		public SymbolIdentifierContext symbolIdentifier(int i) {
			return getRuleContext(SymbolIdentifierContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public SymbolIdentifiersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_symbolIdentifiers; }
	}

	public final SymbolIdentifiersContext symbolIdentifiers() throws RecognitionException {
		SymbolIdentifiersContext _localctx = new SymbolIdentifiersContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_symbolIdentifiers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			symbolIdentifier();
			setState(380);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(376);
				match(COMMA);
				setState(377);
				symbolIdentifier();
				}
				}
				setState(382);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QualifiedIdentifiersContext extends ParserRuleContext {
		public List<QualifiedIdentifierContext> qualifiedIdentifier() {
			return getRuleContexts(QualifiedIdentifierContext.class);
		}
		public QualifiedIdentifierContext qualifiedIdentifier(int i) {
			return getRuleContext(QualifiedIdentifierContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public QualifiedIdentifiersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifiedIdentifiers; }
	}

	public final QualifiedIdentifiersContext qualifiedIdentifiers() throws RecognitionException {
		QualifiedIdentifiersContext _localctx = new QualifiedIdentifiersContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_qualifiedIdentifiers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(383);
			qualifiedIdentifier();
			setState(388);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(384);
				match(COMMA);
				setState(385);
				qualifiedIdentifier();
				}
				}
				setState(390);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PredeclaredValueContext extends ParserRuleContext {
		public TerminalNode IOTA() { return getToken(NeoBasicParser.IOTA, 0); }
		public PredeclaredValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predeclaredValue; }
	}

	public final PredeclaredValueContext predeclaredValue() throws RecognitionException {
		PredeclaredValueContext _localctx = new PredeclaredValueContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_predeclaredValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(391);
			match(IOTA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public EscalarLiteralContext escalarLiteral() {
			return getRuleContext(EscalarLiteralContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(393);
			escalarLiteral();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EscalarLiteralContext extends ParserRuleContext {
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public NumericLiteralContext numericLiteral() {
			return getRuleContext(NumericLiteralContext.class,0);
		}
		public EscalarLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escalarLiteral; }
	}

	public final EscalarLiteralContext escalarLiteral() throws RecognitionException {
		EscalarLiteralContext _localctx = new EscalarLiteralContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_escalarLiteral);
		try {
			setState(397);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
				enterOuterAlt(_localctx, 1);
				{
				setState(395);
				booleanLiteral();
				}
				break;
			case REAL_LIT:
			case NATURAL_LIT:
			case INTEGER_LIT:
			case NONZERO:
			case ZERO:
			case MINVALUE:
			case MAXVALUE:
			case NAN:
			case POSITIVEINFINITY:
			case NEGATIVEINFINITY:
				enterOuterAlt(_localctx, 2);
				{
				setState(396);
				numericLiteral();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BooleanLiteralContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(NeoBasicParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(NeoBasicParser.FALSE, 0); }
		public BooleanLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanLiteral; }
	}

	public final BooleanLiteralContext booleanLiteral() throws RecognitionException {
		BooleanLiteralContext _localctx = new BooleanLiteralContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_booleanLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(399);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumericLiteralContext extends ParserRuleContext {
		public TerminalNode NATURAL_LIT() { return getToken(NeoBasicParser.NATURAL_LIT, 0); }
		public TerminalNode INTEGER_LIT() { return getToken(NeoBasicParser.INTEGER_LIT, 0); }
		public TerminalNode REAL_LIT() { return getToken(NeoBasicParser.REAL_LIT, 0); }
		public TerminalNode NONZERO() { return getToken(NeoBasicParser.NONZERO, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode ZERO() { return getToken(NeoBasicParser.ZERO, 0); }
		public TerminalNode MINVALUE() { return getToken(NeoBasicParser.MINVALUE, 0); }
		public TerminalNode MAXVALUE() { return getToken(NeoBasicParser.MAXVALUE, 0); }
		public TerminalNode NAN() { return getToken(NeoBasicParser.NAN, 0); }
		public TerminalNode POSITIVEINFINITY() { return getToken(NeoBasicParser.POSITIVEINFINITY, 0); }
		public TerminalNode NEGATIVEINFINITY() { return getToken(NeoBasicParser.NEGATIVEINFINITY, 0); }
		public NumericLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericLiteral; }
	}

	public final NumericLiteralContext numericLiteral() throws RecognitionException {
		NumericLiteralContext _localctx = new NumericLiteralContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_numericLiteral);
		try {
			setState(412);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NATURAL_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(401);
				match(NATURAL_LIT);
				}
				break;
			case INTEGER_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(402);
				match(INTEGER_LIT);
				}
				break;
			case REAL_LIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(403);
				match(REAL_LIT);
				}
				break;
			case NONZERO:
				enterOuterAlt(_localctx, 4);
				{
				setState(404);
				match(NONZERO);
				setState(405);
				expression(0);
				}
				break;
			case ZERO:
				enterOuterAlt(_localctx, 5);
				{
				setState(406);
				match(ZERO);
				}
				break;
			case MINVALUE:
				enterOuterAlt(_localctx, 6);
				{
				setState(407);
				match(MINVALUE);
				}
				break;
			case MAXVALUE:
				enterOuterAlt(_localctx, 7);
				{
				setState(408);
				match(MAXVALUE);
				}
				break;
			case NAN:
				enterOuterAlt(_localctx, 8);
				{
				setState(409);
				match(NAN);
				}
				break;
			case POSITIVEINFINITY:
				enterOuterAlt(_localctx, 9);
				{
				setState(410);
				match(POSITIVEINFINITY);
				}
				break;
			case NEGATIVEINFINITY:
				enterOuterAlt(_localctx, 10);
				{
				setState(411);
				match(NEGATIVEINFINITY);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public NativeTypeContext nativeType() {
			return getRuleContext(NativeTypeContext.class,0);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(414);
			nativeType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NativeTypeContext extends ParserRuleContext {
		public EscalarTypeContext escalarType() {
			return getRuleContext(EscalarTypeContext.class,0);
		}
		public NativeTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nativeType; }
	}

	public final NativeTypeContext nativeType() throws RecognitionException {
		NativeTypeContext _localctx = new NativeTypeContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_nativeType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(416);
			escalarType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EscalarTypeContext extends ParserRuleContext {
		public BooleanTypeContext booleanType() {
			return getRuleContext(BooleanTypeContext.class,0);
		}
		public NumericTypeContext numericType() {
			return getRuleContext(NumericTypeContext.class,0);
		}
		public EscalarTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escalarType; }
	}

	public final EscalarTypeContext escalarType() throws RecognitionException {
		EscalarTypeContext _localctx = new EscalarTypeContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_escalarType);
		try {
			setState(420);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOL8:
			case BOOL16:
			case BOOL32:
			case BOOL64:
			case BOOL128:
			case BOOL:
				enterOuterAlt(_localctx, 1);
				{
				setState(418);
				booleanType();
				}
				break;
			case NAT8:
			case NAT16:
			case NAT32:
			case NAT64:
			case NAT128:
			case BYTE:
			case NAT:
			case INT8:
			case INT16:
			case INT32:
			case INT64:
			case INT128:
			case INT:
			case REAL8:
			case REAL16:
			case REAL32:
			case REAL64:
			case REAL128:
			case REAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(419);
				numericType();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BooleanTypeContext extends ParserRuleContext {
		public TerminalNode BOOL8() { return getToken(NeoBasicParser.BOOL8, 0); }
		public TerminalNode BOOL16() { return getToken(NeoBasicParser.BOOL16, 0); }
		public TerminalNode BOOL32() { return getToken(NeoBasicParser.BOOL32, 0); }
		public TerminalNode BOOL64() { return getToken(NeoBasicParser.BOOL64, 0); }
		public TerminalNode BOOL128() { return getToken(NeoBasicParser.BOOL128, 0); }
		public TerminalNode BOOL() { return getToken(NeoBasicParser.BOOL, 0); }
		public BooleanTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanType; }
	}

	public final BooleanTypeContext booleanType() throws RecognitionException {
		BooleanTypeContext _localctx = new BooleanTypeContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_booleanType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(422);
			_la = _input.LA(1);
			if ( !(((((_la - 163)) & ~0x3f) == 0 && ((1L << (_la - 163)) & 63L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumericTypeContext extends ParserRuleContext {
		public NumericNaturalContext numericNatural() {
			return getRuleContext(NumericNaturalContext.class,0);
		}
		public NumericIntegerContext numericInteger() {
			return getRuleContext(NumericIntegerContext.class,0);
		}
		public NumericRealContext numericReal() {
			return getRuleContext(NumericRealContext.class,0);
		}
		public NumericTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericType; }
	}

	public final NumericTypeContext numericType() throws RecognitionException {
		NumericTypeContext _localctx = new NumericTypeContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_numericType);
		try {
			setState(427);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAT8:
			case NAT16:
			case NAT32:
			case NAT64:
			case NAT128:
			case BYTE:
			case NAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(424);
				numericNatural();
				}
				break;
			case INT8:
			case INT16:
			case INT32:
			case INT64:
			case INT128:
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(425);
				numericInteger();
				}
				break;
			case REAL8:
			case REAL16:
			case REAL32:
			case REAL64:
			case REAL128:
			case REAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(426);
				numericReal();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumericNaturalContext extends ParserRuleContext {
		public TerminalNode NAT8() { return getToken(NeoBasicParser.NAT8, 0); }
		public TerminalNode NAT16() { return getToken(NeoBasicParser.NAT16, 0); }
		public TerminalNode NAT32() { return getToken(NeoBasicParser.NAT32, 0); }
		public TerminalNode NAT64() { return getToken(NeoBasicParser.NAT64, 0); }
		public TerminalNode NAT128() { return getToken(NeoBasicParser.NAT128, 0); }
		public TerminalNode BYTE() { return getToken(NeoBasicParser.BYTE, 0); }
		public TerminalNode NAT() { return getToken(NeoBasicParser.NAT, 0); }
		public NumericNaturalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericNatural; }
	}

	public final NumericNaturalContext numericNatural() throws RecognitionException {
		NumericNaturalContext _localctx = new NumericNaturalContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_numericNatural);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(429);
			_la = _input.LA(1);
			if ( !(((((_la - 169)) & ~0x3f) == 0 && ((1L << (_la - 169)) & 127L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumericIntegerContext extends ParserRuleContext {
		public TerminalNode INT8() { return getToken(NeoBasicParser.INT8, 0); }
		public TerminalNode INT16() { return getToken(NeoBasicParser.INT16, 0); }
		public TerminalNode INT32() { return getToken(NeoBasicParser.INT32, 0); }
		public TerminalNode INT64() { return getToken(NeoBasicParser.INT64, 0); }
		public TerminalNode INT128() { return getToken(NeoBasicParser.INT128, 0); }
		public TerminalNode INT() { return getToken(NeoBasicParser.INT, 0); }
		public NumericIntegerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericInteger; }
	}

	public final NumericIntegerContext numericInteger() throws RecognitionException {
		NumericIntegerContext _localctx = new NumericIntegerContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_numericInteger);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(431);
			_la = _input.LA(1);
			if ( !(((((_la - 176)) & ~0x3f) == 0 && ((1L << (_la - 176)) & 63L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumericRealContext extends ParserRuleContext {
		public TerminalNode REAL8() { return getToken(NeoBasicParser.REAL8, 0); }
		public TerminalNode REAL16() { return getToken(NeoBasicParser.REAL16, 0); }
		public TerminalNode REAL32() { return getToken(NeoBasicParser.REAL32, 0); }
		public TerminalNode REAL64() { return getToken(NeoBasicParser.REAL64, 0); }
		public TerminalNode REAL128() { return getToken(NeoBasicParser.REAL128, 0); }
		public TerminalNode REAL() { return getToken(NeoBasicParser.REAL, 0); }
		public NumericRealContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericReal; }
	}

	public final NumericRealContext numericReal() throws RecognitionException {
		NumericRealContext _localctx = new NumericRealContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_numericReal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(433);
			_la = _input.LA(1);
			if ( !(((((_la - 182)) & ~0x3f) == 0 && ((1L << (_la - 182)) & 63L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public ExpressionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressions; }
	}

	public final ExpressionsContext expressions() throws RecognitionException {
		ExpressionsContext _localctx = new ExpressionsContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_expressions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(435);
			expression(0);
			setState(440);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(436);
				match(COMMA);
				setState(437);
				expression(0);
				}
				}
				setState(442);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionsContext extends ParserRuleContext {
		public List<PrimaryExpressionContext> primaryExpression() {
			return getRuleContexts(PrimaryExpressionContext.class);
		}
		public PrimaryExpressionContext primaryExpression(int i) {
			return getRuleContext(PrimaryExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(NeoBasicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(NeoBasicParser.COMMA, i);
		}
		public PrimaryExpressionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpressions; }
	}

	public final PrimaryExpressionsContext primaryExpressions() throws RecognitionException {
		PrimaryExpressionsContext _localctx = new PrimaryExpressionsContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_primaryExpressions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(443);
			primaryExpression(0);
			setState(448);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(444);
				match(COMMA);
				setState(445);
				primaryExpression(0);
				}
				}
				setState(450);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public ParenthesizedExpressionContext parenthesizedExpression() {
			return getRuleContext(ParenthesizedExpressionContext.class,0);
		}
		public PrefixUnaryOperatorContext prefixUnaryOperator() {
			return getRuleContext(PrefixUnaryOperatorContext.class,0);
		}
		public List<PrimaryExpressionContext> primaryExpression() {
			return getRuleContexts(PrimaryExpressionContext.class);
		}
		public PrimaryExpressionContext primaryExpression(int i) {
			return getRuleContext(PrimaryExpressionContext.class,i);
		}
		public QualifiedIdentifierContext qualifiedIdentifier() {
			return getRuleContext(QualifiedIdentifierContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode DOT() { return getToken(NeoBasicParser.DOT, 0); }
		public TerminalNode SEMICOLON() { return getToken(NeoBasicParser.SEMICOLON, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(NeoBasicParser.LEFT_PARENTHESIS, 0); }
		public ExpressionsContext expressions() {
			return getRuleContext(ExpressionsContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(NeoBasicParser.RIGHT_PARENTHESIS, 0); }
		public PosfixUnaryOperatorContext posfixUnaryOperator() {
			return getRuleContext(PosfixUnaryOperatorContext.class,0);
		}
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		return primaryExpression(0);
	}

	private PrimaryExpressionContext primaryExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, _parentState);
		PrimaryExpressionContext _prevctx = _localctx;
		int _startState = 142;
		enterRecursionRule(_localctx, 142, RULE_primaryExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(460);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				{
				setState(452);
				operand();
				}
				break;
			case 2:
				{
				setState(453);
				parenthesizedExpression();
				}
				break;
			case 3:
				{
				setState(454);
				prefixUnaryOperator();
				setState(455);
				primaryExpression(2);
				}
				break;
			case 4:
				{
				setState(457);
				qualifiedIdentifier();
				setState(458);
				expression(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(477);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(475);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
					case 1:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(462);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(463);
						match(DOT);
						setState(464);
						primaryExpression(7);
						}
						break;
					case 2:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(465);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(466);
						match(SEMICOLON);
						setState(467);
						primaryExpression(5);
						}
						break;
					case 3:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(468);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(469);
						match(LEFT_PARENTHESIS);
						setState(470);
						expressions();
						setState(471);
						match(RIGHT_PARENTHESIS);
						}
						break;
					case 4:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(473);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(474);
						posfixUnaryOperator();
						}
						break;
					}
					} 
				}
				setState(479);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperandContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public PredeclaredValueContext predeclaredValue() {
			return getRuleContext(PredeclaredValueContext.class,0);
		}
		public QualifiedIdentifierContext qualifiedIdentifier() {
			return getRuleContext(QualifiedIdentifierContext.class,0);
		}
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_operand);
		try {
			setState(483);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REAL_LIT:
			case NATURAL_LIT:
			case INTEGER_LIT:
			case TRUE:
			case FALSE:
			case NONZERO:
			case ZERO:
			case MINVALUE:
			case MAXVALUE:
			case NAN:
			case POSITIVEINFINITY:
			case NEGATIVEINFINITY:
				enterOuterAlt(_localctx, 1);
				{
				setState(480);
				literal();
				}
				break;
			case IOTA:
				enterOuterAlt(_localctx, 2);
				{
				setState(481);
				predeclaredValue();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 3);
				{
				setState(482);
				qualifiedIdentifier();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParenthesizedExpressionContext extends ParserRuleContext {
		public TerminalNode LEFT_PARENTHESIS() { return getToken(NeoBasicParser.LEFT_PARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(NeoBasicParser.RIGHT_PARENTHESIS, 0); }
		public ParenthesizedExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parenthesizedExpression; }
	}

	public final ParenthesizedExpressionContext parenthesizedExpression() throws RecognitionException {
		ParenthesizedExpressionContext _localctx = new ParenthesizedExpressionContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_parenthesizedExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(485);
			match(LEFT_PARENTHESIS);
			setState(486);
			expression(0);
			setState(487);
			match(RIGHT_PARENTHESIS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public BinaryExponentialOperatorContext binaryExponentialOperator() {
			return getRuleContext(BinaryExponentialOperatorContext.class,0);
		}
		public BinaryMultiplicativeOperatorContext binaryMultiplicativeOperator() {
			return getRuleContext(BinaryMultiplicativeOperatorContext.class,0);
		}
		public BinaryAdditiveOperatorContext binaryAdditiveOperator() {
			return getRuleContext(BinaryAdditiveOperatorContext.class,0);
		}
		public BitShiftOperatorContext bitShiftOperator() {
			return getRuleContext(BitShiftOperatorContext.class,0);
		}
		public BitConjunctionOperatorContext bitConjunctionOperator() {
			return getRuleContext(BitConjunctionOperatorContext.class,0);
		}
		public BitExclusiveDisjunctionOperatorContext bitExclusiveDisjunctionOperator() {
			return getRuleContext(BitExclusiveDisjunctionOperatorContext.class,0);
		}
		public BitDisjunctionOperatorContext bitDisjunctionOperator() {
			return getRuleContext(BitDisjunctionOperatorContext.class,0);
		}
		public BinaryComparisonOperatorContext binaryComparisonOperator() {
			return getRuleContext(BinaryComparisonOperatorContext.class,0);
		}
		public BinaryRelationalOperatorContext binaryRelationalOperator() {
			return getRuleContext(BinaryRelationalOperatorContext.class,0);
		}
		public BinaryConditionalOperatorContext binaryConditionalOperator() {
			return getRuleContext(BinaryConditionalOperatorContext.class,0);
		}
		public BinaryConjunctionOperatorContext binaryConjunctionOperator() {
			return getRuleContext(BinaryConjunctionOperatorContext.class,0);
		}
		public BinaryExclusiveDisjunctionOperatorContext binaryExclusiveDisjunctionOperator() {
			return getRuleContext(BinaryExclusiveDisjunctionOperatorContext.class,0);
		}
		public BinaryDisjunctionOperatorContext binaryDisjunctionOperator() {
			return getRuleContext(BinaryDisjunctionOperatorContext.class,0);
		}
		public BinaryCoalescingOperatorContext binaryCoalescingOperator() {
			return getRuleContext(BinaryCoalescingOperatorContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 148;
		enterRecursionRule(_localctx, 148, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(492);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				{
				setState(490);
				primaryExpression(0);
				}
				break;
			case 2:
				{
				setState(491);
				assignmentExpression();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(553);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(551);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(494);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(495);
						binaryExponentialOperator();
						setState(496);
						expression(16);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(498);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(499);
						binaryMultiplicativeOperator();
						setState(500);
						expression(15);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(502);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(503);
						binaryAdditiveOperator();
						setState(504);
						expression(14);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(506);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(507);
						bitShiftOperator();
						setState(508);
						expression(13);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(510);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(511);
						bitConjunctionOperator();
						setState(512);
						expression(12);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(514);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(515);
						bitExclusiveDisjunctionOperator();
						setState(516);
						expression(11);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(518);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(519);
						bitDisjunctionOperator();
						setState(520);
						expression(10);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(522);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(523);
						binaryComparisonOperator();
						setState(524);
						expression(9);
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(526);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(527);
						binaryRelationalOperator();
						setState(528);
						expression(8);
						}
						break;
					case 10:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(530);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(531);
						binaryConditionalOperator();
						setState(532);
						expression(7);
						}
						break;
					case 11:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(534);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(535);
						binaryConjunctionOperator();
						setState(536);
						expression(6);
						}
						break;
					case 12:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(538);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(539);
						binaryExclusiveDisjunctionOperator();
						setState(540);
						expression(5);
						}
						break;
					case 13:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(542);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(543);
						binaryDisjunctionOperator();
						setState(544);
						expression(4);
						}
						break;
					case 14:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(546);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(547);
						binaryCoalescingOperator();
						setState(549);
						_errHandler.sync(this);
						switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
						case 1:
							{
							setState(548);
							expression(0);
							}
							break;
						}
						}
						break;
					}
					} 
				}
				setState(555);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public AssignmentOperatorContext assignmentOperator() {
			return getRuleContext(AssignmentOperatorContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentExpression; }
	}

	public final AssignmentExpressionContext assignmentExpression() throws RecognitionException {
		AssignmentExpressionContext _localctx = new AssignmentExpressionContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_assignmentExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			primaryExpression(0);
			setState(557);
			assignmentOperator();
			setState(558);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 71:
			return primaryExpression_sempred((PrimaryExpressionContext)_localctx, predIndex);
		case 74:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean primaryExpression_sempred(PrimaryExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 5);
		case 3:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 15);
		case 5:
			return precpred(_ctx, 14);
		case 6:
			return precpred(_ctx, 13);
		case 7:
			return precpred(_ctx, 12);
		case 8:
			return precpred(_ctx, 11);
		case 9:
			return precpred(_ctx, 10);
		case 10:
			return precpred(_ctx, 9);
		case 11:
			return precpred(_ctx, 8);
		case 12:
			return precpred(_ctx, 7);
		case 13:
			return precpred(_ctx, 6);
		case 14:
			return precpred(_ctx, 5);
		case 15:
			return precpred(_ctx, 4);
		case 16:
			return precpred(_ctx, 3);
		case 17:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u00c6\u0231\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007"+
		"\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007"+
		"\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007"+
		"\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007"+
		"\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007"+
		"\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007"+
		",\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u0007"+
		"1\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u0007"+
		"6\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0002;\u0007"+
		";\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007?\u0002@\u0007"+
		"@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007D\u0002E\u0007"+
		"E\u0002F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007I\u0002J\u0007"+
		"J\u0002K\u0007K\u0001\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u009c"+
		"\b\u0000\u000b\u0000\f\u0000\u009d\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002\u00a5\b\u0002\u0001\u0003\u0005\u0003"+
		"\u00a8\b\u0003\n\u0003\f\u0003\u00ab\t\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0003\u0006\u00b7\b\u0006\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u00bb\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0004\b\u00c3\b\b\u000b\b\f\b\u00c4\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\n\u0005\n\u00cc\b\n\n\n\f\n\u00cf\t\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u00db\b\r\u0001\u000e\u0001\u000e\u0003\u000e\u00df\b\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u00e4\b\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0004\u000f\u00e9\b\u000f\u000b\u000f\f\u000f\u00ea\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0005\u0011\u00f2"+
		"\b\u0011\n\u0011\f\u0011\u00f5\t\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u0101\b\u0014\u0001\u0015\u0001\u0015\u0003\u0015"+
		"\u0105\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u010a\b"+
		"\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0004\u0016\u010f\b\u0016\u000b"+
		"\u0016\f\u0016\u0110\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0003"+
		"\u0018\u011d\b\u0018\u0001\u0019\u0001\u0019\u0003\u0019\u0121\b\u0019"+
		"\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f"+
		"\u0001 \u0001 \u0001!\u0001!\u0001\"\u0001\"\u0001#\u0001#\u0001$\u0001"+
		"$\u0001%\u0001%\u0001&\u0001&\u0001\'\u0001\'\u0001(\u0001(\u0001)\u0001"+
		")\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001"+
		"*\u0001*\u0001*\u0001*\u0001*\u0003*\u0151\b*\u0001+\u0001+\u0001,\u0001"+
		",\u0001-\u0001-\u0001.\u0001.\u0001/\u0001/\u0001/\u0003/\u015e\b/\u0001"+
		"0\u00010\u00011\u00011\u00012\u00012\u00013\u00013\u00014\u00014\u0001"+
		"4\u00054\u016b\b4\n4\f4\u016e\t4\u00015\u00015\u00015\u00055\u0173\b5"+
		"\n5\f5\u0176\t5\u00016\u00016\u00016\u00056\u017b\b6\n6\f6\u017e\t6\u0001"+
		"7\u00017\u00017\u00057\u0183\b7\n7\f7\u0186\t7\u00018\u00018\u00019\u0001"+
		"9\u0001:\u0001:\u0003:\u018e\b:\u0001;\u0001;\u0001<\u0001<\u0001<\u0001"+
		"<\u0001<\u0001<\u0001<\u0001<\u0001<\u0001<\u0001<\u0003<\u019d\b<\u0001"+
		"=\u0001=\u0001>\u0001>\u0001?\u0001?\u0003?\u01a5\b?\u0001@\u0001@\u0001"+
		"A\u0001A\u0001A\u0003A\u01ac\bA\u0001B\u0001B\u0001C\u0001C\u0001D\u0001"+
		"D\u0001E\u0001E\u0001E\u0005E\u01b7\bE\nE\fE\u01ba\tE\u0001F\u0001F\u0001"+
		"F\u0005F\u01bf\bF\nF\fF\u01c2\tF\u0001G\u0001G\u0001G\u0001G\u0001G\u0001"+
		"G\u0001G\u0001G\u0001G\u0003G\u01cd\bG\u0001G\u0001G\u0001G\u0001G\u0001"+
		"G\u0001G\u0001G\u0001G\u0001G\u0001G\u0001G\u0001G\u0001G\u0005G\u01dc"+
		"\bG\nG\fG\u01df\tG\u0001H\u0001H\u0001H\u0003H\u01e4\bH\u0001I\u0001I"+
		"\u0001I\u0001I\u0001J\u0001J\u0001J\u0003J\u01ed\bJ\u0001J\u0001J\u0001"+
		"J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001"+
		"J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001"+
		"J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001"+
		"J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001"+
		"J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001J\u0001"+
		"J\u0001J\u0001J\u0003J\u0226\bJ\u0005J\u0228\bJ\nJ\fJ\u022b\tJ\u0001K"+
		"\u0001K\u0001K\u0001K\u0001K\u0000\u0002\u008e\u0094L\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086"+
		"\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0000\u001a\u0001\u0000"+
		"\u0091\u0092\u0001\u0000\u0091\u0093\u0002\u0000 !/3\u0002\u0000\u001b"+
		"\u001b44\u0002\u0000\u001c\u001c66\u0002\u0000\u001f\u001f55\u0001\u0000"+
		"\u0095\u0096\u0001\u000012\u0002\u0000\u0016\u00197<\u0001\u0000 !\u0002"+
		"\u0000()>>\u0002\u0000\u0015\u0015==\u0001\u0000AB\u0002\u0000\u0007\b"+
		"CH\u0002\u0000\u009d\u009d\u00a0\u00a0\u0002\u0000\u009f\u009f\u00a2\u00a2"+
		"\u0002\u0000\u009e\u009e\u00a1\u00a1\u0003\u0000\r\u000e*+II\u0002\u0000"+
		"\u001f\u001fJL\u0002\u0000\u001f\u001fMM\u0002\u0000NRTc\u0001\u0000\u00bc"+
		"\u00bd\u0001\u0000\u00a3\u00a8\u0001\u0000\u00a9\u00af\u0001\u0000\u00b0"+
		"\u00b5\u0001\u0000\u00b6\u00bb\u0235\u0000\u009b\u0001\u0000\u0000\u0000"+
		"\u0002\u009f\u0001\u0000\u0000\u0000\u0004\u00a4\u0001\u0000\u0000\u0000"+
		"\u0006\u00a9\u0001\u0000\u0000\u0000\b\u00ae\u0001\u0000\u0000\u0000\n"+
		"\u00b0\u0001\u0000\u0000\u0000\f\u00b6\u0001\u0000\u0000\u0000\u000e\u00b8"+
		"\u0001\u0000\u0000\u0000\u0010\u00bf\u0001\u0000\u0000\u0000\u0012\u00c6"+
		"\u0001\u0000\u0000\u0000\u0014\u00cd\u0001\u0000\u0000\u0000\u0016\u00d2"+
		"\u0001\u0000\u0000\u0000\u0018\u00d4\u0001\u0000\u0000\u0000\u001a\u00da"+
		"\u0001\u0000\u0000\u0000\u001c\u00dc\u0001\u0000\u0000\u0000\u001e\u00e5"+
		"\u0001\u0000\u0000\u0000 \u00ec\u0001\u0000\u0000\u0000\"\u00f3\u0001"+
		"\u0000\u0000\u0000$\u00f8\u0001\u0000\u0000\u0000&\u00fa\u0001\u0000\u0000"+
		"\u0000(\u0100\u0001\u0000\u0000\u0000*\u0102\u0001\u0000\u0000\u0000,"+
		"\u010b\u0001\u0000\u0000\u0000.\u0112\u0001\u0000\u0000\u00000\u011c\u0001"+
		"\u0000\u0000\u00002\u0120\u0001\u0000\u0000\u00004\u0122\u0001\u0000\u0000"+
		"\u00006\u0124\u0001\u0000\u0000\u00008\u0126\u0001\u0000\u0000\u0000:"+
		"\u0128\u0001\u0000\u0000\u0000<\u012a\u0001\u0000\u0000\u0000>\u012c\u0001"+
		"\u0000\u0000\u0000@\u012e\u0001\u0000\u0000\u0000B\u0130\u0001\u0000\u0000"+
		"\u0000D\u0132\u0001\u0000\u0000\u0000F\u0134\u0001\u0000\u0000\u0000H"+
		"\u0136\u0001\u0000\u0000\u0000J\u0138\u0001\u0000\u0000\u0000L\u013a\u0001"+
		"\u0000\u0000\u0000N\u013c\u0001\u0000\u0000\u0000P\u013e\u0001\u0000\u0000"+
		"\u0000R\u0140\u0001\u0000\u0000\u0000T\u0150\u0001\u0000\u0000\u0000V"+
		"\u0152\u0001\u0000\u0000\u0000X\u0154\u0001\u0000\u0000\u0000Z\u0156\u0001"+
		"\u0000\u0000\u0000\\\u0158\u0001\u0000\u0000\u0000^\u015d\u0001\u0000"+
		"\u0000\u0000`\u015f\u0001\u0000\u0000\u0000b\u0161\u0001\u0000\u0000\u0000"+
		"d\u0163\u0001\u0000\u0000\u0000f\u0165\u0001\u0000\u0000\u0000h\u0167"+
		"\u0001\u0000\u0000\u0000j\u016f\u0001\u0000\u0000\u0000l\u0177\u0001\u0000"+
		"\u0000\u0000n\u017f\u0001\u0000\u0000\u0000p\u0187\u0001\u0000\u0000\u0000"+
		"r\u0189\u0001\u0000\u0000\u0000t\u018d\u0001\u0000\u0000\u0000v\u018f"+
		"\u0001\u0000\u0000\u0000x\u019c\u0001\u0000\u0000\u0000z\u019e\u0001\u0000"+
		"\u0000\u0000|\u01a0\u0001\u0000\u0000\u0000~\u01a4\u0001\u0000\u0000\u0000"+
		"\u0080\u01a6\u0001\u0000\u0000\u0000\u0082\u01ab\u0001\u0000\u0000\u0000"+
		"\u0084\u01ad\u0001\u0000\u0000\u0000\u0086\u01af\u0001\u0000\u0000\u0000"+
		"\u0088\u01b1\u0001\u0000\u0000\u0000\u008a\u01b3\u0001\u0000\u0000\u0000"+
		"\u008c\u01bb\u0001\u0000\u0000\u0000\u008e\u01cc\u0001\u0000\u0000\u0000"+
		"\u0090\u01e3\u0001\u0000\u0000\u0000\u0092\u01e5\u0001\u0000\u0000\u0000"+
		"\u0094\u01ec\u0001\u0000\u0000\u0000\u0096\u022c\u0001\u0000\u0000\u0000"+
		"\u0098\u0099\u0003\u0002\u0001\u0000\u0099\u009a\u0005\u008b\u0000\u0000"+
		"\u009a\u009c\u0001\u0000\u0000\u0000\u009b\u0098\u0001\u0000\u0000\u0000"+
		"\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000"+
		"\u009d\u009e\u0001\u0000\u0000\u0000\u009e\u0001\u0001\u0000\u0000\u0000"+
		"\u009f\u00a0\u0003\u0004\u0002\u0000\u00a0\u0003\u0001\u0000\u0000\u0000"+
		"\u00a1\u00a5\u0003\u0006\u0003\u0000\u00a2\u00a5\u0003\u0014\n\u0000\u00a3"+
		"\u00a5\u0003\"\u0011\u0000\u00a4\u00a1\u0001\u0000\u0000\u0000\u00a4\u00a2"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a5\u0005"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a8\u0003\b\u0004\u0000\u00a7\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a8\u00ab\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001"+
		"\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa\u00ac\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ac\u00ad\u0003"+
		"\n\u0005\u0000\u00ad\u0007\u0001\u0000\u0000\u0000\u00ae\u00af\u0007\u0000"+
		"\u0000\u0000\u00af\t\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005\u008e\u0000"+
		"\u0000\u00b1\u00b2\u0003\f\u0006\u0000\u00b2\u000b\u0001\u0000\u0000\u0000"+
		"\u00b3\u00b7\u0003\u000e\u0007\u0000\u00b4\u00b7\u0003\u0010\b\u0000\u00b5"+
		"\u00b7\u0003\u0012\t\u0000\u00b6\u00b3\u0001\u0000\u0000\u0000\u00b6\u00b4"+
		"\u0001\u0000\u0000\u0000\u00b6\u00b5\u0001\u0000\u0000\u0000\u00b7\r\u0001"+
		"\u0000\u0000\u0000\u00b8\u00ba\u0003f3\u0000\u00b9\u00bb\u0003z=\u0000"+
		"\u00ba\u00b9\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001\u0000\u0000\u0000"+
		"\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00bd\u0003`0\u0000\u00bd\u00be"+
		"\u0003\u0094J\u0000\u00be\u000f\u0001\u0000\u0000\u0000\u00bf\u00c2\u0003"+
		"\u000e\u0007\u0000\u00c0\u00c1\u0005\n\u0000\u0000\u00c1\u00c3\u0003\u000e"+
		"\u0007\u0000\u00c2\u00c0\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000"+
		"\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000"+
		"\u0000\u0000\u00c5\u0011\u0001\u0000\u0000\u0000\u00c6\u00c7\u0003l6\u0000"+
		"\u00c7\u00c8\u0003b1\u0000\u00c8\u00c9\u0003\u008aE\u0000\u00c9\u0013"+
		"\u0001\u0000\u0000\u0000\u00ca\u00cc\u0003\u0016\u000b\u0000\u00cb\u00ca"+
		"\u0001\u0000\u0000\u0000\u00cc\u00cf\u0001\u0000\u0000\u0000\u00cd\u00cb"+
		"\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce\u00d0"+
		"\u0001\u0000\u0000\u0000\u00cf\u00cd\u0001\u0000\u0000\u0000\u00d0\u00d1"+
		"\u0003\u0018\f\u0000\u00d1\u0015\u0001\u0000\u0000\u0000\u00d2\u00d3\u0007"+
		"\u0001\u0000\u0000\u00d3\u0017\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005"+
		"\u008f\u0000\u0000\u00d5\u00d6\u0003(\u0014\u0000\u00d6\u0019\u0001\u0000"+
		"\u0000\u0000\u00d7\u00db\u0003\u001c\u000e\u0000\u00d8\u00db\u0003\u001e"+
		"\u000f\u0000\u00d9\u00db\u0003 \u0010\u0000\u00da\u00d7\u0001\u0000\u0000"+
		"\u0000\u00da\u00d8\u0001\u0000\u0000\u0000\u00da\u00d9\u0001\u0000\u0000"+
		"\u0000\u00db\u001b\u0001\u0000\u0000\u0000\u00dc\u00de\u0003f3\u0000\u00dd"+
		"\u00df\u0003z=\u0000\u00de\u00dd\u0001\u0000\u0000\u0000\u00de\u00df\u0001"+
		"\u0000\u0000\u0000\u00df\u00e3\u0001\u0000\u0000\u0000\u00e0\u00e1\u0003"+
		"`0\u0000\u00e1\u00e2\u0003\u0094J\u0000\u00e2\u00e4\u0001\u0000\u0000"+
		"\u0000\u00e3\u00e0\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000"+
		"\u0000\u00e4\u001d\u0001\u0000\u0000\u0000\u00e5\u00e8\u0003\u001c\u000e"+
		"\u0000\u00e6\u00e7\u0005\n\u0000\u0000\u00e7\u00e9\u0003\u001c\u000e\u0000"+
		"\u00e8\u00e6\u0001\u0000\u0000\u0000\u00e9\u00ea\u0001\u0000\u0000\u0000"+
		"\u00ea\u00e8\u0001\u0000\u0000\u0000\u00ea\u00eb\u0001\u0000\u0000\u0000"+
		"\u00eb\u001f\u0001\u0000\u0000\u0000\u00ec\u00ed\u0003l6\u0000\u00ed\u00ee"+
		"\u0003b1\u0000\u00ee\u00ef\u0003\u008aE\u0000\u00ef!\u0001\u0000\u0000"+
		"\u0000\u00f0\u00f2\u0003$\u0012\u0000\u00f1\u00f0\u0001\u0000\u0000\u0000"+
		"\u00f2\u00f5\u0001\u0000\u0000\u0000\u00f3\u00f1\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f4\u0001\u0000\u0000\u0000\u00f4\u00f6\u0001\u0000\u0000\u0000"+
		"\u00f5\u00f3\u0001\u0000\u0000\u0000\u00f6\u00f7\u0003&\u0013\u0000\u00f7"+
		"#\u0001\u0000\u0000\u0000\u00f8\u00f9\u0007\u0001\u0000\u0000\u00f9%\u0001"+
		"\u0000\u0000\u0000\u00fa\u00fb\u0005\u0090\u0000\u0000\u00fb\u00fc\u0003"+
		"(\u0014\u0000\u00fc\'\u0001\u0000\u0000\u0000\u00fd\u0101\u0003*\u0015"+
		"\u0000\u00fe\u0101\u0003,\u0016\u0000\u00ff\u0101\u0003.\u0017\u0000\u0100"+
		"\u00fd\u0001\u0000\u0000\u0000\u0100\u00fe\u0001\u0000\u0000\u0000\u0100"+
		"\u00ff\u0001\u0000\u0000\u0000\u0101)\u0001\u0000\u0000\u0000\u0102\u0104"+
		"\u0003f3\u0000\u0103\u0105\u0003z=\u0000\u0104\u0103\u0001\u0000\u0000"+
		"\u0000\u0104\u0105\u0001\u0000\u0000\u0000\u0105\u0109\u0001\u0000\u0000"+
		"\u0000\u0106\u0107\u0003`0\u0000\u0107\u0108\u0003\u0094J\u0000\u0108"+
		"\u010a\u0001\u0000\u0000\u0000\u0109\u0106\u0001\u0000\u0000\u0000\u0109"+
		"\u010a\u0001\u0000\u0000\u0000\u010a+\u0001\u0000\u0000\u0000\u010b\u010e"+
		"\u0003*\u0015\u0000\u010c\u010d\u0005\n\u0000\u0000\u010d\u010f\u0003"+
		"*\u0015\u0000\u010e\u010c\u0001\u0000\u0000\u0000\u010f\u0110\u0001\u0000"+
		"\u0000\u0000\u0110\u010e\u0001\u0000\u0000\u0000\u0110\u0111\u0001\u0000"+
		"\u0000\u0000\u0111-\u0001\u0000\u0000\u0000\u0112\u0113\u0003l6\u0000"+
		"\u0113\u0114\u0003b1\u0000\u0114\u0115\u0003\u008aE\u0000\u0115/\u0001"+
		"\u0000\u0000\u0000\u0116\u011d\u00034\u001a\u0000\u0117\u011d\u00036\u001b"+
		"\u0000\u0118\u011d\u00038\u001c\u0000\u0119\u011d\u0003:\u001d\u0000\u011a"+
		"\u011d\u0003<\u001e\u0000\u011b\u011d\u0003@ \u0000\u011c\u0116\u0001"+
		"\u0000\u0000\u0000\u011c\u0117\u0001\u0000\u0000\u0000\u011c\u0118\u0001"+
		"\u0000\u0000\u0000\u011c\u0119\u0001\u0000\u0000\u0000\u011c\u011a\u0001"+
		"\u0000\u0000\u0000\u011c\u011b\u0001\u0000\u0000\u0000\u011d1\u0001\u0000"+
		"\u0000\u0000\u011e\u0121\u0003<\u001e\u0000\u011f\u0121\u0003>\u001f\u0000"+
		"\u0120\u011e\u0001\u0000\u0000\u0000\u0120\u011f\u0001\u0000\u0000\u0000"+
		"\u01213\u0001\u0000\u0000\u0000\u0122\u0123\u0007\u0002\u0000\u0000\u0123"+
		"5\u0001\u0000\u0000\u0000\u0124\u0125\u0007\u0003\u0000\u0000\u01257\u0001"+
		"\u0000\u0000\u0000\u0126\u0127\u0005\u009c\u0000\u0000\u01279\u0001\u0000"+
		"\u0000\u0000\u0128\u0129\u0005\"\u0000\u0000\u0129;\u0001\u0000\u0000"+
		"\u0000\u012a\u012b\u0007\u0004\u0000\u0000\u012b=\u0001\u0000\u0000\u0000"+
		"\u012c\u012d\u0007\u0005\u0000\u0000\u012d?\u0001\u0000\u0000\u0000\u012e"+
		"\u012f\u0007\u0006\u0000\u0000\u012fA\u0001\u0000\u0000\u0000\u0130\u0131"+
		"\u0007\u0007\u0000\u0000\u0131C\u0001\u0000\u0000\u0000\u0132\u0133\u0007"+
		"\b\u0000\u0000\u0133E\u0001\u0000\u0000\u0000\u0134\u0135\u0007\t\u0000"+
		"\u0000\u0135G\u0001\u0000\u0000\u0000\u0136\u0137\u0007\n\u0000\u0000"+
		"\u0137I\u0001\u0000\u0000\u0000\u0138\u0139\u0007\u000b\u0000\u0000\u0139"+
		"K\u0001\u0000\u0000\u0000\u013a\u013b\u0005\u001c\u0000\u0000\u013bM\u0001"+
		"\u0000\u0000\u0000\u013c\u013d\u0005\u001d\u0000\u0000\u013dO\u0001\u0000"+
		"\u0000\u0000\u013e\u013f\u0007\f\u0000\u0000\u013fQ\u0001\u0000\u0000"+
		"\u0000\u0140\u0141\u0007\r\u0000\u0000\u0141S\u0001\u0000\u0000\u0000"+
		"\u0142\u0151\u0005\u0098\u0000\u0000\u0143\u0144\u0005\u0098\u0000\u0000"+
		"\u0144\u0151\u0005\u009c\u0000\u0000\u0145\u0151\u0005\u0099\u0000\u0000"+
		"\u0146\u0147\u0005\u009c\u0000\u0000\u0147\u0151\u0005\u0099\u0000\u0000"+
		"\u0148\u0151\u0005\u009a\u0000\u0000\u0149\u014a\u0005\u009c\u0000\u0000"+
		"\u014a\u0151\u0005\u009a\u0000\u0000\u014b\u0151\u0005\u009b\u0000\u0000"+
		"\u014c\u014d\u0005\u009c\u0000\u0000\u014d\u0151\u0005\u009b\u0000\u0000"+
		"\u014e\u0151\u0005?\u0000\u0000\u014f\u0151\u0005@\u0000\u0000\u0150\u0142"+
		"\u0001\u0000\u0000\u0000\u0150\u0143\u0001\u0000\u0000\u0000\u0150\u0145"+
		"\u0001\u0000\u0000\u0000\u0150\u0146\u0001\u0000\u0000\u0000\u0150\u0148"+
		"\u0001\u0000\u0000\u0000\u0150\u0149\u0001\u0000\u0000\u0000\u0150\u014b"+
		"\u0001\u0000\u0000\u0000\u0150\u014c\u0001\u0000\u0000\u0000\u0150\u014e"+
		"\u0001\u0000\u0000\u0000\u0150\u014f\u0001\u0000\u0000\u0000\u0151U\u0001"+
		"\u0000\u0000\u0000\u0152\u0153\u0007\u000e\u0000\u0000\u0153W\u0001\u0000"+
		"\u0000\u0000\u0154\u0155\u0007\u000f\u0000\u0000\u0155Y\u0001\u0000\u0000"+
		"\u0000\u0156\u0157\u0007\u0010\u0000\u0000\u0157[\u0001\u0000\u0000\u0000"+
		"\u0158\u0159\u0007\u0011\u0000\u0000\u0159]\u0001\u0000\u0000\u0000\u015a"+
		"\u015e\u0003`0\u0000\u015b\u015e\u0003b1\u0000\u015c\u015e\u0003d2\u0000"+
		"\u015d\u015a\u0001\u0000\u0000\u0000\u015d\u015b\u0001\u0000\u0000\u0000"+
		"\u015d\u015c\u0001\u0000\u0000\u0000\u015e_\u0001\u0000\u0000\u0000\u015f"+
		"\u0160\u0007\u0012\u0000\u0000\u0160a\u0001\u0000\u0000\u0000\u0161\u0162"+
		"\u0007\u0013\u0000\u0000\u0162c\u0001\u0000\u0000\u0000\u0163\u0164\u0007"+
		"\u0014\u0000\u0000\u0164e\u0001\u0000\u0000\u0000\u0165\u0166\u0005\u008a"+
		"\u0000\u0000\u0166g\u0001\u0000\u0000\u0000\u0167\u016c\u0005\u008a\u0000"+
		"\u0000\u0168\u0169\u0005\t\u0000\u0000\u0169\u016b\u0005\u008a\u0000\u0000"+
		"\u016a\u0168\u0001\u0000\u0000\u0000\u016b\u016e\u0001\u0000\u0000\u0000"+
		"\u016c\u016a\u0001\u0000\u0000\u0000\u016c\u016d\u0001\u0000\u0000\u0000"+
		"\u016di\u0001\u0000\u0000\u0000\u016e\u016c\u0001\u0000\u0000\u0000\u016f"+
		"\u0174\u0005\u008a\u0000\u0000\u0170\u0171\u0005\n\u0000\u0000\u0171\u0173"+
		"\u0005\u008a\u0000\u0000\u0172\u0170\u0001\u0000\u0000\u0000\u0173\u0176"+
		"\u0001\u0000\u0000\u0000\u0174\u0172\u0001\u0000\u0000\u0000\u0174\u0175"+
		"\u0001\u0000\u0000\u0000\u0175k\u0001\u0000\u0000\u0000\u0176\u0174\u0001"+
		"\u0000\u0000\u0000\u0177\u017c\u0003f3\u0000\u0178\u0179\u0005\n\u0000"+
		"\u0000\u0179\u017b\u0003f3\u0000\u017a\u0178\u0001\u0000\u0000\u0000\u017b"+
		"\u017e\u0001\u0000\u0000\u0000\u017c\u017a\u0001\u0000\u0000\u0000\u017c"+
		"\u017d\u0001\u0000\u0000\u0000\u017dm\u0001\u0000\u0000\u0000\u017e\u017c"+
		"\u0001\u0000\u0000\u0000\u017f\u0184\u0003h4\u0000\u0180\u0181\u0005\n"+
		"\u0000\u0000\u0181\u0183\u0003h4\u0000\u0182\u0180\u0001\u0000\u0000\u0000"+
		"\u0183\u0186\u0001\u0000\u0000\u0000\u0184\u0182\u0001\u0000\u0000\u0000"+
		"\u0184\u0185\u0001\u0000\u0000\u0000\u0185o\u0001\u0000\u0000\u0000\u0186"+
		"\u0184\u0001\u0000\u0000\u0000\u0187\u0188\u0005\u0094\u0000\u0000\u0188"+
		"q\u0001\u0000\u0000\u0000\u0189\u018a\u0003t:\u0000\u018as\u0001\u0000"+
		"\u0000\u0000\u018b\u018e\u0003v;\u0000\u018c\u018e\u0003x<\u0000\u018d"+
		"\u018b\u0001\u0000\u0000\u0000\u018d\u018c\u0001\u0000\u0000\u0000\u018e"+
		"u\u0001\u0000\u0000\u0000\u018f\u0190\u0007\u0015\u0000\u0000\u0190w\u0001"+
		"\u0000\u0000\u0000\u0191\u019d\u0005\u0082\u0000\u0000\u0192\u019d\u0005"+
		"\u0083\u0000\u0000\u0193\u019d\u0005}\u0000\u0000\u0194\u0195\u0005\u00be"+
		"\u0000\u0000\u0195\u019d\u0003\u0094J\u0000\u0196\u019d\u0005\u00bf\u0000"+
		"\u0000\u0197\u019d\u0005\u00c0\u0000\u0000\u0198\u019d\u0005\u00c1\u0000"+
		"\u0000\u0199\u019d\u0005\u00c2\u0000\u0000\u019a\u019d\u0005\u00c3\u0000"+
		"\u0000\u019b\u019d\u0005\u00c4\u0000\u0000\u019c\u0191\u0001\u0000\u0000"+
		"\u0000\u019c\u0192\u0001\u0000\u0000\u0000\u019c\u0193\u0001\u0000\u0000"+
		"\u0000\u019c\u0194\u0001\u0000\u0000\u0000\u019c\u0196\u0001\u0000\u0000"+
		"\u0000\u019c\u0197\u0001\u0000\u0000\u0000\u019c\u0198\u0001\u0000\u0000"+
		"\u0000\u019c\u0199\u0001\u0000\u0000\u0000\u019c\u019a\u0001\u0000\u0000"+
		"\u0000\u019c\u019b\u0001\u0000\u0000\u0000\u019dy\u0001\u0000\u0000\u0000"+
		"\u019e\u019f\u0003|>\u0000\u019f{\u0001\u0000\u0000\u0000\u01a0\u01a1"+
		"\u0003~?\u0000\u01a1}\u0001\u0000\u0000\u0000\u01a2\u01a5\u0003\u0080"+
		"@\u0000\u01a3\u01a5\u0003\u0082A\u0000\u01a4\u01a2\u0001\u0000\u0000\u0000"+
		"\u01a4\u01a3\u0001\u0000\u0000\u0000\u01a5\u007f\u0001\u0000\u0000\u0000"+
		"\u01a6\u01a7\u0007\u0016\u0000\u0000\u01a7\u0081\u0001\u0000\u0000\u0000"+
		"\u01a8\u01ac\u0003\u0084B\u0000\u01a9\u01ac\u0003\u0086C\u0000\u01aa\u01ac"+
		"\u0003\u0088D\u0000\u01ab\u01a8\u0001\u0000\u0000\u0000\u01ab\u01a9\u0001"+
		"\u0000\u0000\u0000\u01ab\u01aa\u0001\u0000\u0000\u0000\u01ac\u0083\u0001"+
		"\u0000\u0000\u0000\u01ad\u01ae\u0007\u0017\u0000\u0000\u01ae\u0085\u0001"+
		"\u0000\u0000\u0000\u01af\u01b0\u0007\u0018\u0000\u0000\u01b0\u0087\u0001"+
		"\u0000\u0000\u0000\u01b1\u01b2\u0007\u0019\u0000\u0000\u01b2\u0089\u0001"+
		"\u0000\u0000\u0000\u01b3\u01b8\u0003\u0094J\u0000\u01b4\u01b5\u0005\n"+
		"\u0000\u0000\u01b5\u01b7\u0003\u0094J\u0000\u01b6\u01b4\u0001\u0000\u0000"+
		"\u0000\u01b7\u01ba\u0001\u0000\u0000\u0000\u01b8\u01b6\u0001\u0000\u0000"+
		"\u0000\u01b8\u01b9\u0001\u0000\u0000\u0000\u01b9\u008b\u0001\u0000\u0000"+
		"\u0000\u01ba\u01b8\u0001\u0000\u0000\u0000\u01bb\u01c0\u0003\u008eG\u0000"+
		"\u01bc\u01bd\u0005\n\u0000\u0000\u01bd\u01bf\u0003\u008eG\u0000\u01be"+
		"\u01bc\u0001\u0000\u0000\u0000\u01bf\u01c2\u0001\u0000\u0000\u0000\u01c0"+
		"\u01be\u0001\u0000\u0000\u0000\u01c0\u01c1\u0001\u0000\u0000\u0000\u01c1"+
		"\u008d\u0001\u0000\u0000\u0000\u01c2\u01c0\u0001\u0000\u0000\u0000\u01c3"+
		"\u01c4\u0006G\uffff\uffff\u0000\u01c4\u01cd\u0003\u0090H\u0000\u01c5\u01cd"+
		"\u0003\u0092I\u0000\u01c6\u01c7\u00030\u0018\u0000\u01c7\u01c8\u0003\u008e"+
		"G\u0002\u01c8\u01cd\u0001\u0000\u0000\u0000\u01c9\u01ca\u0003h4\u0000"+
		"\u01ca\u01cb\u0003\u0094J\u0000\u01cb\u01cd\u0001\u0000\u0000\u0000\u01cc"+
		"\u01c3\u0001\u0000\u0000\u0000\u01cc\u01c5\u0001\u0000\u0000\u0000\u01cc"+
		"\u01c6\u0001\u0000\u0000\u0000\u01cc\u01c9\u0001\u0000\u0000\u0000\u01cd"+
		"\u01dd\u0001\u0000\u0000\u0000\u01ce\u01cf\n\u0006\u0000\u0000\u01cf\u01d0"+
		"\u0005\t\u0000\u0000\u01d0\u01dc\u0003\u008eG\u0007\u01d1\u01d2\n\u0004"+
		"\u0000\u0000\u01d2\u01d3\u0005\u000b\u0000\u0000\u01d3\u01dc\u0003\u008e"+
		"G\u0005\u01d4\u01d5\n\u0005\u0000\u0000\u01d5\u01d6\u0005\u0001\u0000"+
		"\u0000\u01d6\u01d7\u0003\u008aE\u0000\u01d7\u01d8\u0005\u0002\u0000\u0000"+
		"\u01d8\u01dc\u0001\u0000\u0000\u0000\u01d9\u01da\n\u0003\u0000\u0000\u01da"+
		"\u01dc\u00032\u0019\u0000\u01db\u01ce\u0001\u0000\u0000\u0000\u01db\u01d1"+
		"\u0001\u0000\u0000\u0000\u01db\u01d4\u0001\u0000\u0000\u0000\u01db\u01d9"+
		"\u0001\u0000\u0000\u0000\u01dc\u01df\u0001\u0000\u0000\u0000\u01dd\u01db"+
		"\u0001\u0000\u0000\u0000\u01dd\u01de\u0001\u0000\u0000\u0000\u01de\u008f"+
		"\u0001\u0000\u0000\u0000\u01df\u01dd\u0001\u0000\u0000\u0000\u01e0\u01e4"+
		"\u0003r9\u0000\u01e1\u01e4\u0003p8\u0000\u01e2\u01e4\u0003h4\u0000\u01e3"+
		"\u01e0\u0001\u0000\u0000\u0000\u01e3\u01e1\u0001\u0000\u0000\u0000\u01e3"+
		"\u01e2\u0001\u0000\u0000\u0000\u01e4\u0091\u0001\u0000\u0000\u0000\u01e5"+
		"\u01e6\u0005\u0001\u0000\u0000\u01e6\u01e7\u0003\u0094J\u0000\u01e7\u01e8"+
		"\u0005\u0002\u0000\u0000\u01e8\u0093\u0001\u0000\u0000\u0000\u01e9\u01ea"+
		"\u0006J\uffff\uffff\u0000\u01ea\u01ed\u0003\u008eG\u0000\u01eb\u01ed\u0003"+
		"\u0096K\u0000\u01ec\u01e9\u0001\u0000\u0000\u0000\u01ec\u01eb\u0001\u0000"+
		"\u0000\u0000\u01ed\u0229\u0001\u0000\u0000\u0000\u01ee\u01ef\n\u000f\u0000"+
		"\u0000\u01ef\u01f0\u0003B!\u0000\u01f0\u01f1\u0003\u0094J\u0010\u01f1"+
		"\u0228\u0001\u0000\u0000\u0000\u01f2\u01f3\n\u000e\u0000\u0000\u01f3\u01f4"+
		"\u0003D\"\u0000\u01f4\u01f5\u0003\u0094J\u000f\u01f5\u0228\u0001\u0000"+
		"\u0000\u0000\u01f6\u01f7\n\r\u0000\u0000\u01f7\u01f8\u0003F#\u0000\u01f8"+
		"\u01f9\u0003\u0094J\u000e\u01f9\u0228\u0001\u0000\u0000\u0000\u01fa\u01fb"+
		"\n\f\u0000\u0000\u01fb\u01fc\u0003H$\u0000\u01fc\u01fd\u0003\u0094J\r"+
		"\u01fd\u0228\u0001\u0000\u0000\u0000\u01fe\u01ff\n\u000b\u0000\u0000\u01ff"+
		"\u0200\u0003J%\u0000\u0200\u0201\u0003\u0094J\f\u0201\u0228\u0001\u0000"+
		"\u0000\u0000\u0202\u0203\n\n\u0000\u0000\u0203\u0204\u0003L&\u0000\u0204"+
		"\u0205\u0003\u0094J\u000b\u0205\u0228\u0001\u0000\u0000\u0000\u0206\u0207"+
		"\n\t\u0000\u0000\u0207\u0208\u0003N\'\u0000\u0208\u0209\u0003\u0094J\n"+
		"\u0209\u0228\u0001\u0000\u0000\u0000\u020a\u020b\n\b\u0000\u0000\u020b"+
		"\u020c\u0003P(\u0000\u020c\u020d\u0003\u0094J\t\u020d\u0228\u0001\u0000"+
		"\u0000\u0000\u020e\u020f\n\u0007\u0000\u0000\u020f\u0210\u0003R)\u0000"+
		"\u0210\u0211\u0003\u0094J\b\u0211\u0228\u0001\u0000\u0000\u0000\u0212"+
		"\u0213\n\u0006\u0000\u0000\u0213\u0214\u0003T*\u0000\u0214\u0215\u0003"+
		"\u0094J\u0007\u0215\u0228\u0001\u0000\u0000\u0000\u0216\u0217\n\u0005"+
		"\u0000\u0000\u0217\u0218\u0003V+\u0000\u0218\u0219\u0003\u0094J\u0006"+
		"\u0219\u0228\u0001\u0000\u0000\u0000\u021a\u021b\n\u0004\u0000\u0000\u021b"+
		"\u021c\u0003X,\u0000\u021c\u021d\u0003\u0094J\u0005\u021d\u0228\u0001"+
		"\u0000\u0000\u0000\u021e\u021f\n\u0003\u0000\u0000\u021f\u0220\u0003Z"+
		"-\u0000\u0220\u0221\u0003\u0094J\u0004\u0221\u0228\u0001\u0000\u0000\u0000"+
		"\u0222\u0223\n\u0002\u0000\u0000\u0223\u0225\u0003\\.\u0000\u0224\u0226"+
		"\u0003\u0094J\u0000\u0225\u0224\u0001\u0000\u0000\u0000\u0225\u0226\u0001"+
		"\u0000\u0000\u0000\u0226\u0228\u0001\u0000\u0000\u0000\u0227\u01ee\u0001"+
		"\u0000\u0000\u0000\u0227\u01f2\u0001\u0000\u0000\u0000\u0227\u01f6\u0001"+
		"\u0000\u0000\u0000\u0227\u01fa\u0001\u0000\u0000\u0000\u0227\u01fe\u0001"+
		"\u0000\u0000\u0000\u0227\u0202\u0001\u0000\u0000\u0000\u0227\u0206\u0001"+
		"\u0000\u0000\u0000\u0227\u020a\u0001\u0000\u0000\u0000\u0227\u020e\u0001"+
		"\u0000\u0000\u0000\u0227\u0212\u0001\u0000\u0000\u0000\u0227\u0216\u0001"+
		"\u0000\u0000\u0000\u0227\u021a\u0001\u0000\u0000\u0000\u0227\u021e\u0001"+
		"\u0000\u0000\u0000\u0227\u0222\u0001\u0000\u0000\u0000\u0228\u022b\u0001"+
		"\u0000\u0000\u0000\u0229\u0227\u0001\u0000\u0000\u0000\u0229\u022a\u0001"+
		"\u0000\u0000\u0000\u022a\u0095\u0001\u0000\u0000\u0000\u022b\u0229\u0001"+
		"\u0000\u0000\u0000\u022c\u022d\u0003\u008eG\u0000\u022d\u022e\u0003^/"+
		"\u0000\u022e\u022f\u0003\u0094J\u0000\u022f\u0097\u0001\u0000\u0000\u0000"+
		"&\u009d\u00a4\u00a9\u00b6\u00ba\u00c4\u00cd\u00da\u00de\u00e3\u00ea\u00f3"+
		"\u0100\u0104\u0109\u0110\u011c\u0120\u0150\u015d\u016c\u0174\u017c\u0184"+
		"\u018d\u019c\u01a4\u01ab\u01b8\u01c0\u01cc\u01db\u01dd\u01e3\u01ec\u0225"+
		"\u0227\u0229";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}