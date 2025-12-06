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


    # Visit a parse tree produced by NeoBasicParser#logicalInstructions.
    def visitLogicalInstructions(self, ctx:NeoBasicParser.LogicalInstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#logicalInstructionSuite.
    def visitLogicalInstructionSuite(self, ctx:NeoBasicParser.LogicalInstructionSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#logicalInstruction.
    def visitLogicalInstruction(self, ctx:NeoBasicParser.LogicalInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#directiveInstructionLiner.
    def visitDirectiveInstructionLiner(self, ctx:NeoBasicParser.DirectiveInstructionLinerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#directiveInstructionSuite.
    def visitDirectiveInstructionSuite(self, ctx:NeoBasicParser.DirectiveInstructionSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#instructionSentence.
    def visitInstructionSentence(self, ctx:NeoBasicParser.InstructionSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#shebangInterpreter.
    def visitShebangInterpreter(self, ctx:NeoBasicParser.ShebangInterpreterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#directiveSentence.
    def visitDirectiveSentence(self, ctx:NeoBasicParser.DirectiveSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compilerPragmaDirective.
    def visitCompilerPragmaDirective(self, ctx:NeoBasicParser.CompilerPragmaDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#shellLookupDirective.
    def visitShellLookupDirective(self, ctx:NeoBasicParser.ShellLookupDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#lookupStatement.
    def visitLookupStatement(self, ctx:NeoBasicParser.LookupStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#canaryTestingDirective.
    def visitCanaryTestingDirective(self, ctx:NeoBasicParser.CanaryTestingDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#testingLine.
    def visitTestingLine(self, ctx:NeoBasicParser.TestingLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#testingBlock.
    def visitTestingBlock(self, ctx:NeoBasicParser.TestingBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#labelIdentifier.
    def visitLabelIdentifier(self, ctx:NeoBasicParser.LabelIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:NeoBasicParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#decoratedIdentifier.
    def visitDecoratedIdentifier(self, ctx:NeoBasicParser.DecoratedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#decoratedType.
    def visitDecoratedType(self, ctx:NeoBasicParser.DecoratedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typedDecoratedIdentifier.
    def visitTypedDecoratedIdentifier(self, ctx:NeoBasicParser.TypedDecoratedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#inferredDecoratedIdentifier.
    def visitInferredDecoratedIdentifier(self, ctx:NeoBasicParser.InferredDecoratedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#genericDecoratedIdentifier.
    def visitGenericDecoratedIdentifier(self, ctx:NeoBasicParser.GenericDecoratedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#declarationIdentifier.
    def visitDeclarationIdentifier(self, ctx:NeoBasicParser.DeclarationIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#identifiers.
    def visitIdentifiers(self, ctx:NeoBasicParser.IdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def visitQualifiedIdentifiers(self, ctx:NeoBasicParser.QualifiedIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#decoratedIdentifiers.
    def visitDecoratedIdentifiers(self, ctx:NeoBasicParser.DecoratedIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#decoratedTypes.
    def visitDecoratedTypes(self, ctx:NeoBasicParser.DecoratedTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typedDecoratedIdentifiers.
    def visitTypedDecoratedIdentifiers(self, ctx:NeoBasicParser.TypedDecoratedIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#inferredDecoratedIdentifiers.
    def visitInferredDecoratedIdentifiers(self, ctx:NeoBasicParser.InferredDecoratedIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#topLevelSentence.
    def visitTopLevelSentence(self, ctx:NeoBasicParser.TopLevelSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#identificationSentence.
    def visitIdentificationSentence(self, ctx:NeoBasicParser.IdentificationSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#appletClause.
    def visitAppletClause(self, ctx:NeoBasicParser.AppletClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#moduleClause.
    def visitModuleClause(self, ctx:NeoBasicParser.ModuleClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#notabeneClause.
    def visitNotabeneClause(self, ctx:NeoBasicParser.NotabeneClauseContext):
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


    # Visit a parse tree produced by NeoBasicParser#undefSuite.
    def visitUndefSuite(self, ctx:NeoBasicParser.UndefSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#undefDeclareBlock.
    def visitUndefDeclareBlock(self, ctx:NeoBasicParser.UndefDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#undefDeclare.
    def visitUndefDeclare(self, ctx:NeoBasicParser.UndefDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defAtom.
    def visitDefAtom(self, ctx:NeoBasicParser.DefAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defAtoms.
    def visitDefAtoms(self, ctx:NeoBasicParser.DefAtomsContext):
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


    # Visit a parse tree produced by NeoBasicParser#interfaceSentence.
    def visitInterfaceSentence(self, ctx:NeoBasicParser.InterfaceSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#interfaceClause.
    def visitInterfaceClause(self, ctx:NeoBasicParser.InterfaceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#interfaceBody.
    def visitInterfaceBody(self, ctx:NeoBasicParser.InterfaceBodyContext):
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


    # Visit a parse tree produced by NeoBasicParser#declarationSentence.
    def visitDeclarationSentence(self, ctx:NeoBasicParser.DeclarationSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#adhocMetadata.
    def visitAdhocMetadata(self, ctx:NeoBasicParser.AdhocMetadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#metadataDecorators.
    def visitMetadataDecorators(self, ctx:NeoBasicParser.MetadataDecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#metadataGenerics.
    def visitMetadataGenerics(self, ctx:NeoBasicParser.MetadataGenericsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#visibilityModifier.
    def visitVisibilityModifier(self, ctx:NeoBasicParser.VisibilityModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#visibilityLabelSuite.
    def visitVisibilityLabelSuite(self, ctx:NeoBasicParser.VisibilityLabelSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#extendsClause.
    def visitExtendsClause(self, ctx:NeoBasicParser.ExtendsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#implementsClause.
    def visitImplementsClause(self, ctx:NeoBasicParser.ImplementsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#mixesClause.
    def visitMixesClause(self, ctx:NeoBasicParser.MixesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#raisesClause.
    def visitRaisesClause(self, ctx:NeoBasicParser.RaisesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#parenthesizedArguments.
    def visitParenthesizedArguments(self, ctx:NeoBasicParser.ParenthesizedArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#namedArguments.
    def visitNamedArguments(self, ctx:NeoBasicParser.NamedArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#namedArgument.
    def visitNamedArgument(self, ctx:NeoBasicParser.NamedArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#parenthesizedParameters.
    def visitParenthesizedParameters(self, ctx:NeoBasicParser.ParenthesizedParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procParameters.
    def visitProcParameters(self, ctx:NeoBasicParser.ProcParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procParameter.
    def visitProcParameter(self, ctx:NeoBasicParser.ProcParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#modeParameterSpecifier.
    def visitModeParameterSpecifier(self, ctx:NeoBasicParser.ModeParameterSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#prefixParameterName.
    def visitPrefixParameterName(self, ctx:NeoBasicParser.PrefixParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#prefixParameterType.
    def visitPrefixParameterType(self, ctx:NeoBasicParser.PrefixParameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procResultType.
    def visitProcResultType(self, ctx:NeoBasicParser.ProcResultTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procBody.
    def visitProcBody(self, ctx:NeoBasicParser.ProcBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procSuite.
    def visitProcSuite(self, ctx:NeoBasicParser.ProcSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procSemex.
    def visitProcSemex(self, ctx:NeoBasicParser.ProcSemexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procSpecifier.
    def visitProcSpecifier(self, ctx:NeoBasicParser.ProcSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procImplicitReturn.
    def visitProcImplicitReturn(self, ctx:NeoBasicParser.ProcImplicitReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procPatternGuards.
    def visitProcPatternGuards(self, ctx:NeoBasicParser.ProcPatternGuardsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#guardBranchClause.
    def visitGuardBranchClause(self, ctx:NeoBasicParser.GuardBranchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#guardElseClause.
    def visitGuardElseClause(self, ctx:NeoBasicParser.GuardElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#outerDeclareSentence.
    def visitOuterDeclareSentence(self, ctx:NeoBasicParser.OuterDeclareSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeSentence.
    def visitTypeSentence(self, ctx:NeoBasicParser.TypeSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeClause.
    def visitTypeClause(self, ctx:NeoBasicParser.TypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeSuite.
    def visitTypeSuite(self, ctx:NeoBasicParser.TypeSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeDeclareBlock.
    def visitTypeDeclareBlock(self, ctx:NeoBasicParser.TypeDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeDeclare.
    def visitTypeDeclare(self, ctx:NeoBasicParser.TypeDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeDeclareSingle.
    def visitTypeDeclareSingle(self, ctx:NeoBasicParser.TypeDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeDeclareSubrange.
    def visitTypeDeclareSubrange(self, ctx:NeoBasicParser.TypeDeclareSubrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constSentence.
    def visitConstSentence(self, ctx:NeoBasicParser.ConstSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constClause.
    def visitConstClause(self, ctx:NeoBasicParser.ConstClauseContext):
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


    # Visit a parse tree produced by NeoBasicParser#letSentence.
    def visitLetSentence(self, ctx:NeoBasicParser.LetSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#letClause.
    def visitLetClause(self, ctx:NeoBasicParser.LetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#letSuite.
    def visitLetSuite(self, ctx:NeoBasicParser.LetSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#letDeclareBlock.
    def visitLetDeclareBlock(self, ctx:NeoBasicParser.LetDeclareBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#letDeclare.
    def visitLetDeclare(self, ctx:NeoBasicParser.LetDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#letDeclareSingle.
    def visitLetDeclareSingle(self, ctx:NeoBasicParser.LetDeclareSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#letDeclareMultiple.
    def visitLetDeclareMultiple(self, ctx:NeoBasicParser.LetDeclareMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#letDeclareParallel.
    def visitLetDeclareParallel(self, ctx:NeoBasicParser.LetDeclareParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varSentence.
    def visitVarSentence(self, ctx:NeoBasicParser.VarSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#varClause.
    def visitVarClause(self, ctx:NeoBasicParser.VarClauseContext):
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


    # Visit a parse tree produced by NeoBasicParser#castSentence.
    def visitCastSentence(self, ctx:NeoBasicParser.CastSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#castClause.
    def visitCastClause(self, ctx:NeoBasicParser.CastClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#castBody.
    def visitCastBody(self, ctx:NeoBasicParser.CastBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#factSentence.
    def visitFactSentence(self, ctx:NeoBasicParser.FactSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#factClause.
    def visitFactClause(self, ctx:NeoBasicParser.FactClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#macroSentence.
    def visitMacroSentence(self, ctx:NeoBasicParser.MacroSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#macroClause.
    def visitMacroClause(self, ctx:NeoBasicParser.MacroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#funcSentence.
    def visitFuncSentence(self, ctx:NeoBasicParser.FuncSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#funcClause.
    def visitFuncClause(self, ctx:NeoBasicParser.FuncClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#feedSentence.
    def visitFeedSentence(self, ctx:NeoBasicParser.FeedSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#feedClause.
    def visitFeedClause(self, ctx:NeoBasicParser.FeedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#subSentence.
    def visitSubSentence(self, ctx:NeoBasicParser.SubSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#subClause.
    def visitSubClause(self, ctx:NeoBasicParser.SubClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#operatorSentence.
    def visitOperatorSentence(self, ctx:NeoBasicParser.OperatorSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#operatorClause.
    def visitOperatorClause(self, ctx:NeoBasicParser.OperatorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#operatorIdentifier.
    def visitOperatorIdentifier(self, ctx:NeoBasicParser.OperatorIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#declarationOperator.
    def visitDeclarationOperator(self, ctx:NeoBasicParser.DeclarationOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#eventSentence.
    def visitEventSentence(self, ctx:NeoBasicParser.EventSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#eventClause.
    def visitEventClause(self, ctx:NeoBasicParser.EventClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#bracketedParameters.
    def visitBracketedParameters(self, ctx:NeoBasicParser.BracketedParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumSentence.
    def visitEnumSentence(self, ctx:NeoBasicParser.EnumSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumClause.
    def visitEnumClause(self, ctx:NeoBasicParser.EnumClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumType.
    def visitEnumType(self, ctx:NeoBasicParser.EnumTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumBody.
    def visitEnumBody(self, ctx:NeoBasicParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumSemex.
    def visitEnumSemex(self, ctx:NeoBasicParser.EnumSemexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumSuite.
    def visitEnumSuite(self, ctx:NeoBasicParser.EnumSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumMembersBlock.
    def visitEnumMembersBlock(self, ctx:NeoBasicParser.EnumMembersBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumMember.
    def visitEnumMember(self, ctx:NeoBasicParser.EnumMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumFieldSingle.
    def visitEnumFieldSingle(self, ctx:NeoBasicParser.EnumFieldSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#enumFieldMultiple.
    def visitEnumFieldMultiple(self, ctx:NeoBasicParser.EnumFieldMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structSentence.
    def visitStructSentence(self, ctx:NeoBasicParser.StructSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structClause.
    def visitStructClause(self, ctx:NeoBasicParser.StructClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structBody.
    def visitStructBody(self, ctx:NeoBasicParser.StructBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structSemex.
    def visitStructSemex(self, ctx:NeoBasicParser.StructSemexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structSuite.
    def visitStructSuite(self, ctx:NeoBasicParser.StructSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structMembersBlock.
    def visitStructMembersBlock(self, ctx:NeoBasicParser.StructMembersBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structMember.
    def visitStructMember(self, ctx:NeoBasicParser.StructMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structFieldSingle.
    def visitStructFieldSingle(self, ctx:NeoBasicParser.StructFieldSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#attributeTag.
    def visitAttributeTag(self, ctx:NeoBasicParser.AttributeTagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structFieldMultiple.
    def visitStructFieldMultiple(self, ctx:NeoBasicParser.StructFieldMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#structMemberEmbedded.
    def visitStructMemberEmbedded(self, ctx:NeoBasicParser.StructMemberEmbeddedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#protoSentence.
    def visitProtoSentence(self, ctx:NeoBasicParser.ProtoSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#protoClause.
    def visitProtoClause(self, ctx:NeoBasicParser.ProtoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#protoBody.
    def visitProtoBody(self, ctx:NeoBasicParser.ProtoBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#traitSentence.
    def visitTraitSentence(self, ctx:NeoBasicParser.TraitSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#traitClause.
    def visitTraitClause(self, ctx:NeoBasicParser.TraitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#traitBody.
    def visitTraitBody(self, ctx:NeoBasicParser.TraitBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classSentence.
    def visitClassSentence(self, ctx:NeoBasicParser.ClassSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classClause.
    def visitClassClause(self, ctx:NeoBasicParser.ClassClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classBody.
    def visitClassBody(self, ctx:NeoBasicParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classSemex.
    def visitClassSemex(self, ctx:NeoBasicParser.ClassSemexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classFieldMultiple.
    def visitClassFieldMultiple(self, ctx:NeoBasicParser.ClassFieldMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classFieldSimple.
    def visitClassFieldSimple(self, ctx:NeoBasicParser.ClassFieldSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classSuite.
    def visitClassSuite(self, ctx:NeoBasicParser.ClassSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#objectSentence.
    def visitObjectSentence(self, ctx:NeoBasicParser.ObjectSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#objectClause.
    def visitObjectClause(self, ctx:NeoBasicParser.ObjectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#objectBody.
    def visitObjectBody(self, ctx:NeoBasicParser.ObjectBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#innerDeclareSentence.
    def visitInnerDeclareSentence(self, ctx:NeoBasicParser.InnerDeclareSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constructSentence.
    def visitConstructSentence(self, ctx:NeoBasicParser.ConstructSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#constructClause.
    def visitConstructClause(self, ctx:NeoBasicParser.ConstructClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classInitializer.
    def visitClassInitializer(self, ctx:NeoBasicParser.ClassInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classInitializingMembers.
    def visitClassInitializingMembers(self, ctx:NeoBasicParser.ClassInitializingMembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#classInitializingMember.
    def visitClassInitializingMember(self, ctx:NeoBasicParser.ClassInitializingMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#destructSentence.
    def visitDestructSentence(self, ctx:NeoBasicParser.DestructSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#destructClause.
    def visitDestructClause(self, ctx:NeoBasicParser.DestructClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#propertySentence.
    def visitPropertySentence(self, ctx:NeoBasicParser.PropertySentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#propertyClause.
    def visitPropertyClause(self, ctx:NeoBasicParser.PropertyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#propertyBody.
    def visitPropertyBody(self, ctx:NeoBasicParser.PropertyBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#propertyAccessorSentence.
    def visitPropertyAccessorSentence(self, ctx:NeoBasicParser.PropertyAccessorSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#propertyGetterClause.
    def visitPropertyGetterClause(self, ctx:NeoBasicParser.PropertyGetterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#propertySetterClause.
    def visitPropertySetterClause(self, ctx:NeoBasicParser.PropertySetterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#statementSentence.
    def visitStatementSentence(self, ctx:NeoBasicParser.StatementSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#statementSuite.
    def visitStatementSuite(self, ctx:NeoBasicParser.StatementSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#statementBlock.
    def visitStatementBlock(self, ctx:NeoBasicParser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#clauseStatement.
    def visitClauseStatement(self, ctx:NeoBasicParser.ClauseStatementContext):
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


    # Visit a parse tree produced by NeoBasicParser#atClause.
    def visitAtClause(self, ctx:NeoBasicParser.AtClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#echoCommand.
    def visitEchoCommand(self, ctx:NeoBasicParser.EchoCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#scanCommand.
    def visitScanCommand(self, ctx:NeoBasicParser.ScanCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#alertCommand.
    def visitAlertCommand(self, ctx:NeoBasicParser.AlertCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#entryCommand.
    def visitEntryCommand(self, ctx:NeoBasicParser.EntryCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#playCommand.
    def visitPlayCommand(self, ctx:NeoBasicParser.PlayCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#deterministicStatement.
    def visitDeterministicStatement(self, ctx:NeoBasicParser.DeterministicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#deferSentence.
    def visitDeferSentence(self, ctx:NeoBasicParser.DeferSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#raiseSentence.
    def visitRaiseSentence(self, ctx:NeoBasicParser.RaiseSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#panicSentence.
    def visitPanicSentence(self, ctx:NeoBasicParser.PanicSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#exitSentence.
    def visitExitSentence(self, ctx:NeoBasicParser.ExitSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#continueSentence.
    def visitContinueSentence(self, ctx:NeoBasicParser.ContinueSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#breakSentence.
    def visitBreakSentence(self, ctx:NeoBasicParser.BreakSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#fallthroughSentence.
    def visitFallthroughSentence(self, ctx:NeoBasicParser.FallthroughSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#returnSentence.
    def visitReturnSentence(self, ctx:NeoBasicParser.ReturnSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#yieldSentence.
    def visitYieldSentence(self, ctx:NeoBasicParser.YieldSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#nondeterministicStatement.
    def visitNondeterministicStatement(self, ctx:NeoBasicParser.NondeterministicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ifThenSentence.
    def visitIfThenSentence(self, ctx:NeoBasicParser.IfThenSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#goSentence.
    def visitGoSentence(self, ctx:NeoBasicParser.GoSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#awaitSentence.
    def visitAwaitSentence(self, ctx:NeoBasicParser.AwaitSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compoundStatement.
    def visitCompoundStatement(self, ctx:NeoBasicParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:NeoBasicParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#iterationStatement.
    def visitIterationStatement(self, ctx:NeoBasicParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#controlFlowStatement.
    def visitControlFlowStatement(self, ctx:NeoBasicParser.ControlFlowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#concurrencyStatement.
    def visitConcurrencyStatement(self, ctx:NeoBasicParser.ConcurrencyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ifSentence.
    def visitIfSentence(self, ctx:NeoBasicParser.IfSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#ifClause.
    def visitIfClause(self, ctx:NeoBasicParser.IfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#elifClause.
    def visitElifClause(self, ctx:NeoBasicParser.ElifClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#elseClause.
    def visitElseClause(self, ctx:NeoBasicParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#matchSentence.
    def visitMatchSentence(self, ctx:NeoBasicParser.MatchSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#matchClause.
    def visitMatchClause(self, ctx:NeoBasicParser.MatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#caseClause.
    def visitCaseClause(self, ctx:NeoBasicParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#trySentence.
    def visitTrySentence(self, ctx:NeoBasicParser.TrySentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#tryClause.
    def visitTryClause(self, ctx:NeoBasicParser.TryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#catchClause.
    def visitCatchClause(self, ctx:NeoBasicParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#switchSentence.
    def visitSwitchSentence(self, ctx:NeoBasicParser.SwitchSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#switchClause.
    def visitSwitchClause(self, ctx:NeoBasicParser.SwitchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#whenClause.
    def visitWhenClause(self, ctx:NeoBasicParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#defaultClause.
    def visitDefaultClause(self, ctx:NeoBasicParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopSentence.
    def visitLoopSentence(self, ctx:NeoBasicParser.LoopSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopClause.
    def visitLoopClause(self, ctx:NeoBasicParser.LoopClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopBody.
    def visitLoopBody(self, ctx:NeoBasicParser.LoopBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopNoCheck.
    def visitLoopNoCheck(self, ctx:NeoBasicParser.LoopNoCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopCheckFirst.
    def visitLoopCheckFirst(self, ctx:NeoBasicParser.LoopCheckFirstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopCheckLast.
    def visitLoopCheckLast(self, ctx:NeoBasicParser.LoopCheckLastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#nextClause.
    def visitNextClause(self, ctx:NeoBasicParser.NextClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#uptoClause.
    def visitUptoClause(self, ctx:NeoBasicParser.UptoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#pretestClause.
    def visitPretestClause(self, ctx:NeoBasicParser.PretestClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#posttestClause.
    def visitPosttestClause(self, ctx:NeoBasicParser.PosttestClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopEachClause.
    def visitLoopEachClause(self, ctx:NeoBasicParser.LoopEachClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopWhileClause.
    def visitLoopWhileClause(self, ctx:NeoBasicParser.LoopWhileClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#loopUntilClause.
    def visitLoopUntilClause(self, ctx:NeoBasicParser.LoopUntilClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#thenClause.
    def visitThenClause(self, ctx:NeoBasicParser.ThenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#beginSentence.
    def visitBeginSentence(self, ctx:NeoBasicParser.BeginSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#beginClause.
    def visitBeginClause(self, ctx:NeoBasicParser.BeginClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#endClause.
    def visitEndClause(self, ctx:NeoBasicParser.EndClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#withSentence.
    def visitWithSentence(self, ctx:NeoBasicParser.WithSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#withClause.
    def visitWithClause(self, ctx:NeoBasicParser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#gosubSentence.
    def visitGosubSentence(self, ctx:NeoBasicParser.GosubSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#gosubClause.
    def visitGosubClause(self, ctx:NeoBasicParser.GosubClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#forkClause.
    def visitForkClause(self, ctx:NeoBasicParser.ForkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#forEachClause.
    def visitForEachClause(self, ctx:NeoBasicParser.ForEachClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#testingStatement.
    def visitTestingStatement(self, ctx:NeoBasicParser.TestingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#simpleTestStatement.
    def visitSimpleTestStatement(self, ctx:NeoBasicParser.SimpleTestStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compoundTestStatement.
    def visitCompoundTestStatement(self, ctx:NeoBasicParser.CompoundTestStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assertTestStatement.
    def visitAssertTestStatement(self, ctx:NeoBasicParser.AssertTestStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assertClause.
    def visitAssertClause(self, ctx:NeoBasicParser.AssertClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unitTestStatement.
    def visitUnitTestStatement(self, ctx:NeoBasicParser.UnitTestStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unitClause.
    def visitUnitClause(self, ctx:NeoBasicParser.UnitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#fromClause.
    def visitFromClause(self, ctx:NeoBasicParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#onceClause.
    def visitOnceClause(self, ctx:NeoBasicParser.OnceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#dataClause.
    def visitDataClause(self, ctx:NeoBasicParser.DataClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#dataTable.
    def visitDataTable(self, ctx:NeoBasicParser.DataTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#dataRow.
    def visitDataRow(self, ctx:NeoBasicParser.DataRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#callClause.
    def visitCallClause(self, ctx:NeoBasicParser.CallClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#hideClause.
    def visitHideClause(self, ctx:NeoBasicParser.HideClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#showClause.
    def visitShowClause(self, ctx:NeoBasicParser.ShowClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#stayClause.
    def visitStayClause(self, ctx:NeoBasicParser.StayClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#passClause.
    def visitPassClause(self, ctx:NeoBasicParser.PassClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#pastClause.
    def visitPastClause(self, ctx:NeoBasicParser.PastClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#failClause.
    def visitFailClause(self, ctx:NeoBasicParser.FailClauseContext):
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


    # Visit a parse tree produced by NeoBasicParser#unaryArrayOperator.
    def visitUnaryArrayOperator(self, ctx:NeoBasicParser.UnaryArrayOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def visitUnarySpreadOperator(self, ctx:NeoBasicParser.UnarySpreadOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unaryCloneOperator.
    def visitUnaryCloneOperator(self, ctx:NeoBasicParser.UnaryCloneOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unaryMoveOperator.
    def visitUnaryMoveOperator(self, ctx:NeoBasicParser.UnaryMoveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def visitUnaryMetaOperator(self, ctx:NeoBasicParser.UnaryMetaOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryArithmeticOperator.
    def visitBinaryArithmeticOperator(self, ctx:NeoBasicParser.BinaryArithmeticOperatorContext):
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


    # Visit a parse tree produced by NeoBasicParser#binaryArrayOperator.
    def visitBinaryArrayOperator(self, ctx:NeoBasicParser.BinaryArrayOperatorContext):
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


    # Visit a parse tree produced by NeoBasicParser#binaryMonadBindOperator.
    def visitBinaryMonadBindOperator(self, ctx:NeoBasicParser.BinaryMonadBindOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#binaryPipelineOperator.
    def visitBinaryPipelineOperator(self, ctx:NeoBasicParser.BinaryPipelineOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#coalescingOperator.
    def visitCoalescingOperator(self, ctx:NeoBasicParser.CoalescingOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#executionFlowOperator.
    def visitExecutionFlowOperator(self, ctx:NeoBasicParser.ExecutionFlowOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#intervalOperator.
    def visitIntervalOperator(self, ctx:NeoBasicParser.IntervalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#leftIntervalOperator.
    def visitLeftIntervalOperator(self, ctx:NeoBasicParser.LeftIntervalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#rightIntervalOperator.
    def visitRightIntervalOperator(self, ctx:NeoBasicParser.RightIntervalOperatorContext):
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


    # Visit a parse tree produced by NeoBasicParser#overloadableOperator.
    def visitOverloadableOperator(self, ctx:NeoBasicParser.OverloadableOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#symbolDecorators.
    def visitSymbolDecorators(self, ctx:NeoBasicParser.SymbolDecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#symbolDecorator.
    def visitSymbolDecorator(self, ctx:NeoBasicParser.SymbolDecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#annotationDecorator.
    def visitAnnotationDecorator(self, ctx:NeoBasicParser.AnnotationDecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#aspectDecorator.
    def visitAspectDecorator(self, ctx:NeoBasicParser.AspectDecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#taggedValuePairs.
    def visitTaggedValuePairs(self, ctx:NeoBasicParser.TaggedValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#taggedValuePair.
    def visitTaggedValuePair(self, ctx:NeoBasicParser.TaggedValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#genericTypeParameters.
    def visitGenericTypeParameters(self, ctx:NeoBasicParser.GenericTypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeParameters.
    def visitTypeParameters(self, ctx:NeoBasicParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#typeParameter.
    def visitTypeParameter(self, ctx:NeoBasicParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#types.
    def visitTypes(self, ctx:NeoBasicParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#type.
    def visitType(self, ctx:NeoBasicParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#prefixTypeModifier.
    def visitPrefixTypeModifier(self, ctx:NeoBasicParser.PrefixTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#postfixTypeWrapper.
    def visitPostfixTypeWrapper(self, ctx:NeoBasicParser.PostfixTypeWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#nativeType.
    def visitNativeType(self, ctx:NeoBasicParser.NativeTypeContext):
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


    # Visit a parse tree produced by NeoBasicParser#optionType.
    def visitOptionType(self, ctx:NeoBasicParser.OptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#metaType.
    def visitMetaType(self, ctx:NeoBasicParser.MetaTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procType.
    def visitProcType(self, ctx:NeoBasicParser.ProcTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#castType.
    def visitCastType(self, ctx:NeoBasicParser.CastTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#factType.
    def visitFactType(self, ctx:NeoBasicParser.FactTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#macroType.
    def visitMacroType(self, ctx:NeoBasicParser.MacroTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#funcType.
    def visitFuncType(self, ctx:NeoBasicParser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#feedType.
    def visitFeedType(self, ctx:NeoBasicParser.FeedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#subType.
    def visitSubType(self, ctx:NeoBasicParser.SubTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#operatorType.
    def visitOperatorType(self, ctx:NeoBasicParser.OperatorTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#eventType.
    def visitEventType(self, ctx:NeoBasicParser.EventTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#getterType.
    def visitGetterType(self, ctx:NeoBasicParser.GetterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#setterType.
    def visitSetterType(self, ctx:NeoBasicParser.SetterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#parenthesizedParameterTypes.
    def visitParenthesizedParameterTypes(self, ctx:NeoBasicParser.ParenthesizedParameterTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#bracketedParameterTypes.
    def visitBracketedParameterTypes(self, ctx:NeoBasicParser.BracketedParameterTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procParameterTypes.
    def visitProcParameterTypes(self, ctx:NeoBasicParser.ProcParameterTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#procParameterType.
    def visitProcParameterType(self, ctx:NeoBasicParser.ProcParameterTypeContext):
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


    # Visit a parse tree produced by NeoBasicParser#optionLiteral.
    def visitOptionLiteral(self, ctx:NeoBasicParser.OptionLiteralContext):
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


    # Visit a parse tree produced by NeoBasicParser#compoundLiteral.
    def visitCompoundLiteral(self, ctx:NeoBasicParser.CompoundLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sequenceLiteral.
    def visitSequenceLiteral(self, ctx:NeoBasicParser.SequenceLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#stringLiteral.
    def visitStringLiteral(self, ctx:NeoBasicParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#musicalLiteral.
    def visitMusicalLiteral(self, ctx:NeoBasicParser.MusicalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#compositeLiteral.
    def visitCompositeLiteral(self, ctx:NeoBasicParser.CompositeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#rangeLiteral.
    def visitRangeLiteral(self, ctx:NeoBasicParser.RangeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#pairLiteral.
    def visitPairLiteral(self, ctx:NeoBasicParser.PairLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#tupleLiteral.
    def visitTupleLiteral(self, ctx:NeoBasicParser.TupleLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#inetLiteral.
    def visitInetLiteral(self, ctx:NeoBasicParser.InetLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#uriLiteral.
    def visitUriLiteral(self, ctx:NeoBasicParser.UriLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#shellPathLiteral.
    def visitShellPathLiteral(self, ctx:NeoBasicParser.ShellPathLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#shellPathLiterals.
    def visitShellPathLiterals(self, ctx:NeoBasicParser.ShellPathLiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlDocLiteral.
    def visitXmlDocLiteral(self, ctx:NeoBasicParser.XmlDocLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlDocElement.
    def visitXmlDocElement(self, ctx:NeoBasicParser.XmlDocElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlElementPaired.
    def visitXmlElementPaired(self, ctx:NeoBasicParser.XmlElementPairedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlOpeningElement.
    def visitXmlOpeningElement(self, ctx:NeoBasicParser.XmlOpeningElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlClosingElement.
    def visitXmlClosingElement(self, ctx:NeoBasicParser.XmlClosingElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlElementSelfClosed.
    def visitXmlElementSelfClosed(self, ctx:NeoBasicParser.XmlElementSelfClosedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlDocFragment.
    def visitXmlDocFragment(self, ctx:NeoBasicParser.XmlDocFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlFragmentPaired.
    def visitXmlFragmentPaired(self, ctx:NeoBasicParser.XmlFragmentPairedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlFragmentSelfClosed.
    def visitXmlFragmentSelfClosed(self, ctx:NeoBasicParser.XmlFragmentSelfClosedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlTagName.
    def visitXmlTagName(self, ctx:NeoBasicParser.XmlTagNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlAttributes.
    def visitXmlAttributes(self, ctx:NeoBasicParser.XmlAttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlAttributeValue.
    def visitXmlAttributeValue(self, ctx:NeoBasicParser.XmlAttributeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#xmlChildren.
    def visitXmlChildren(self, ctx:NeoBasicParser.XmlChildrenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#expressionPlaceholder.
    def visitExpressionPlaceholder(self, ctx:NeoBasicParser.ExpressionPlaceholderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#collectionLiteral.
    def visitCollectionLiteral(self, ctx:NeoBasicParser.CollectionLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#collectionLiteralValue.
    def visitCollectionLiteralValue(self, ctx:NeoBasicParser.CollectionLiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#elements.
    def visitElements(self, ctx:NeoBasicParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#element.
    def visitElement(self, ctx:NeoBasicParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#elementKey.
    def visitElementKey(self, ctx:NeoBasicParser.ElementKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#elementValue.
    def visitElementValue(self, ctx:NeoBasicParser.ElementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#arrayAosToSoaLiteral.
    def visitArrayAosToSoaLiteral(self, ctx:NeoBasicParser.ArrayAosToSoaLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#listComprehension.
    def visitListComprehension(self, ctx:NeoBasicParser.ListComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#comprehensionClause.
    def visitComprehensionClause(self, ctx:NeoBasicParser.ComprehensionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#objectLiteral.
    def visitObjectLiteral(self, ctx:NeoBasicParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#objectLiteralValue.
    def visitObjectLiteralValue(self, ctx:NeoBasicParser.ObjectLiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#objectMembers.
    def visitObjectMembers(self, ctx:NeoBasicParser.ObjectMembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#objectMember.
    def visitObjectMember(self, ctx:NeoBasicParser.ObjectMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#memberName.
    def visitMemberName(self, ctx:NeoBasicParser.MemberNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#memberValue.
    def visitMemberValue(self, ctx:NeoBasicParser.MemberValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#lambdaLiteral.
    def visitLambdaLiteral(self, ctx:NeoBasicParser.LambdaLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#lambdaClause.
    def visitLambdaClause(self, ctx:NeoBasicParser.LambdaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#lambdaStatement.
    def visitLambdaStatement(self, ctx:NeoBasicParser.LambdaStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#arithmeticComprehension.
    def visitArithmeticComprehension(self, ctx:NeoBasicParser.ArithmeticComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#predeclaredValue.
    def visitPredeclaredValue(self, ctx:NeoBasicParser.PredeclaredValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#predefinedIdentifier.
    def visitPredefinedIdentifier(self, ctx:NeoBasicParser.PredefinedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#predefinedShellValue.
    def visitPredefinedShellValue(self, ctx:NeoBasicParser.PredefinedShellValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#predeclaredFunctor.
    def visitPredeclaredFunctor(self, ctx:NeoBasicParser.PredeclaredFunctorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#predeclaredFact.
    def visitPredeclaredFact(self, ctx:NeoBasicParser.PredeclaredFactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#predeclaredFmap.
    def visitPredeclaredFmap(self, ctx:NeoBasicParser.PredeclaredFmapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#primaryExpressions.
    def visitPrimaryExpressions(self, ctx:NeoBasicParser.PrimaryExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:NeoBasicParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#primaryOperand.
    def visitPrimaryOperand(self, ctx:NeoBasicParser.PrimaryOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#primaryFunctor.
    def visitPrimaryFunctor(self, ctx:NeoBasicParser.PrimaryFunctorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sos_Expression.
    def visitSos_Expression(self, ctx:NeoBasicParser.Sos_ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:NeoBasicParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#arrayIndexing.
    def visitArrayIndexing(self, ctx:NeoBasicParser.ArrayIndexingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#intervalExpression.
    def visitIntervalExpression(self, ctx:NeoBasicParser.IntervalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#sliceExpression.
    def visitSliceExpression(self, ctx:NeoBasicParser.SliceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#formatType.
    def visitFormatType(self, ctx:NeoBasicParser.FormatTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#macroOption.
    def visitMacroOption(self, ctx:NeoBasicParser.MacroOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#juxtapositionExpression.
    def visitJuxtapositionExpression(self, ctx:NeoBasicParser.JuxtapositionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#expressions.
    def visitExpressions(self, ctx:NeoBasicParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#expression.
    def visitExpression(self, ctx:NeoBasicParser.ExpressionContext):
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


    # Visit a parse tree produced by NeoBasicParser#shellProcess.
    def visitShellProcess(self, ctx:NeoBasicParser.ShellProcessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoBasicParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:NeoBasicParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)



del NeoBasicParser