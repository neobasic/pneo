// Generated from /home/dever/workspace/neobasic/ngne/antlr4/NeoBasicParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link NeoBasicParser}.
 */
public interface NeoBasicParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#neoProgram}.
	 * @param ctx the parse tree
	 */
	void enterNeoProgram(NeoBasicParser.NeoProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#neoProgram}.
	 * @param ctx the parse tree
	 */
	void exitNeoProgram(NeoBasicParser.NeoProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#oneLinerProgram}.
	 * @param ctx the parse tree
	 */
	void enterOneLinerProgram(NeoBasicParser.OneLinerProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#oneLinerProgram}.
	 * @param ctx the parse tree
	 */
	void exitOneLinerProgram(NeoBasicParser.OneLinerProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#scriptFileProgram}.
	 * @param ctx the parse tree
	 */
	void enterScriptFileProgram(NeoBasicParser.ScriptFileProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#scriptFileProgram}.
	 * @param ctx the parse tree
	 */
	void exitScriptFileProgram(NeoBasicParser.ScriptFileProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#instructionSentence}.
	 * @param ctx the parse tree
	 */
	void enterInstructionSentence(NeoBasicParser.InstructionSentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#instructionSentence}.
	 * @param ctx the parse tree
	 */
	void exitInstructionSentence(NeoBasicParser.InstructionSentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#directive}.
	 * @param ctx the parse tree
	 */
	void enterDirective(NeoBasicParser.DirectiveContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#directive}.
	 * @param ctx the parse tree
	 */
	void exitDirective(NeoBasicParser.DirectiveContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#interpreterDirective}.
	 * @param ctx the parse tree
	 */
	void enterInterpreterDirective(NeoBasicParser.InterpreterDirectiveContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#interpreterDirective}.
	 * @param ctx the parse tree
	 */
	void exitInterpreterDirective(NeoBasicParser.InterpreterDirectiveContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#pragmaDirective}.
	 * @param ctx the parse tree
	 */
	void enterPragmaDirective(NeoBasicParser.PragmaDirectiveContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#pragmaDirective}.
	 * @param ctx the parse tree
	 */
	void exitPragmaDirective(NeoBasicParser.PragmaDirectiveContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#canaryTestingDirective}.
	 * @param ctx the parse tree
	 */
	void enterCanaryTestingDirective(NeoBasicParser.CanaryTestingDirectiveContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#canaryTestingDirective}.
	 * @param ctx the parse tree
	 */
	void exitCanaryTestingDirective(NeoBasicParser.CanaryTestingDirectiveContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(NeoBasicParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(NeoBasicParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#accessSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterAccessSpecifier(NeoBasicParser.AccessSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#accessSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitAccessSpecifier(NeoBasicParser.AccessSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#constSentence}.
	 * @param ctx the parse tree
	 */
	void enterConstSentence(NeoBasicParser.ConstSentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#constSentence}.
	 * @param ctx the parse tree
	 */
	void exitConstSentence(NeoBasicParser.ConstSentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#constSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterConstSpecifier(NeoBasicParser.ConstSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#constSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitConstSpecifier(NeoBasicParser.ConstSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#constClause}.
	 * @param ctx the parse tree
	 */
	void enterConstClause(NeoBasicParser.ConstClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#constClause}.
	 * @param ctx the parse tree
	 */
	void exitConstClause(NeoBasicParser.ConstClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#constDeclare}.
	 * @param ctx the parse tree
	 */
	void enterConstDeclare(NeoBasicParser.ConstDeclareContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#constDeclare}.
	 * @param ctx the parse tree
	 */
	void exitConstDeclare(NeoBasicParser.ConstDeclareContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#constDeclareSingle}.
	 * @param ctx the parse tree
	 */
	void enterConstDeclareSingle(NeoBasicParser.ConstDeclareSingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#constDeclareSingle}.
	 * @param ctx the parse tree
	 */
	void exitConstDeclareSingle(NeoBasicParser.ConstDeclareSingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#constDeclareMultiple}.
	 * @param ctx the parse tree
	 */
	void enterConstDeclareMultiple(NeoBasicParser.ConstDeclareMultipleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#constDeclareMultiple}.
	 * @param ctx the parse tree
	 */
	void exitConstDeclareMultiple(NeoBasicParser.ConstDeclareMultipleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#constDeclareParallel}.
	 * @param ctx the parse tree
	 */
	void enterConstDeclareParallel(NeoBasicParser.ConstDeclareParallelContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#constDeclareParallel}.
	 * @param ctx the parse tree
	 */
	void exitConstDeclareParallel(NeoBasicParser.ConstDeclareParallelContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valSentence}.
	 * @param ctx the parse tree
	 */
	void enterValSentence(NeoBasicParser.ValSentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valSentence}.
	 * @param ctx the parse tree
	 */
	void exitValSentence(NeoBasicParser.ValSentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterValSpecifier(NeoBasicParser.ValSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitValSpecifier(NeoBasicParser.ValSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valClause}.
	 * @param ctx the parse tree
	 */
	void enterValClause(NeoBasicParser.ValClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valClause}.
	 * @param ctx the parse tree
	 */
	void exitValClause(NeoBasicParser.ValClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valDeclare}.
	 * @param ctx the parse tree
	 */
	void enterValDeclare(NeoBasicParser.ValDeclareContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valDeclare}.
	 * @param ctx the parse tree
	 */
	void exitValDeclare(NeoBasicParser.ValDeclareContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valDeclareSingle}.
	 * @param ctx the parse tree
	 */
	void enterValDeclareSingle(NeoBasicParser.ValDeclareSingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valDeclareSingle}.
	 * @param ctx the parse tree
	 */
	void exitValDeclareSingle(NeoBasicParser.ValDeclareSingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valDeclareMultiple}.
	 * @param ctx the parse tree
	 */
	void enterValDeclareMultiple(NeoBasicParser.ValDeclareMultipleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valDeclareMultiple}.
	 * @param ctx the parse tree
	 */
	void exitValDeclareMultiple(NeoBasicParser.ValDeclareMultipleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valDeclareParallel}.
	 * @param ctx the parse tree
	 */
	void enterValDeclareParallel(NeoBasicParser.ValDeclareParallelContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valDeclareParallel}.
	 * @param ctx the parse tree
	 */
	void exitValDeclareParallel(NeoBasicParser.ValDeclareParallelContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#varSentence}.
	 * @param ctx the parse tree
	 */
	void enterVarSentence(NeoBasicParser.VarSentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#varSentence}.
	 * @param ctx the parse tree
	 */
	void exitVarSentence(NeoBasicParser.VarSentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#varSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterVarSpecifier(NeoBasicParser.VarSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#varSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitVarSpecifier(NeoBasicParser.VarSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#varClause}.
	 * @param ctx the parse tree
	 */
	void enterVarClause(NeoBasicParser.VarClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#varClause}.
	 * @param ctx the parse tree
	 */
	void exitVarClause(NeoBasicParser.VarClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#varDeclare}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclare(NeoBasicParser.VarDeclareContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#varDeclare}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclare(NeoBasicParser.VarDeclareContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#varDeclareSingle}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclareSingle(NeoBasicParser.VarDeclareSingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#varDeclareSingle}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclareSingle(NeoBasicParser.VarDeclareSingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#varDeclareMultiple}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclareMultiple(NeoBasicParser.VarDeclareMultipleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#varDeclareMultiple}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclareMultiple(NeoBasicParser.VarDeclareMultipleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#varDeclareParallel}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclareParallel(NeoBasicParser.VarDeclareParallelContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#varDeclareParallel}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclareParallel(NeoBasicParser.VarDeclareParallelContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(NeoBasicParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(NeoBasicParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void enterSimpleStatement(NeoBasicParser.SimpleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void exitSimpleStatement(NeoBasicParser.SimpleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void enterEmptyStatement(NeoBasicParser.EmptyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void exitEmptyStatement(NeoBasicParser.EmptyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(NeoBasicParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(NeoBasicParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(NeoBasicParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(NeoBasicParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#assignmentSingle}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentSingle(NeoBasicParser.AssignmentSingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#assignmentSingle}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentSingle(NeoBasicParser.AssignmentSingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#assignmentMultiple}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentMultiple(NeoBasicParser.AssignmentMultipleContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#assignmentMultiple}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentMultiple(NeoBasicParser.AssignmentMultipleContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#assignmentParallel}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentParallel(NeoBasicParser.AssignmentParallelContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#assignmentParallel}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentParallel(NeoBasicParser.AssignmentParallelContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void enterCompoundStatement(NeoBasicParser.CompoundStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void exitCompoundStatement(NeoBasicParser.CompoundStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#conditionalStatement}.
	 * @param ctx the parse tree
	 */
	void enterConditionalStatement(NeoBasicParser.ConditionalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#conditionalStatement}.
	 * @param ctx the parse tree
	 */
	void exitConditionalStatement(NeoBasicParser.ConditionalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(NeoBasicParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(NeoBasicParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#ifThenClause}.
	 * @param ctx the parse tree
	 */
	void enterIfThenClause(NeoBasicParser.IfThenClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#ifThenClause}.
	 * @param ctx the parse tree
	 */
	void exitIfThenClause(NeoBasicParser.IfThenClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unlessStatement}.
	 * @param ctx the parse tree
	 */
	void enterUnlessStatement(NeoBasicParser.UnlessStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unlessStatement}.
	 * @param ctx the parse tree
	 */
	void exitUnlessStatement(NeoBasicParser.UnlessStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unlessClause}.
	 * @param ctx the parse tree
	 */
	void enterUnlessClause(NeoBasicParser.UnlessClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unlessClause}.
	 * @param ctx the parse tree
	 */
	void exitUnlessClause(NeoBasicParser.UnlessClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#prefixUnaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterPrefixUnaryOperator(NeoBasicParser.PrefixUnaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#prefixUnaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitPrefixUnaryOperator(NeoBasicParser.PrefixUnaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#posfixUnaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterPosfixUnaryOperator(NeoBasicParser.PosfixUnaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#posfixUnaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitPosfixUnaryOperator(NeoBasicParser.PosfixUnaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unaryArithmeticOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryArithmeticOperator(NeoBasicParser.UnaryArithmeticOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unaryArithmeticOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryArithmeticOperator(NeoBasicParser.UnaryArithmeticOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unaryBitwiseOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryBitwiseOperator(NeoBasicParser.UnaryBitwiseOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unaryBitwiseOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryBitwiseOperator(NeoBasicParser.UnaryBitwiseOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unaryLogicalOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryLogicalOperator(NeoBasicParser.UnaryLogicalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unaryLogicalOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryLogicalOperator(NeoBasicParser.UnaryLogicalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unarySpreadOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnarySpreadOperator(NeoBasicParser.UnarySpreadOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unarySpreadOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnarySpreadOperator(NeoBasicParser.UnarySpreadOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unarySortOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnarySortOperator(NeoBasicParser.UnarySortOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unarySortOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnarySortOperator(NeoBasicParser.UnarySortOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unaryCloneOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryCloneOperator(NeoBasicParser.UnaryCloneOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unaryCloneOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryCloneOperator(NeoBasicParser.UnaryCloneOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#unaryMetaOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMetaOperator(NeoBasicParser.UnaryMetaOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#unaryMetaOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMetaOperator(NeoBasicParser.UnaryMetaOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryExponentialOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryExponentialOperator(NeoBasicParser.BinaryExponentialOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryExponentialOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryExponentialOperator(NeoBasicParser.BinaryExponentialOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryMultiplicativeOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryMultiplicativeOperator(NeoBasicParser.BinaryMultiplicativeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryMultiplicativeOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryMultiplicativeOperator(NeoBasicParser.BinaryMultiplicativeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryAdditiveOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryAdditiveOperator(NeoBasicParser.BinaryAdditiveOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryAdditiveOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryAdditiveOperator(NeoBasicParser.BinaryAdditiveOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#bitShiftOperator}.
	 * @param ctx the parse tree
	 */
	void enterBitShiftOperator(NeoBasicParser.BitShiftOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#bitShiftOperator}.
	 * @param ctx the parse tree
	 */
	void exitBitShiftOperator(NeoBasicParser.BitShiftOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#bitConjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void enterBitConjunctionOperator(NeoBasicParser.BitConjunctionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#bitConjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void exitBitConjunctionOperator(NeoBasicParser.BitConjunctionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#bitExclusiveDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void enterBitExclusiveDisjunctionOperator(NeoBasicParser.BitExclusiveDisjunctionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#bitExclusiveDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void exitBitExclusiveDisjunctionOperator(NeoBasicParser.BitExclusiveDisjunctionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#bitDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void enterBitDisjunctionOperator(NeoBasicParser.BitDisjunctionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#bitDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void exitBitDisjunctionOperator(NeoBasicParser.BitDisjunctionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryComparisonOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryComparisonOperator(NeoBasicParser.BinaryComparisonOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryComparisonOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryComparisonOperator(NeoBasicParser.BinaryComparisonOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryRelationalOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryRelationalOperator(NeoBasicParser.BinaryRelationalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryRelationalOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryRelationalOperator(NeoBasicParser.BinaryRelationalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryConditionalOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryConditionalOperator(NeoBasicParser.BinaryConditionalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryConditionalOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryConditionalOperator(NeoBasicParser.BinaryConditionalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryConjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryConjunctionOperator(NeoBasicParser.BinaryConjunctionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryConjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryConjunctionOperator(NeoBasicParser.BinaryConjunctionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryExclusiveDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryExclusiveDisjunctionOperator(NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryExclusiveDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryExclusiveDisjunctionOperator(NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryDisjunctionOperator(NeoBasicParser.BinaryDisjunctionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryDisjunctionOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryDisjunctionOperator(NeoBasicParser.BinaryDisjunctionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#binaryCoalescingOperator}.
	 * @param ctx the parse tree
	 */
	void enterBinaryCoalescingOperator(NeoBasicParser.BinaryCoalescingOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#binaryCoalescingOperator}.
	 * @param ctx the parse tree
	 */
	void exitBinaryCoalescingOperator(NeoBasicParser.BinaryCoalescingOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentOperator(NeoBasicParser.AssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentOperator(NeoBasicParser.AssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#singleAssignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterSingleAssignmentOperator(NeoBasicParser.SingleAssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#singleAssignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitSingleAssignmentOperator(NeoBasicParser.SingleAssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#multipleAssignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterMultipleAssignmentOperator(NeoBasicParser.MultipleAssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#multipleAssignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitMultipleAssignmentOperator(NeoBasicParser.MultipleAssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#compoundAssignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterCompoundAssignmentOperator(NeoBasicParser.CompoundAssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#compoundAssignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitCompoundAssignmentOperator(NeoBasicParser.CompoundAssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#labelIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterLabelIdentifier(NeoBasicParser.LabelIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#labelIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitLabelIdentifier(NeoBasicParser.LabelIdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#symbolIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterSymbolIdentifier(NeoBasicParser.SymbolIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#symbolIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitSymbolIdentifier(NeoBasicParser.SymbolIdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#qualifiedIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedIdentifier(NeoBasicParser.QualifiedIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#qualifiedIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedIdentifier(NeoBasicParser.QualifiedIdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#identifiers}.
	 * @param ctx the parse tree
	 */
	void enterIdentifiers(NeoBasicParser.IdentifiersContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#identifiers}.
	 * @param ctx the parse tree
	 */
	void exitIdentifiers(NeoBasicParser.IdentifiersContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#symbolIdentifiers}.
	 * @param ctx the parse tree
	 */
	void enterSymbolIdentifiers(NeoBasicParser.SymbolIdentifiersContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#symbolIdentifiers}.
	 * @param ctx the parse tree
	 */
	void exitSymbolIdentifiers(NeoBasicParser.SymbolIdentifiersContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#qualifiedIdentifiers}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedIdentifiers(NeoBasicParser.QualifiedIdentifiersContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#qualifiedIdentifiers}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedIdentifiers(NeoBasicParser.QualifiedIdentifiersContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(NeoBasicParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(NeoBasicParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#nativeType}.
	 * @param ctx the parse tree
	 */
	void enterNativeType(NeoBasicParser.NativeTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#nativeType}.
	 * @param ctx the parse tree
	 */
	void exitNativeType(NeoBasicParser.NativeTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#posfixTypeWrapper}.
	 * @param ctx the parse tree
	 */
	void enterPosfixTypeWrapper(NeoBasicParser.PosfixTypeWrapperContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#posfixTypeWrapper}.
	 * @param ctx the parse tree
	 */
	void exitPosfixTypeWrapper(NeoBasicParser.PosfixTypeWrapperContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#escalarType}.
	 * @param ctx the parse tree
	 */
	void enterEscalarType(NeoBasicParser.EscalarTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#escalarType}.
	 * @param ctx the parse tree
	 */
	void exitEscalarType(NeoBasicParser.EscalarTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#booleanType}.
	 * @param ctx the parse tree
	 */
	void enterBooleanType(NeoBasicParser.BooleanTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#booleanType}.
	 * @param ctx the parse tree
	 */
	void exitBooleanType(NeoBasicParser.BooleanTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericType}.
	 * @param ctx the parse tree
	 */
	void enterNumericType(NeoBasicParser.NumericTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericType}.
	 * @param ctx the parse tree
	 */
	void exitNumericType(NeoBasicParser.NumericTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericDigit}.
	 * @param ctx the parse tree
	 */
	void enterNumericDigit(NeoBasicParser.NumericDigitContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericDigit}.
	 * @param ctx the parse tree
	 */
	void exitNumericDigit(NeoBasicParser.NumericDigitContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericNatural}.
	 * @param ctx the parse tree
	 */
	void enterNumericNatural(NeoBasicParser.NumericNaturalContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericNatural}.
	 * @param ctx the parse tree
	 */
	void exitNumericNatural(NeoBasicParser.NumericNaturalContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericInteger}.
	 * @param ctx the parse tree
	 */
	void enterNumericInteger(NeoBasicParser.NumericIntegerContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericInteger}.
	 * @param ctx the parse tree
	 */
	void exitNumericInteger(NeoBasicParser.NumericIntegerContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericReal}.
	 * @param ctx the parse tree
	 */
	void enterNumericReal(NeoBasicParser.NumericRealContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericReal}.
	 * @param ctx the parse tree
	 */
	void exitNumericReal(NeoBasicParser.NumericRealContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericDecimal}.
	 * @param ctx the parse tree
	 */
	void enterNumericDecimal(NeoBasicParser.NumericDecimalContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericDecimal}.
	 * @param ctx the parse tree
	 */
	void exitNumericDecimal(NeoBasicParser.NumericDecimalContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericRatio}.
	 * @param ctx the parse tree
	 */
	void enterNumericRatio(NeoBasicParser.NumericRatioContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericRatio}.
	 * @param ctx the parse tree
	 */
	void exitNumericRatio(NeoBasicParser.NumericRatioContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericComplex}.
	 * @param ctx the parse tree
	 */
	void enterNumericComplex(NeoBasicParser.NumericComplexContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericComplex}.
	 * @param ctx the parse tree
	 */
	void exitNumericComplex(NeoBasicParser.NumericComplexContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericQuaternion}.
	 * @param ctx the parse tree
	 */
	void enterNumericQuaternion(NeoBasicParser.NumericQuaternionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericQuaternion}.
	 * @param ctx the parse tree
	 */
	void exitNumericQuaternion(NeoBasicParser.NumericQuaternionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#temporalType}.
	 * @param ctx the parse tree
	 */
	void enterTemporalType(NeoBasicParser.TemporalTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#temporalType}.
	 * @param ctx the parse tree
	 */
	void exitTemporalType(NeoBasicParser.TemporalTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#characterType}.
	 * @param ctx the parse tree
	 */
	void enterCharacterType(NeoBasicParser.CharacterTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#characterType}.
	 * @param ctx the parse tree
	 */
	void exitCharacterType(NeoBasicParser.CharacterTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#sequenceType}.
	 * @param ctx the parse tree
	 */
	void enterSequenceType(NeoBasicParser.SequenceTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#sequenceType}.
	 * @param ctx the parse tree
	 */
	void exitSequenceType(NeoBasicParser.SequenceTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#compositeType}.
	 * @param ctx the parse tree
	 */
	void enterCompositeType(NeoBasicParser.CompositeTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#compositeType}.
	 * @param ctx the parse tree
	 */
	void exitCompositeType(NeoBasicParser.CompositeTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#metaType}.
	 * @param ctx the parse tree
	 */
	void enterMetaType(NeoBasicParser.MetaTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#metaType}.
	 * @param ctx the parse tree
	 */
	void exitMetaType(NeoBasicParser.MetaTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#expressions}.
	 * @param ctx the parse tree
	 */
	void enterExpressions(NeoBasicParser.ExpressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#expressions}.
	 * @param ctx the parse tree
	 */
	void exitExpressions(NeoBasicParser.ExpressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#juxtapositionExpressions}.
	 * @param ctx the parse tree
	 */
	void enterJuxtapositionExpressions(NeoBasicParser.JuxtapositionExpressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#juxtapositionExpressions}.
	 * @param ctx the parse tree
	 */
	void exitJuxtapositionExpressions(NeoBasicParser.JuxtapositionExpressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#primaryExpressions}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpressions(NeoBasicParser.PrimaryExpressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#primaryExpressions}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpressions(NeoBasicParser.PrimaryExpressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(NeoBasicParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(NeoBasicParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(NeoBasicParser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(NeoBasicParser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#operand}.
	 * @param ctx the parse tree
	 */
	void enterOperand(NeoBasicParser.OperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#operand}.
	 * @param ctx the parse tree
	 */
	void exitOperand(NeoBasicParser.OperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#factScope}.
	 * @param ctx the parse tree
	 */
	void enterFactScope(NeoBasicParser.FactScopeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#factScope}.
	 * @param ctx the parse tree
	 */
	void exitFactScope(NeoBasicParser.FactScopeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#converter}.
	 * @param ctx the parse tree
	 */
	void enterConverter(NeoBasicParser.ConverterContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#converter}.
	 * @param ctx the parse tree
	 */
	void exitConverter(NeoBasicParser.ConverterContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#selector}.
	 * @param ctx the parse tree
	 */
	void enterSelector(NeoBasicParser.SelectorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#selector}.
	 * @param ctx the parse tree
	 */
	void exitSelector(NeoBasicParser.SelectorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#indexing}.
	 * @param ctx the parse tree
	 */
	void enterIndexing(NeoBasicParser.IndexingContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#indexing}.
	 * @param ctx the parse tree
	 */
	void exitIndexing(NeoBasicParser.IndexingContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#slicing}.
	 * @param ctx the parse tree
	 */
	void enterSlicing(NeoBasicParser.SlicingContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#slicing}.
	 * @param ctx the parse tree
	 */
	void exitSlicing(NeoBasicParser.SlicingContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#slicingRange}.
	 * @param ctx the parse tree
	 */
	void enterSlicingRange(NeoBasicParser.SlicingRangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#slicingRange}.
	 * @param ctx the parse tree
	 */
	void exitSlicingRange(NeoBasicParser.SlicingRangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#rangeExpression}.
	 * @param ctx the parse tree
	 */
	void enterRangeExpression(NeoBasicParser.RangeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#rangeExpression}.
	 * @param ctx the parse tree
	 */
	void exitRangeExpression(NeoBasicParser.RangeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(NeoBasicParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(NeoBasicParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression(NeoBasicParser.AssignmentExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression(NeoBasicParser.AssignmentExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#condicionalExpression}.
	 * @param ctx the parse tree
	 */
	void enterCondicionalExpression(NeoBasicParser.CondicionalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#condicionalExpression}.
	 * @param ctx the parse tree
	 */
	void exitCondicionalExpression(NeoBasicParser.CondicionalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#guardsExpression}.
	 * @param ctx the parse tree
	 */
	void enterGuardsExpression(NeoBasicParser.GuardsExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#guardsExpression}.
	 * @param ctx the parse tree
	 */
	void exitGuardsExpression(NeoBasicParser.GuardsExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#guardClause}.
	 * @param ctx the parse tree
	 */
	void enterGuardClause(NeoBasicParser.GuardClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#guardClause}.
	 * @param ctx the parse tree
	 */
	void exitGuardClause(NeoBasicParser.GuardClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#guardDefault}.
	 * @param ctx the parse tree
	 */
	void enterGuardDefault(NeoBasicParser.GuardDefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#guardDefault}.
	 * @param ctx the parse tree
	 */
	void exitGuardDefault(NeoBasicParser.GuardDefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#macroExpression}.
	 * @param ctx the parse tree
	 */
	void enterMacroExpression(NeoBasicParser.MacroExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#macroExpression}.
	 * @param ctx the parse tree
	 */
	void exitMacroExpression(NeoBasicParser.MacroExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#macroCall}.
	 * @param ctx the parse tree
	 */
	void enterMacroCall(NeoBasicParser.MacroCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#macroCall}.
	 * @param ctx the parse tree
	 */
	void exitMacroCall(NeoBasicParser.MacroCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(NeoBasicParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(NeoBasicParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#predeclaredValue}.
	 * @param ctx the parse tree
	 */
	void enterPredeclaredValue(NeoBasicParser.PredeclaredValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#predeclaredValue}.
	 * @param ctx the parse tree
	 */
	void exitPredeclaredValue(NeoBasicParser.PredeclaredValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#valueConstruct}.
	 * @param ctx the parse tree
	 */
	void enterValueConstruct(NeoBasicParser.ValueConstructContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#valueConstruct}.
	 * @param ctx the parse tree
	 */
	void exitValueConstruct(NeoBasicParser.ValueConstructContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#escalarLiteral}.
	 * @param ctx the parse tree
	 */
	void enterEscalarLiteral(NeoBasicParser.EscalarLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#escalarLiteral}.
	 * @param ctx the parse tree
	 */
	void exitEscalarLiteral(NeoBasicParser.EscalarLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteral(NeoBasicParser.BooleanLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteral(NeoBasicParser.BooleanLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void enterNumericLiteral(NeoBasicParser.NumericLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void exitNumericLiteral(NeoBasicParser.NumericLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#temporalLiteral}.
	 * @param ctx the parse tree
	 */
	void enterTemporalLiteral(NeoBasicParser.TemporalLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#temporalLiteral}.
	 * @param ctx the parse tree
	 */
	void exitTemporalLiteral(NeoBasicParser.TemporalLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#characterLiteral}.
	 * @param ctx the parse tree
	 */
	void enterCharacterLiteral(NeoBasicParser.CharacterLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#characterLiteral}.
	 * @param ctx the parse tree
	 */
	void exitCharacterLiteral(NeoBasicParser.CharacterLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#sequenceLiteral}.
	 * @param ctx the parse tree
	 */
	void enterSequenceLiteral(NeoBasicParser.SequenceLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#sequenceLiteral}.
	 * @param ctx the parse tree
	 */
	void exitSequenceLiteral(NeoBasicParser.SequenceLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#optionLiteral}.
	 * @param ctx the parse tree
	 */
	void enterOptionLiteral(NeoBasicParser.OptionLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#optionLiteral}.
	 * @param ctx the parse tree
	 */
	void exitOptionLiteral(NeoBasicParser.OptionLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#resultLiteral}.
	 * @param ctx the parse tree
	 */
	void enterResultLiteral(NeoBasicParser.ResultLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#resultLiteral}.
	 * @param ctx the parse tree
	 */
	void exitResultLiteral(NeoBasicParser.ResultLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#maybeLiteral}.
	 * @param ctx the parse tree
	 */
	void enterMaybeLiteral(NeoBasicParser.MaybeLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#maybeLiteral}.
	 * @param ctx the parse tree
	 */
	void exitMaybeLiteral(NeoBasicParser.MaybeLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#eitherLiteral}.
	 * @param ctx the parse tree
	 */
	void enterEitherLiteral(NeoBasicParser.EitherLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#eitherLiteral}.
	 * @param ctx the parse tree
	 */
	void exitEitherLiteral(NeoBasicParser.EitherLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#streamLiteral}.
	 * @param ctx the parse tree
	 */
	void enterStreamLiteral(NeoBasicParser.StreamLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#streamLiteral}.
	 * @param ctx the parse tree
	 */
	void exitStreamLiteral(NeoBasicParser.StreamLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link NeoBasicParser#loggingLevel}.
	 * @param ctx the parse tree
	 */
	void enterLoggingLevel(NeoBasicParser.LoggingLevelContext ctx);
	/**
	 * Exit a parse tree produced by {@link NeoBasicParser#loggingLevel}.
	 * @param ctx the parse tree
	 */
	void exitLoggingLevel(NeoBasicParser.LoggingLevelContext ctx);
}