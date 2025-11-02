# Generated from NeoBasicParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NeoBasicParser import NeoBasicParser
else:
    from NeoBasicParser import NeoBasicParser

# This class defines a complete generic visitor for a parse tree produced by NeoBasicParser.

class NeoBasicParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NeoBasicParser#scriptProgram.
    def visitScriptProgram(self, ctx:NeoBasicParser.ScriptProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sourceCodeProgram.
    def visitSourceCodeProgram(self, ctx:NeoBasicParser.SourceCodeProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#oneLinerProgram.
    def visitOneLinerProgram(self, ctx:NeoBasicParser.OneLinerProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#neoBasic.
    def visitNeoBasic(self, ctx:NeoBasicParser.NeoBasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#shebangInterpreter.
    def visitShebangInterpreter(self, ctx:NeoBasicParser.ShebangInterpreterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#logicalInstructionSuite.
    def visitLogicalInstructionSuite(self, ctx:NeoBasicParser.LogicalInstructionSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#logicalInstructions.
    def visitLogicalInstructions(self, ctx:NeoBasicParser.LogicalInstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#logicalInstruction.
    def visitLogicalInstruction(self, ctx:NeoBasicParser.LogicalInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#instructionSentence.
    def visitInstructionSentence(self, ctx:NeoBasicParser.InstructionSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#directive.
    def visitDirective(self, ctx:NeoBasicParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#pragmaDirective.
    def visitPragmaDirective(self, ctx:NeoBasicParser.PragmaDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#canaryTestingDirective.
    def visitCanaryTestingDirective(self, ctx:NeoBasicParser.CanaryTestingDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#testStatement.
    def visitTestStatement(self, ctx:NeoBasicParser.TestStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assertStatement.
    def visitAssertStatement(self, ctx:NeoBasicParser.AssertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#declaration.
    def visitDeclaration(self, ctx:NeoBasicParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#moduleSentence.
    def visitModuleSentence(self, ctx:NeoBasicParser.ModuleSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#moduleClause.
    def visitModuleClause(self, ctx:NeoBasicParser.ModuleClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#appletSentence.
    def visitAppletSentence(self, ctx:NeoBasicParser.AppletSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#appletClause.
    def visitAppletClause(self, ctx:NeoBasicParser.AppletClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#notabeneSentence.
    def visitNotabeneSentence(self, ctx:NeoBasicParser.NotabeneSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#notabeneClause.
    def visitNotabeneClause(self, ctx:NeoBasicParser.NotabeneClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useSentence.
    def visitUseSentence(self, ctx:NeoBasicParser.UseSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useClause.
    def visitUseClause(self, ctx:NeoBasicParser.UseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useSuite.
    def visitUseSuite(self, ctx:NeoBasicParser.UseSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useDeclareBlock.
    def visitUseDeclareBlock(self, ctx:NeoBasicParser.UseDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useDeclare.
    def visitUseDeclare(self, ctx:NeoBasicParser.UseDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useDeclareSingle.
    def visitUseDeclareSingle(self, ctx:NeoBasicParser.UseDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useDeclareMultiple.
    def visitUseDeclareMultiple(self, ctx:NeoBasicParser.UseDeclareMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useDeclareAs.
    def visitUseDeclareAs(self, ctx:NeoBasicParser.UseDeclareAsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#useDeclareOf.
    def visitUseDeclareOf(self, ctx:NeoBasicParser.UseDeclareOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeSentence.
    def visitIncludeSentence(self, ctx:NeoBasicParser.IncludeSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeClause.
    def visitIncludeClause(self, ctx:NeoBasicParser.IncludeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeSuite.
    def visitIncludeSuite(self, ctx:NeoBasicParser.IncludeSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeDeclareBlock.
    def visitIncludeDeclareBlock(self, ctx:NeoBasicParser.IncludeDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeDeclare.
    def visitIncludeDeclare(self, ctx:NeoBasicParser.IncludeDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeDeclareSingle.
    def visitIncludeDeclareSingle(self, ctx:NeoBasicParser.IncludeDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeDeclareMultiple.
    def visitIncludeDeclareMultiple(self, ctx:NeoBasicParser.IncludeDeclareMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#includeDeclareAs.
    def visitIncludeDeclareAs(self, ctx:NeoBasicParser.IncludeDeclareAsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#deflagSentence.
    def visitDeflagSentence(self, ctx:NeoBasicParser.DeflagSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defineClause.
    def visitDefineClause(self, ctx:NeoBasicParser.DefineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defineSuite.
    def visitDefineSuite(self, ctx:NeoBasicParser.DefineSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defineDeclareBlock.
    def visitDefineDeclareBlock(self, ctx:NeoBasicParser.DefineDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defineDeclare.
    def visitDefineDeclare(self, ctx:NeoBasicParser.DefineDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defineDeclareSingle.
    def visitDefineDeclareSingle(self, ctx:NeoBasicParser.DefineDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defineDeclareMultiple.
    def visitDefineDeclareMultiple(self, ctx:NeoBasicParser.DefineDeclareMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#undefClause.
    def visitUndefClause(self, ctx:NeoBasicParser.UndefClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#undefDeclare.
    def visitUndefDeclare(self, ctx:NeoBasicParser.UndefDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:NeoBasicParser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constSentence.
    def visitConstSentence(self, ctx:NeoBasicParser.ConstSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constClause.
    def visitConstClause(self, ctx:NeoBasicParser.ConstClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constSpecifier.
    def visitConstSpecifier(self, ctx:NeoBasicParser.ConstSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constSuite.
    def visitConstSuite(self, ctx:NeoBasicParser.ConstSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constDeclareBlock.
    def visitConstDeclareBlock(self, ctx:NeoBasicParser.ConstDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constDeclare.
    def visitConstDeclare(self, ctx:NeoBasicParser.ConstDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constDeclareSingle.
    def visitConstDeclareSingle(self, ctx:NeoBasicParser.ConstDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constDeclareMultiple.
    def visitConstDeclareMultiple(self, ctx:NeoBasicParser.ConstDeclareMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constDeclareParallel.
    def visitConstDeclareParallel(self, ctx:NeoBasicParser.ConstDeclareParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalSentence.
    def visitIvalSentence(self, ctx:NeoBasicParser.IvalSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalClause.
    def visitIvalClause(self, ctx:NeoBasicParser.IvalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalSpecifier.
    def visitIvalSpecifier(self, ctx:NeoBasicParser.IvalSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalSuite.
    def visitIvalSuite(self, ctx:NeoBasicParser.IvalSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalDeclareBlock.
    def visitIvalDeclareBlock(self, ctx:NeoBasicParser.IvalDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalDeclare.
    def visitIvalDeclare(self, ctx:NeoBasicParser.IvalDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalDeclareSingle.
    def visitIvalDeclareSingle(self, ctx:NeoBasicParser.IvalDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalDeclareMultiple.
    def visitIvalDeclareMultiple(self, ctx:NeoBasicParser.IvalDeclareMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ivalDeclareParallel.
    def visitIvalDeclareParallel(self, ctx:NeoBasicParser.IvalDeclareParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varSentence.
    def visitVarSentence(self, ctx:NeoBasicParser.VarSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varClause.
    def visitVarClause(self, ctx:NeoBasicParser.VarClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varSpecifier.
    def visitVarSpecifier(self, ctx:NeoBasicParser.VarSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varSuite.
    def visitVarSuite(self, ctx:NeoBasicParser.VarSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varDeclareBlock.
    def visitVarDeclareBlock(self, ctx:NeoBasicParser.VarDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varDeclare.
    def visitVarDeclare(self, ctx:NeoBasicParser.VarDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varDeclareSingle.
    def visitVarDeclareSingle(self, ctx:NeoBasicParser.VarDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varDeclareMultiple.
    def visitVarDeclareMultiple(self, ctx:NeoBasicParser.VarDeclareMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varDeclareParallel.
    def visitVarDeclareParallel(self, ctx:NeoBasicParser.VarDeclareParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#statement.
    def visitStatement(self, ctx:NeoBasicParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#simpleStatement.
    def visitSimpleStatement(self, ctx:NeoBasicParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#expressionStatement.
    def visitExpressionStatement(self, ctx:NeoBasicParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#emptyStatement.
    def visitEmptyStatement(self, ctx:NeoBasicParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:NeoBasicParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assignmentSingle.
    def visitAssignmentSingle(self, ctx:NeoBasicParser.AssignmentSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assignmentMultiple.
    def visitAssignmentMultiple(self, ctx:NeoBasicParser.AssignmentMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assignmentParallel.
    def visitAssignmentParallel(self, ctx:NeoBasicParser.AssignmentParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#consoleStatement.
    def visitConsoleStatement(self, ctx:NeoBasicParser.ConsoleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#echoCommand.
    def visitEchoCommand(self, ctx:NeoBasicParser.EchoCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#scanCommand.
    def visitScanCommand(self, ctx:NeoBasicParser.ScanCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compoundStatement.
    def visitCompoundStatement(self, ctx:NeoBasicParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#controlFlowStatement.
    def visitControlFlowStatement(self, ctx:NeoBasicParser.ControlFlowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:NeoBasicParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#otherwiseSentence.
    def visitOtherwiseSentence(self, ctx:NeoBasicParser.OtherwiseSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ifStatement.
    def visitIfStatement(self, ctx:NeoBasicParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ifThenClause.
    def visitIfThenClause(self, ctx:NeoBasicParser.IfThenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unlessStatement.
    def visitUnlessStatement(self, ctx:NeoBasicParser.UnlessStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unlessClause.
    def visitUnlessClause(self, ctx:NeoBasicParser.UnlessClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#prefixUnaryOperator.
    def visitPrefixUnaryOperator(self, ctx:NeoBasicParser.PrefixUnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unaryArithmeticOperator.
    def visitUnaryArithmeticOperator(self, ctx:NeoBasicParser.UnaryArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unaryLogicalOperator.
    def visitUnaryLogicalOperator(self, ctx:NeoBasicParser.UnaryLogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def visitUnarySpreadOperator(self, ctx:NeoBasicParser.UnarySpreadOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def visitUnaryMetaOperator(self, ctx:NeoBasicParser.UnaryMetaOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryExponentialOperator.
    def visitBinaryExponentialOperator(self, ctx:NeoBasicParser.BinaryExponentialOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryMultiplicativeOperator.
    def visitBinaryMultiplicativeOperator(self, ctx:NeoBasicParser.BinaryMultiplicativeOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryAdditiveOperator.
    def visitBinaryAdditiveOperator(self, ctx:NeoBasicParser.BinaryAdditiveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#bitShiftOperator.
    def visitBitShiftOperator(self, ctx:NeoBasicParser.BitShiftOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryConjunctionOperator.
    def visitBinaryConjunctionOperator(self, ctx:NeoBasicParser.BinaryConjunctionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryExclusiveDisjunctionOperator.
    def visitBinaryExclusiveDisjunctionOperator(self, ctx:NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryDisjunctionOperator.
    def visitBinaryDisjunctionOperator(self, ctx:NeoBasicParser.BinaryDisjunctionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryComparisonOperator.
    def visitBinaryComparisonOperator(self, ctx:NeoBasicParser.BinaryComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryRelationalOperator.
    def visitBinaryRelationalOperator(self, ctx:NeoBasicParser.BinaryRelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryConditionalOperator.
    def visitBinaryConditionalOperator(self, ctx:NeoBasicParser.BinaryConditionalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#executionFlowOperator.
    def visitExecutionFlowOperator(self, ctx:NeoBasicParser.ExecutionFlowOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryCoalescingOperator.
    def visitBinaryCoalescingOperator(self, ctx:NeoBasicParser.BinaryCoalescingOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:NeoBasicParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#singleAssignmentOperator.
    def visitSingleAssignmentOperator(self, ctx:NeoBasicParser.SingleAssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unpackingAssignmentOperator.
    def visitUnpackingAssignmentOperator(self, ctx:NeoBasicParser.UnpackingAssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compoundAssignmentOperator.
    def visitCompoundAssignmentOperator(self, ctx:NeoBasicParser.CompoundAssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#labelIdentifier.
    def visitLabelIdentifier(self, ctx:NeoBasicParser.LabelIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#symbolIdentifier.
    def visitSymbolIdentifier(self, ctx:NeoBasicParser.SymbolIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typedIdentifier.
    def visitTypedIdentifier(self, ctx:NeoBasicParser.TypedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:NeoBasicParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#identifiers.
    def visitIdentifiers(self, ctx:NeoBasicParser.IdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#symbolIdentifiers.
    def visitSymbolIdentifiers(self, ctx:NeoBasicParser.SymbolIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typedIdentifiers.
    def visitTypedIdentifiers(self, ctx:NeoBasicParser.TypedIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def visitQualifiedIdentifiers(self, ctx:NeoBasicParser.QualifiedIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#type.
    def visitType(self, ctx:NeoBasicParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#nativeType.
    def visitNativeType(self, ctx:NeoBasicParser.NativeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#posfixTypeWrapper.
    def visitPosfixTypeWrapper(self, ctx:NeoBasicParser.PosfixTypeWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#escalarType.
    def visitEscalarType(self, ctx:NeoBasicParser.EscalarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#booleanType.
    def visitBooleanType(self, ctx:NeoBasicParser.BooleanTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericType.
    def visitNumericType(self, ctx:NeoBasicParser.NumericTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericNatural.
    def visitNumericNatural(self, ctx:NeoBasicParser.NumericNaturalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericInteger.
    def visitNumericInteger(self, ctx:NeoBasicParser.NumericIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericDecimal.
    def visitNumericDecimal(self, ctx:NeoBasicParser.NumericDecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericReal.
    def visitNumericReal(self, ctx:NeoBasicParser.NumericRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericRatio.
    def visitNumericRatio(self, ctx:NeoBasicParser.NumericRatioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericComplex.
    def visitNumericComplex(self, ctx:NeoBasicParser.NumericComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericQuaternion.
    def visitNumericQuaternion(self, ctx:NeoBasicParser.NumericQuaternionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#temporalType.
    def visitTemporalType(self, ctx:NeoBasicParser.TemporalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#characterType.
    def visitCharacterType(self, ctx:NeoBasicParser.CharacterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compoundType.
    def visitCompoundType(self, ctx:NeoBasicParser.CompoundTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sequenceType.
    def visitSequenceType(self, ctx:NeoBasicParser.SequenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compositeType.
    def visitCompositeType(self, ctx:NeoBasicParser.CompositeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#collectionType.
    def visitCollectionType(self, ctx:NeoBasicParser.CollectionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#optionalType.
    def visitOptionalType(self, ctx:NeoBasicParser.OptionalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#metaType.
    def visitMetaType(self, ctx:NeoBasicParser.MetaTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#literal.
    def visitLiteral(self, ctx:NeoBasicParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#escalarLiteral.
    def visitEscalarLiteral(self, ctx:NeoBasicParser.EscalarLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:NeoBasicParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#numericLiteral.
    def visitNumericLiteral(self, ctx:NeoBasicParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#elapseLiteral.
    def visitElapseLiteral(self, ctx:NeoBasicParser.ElapseLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#dateLiteral.
    def visitDateLiteral(self, ctx:NeoBasicParser.DateLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#characterLiteral.
    def visitCharacterLiteral(self, ctx:NeoBasicParser.CharacterLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compoundLiteral.
    def visitCompoundLiteral(self, ctx:NeoBasicParser.CompoundLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sequenceLiteral.
    def visitSequenceLiteral(self, ctx:NeoBasicParser.SequenceLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#shellPathLiteral.
    def visitShellPathLiteral(self, ctx:NeoBasicParser.ShellPathLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#optionalLiteral.
    def visitOptionalLiteral(self, ctx:NeoBasicParser.OptionalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#resultLiteral.
    def visitResultLiteral(self, ctx:NeoBasicParser.ResultLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#maybeLiteral.
    def visitMaybeLiteral(self, ctx:NeoBasicParser.MaybeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#eitherLiteral.
    def visitEitherLiteral(self, ctx:NeoBasicParser.EitherLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#streamLiteral.
    def visitStreamLiteral(self, ctx:NeoBasicParser.StreamLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#predeclaredValue.
    def visitPredeclaredValue(self, ctx:NeoBasicParser.PredeclaredValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#operand.
    def visitOperand(self, ctx:NeoBasicParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:NeoBasicParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#slicingRange.
    def visitSlicingRange(self, ctx:NeoBasicParser.SlicingRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#intervalExpression.
    def visitIntervalExpression(self, ctx:NeoBasicParser.IntervalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sliceExpression.
    def visitSliceExpression(self, ctx:NeoBasicParser.SliceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#factScope.
    def visitFactScope(self, ctx:NeoBasicParser.FactScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#expression.
    def visitExpression(self, ctx:NeoBasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sos_Expression.
    def visitSos_Expression(self, ctx:NeoBasicParser.Sos_ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:NeoBasicParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#condicionalExpression.
    def visitCondicionalExpression(self, ctx:NeoBasicParser.CondicionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#guardsExpression.
    def visitGuardsExpression(self, ctx:NeoBasicParser.GuardsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#guardClause.
    def visitGuardClause(self, ctx:NeoBasicParser.GuardClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#guardDefault.
    def visitGuardDefault(self, ctx:NeoBasicParser.GuardDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#macroExpression.
    def visitMacroExpression(self, ctx:NeoBasicParser.MacroExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#macroCall.
    def visitMacroCall(self, ctx:NeoBasicParser.MacroCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:NeoBasicParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#primaryExpressions.
    def visitPrimaryExpressions(self, ctx:NeoBasicParser.PrimaryExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#expressions.
    def visitExpressions(self, ctx:NeoBasicParser.ExpressionsContext):
        return self.visitChildren(ctx)



del NeoBasicParser