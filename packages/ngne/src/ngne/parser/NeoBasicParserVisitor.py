# Generated from NeoBasicParser.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .NeoBasicParser import NeoBasicParser
else:
    from NeoBasicParser import NeoBasicParser

# This class defines a complete generic visitor for a parse tree produced by NeoBasicParser.


class NeoBasicParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NeoBasicParser#neoProgram.
    def visitNeoProgram(self, ctx: NeoBasicParser.NeoProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#instructionSentence.
    def visitInstructionSentence(self, ctx: NeoBasicParser.InstructionSentenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#declaration.
    def visitDeclaration(self, ctx: NeoBasicParser.DeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#constSentence.
    def visitConstSentence(self, ctx: NeoBasicParser.ConstSentenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#constSpecifier.
    def visitConstSpecifier(self, ctx: NeoBasicParser.ConstSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#constClause.
    def visitConstClause(self, ctx: NeoBasicParser.ConstClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#constDeclare.
    def visitConstDeclare(self, ctx: NeoBasicParser.ConstDeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#constDeclareSingle.
    def visitConstDeclareSingle(self, ctx: NeoBasicParser.ConstDeclareSingleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#constDeclareMultiple.
    def visitConstDeclareMultiple(self, ctx: NeoBasicParser.ConstDeclareMultipleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#constDeclareParallel.
    def visitConstDeclareParallel(self, ctx: NeoBasicParser.ConstDeclareParallelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#valSentence.
    def visitValSentence(self, ctx: NeoBasicParser.ValSentenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#valSpecifier.
    def visitValSpecifier(self, ctx: NeoBasicParser.ValSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#valClause.
    def visitValClause(self, ctx: NeoBasicParser.ValClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#valDeclare.
    def visitValDeclare(self, ctx: NeoBasicParser.ValDeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#valDeclareSingle.
    def visitValDeclareSingle(self, ctx: NeoBasicParser.ValDeclareSingleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#valDeclareMultiple.
    def visitValDeclareMultiple(self, ctx: NeoBasicParser.ValDeclareMultipleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#valDeclareParallel.
    def visitValDeclareParallel(self, ctx: NeoBasicParser.ValDeclareParallelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#varSentence.
    def visitVarSentence(self, ctx: NeoBasicParser.VarSentenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#varSpecifier.
    def visitVarSpecifier(self, ctx: NeoBasicParser.VarSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#varClause.
    def visitVarClause(self, ctx: NeoBasicParser.VarClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#varDeclare.
    def visitVarDeclare(self, ctx: NeoBasicParser.VarDeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#varDeclareSingle.
    def visitVarDeclareSingle(self, ctx: NeoBasicParser.VarDeclareSingleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#varDeclareMultiple.
    def visitVarDeclareMultiple(self, ctx: NeoBasicParser.VarDeclareMultipleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#varDeclareParallel.
    def visitVarDeclareParallel(self, ctx: NeoBasicParser.VarDeclareParallelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#prefixUnaryOperator.
    def visitPrefixUnaryOperator(self, ctx: NeoBasicParser.PrefixUnaryOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#posfixUnaryOperator.
    def visitPosfixUnaryOperator(self, ctx: NeoBasicParser.PosfixUnaryOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#unaryArithmeticOperator.
    def visitUnaryArithmeticOperator(self, ctx: NeoBasicParser.UnaryArithmeticOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#unaryBitwiseOperator.
    def visitUnaryBitwiseOperator(self, ctx: NeoBasicParser.UnaryBitwiseOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#unaryLogicalOperator.
    def visitUnaryLogicalOperator(self, ctx: NeoBasicParser.UnaryLogicalOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def visitUnarySpreadOperator(self, ctx: NeoBasicParser.UnarySpreadOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#unarySortOperator.
    def visitUnarySortOperator(self, ctx: NeoBasicParser.UnarySortOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#unaryCloneOperator.
    def visitUnaryCloneOperator(self, ctx: NeoBasicParser.UnaryCloneOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def visitUnaryMetaOperator(self, ctx: NeoBasicParser.UnaryMetaOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryExponentialOperator.
    def visitBinaryExponentialOperator(self, ctx: NeoBasicParser.BinaryExponentialOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryMultiplicativeOperator.
    def visitBinaryMultiplicativeOperator(
        self, ctx: NeoBasicParser.BinaryMultiplicativeOperatorContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryAdditiveOperator.
    def visitBinaryAdditiveOperator(self, ctx: NeoBasicParser.BinaryAdditiveOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#bitShiftOperator.
    def visitBitShiftOperator(self, ctx: NeoBasicParser.BitShiftOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#bitConjunctionOperator.
    def visitBitConjunctionOperator(self, ctx: NeoBasicParser.BitConjunctionOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#bitExclusiveDisjunctionOperator.
    def visitBitExclusiveDisjunctionOperator(
        self, ctx: NeoBasicParser.BitExclusiveDisjunctionOperatorContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#bitDisjunctionOperator.
    def visitBitDisjunctionOperator(self, ctx: NeoBasicParser.BitDisjunctionOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryComparisonOperator.
    def visitBinaryComparisonOperator(self, ctx: NeoBasicParser.BinaryComparisonOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryRelationalOperator.
    def visitBinaryRelationalOperator(self, ctx: NeoBasicParser.BinaryRelationalOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryConditionalOperator.
    def visitBinaryConditionalOperator(self, ctx: NeoBasicParser.BinaryConditionalOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryConjunctionOperator.
    def visitBinaryConjunctionOperator(self, ctx: NeoBasicParser.BinaryConjunctionOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryExclusiveDisjunctionOperator.
    def visitBinaryExclusiveDisjunctionOperator(
        self, ctx: NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryDisjunctionOperator.
    def visitBinaryDisjunctionOperator(self, ctx: NeoBasicParser.BinaryDisjunctionOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#binaryCoalescingOperator.
    def visitBinaryCoalescingOperator(self, ctx: NeoBasicParser.BinaryCoalescingOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: NeoBasicParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#singleAssignmentOperator.
    def visitSingleAssignmentOperator(self, ctx: NeoBasicParser.SingleAssignmentOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#multipleAssignmentOperator.
    def visitMultipleAssignmentOperator(
        self, ctx: NeoBasicParser.MultipleAssignmentOperatorContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#compoundAssignmentOperator.
    def visitCompoundAssignmentOperator(
        self, ctx: NeoBasicParser.CompoundAssignmentOperatorContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#symbolIdentifier.
    def visitSymbolIdentifier(self, ctx: NeoBasicParser.SymbolIdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx: NeoBasicParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#identifiers.
    def visitIdentifiers(self, ctx: NeoBasicParser.IdentifiersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#symbolIdentifiers.
    def visitSymbolIdentifiers(self, ctx: NeoBasicParser.SymbolIdentifiersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def visitQualifiedIdentifiers(self, ctx: NeoBasicParser.QualifiedIdentifiersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#predeclaredValue.
    def visitPredeclaredValue(self, ctx: NeoBasicParser.PredeclaredValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#literal.
    def visitLiteral(self, ctx: NeoBasicParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#escalarLiteral.
    def visitEscalarLiteral(self, ctx: NeoBasicParser.EscalarLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx: NeoBasicParser.BooleanLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#numericLiteral.
    def visitNumericLiteral(self, ctx: NeoBasicParser.NumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#type.
    def visitType(self, ctx: NeoBasicParser.TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#nativeType.
    def visitNativeType(self, ctx: NeoBasicParser.NativeTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#escalarType.
    def visitEscalarType(self, ctx: NeoBasicParser.EscalarTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#booleanType.
    def visitBooleanType(self, ctx: NeoBasicParser.BooleanTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#numericType.
    def visitNumericType(self, ctx: NeoBasicParser.NumericTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#numericNatural.
    def visitNumericNatural(self, ctx: NeoBasicParser.NumericNaturalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#numericInteger.
    def visitNumericInteger(self, ctx: NeoBasicParser.NumericIntegerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#numericReal.
    def visitNumericReal(self, ctx: NeoBasicParser.NumericRealContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#expressions.
    def visitExpressions(self, ctx: NeoBasicParser.ExpressionsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#primaryExpressions.
    def visitPrimaryExpressions(self, ctx: NeoBasicParser.PrimaryExpressionsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#primaryExpression.
    def visitPrimaryExpression(self, ctx: NeoBasicParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#operand.
    def visitOperand(self, ctx: NeoBasicParser.OperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx: NeoBasicParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#expression.
    def visitExpression(self, ctx: NeoBasicParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NeoBasicParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx: NeoBasicParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


del NeoBasicParser
