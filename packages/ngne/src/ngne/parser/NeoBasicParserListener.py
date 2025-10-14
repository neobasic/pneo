# Generated from NeoBasicParser.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .NeoBasicParser import NeoBasicParser
else:
    from NeoBasicParser import NeoBasicParser


# This class defines a complete listener for a parse tree produced by NeoBasicParser.
class NeoBasicParserListener(ParseTreeListener):

    # Enter a parse tree produced by NeoBasicParser#neoProgram.
    def enterNeoProgram(self, ctx: NeoBasicParser.NeoProgramContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#neoProgram.
    def exitNeoProgram(self, ctx: NeoBasicParser.NeoProgramContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#instructionSentence.
    def enterInstructionSentence(self, ctx: NeoBasicParser.InstructionSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#instructionSentence.
    def exitInstructionSentence(self, ctx: NeoBasicParser.InstructionSentenceContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#declaration.
    def enterDeclaration(self, ctx: NeoBasicParser.DeclarationContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#declaration.
    def exitDeclaration(self, ctx: NeoBasicParser.DeclarationContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#constSentence.
    def enterConstSentence(self, ctx: NeoBasicParser.ConstSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constSentence.
    def exitConstSentence(self, ctx: NeoBasicParser.ConstSentenceContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#constSpecifier.
    def enterConstSpecifier(self, ctx: NeoBasicParser.ConstSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constSpecifier.
    def exitConstSpecifier(self, ctx: NeoBasicParser.ConstSpecifierContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#constClause.
    def enterConstClause(self, ctx: NeoBasicParser.ConstClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constClause.
    def exitConstClause(self, ctx: NeoBasicParser.ConstClauseContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#constDeclare.
    def enterConstDeclare(self, ctx: NeoBasicParser.ConstDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclare.
    def exitConstDeclare(self, ctx: NeoBasicParser.ConstDeclareContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#constDeclareSingle.
    def enterConstDeclareSingle(self, ctx: NeoBasicParser.ConstDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclareSingle.
    def exitConstDeclareSingle(self, ctx: NeoBasicParser.ConstDeclareSingleContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#constDeclareMultiple.
    def enterConstDeclareMultiple(self, ctx: NeoBasicParser.ConstDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclareMultiple.
    def exitConstDeclareMultiple(self, ctx: NeoBasicParser.ConstDeclareMultipleContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#constDeclareParallel.
    def enterConstDeclareParallel(self, ctx: NeoBasicParser.ConstDeclareParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclareParallel.
    def exitConstDeclareParallel(self, ctx: NeoBasicParser.ConstDeclareParallelContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#valSentence.
    def enterValSentence(self, ctx: NeoBasicParser.ValSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#valSentence.
    def exitValSentence(self, ctx: NeoBasicParser.ValSentenceContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#valSpecifier.
    def enterValSpecifier(self, ctx: NeoBasicParser.ValSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#valSpecifier.
    def exitValSpecifier(self, ctx: NeoBasicParser.ValSpecifierContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#valClause.
    def enterValClause(self, ctx: NeoBasicParser.ValClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#valClause.
    def exitValClause(self, ctx: NeoBasicParser.ValClauseContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#valDeclare.
    def enterValDeclare(self, ctx: NeoBasicParser.ValDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#valDeclare.
    def exitValDeclare(self, ctx: NeoBasicParser.ValDeclareContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#valDeclareSingle.
    def enterValDeclareSingle(self, ctx: NeoBasicParser.ValDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#valDeclareSingle.
    def exitValDeclareSingle(self, ctx: NeoBasicParser.ValDeclareSingleContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#valDeclareMultiple.
    def enterValDeclareMultiple(self, ctx: NeoBasicParser.ValDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#valDeclareMultiple.
    def exitValDeclareMultiple(self, ctx: NeoBasicParser.ValDeclareMultipleContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#valDeclareParallel.
    def enterValDeclareParallel(self, ctx: NeoBasicParser.ValDeclareParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#valDeclareParallel.
    def exitValDeclareParallel(self, ctx: NeoBasicParser.ValDeclareParallelContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#varSentence.
    def enterVarSentence(self, ctx: NeoBasicParser.VarSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varSentence.
    def exitVarSentence(self, ctx: NeoBasicParser.VarSentenceContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#varSpecifier.
    def enterVarSpecifier(self, ctx: NeoBasicParser.VarSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varSpecifier.
    def exitVarSpecifier(self, ctx: NeoBasicParser.VarSpecifierContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#varClause.
    def enterVarClause(self, ctx: NeoBasicParser.VarClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varClause.
    def exitVarClause(self, ctx: NeoBasicParser.VarClauseContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#varDeclare.
    def enterVarDeclare(self, ctx: NeoBasicParser.VarDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclare.
    def exitVarDeclare(self, ctx: NeoBasicParser.VarDeclareContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#varDeclareSingle.
    def enterVarDeclareSingle(self, ctx: NeoBasicParser.VarDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclareSingle.
    def exitVarDeclareSingle(self, ctx: NeoBasicParser.VarDeclareSingleContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#varDeclareMultiple.
    def enterVarDeclareMultiple(self, ctx: NeoBasicParser.VarDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclareMultiple.
    def exitVarDeclareMultiple(self, ctx: NeoBasicParser.VarDeclareMultipleContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#varDeclareParallel.
    def enterVarDeclareParallel(self, ctx: NeoBasicParser.VarDeclareParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclareParallel.
    def exitVarDeclareParallel(self, ctx: NeoBasicParser.VarDeclareParallelContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#prefixUnaryOperator.
    def enterPrefixUnaryOperator(self, ctx: NeoBasicParser.PrefixUnaryOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#prefixUnaryOperator.
    def exitPrefixUnaryOperator(self, ctx: NeoBasicParser.PrefixUnaryOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#posfixUnaryOperator.
    def enterPosfixUnaryOperator(self, ctx: NeoBasicParser.PosfixUnaryOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#posfixUnaryOperator.
    def exitPosfixUnaryOperator(self, ctx: NeoBasicParser.PosfixUnaryOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#unaryArithmeticOperator.
    def enterUnaryArithmeticOperator(self, ctx: NeoBasicParser.UnaryArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryArithmeticOperator.
    def exitUnaryArithmeticOperator(self, ctx: NeoBasicParser.UnaryArithmeticOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#unaryBitwiseOperator.
    def enterUnaryBitwiseOperator(self, ctx: NeoBasicParser.UnaryBitwiseOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryBitwiseOperator.
    def exitUnaryBitwiseOperator(self, ctx: NeoBasicParser.UnaryBitwiseOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#unaryLogicalOperator.
    def enterUnaryLogicalOperator(self, ctx: NeoBasicParser.UnaryLogicalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryLogicalOperator.
    def exitUnaryLogicalOperator(self, ctx: NeoBasicParser.UnaryLogicalOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def enterUnarySpreadOperator(self, ctx: NeoBasicParser.UnarySpreadOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def exitUnarySpreadOperator(self, ctx: NeoBasicParser.UnarySpreadOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#unarySortOperator.
    def enterUnarySortOperator(self, ctx: NeoBasicParser.UnarySortOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unarySortOperator.
    def exitUnarySortOperator(self, ctx: NeoBasicParser.UnarySortOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#unaryCloneOperator.
    def enterUnaryCloneOperator(self, ctx: NeoBasicParser.UnaryCloneOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryCloneOperator.
    def exitUnaryCloneOperator(self, ctx: NeoBasicParser.UnaryCloneOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def enterUnaryMetaOperator(self, ctx: NeoBasicParser.UnaryMetaOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def exitUnaryMetaOperator(self, ctx: NeoBasicParser.UnaryMetaOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryExponentialOperator.
    def enterBinaryExponentialOperator(self, ctx: NeoBasicParser.BinaryExponentialOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryExponentialOperator.
    def exitBinaryExponentialOperator(self, ctx: NeoBasicParser.BinaryExponentialOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryMultiplicativeOperator.
    def enterBinaryMultiplicativeOperator(
        self, ctx: NeoBasicParser.BinaryMultiplicativeOperatorContext
    ):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryMultiplicativeOperator.
    def exitBinaryMultiplicativeOperator(
        self, ctx: NeoBasicParser.BinaryMultiplicativeOperatorContext
    ):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryAdditiveOperator.
    def enterBinaryAdditiveOperator(self, ctx: NeoBasicParser.BinaryAdditiveOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryAdditiveOperator.
    def exitBinaryAdditiveOperator(self, ctx: NeoBasicParser.BinaryAdditiveOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#bitShiftOperator.
    def enterBitShiftOperator(self, ctx: NeoBasicParser.BitShiftOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#bitShiftOperator.
    def exitBitShiftOperator(self, ctx: NeoBasicParser.BitShiftOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#bitConjunctionOperator.
    def enterBitConjunctionOperator(self, ctx: NeoBasicParser.BitConjunctionOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#bitConjunctionOperator.
    def exitBitConjunctionOperator(self, ctx: NeoBasicParser.BitConjunctionOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#bitExclusiveDisjunctionOperator.
    def enterBitExclusiveDisjunctionOperator(
        self, ctx: NeoBasicParser.BitExclusiveDisjunctionOperatorContext
    ):
        pass

    # Exit a parse tree produced by NeoBasicParser#bitExclusiveDisjunctionOperator.
    def exitBitExclusiveDisjunctionOperator(
        self, ctx: NeoBasicParser.BitExclusiveDisjunctionOperatorContext
    ):
        pass

    # Enter a parse tree produced by NeoBasicParser#bitDisjunctionOperator.
    def enterBitDisjunctionOperator(self, ctx: NeoBasicParser.BitDisjunctionOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#bitDisjunctionOperator.
    def exitBitDisjunctionOperator(self, ctx: NeoBasicParser.BitDisjunctionOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryComparisonOperator.
    def enterBinaryComparisonOperator(self, ctx: NeoBasicParser.BinaryComparisonOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryComparisonOperator.
    def exitBinaryComparisonOperator(self, ctx: NeoBasicParser.BinaryComparisonOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryRelationalOperator.
    def enterBinaryRelationalOperator(self, ctx: NeoBasicParser.BinaryRelationalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryRelationalOperator.
    def exitBinaryRelationalOperator(self, ctx: NeoBasicParser.BinaryRelationalOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryConditionalOperator.
    def enterBinaryConditionalOperator(self, ctx: NeoBasicParser.BinaryConditionalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryConditionalOperator.
    def exitBinaryConditionalOperator(self, ctx: NeoBasicParser.BinaryConditionalOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryConjunctionOperator.
    def enterBinaryConjunctionOperator(self, ctx: NeoBasicParser.BinaryConjunctionOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryConjunctionOperator.
    def exitBinaryConjunctionOperator(self, ctx: NeoBasicParser.BinaryConjunctionOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryExclusiveDisjunctionOperator.
    def enterBinaryExclusiveDisjunctionOperator(
        self, ctx: NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext
    ):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryExclusiveDisjunctionOperator.
    def exitBinaryExclusiveDisjunctionOperator(
        self, ctx: NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext
    ):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryDisjunctionOperator.
    def enterBinaryDisjunctionOperator(self, ctx: NeoBasicParser.BinaryDisjunctionOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryDisjunctionOperator.
    def exitBinaryDisjunctionOperator(self, ctx: NeoBasicParser.BinaryDisjunctionOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#binaryCoalescingOperator.
    def enterBinaryCoalescingOperator(self, ctx: NeoBasicParser.BinaryCoalescingOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryCoalescingOperator.
    def exitBinaryCoalescingOperator(self, ctx: NeoBasicParser.BinaryCoalescingOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx: NeoBasicParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx: NeoBasicParser.AssignmentOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#singleAssignmentOperator.
    def enterSingleAssignmentOperator(self, ctx: NeoBasicParser.SingleAssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#singleAssignmentOperator.
    def exitSingleAssignmentOperator(self, ctx: NeoBasicParser.SingleAssignmentOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#multipleAssignmentOperator.
    def enterMultipleAssignmentOperator(
        self, ctx: NeoBasicParser.MultipleAssignmentOperatorContext
    ):
        pass

    # Exit a parse tree produced by NeoBasicParser#multipleAssignmentOperator.
    def exitMultipleAssignmentOperator(self, ctx: NeoBasicParser.MultipleAssignmentOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#compoundAssignmentOperator.
    def enterCompoundAssignmentOperator(
        self, ctx: NeoBasicParser.CompoundAssignmentOperatorContext
    ):
        pass

    # Exit a parse tree produced by NeoBasicParser#compoundAssignmentOperator.
    def exitCompoundAssignmentOperator(self, ctx: NeoBasicParser.CompoundAssignmentOperatorContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#symbolIdentifier.
    def enterSymbolIdentifier(self, ctx: NeoBasicParser.SymbolIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#symbolIdentifier.
    def exitSymbolIdentifier(self, ctx: NeoBasicParser.SymbolIdentifierContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx: NeoBasicParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx: NeoBasicParser.QualifiedIdentifierContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#identifiers.
    def enterIdentifiers(self, ctx: NeoBasicParser.IdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#identifiers.
    def exitIdentifiers(self, ctx: NeoBasicParser.IdentifiersContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#symbolIdentifiers.
    def enterSymbolIdentifiers(self, ctx: NeoBasicParser.SymbolIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#symbolIdentifiers.
    def exitSymbolIdentifiers(self, ctx: NeoBasicParser.SymbolIdentifiersContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def enterQualifiedIdentifiers(self, ctx: NeoBasicParser.QualifiedIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def exitQualifiedIdentifiers(self, ctx: NeoBasicParser.QualifiedIdentifiersContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#predeclaredValue.
    def enterPredeclaredValue(self, ctx: NeoBasicParser.PredeclaredValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predeclaredValue.
    def exitPredeclaredValue(self, ctx: NeoBasicParser.PredeclaredValueContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#literal.
    def enterLiteral(self, ctx: NeoBasicParser.LiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#literal.
    def exitLiteral(self, ctx: NeoBasicParser.LiteralContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#escalarLiteral.
    def enterEscalarLiteral(self, ctx: NeoBasicParser.EscalarLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#escalarLiteral.
    def exitEscalarLiteral(self, ctx: NeoBasicParser.EscalarLiteralContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx: NeoBasicParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx: NeoBasicParser.BooleanLiteralContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#numericLiteral.
    def enterNumericLiteral(self, ctx: NeoBasicParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericLiteral.
    def exitNumericLiteral(self, ctx: NeoBasicParser.NumericLiteralContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#type.
    def enterType(self, ctx: NeoBasicParser.TypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#type.
    def exitType(self, ctx: NeoBasicParser.TypeContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#nativeType.
    def enterNativeType(self, ctx: NeoBasicParser.NativeTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#nativeType.
    def exitNativeType(self, ctx: NeoBasicParser.NativeTypeContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#escalarType.
    def enterEscalarType(self, ctx: NeoBasicParser.EscalarTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#escalarType.
    def exitEscalarType(self, ctx: NeoBasicParser.EscalarTypeContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#booleanType.
    def enterBooleanType(self, ctx: NeoBasicParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#booleanType.
    def exitBooleanType(self, ctx: NeoBasicParser.BooleanTypeContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#numericType.
    def enterNumericType(self, ctx: NeoBasicParser.NumericTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericType.
    def exitNumericType(self, ctx: NeoBasicParser.NumericTypeContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#numericNatural.
    def enterNumericNatural(self, ctx: NeoBasicParser.NumericNaturalContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericNatural.
    def exitNumericNatural(self, ctx: NeoBasicParser.NumericNaturalContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#numericInteger.
    def enterNumericInteger(self, ctx: NeoBasicParser.NumericIntegerContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericInteger.
    def exitNumericInteger(self, ctx: NeoBasicParser.NumericIntegerContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#numericReal.
    def enterNumericReal(self, ctx: NeoBasicParser.NumericRealContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericReal.
    def exitNumericReal(self, ctx: NeoBasicParser.NumericRealContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#expressions.
    def enterExpressions(self, ctx: NeoBasicParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expressions.
    def exitExpressions(self, ctx: NeoBasicParser.ExpressionsContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#primaryExpressions.
    def enterPrimaryExpressions(self, ctx: NeoBasicParser.PrimaryExpressionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryExpressions.
    def exitPrimaryExpressions(self, ctx: NeoBasicParser.PrimaryExpressionsContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: NeoBasicParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: NeoBasicParser.PrimaryExpressionContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#operand.
    def enterOperand(self, ctx: NeoBasicParser.OperandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#operand.
    def exitOperand(self, ctx: NeoBasicParser.OperandContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx: NeoBasicParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx: NeoBasicParser.ParenthesizedExpressionContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#expression.
    def enterExpression(self, ctx: NeoBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expression.
    def exitExpression(self, ctx: NeoBasicParser.ExpressionContext):
        pass

    # Enter a parse tree produced by NeoBasicParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx: NeoBasicParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx: NeoBasicParser.AssignmentExpressionContext):
        pass


del NeoBasicParser
