# Generated from NeoBasicParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NeoBasicParser import NeoBasicParser
else:
    from NeoBasicParser import NeoBasicParser

# This class defines a complete listener for a parse tree produced by NeoBasicParser.
class NeoBasicParserListener(ParseTreeListener):

    # Enter a parse tree produced by NeoBasicParser#scriptProgram.
    def enterScriptProgram(self, ctx:NeoBasicParser.ScriptProgramContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#scriptProgram.
    def exitScriptProgram(self, ctx:NeoBasicParser.ScriptProgramContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#sourceCodeProgram.
    def enterSourceCodeProgram(self, ctx:NeoBasicParser.SourceCodeProgramContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#sourceCodeProgram.
    def exitSourceCodeProgram(self, ctx:NeoBasicParser.SourceCodeProgramContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#oneLinerProgram.
    def enterOneLinerProgram(self, ctx:NeoBasicParser.OneLinerProgramContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#oneLinerProgram.
    def exitOneLinerProgram(self, ctx:NeoBasicParser.OneLinerProgramContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#neoBasic.
    def enterNeoBasic(self, ctx:NeoBasicParser.NeoBasicContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#neoBasic.
    def exitNeoBasic(self, ctx:NeoBasicParser.NeoBasicContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#logicalInstructions.
    def enterLogicalInstructions(self, ctx:NeoBasicParser.LogicalInstructionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#logicalInstructions.
    def exitLogicalInstructions(self, ctx:NeoBasicParser.LogicalInstructionsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#logicalInstructionSuite.
    def enterLogicalInstructionSuite(self, ctx:NeoBasicParser.LogicalInstructionSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#logicalInstructionSuite.
    def exitLogicalInstructionSuite(self, ctx:NeoBasicParser.LogicalInstructionSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#logicalInstruction.
    def enterLogicalInstruction(self, ctx:NeoBasicParser.LogicalInstructionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#logicalInstruction.
    def exitLogicalInstruction(self, ctx:NeoBasicParser.LogicalInstructionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#directiveInstructionLiner.
    def enterDirectiveInstructionLiner(self, ctx:NeoBasicParser.DirectiveInstructionLinerContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#directiveInstructionLiner.
    def exitDirectiveInstructionLiner(self, ctx:NeoBasicParser.DirectiveInstructionLinerContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#directiveInstructionSuite.
    def enterDirectiveInstructionSuite(self, ctx:NeoBasicParser.DirectiveInstructionSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#directiveInstructionSuite.
    def exitDirectiveInstructionSuite(self, ctx:NeoBasicParser.DirectiveInstructionSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#instructionSentence.
    def enterInstructionSentence(self, ctx:NeoBasicParser.InstructionSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#instructionSentence.
    def exitInstructionSentence(self, ctx:NeoBasicParser.InstructionSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#shebangInterpreter.
    def enterShebangInterpreter(self, ctx:NeoBasicParser.ShebangInterpreterContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#shebangInterpreter.
    def exitShebangInterpreter(self, ctx:NeoBasicParser.ShebangInterpreterContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#directiveSentence.
    def enterDirectiveSentence(self, ctx:NeoBasicParser.DirectiveSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#directiveSentence.
    def exitDirectiveSentence(self, ctx:NeoBasicParser.DirectiveSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compilerPragmaDirective.
    def enterCompilerPragmaDirective(self, ctx:NeoBasicParser.CompilerPragmaDirectiveContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compilerPragmaDirective.
    def exitCompilerPragmaDirective(self, ctx:NeoBasicParser.CompilerPragmaDirectiveContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#shellLookupDirective.
    def enterShellLookupDirective(self, ctx:NeoBasicParser.ShellLookupDirectiveContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#shellLookupDirective.
    def exitShellLookupDirective(self, ctx:NeoBasicParser.ShellLookupDirectiveContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#lookupStatement.
    def enterLookupStatement(self, ctx:NeoBasicParser.LookupStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#lookupStatement.
    def exitLookupStatement(self, ctx:NeoBasicParser.LookupStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#canaryTestingDirective.
    def enterCanaryTestingDirective(self, ctx:NeoBasicParser.CanaryTestingDirectiveContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#canaryTestingDirective.
    def exitCanaryTestingDirective(self, ctx:NeoBasicParser.CanaryTestingDirectiveContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#testingLine.
    def enterTestingLine(self, ctx:NeoBasicParser.TestingLineContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#testingLine.
    def exitTestingLine(self, ctx:NeoBasicParser.TestingLineContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#testingBlock.
    def enterTestingBlock(self, ctx:NeoBasicParser.TestingBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#testingBlock.
    def exitTestingBlock(self, ctx:NeoBasicParser.TestingBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#labelIdentifier.
    def enterLabelIdentifier(self, ctx:NeoBasicParser.LabelIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#labelIdentifier.
    def exitLabelIdentifier(self, ctx:NeoBasicParser.LabelIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:NeoBasicParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:NeoBasicParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#decoratedIdentifier.
    def enterDecoratedIdentifier(self, ctx:NeoBasicParser.DecoratedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#decoratedIdentifier.
    def exitDecoratedIdentifier(self, ctx:NeoBasicParser.DecoratedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#decoratedType.
    def enterDecoratedType(self, ctx:NeoBasicParser.DecoratedTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#decoratedType.
    def exitDecoratedType(self, ctx:NeoBasicParser.DecoratedTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typedDecoratedIdentifier.
    def enterTypedDecoratedIdentifier(self, ctx:NeoBasicParser.TypedDecoratedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typedDecoratedIdentifier.
    def exitTypedDecoratedIdentifier(self, ctx:NeoBasicParser.TypedDecoratedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#inferredDecoratedIdentifier.
    def enterInferredDecoratedIdentifier(self, ctx:NeoBasicParser.InferredDecoratedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#inferredDecoratedIdentifier.
    def exitInferredDecoratedIdentifier(self, ctx:NeoBasicParser.InferredDecoratedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#genericDecoratedIdentifier.
    def enterGenericDecoratedIdentifier(self, ctx:NeoBasicParser.GenericDecoratedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#genericDecoratedIdentifier.
    def exitGenericDecoratedIdentifier(self, ctx:NeoBasicParser.GenericDecoratedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#declarationIdentifier.
    def enterDeclarationIdentifier(self, ctx:NeoBasicParser.DeclarationIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#declarationIdentifier.
    def exitDeclarationIdentifier(self, ctx:NeoBasicParser.DeclarationIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#identifiers.
    def enterIdentifiers(self, ctx:NeoBasicParser.IdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#identifiers.
    def exitIdentifiers(self, ctx:NeoBasicParser.IdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def enterQualifiedIdentifiers(self, ctx:NeoBasicParser.QualifiedIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def exitQualifiedIdentifiers(self, ctx:NeoBasicParser.QualifiedIdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#decoratedIdentifiers.
    def enterDecoratedIdentifiers(self, ctx:NeoBasicParser.DecoratedIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#decoratedIdentifiers.
    def exitDecoratedIdentifiers(self, ctx:NeoBasicParser.DecoratedIdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#decoratedTypes.
    def enterDecoratedTypes(self, ctx:NeoBasicParser.DecoratedTypesContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#decoratedTypes.
    def exitDecoratedTypes(self, ctx:NeoBasicParser.DecoratedTypesContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typedDecoratedIdentifiers.
    def enterTypedDecoratedIdentifiers(self, ctx:NeoBasicParser.TypedDecoratedIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typedDecoratedIdentifiers.
    def exitTypedDecoratedIdentifiers(self, ctx:NeoBasicParser.TypedDecoratedIdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#inferredDecoratedIdentifiers.
    def enterInferredDecoratedIdentifiers(self, ctx:NeoBasicParser.InferredDecoratedIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#inferredDecoratedIdentifiers.
    def exitInferredDecoratedIdentifiers(self, ctx:NeoBasicParser.InferredDecoratedIdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#topLevelSentence.
    def enterTopLevelSentence(self, ctx:NeoBasicParser.TopLevelSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#topLevelSentence.
    def exitTopLevelSentence(self, ctx:NeoBasicParser.TopLevelSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#identificationSentence.
    def enterIdentificationSentence(self, ctx:NeoBasicParser.IdentificationSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#identificationSentence.
    def exitIdentificationSentence(self, ctx:NeoBasicParser.IdentificationSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#appletClause.
    def enterAppletClause(self, ctx:NeoBasicParser.AppletClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#appletClause.
    def exitAppletClause(self, ctx:NeoBasicParser.AppletClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#moduleClause.
    def enterModuleClause(self, ctx:NeoBasicParser.ModuleClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#moduleClause.
    def exitModuleClause(self, ctx:NeoBasicParser.ModuleClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#notabeneClause.
    def enterNotabeneClause(self, ctx:NeoBasicParser.NotabeneClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#notabeneClause.
    def exitNotabeneClause(self, ctx:NeoBasicParser.NotabeneClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#deflagSentence.
    def enterDeflagSentence(self, ctx:NeoBasicParser.DeflagSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#deflagSentence.
    def exitDeflagSentence(self, ctx:NeoBasicParser.DeflagSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defineClause.
    def enterDefineClause(self, ctx:NeoBasicParser.DefineClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defineClause.
    def exitDefineClause(self, ctx:NeoBasicParser.DefineClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defineSuite.
    def enterDefineSuite(self, ctx:NeoBasicParser.DefineSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defineSuite.
    def exitDefineSuite(self, ctx:NeoBasicParser.DefineSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defineDeclareBlock.
    def enterDefineDeclareBlock(self, ctx:NeoBasicParser.DefineDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defineDeclareBlock.
    def exitDefineDeclareBlock(self, ctx:NeoBasicParser.DefineDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defineDeclare.
    def enterDefineDeclare(self, ctx:NeoBasicParser.DefineDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defineDeclare.
    def exitDefineDeclare(self, ctx:NeoBasicParser.DefineDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defineDeclareSingle.
    def enterDefineDeclareSingle(self, ctx:NeoBasicParser.DefineDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defineDeclareSingle.
    def exitDefineDeclareSingle(self, ctx:NeoBasicParser.DefineDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defineDeclareMultiple.
    def enterDefineDeclareMultiple(self, ctx:NeoBasicParser.DefineDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defineDeclareMultiple.
    def exitDefineDeclareMultiple(self, ctx:NeoBasicParser.DefineDeclareMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#undefClause.
    def enterUndefClause(self, ctx:NeoBasicParser.UndefClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#undefClause.
    def exitUndefClause(self, ctx:NeoBasicParser.UndefClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#undefSuite.
    def enterUndefSuite(self, ctx:NeoBasicParser.UndefSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#undefSuite.
    def exitUndefSuite(self, ctx:NeoBasicParser.UndefSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#undefDeclareBlock.
    def enterUndefDeclareBlock(self, ctx:NeoBasicParser.UndefDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#undefDeclareBlock.
    def exitUndefDeclareBlock(self, ctx:NeoBasicParser.UndefDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#undefDeclare.
    def enterUndefDeclare(self, ctx:NeoBasicParser.UndefDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#undefDeclare.
    def exitUndefDeclare(self, ctx:NeoBasicParser.UndefDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defAtom.
    def enterDefAtom(self, ctx:NeoBasicParser.DefAtomContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defAtom.
    def exitDefAtom(self, ctx:NeoBasicParser.DefAtomContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defAtoms.
    def enterDefAtoms(self, ctx:NeoBasicParser.DefAtomsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defAtoms.
    def exitDefAtoms(self, ctx:NeoBasicParser.DefAtomsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useSentence.
    def enterUseSentence(self, ctx:NeoBasicParser.UseSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useSentence.
    def exitUseSentence(self, ctx:NeoBasicParser.UseSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useClause.
    def enterUseClause(self, ctx:NeoBasicParser.UseClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useClause.
    def exitUseClause(self, ctx:NeoBasicParser.UseClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useSuite.
    def enterUseSuite(self, ctx:NeoBasicParser.UseSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useSuite.
    def exitUseSuite(self, ctx:NeoBasicParser.UseSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useDeclareBlock.
    def enterUseDeclareBlock(self, ctx:NeoBasicParser.UseDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useDeclareBlock.
    def exitUseDeclareBlock(self, ctx:NeoBasicParser.UseDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useDeclare.
    def enterUseDeclare(self, ctx:NeoBasicParser.UseDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useDeclare.
    def exitUseDeclare(self, ctx:NeoBasicParser.UseDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useDeclareSingle.
    def enterUseDeclareSingle(self, ctx:NeoBasicParser.UseDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useDeclareSingle.
    def exitUseDeclareSingle(self, ctx:NeoBasicParser.UseDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useDeclareMultiple.
    def enterUseDeclareMultiple(self, ctx:NeoBasicParser.UseDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useDeclareMultiple.
    def exitUseDeclareMultiple(self, ctx:NeoBasicParser.UseDeclareMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useDeclareAs.
    def enterUseDeclareAs(self, ctx:NeoBasicParser.UseDeclareAsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useDeclareAs.
    def exitUseDeclareAs(self, ctx:NeoBasicParser.UseDeclareAsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#useDeclareOf.
    def enterUseDeclareOf(self, ctx:NeoBasicParser.UseDeclareOfContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#useDeclareOf.
    def exitUseDeclareOf(self, ctx:NeoBasicParser.UseDeclareOfContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#interfaceSentence.
    def enterInterfaceSentence(self, ctx:NeoBasicParser.InterfaceSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#interfaceSentence.
    def exitInterfaceSentence(self, ctx:NeoBasicParser.InterfaceSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#interfaceClause.
    def enterInterfaceClause(self, ctx:NeoBasicParser.InterfaceClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#interfaceClause.
    def exitInterfaceClause(self, ctx:NeoBasicParser.InterfaceClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#interfaceBody.
    def enterInterfaceBody(self, ctx:NeoBasicParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#interfaceBody.
    def exitInterfaceBody(self, ctx:NeoBasicParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeSentence.
    def enterIncludeSentence(self, ctx:NeoBasicParser.IncludeSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeSentence.
    def exitIncludeSentence(self, ctx:NeoBasicParser.IncludeSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeClause.
    def enterIncludeClause(self, ctx:NeoBasicParser.IncludeClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeClause.
    def exitIncludeClause(self, ctx:NeoBasicParser.IncludeClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeSuite.
    def enterIncludeSuite(self, ctx:NeoBasicParser.IncludeSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeSuite.
    def exitIncludeSuite(self, ctx:NeoBasicParser.IncludeSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeDeclareBlock.
    def enterIncludeDeclareBlock(self, ctx:NeoBasicParser.IncludeDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeDeclareBlock.
    def exitIncludeDeclareBlock(self, ctx:NeoBasicParser.IncludeDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeDeclare.
    def enterIncludeDeclare(self, ctx:NeoBasicParser.IncludeDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeDeclare.
    def exitIncludeDeclare(self, ctx:NeoBasicParser.IncludeDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeDeclareSingle.
    def enterIncludeDeclareSingle(self, ctx:NeoBasicParser.IncludeDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeDeclareSingle.
    def exitIncludeDeclareSingle(self, ctx:NeoBasicParser.IncludeDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeDeclareMultiple.
    def enterIncludeDeclareMultiple(self, ctx:NeoBasicParser.IncludeDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeDeclareMultiple.
    def exitIncludeDeclareMultiple(self, ctx:NeoBasicParser.IncludeDeclareMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#includeDeclareAs.
    def enterIncludeDeclareAs(self, ctx:NeoBasicParser.IncludeDeclareAsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#includeDeclareAs.
    def exitIncludeDeclareAs(self, ctx:NeoBasicParser.IncludeDeclareAsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#declarationSentence.
    def enterDeclarationSentence(self, ctx:NeoBasicParser.DeclarationSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#declarationSentence.
    def exitDeclarationSentence(self, ctx:NeoBasicParser.DeclarationSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#adhocMetadata.
    def enterAdhocMetadata(self, ctx:NeoBasicParser.AdhocMetadataContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#adhocMetadata.
    def exitAdhocMetadata(self, ctx:NeoBasicParser.AdhocMetadataContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#metadataDecorators.
    def enterMetadataDecorators(self, ctx:NeoBasicParser.MetadataDecoratorsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#metadataDecorators.
    def exitMetadataDecorators(self, ctx:NeoBasicParser.MetadataDecoratorsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#metadataGenerics.
    def enterMetadataGenerics(self, ctx:NeoBasicParser.MetadataGenericsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#metadataGenerics.
    def exitMetadataGenerics(self, ctx:NeoBasicParser.MetadataGenericsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#visibilityModifier.
    def enterVisibilityModifier(self, ctx:NeoBasicParser.VisibilityModifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#visibilityModifier.
    def exitVisibilityModifier(self, ctx:NeoBasicParser.VisibilityModifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#visibilityLabelSuite.
    def enterVisibilityLabelSuite(self, ctx:NeoBasicParser.VisibilityLabelSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#visibilityLabelSuite.
    def exitVisibilityLabelSuite(self, ctx:NeoBasicParser.VisibilityLabelSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#extendsClause.
    def enterExtendsClause(self, ctx:NeoBasicParser.ExtendsClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#extendsClause.
    def exitExtendsClause(self, ctx:NeoBasicParser.ExtendsClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#implementsClause.
    def enterImplementsClause(self, ctx:NeoBasicParser.ImplementsClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#implementsClause.
    def exitImplementsClause(self, ctx:NeoBasicParser.ImplementsClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#mixesClause.
    def enterMixesClause(self, ctx:NeoBasicParser.MixesClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#mixesClause.
    def exitMixesClause(self, ctx:NeoBasicParser.MixesClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#raisesClause.
    def enterRaisesClause(self, ctx:NeoBasicParser.RaisesClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#raisesClause.
    def exitRaisesClause(self, ctx:NeoBasicParser.RaisesClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#parenthesizedArguments.
    def enterParenthesizedArguments(self, ctx:NeoBasicParser.ParenthesizedArgumentsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#parenthesizedArguments.
    def exitParenthesizedArguments(self, ctx:NeoBasicParser.ParenthesizedArgumentsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#namedArguments.
    def enterNamedArguments(self, ctx:NeoBasicParser.NamedArgumentsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#namedArguments.
    def exitNamedArguments(self, ctx:NeoBasicParser.NamedArgumentsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#namedArgument.
    def enterNamedArgument(self, ctx:NeoBasicParser.NamedArgumentContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#namedArgument.
    def exitNamedArgument(self, ctx:NeoBasicParser.NamedArgumentContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#parenthesizedParameters.
    def enterParenthesizedParameters(self, ctx:NeoBasicParser.ParenthesizedParametersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#parenthesizedParameters.
    def exitParenthesizedParameters(self, ctx:NeoBasicParser.ParenthesizedParametersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procParameters.
    def enterProcParameters(self, ctx:NeoBasicParser.ProcParametersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procParameters.
    def exitProcParameters(self, ctx:NeoBasicParser.ProcParametersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procParameter.
    def enterProcParameter(self, ctx:NeoBasicParser.ProcParameterContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procParameter.
    def exitProcParameter(self, ctx:NeoBasicParser.ProcParameterContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#modeParameterSpecifier.
    def enterModeParameterSpecifier(self, ctx:NeoBasicParser.ModeParameterSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#modeParameterSpecifier.
    def exitModeParameterSpecifier(self, ctx:NeoBasicParser.ModeParameterSpecifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#prefixParameterName.
    def enterPrefixParameterName(self, ctx:NeoBasicParser.PrefixParameterNameContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#prefixParameterName.
    def exitPrefixParameterName(self, ctx:NeoBasicParser.PrefixParameterNameContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#prefixParameterType.
    def enterPrefixParameterType(self, ctx:NeoBasicParser.PrefixParameterTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#prefixParameterType.
    def exitPrefixParameterType(self, ctx:NeoBasicParser.PrefixParameterTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procResultType.
    def enterProcResultType(self, ctx:NeoBasicParser.ProcResultTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procResultType.
    def exitProcResultType(self, ctx:NeoBasicParser.ProcResultTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procBody.
    def enterProcBody(self, ctx:NeoBasicParser.ProcBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procBody.
    def exitProcBody(self, ctx:NeoBasicParser.ProcBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procSuite.
    def enterProcSuite(self, ctx:NeoBasicParser.ProcSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procSuite.
    def exitProcSuite(self, ctx:NeoBasicParser.ProcSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procSemex.
    def enterProcSemex(self, ctx:NeoBasicParser.ProcSemexContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procSemex.
    def exitProcSemex(self, ctx:NeoBasicParser.ProcSemexContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procSpecifier.
    def enterProcSpecifier(self, ctx:NeoBasicParser.ProcSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procSpecifier.
    def exitProcSpecifier(self, ctx:NeoBasicParser.ProcSpecifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procImplicitReturn.
    def enterProcImplicitReturn(self, ctx:NeoBasicParser.ProcImplicitReturnContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procImplicitReturn.
    def exitProcImplicitReturn(self, ctx:NeoBasicParser.ProcImplicitReturnContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procPatternGuards.
    def enterProcPatternGuards(self, ctx:NeoBasicParser.ProcPatternGuardsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procPatternGuards.
    def exitProcPatternGuards(self, ctx:NeoBasicParser.ProcPatternGuardsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#guardBranchClause.
    def enterGuardBranchClause(self, ctx:NeoBasicParser.GuardBranchClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#guardBranchClause.
    def exitGuardBranchClause(self, ctx:NeoBasicParser.GuardBranchClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#guardElseClause.
    def enterGuardElseClause(self, ctx:NeoBasicParser.GuardElseClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#guardElseClause.
    def exitGuardElseClause(self, ctx:NeoBasicParser.GuardElseClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#outerDeclareSentence.
    def enterOuterDeclareSentence(self, ctx:NeoBasicParser.OuterDeclareSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#outerDeclareSentence.
    def exitOuterDeclareSentence(self, ctx:NeoBasicParser.OuterDeclareSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeSentence.
    def enterTypeSentence(self, ctx:NeoBasicParser.TypeSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeSentence.
    def exitTypeSentence(self, ctx:NeoBasicParser.TypeSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeClause.
    def enterTypeClause(self, ctx:NeoBasicParser.TypeClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeClause.
    def exitTypeClause(self, ctx:NeoBasicParser.TypeClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeSuite.
    def enterTypeSuite(self, ctx:NeoBasicParser.TypeSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeSuite.
    def exitTypeSuite(self, ctx:NeoBasicParser.TypeSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeDeclareBlock.
    def enterTypeDeclareBlock(self, ctx:NeoBasicParser.TypeDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeDeclareBlock.
    def exitTypeDeclareBlock(self, ctx:NeoBasicParser.TypeDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeDeclare.
    def enterTypeDeclare(self, ctx:NeoBasicParser.TypeDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeDeclare.
    def exitTypeDeclare(self, ctx:NeoBasicParser.TypeDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeDeclareSingle.
    def enterTypeDeclareSingle(self, ctx:NeoBasicParser.TypeDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeDeclareSingle.
    def exitTypeDeclareSingle(self, ctx:NeoBasicParser.TypeDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeDeclareSubrange.
    def enterTypeDeclareSubrange(self, ctx:NeoBasicParser.TypeDeclareSubrangeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeDeclareSubrange.
    def exitTypeDeclareSubrange(self, ctx:NeoBasicParser.TypeDeclareSubrangeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constSentence.
    def enterConstSentence(self, ctx:NeoBasicParser.ConstSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constSentence.
    def exitConstSentence(self, ctx:NeoBasicParser.ConstSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constClause.
    def enterConstClause(self, ctx:NeoBasicParser.ConstClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constClause.
    def exitConstClause(self, ctx:NeoBasicParser.ConstClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constSuite.
    def enterConstSuite(self, ctx:NeoBasicParser.ConstSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constSuite.
    def exitConstSuite(self, ctx:NeoBasicParser.ConstSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constDeclareBlock.
    def enterConstDeclareBlock(self, ctx:NeoBasicParser.ConstDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclareBlock.
    def exitConstDeclareBlock(self, ctx:NeoBasicParser.ConstDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constDeclare.
    def enterConstDeclare(self, ctx:NeoBasicParser.ConstDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclare.
    def exitConstDeclare(self, ctx:NeoBasicParser.ConstDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constDeclareSingle.
    def enterConstDeclareSingle(self, ctx:NeoBasicParser.ConstDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclareSingle.
    def exitConstDeclareSingle(self, ctx:NeoBasicParser.ConstDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constDeclareMultiple.
    def enterConstDeclareMultiple(self, ctx:NeoBasicParser.ConstDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclareMultiple.
    def exitConstDeclareMultiple(self, ctx:NeoBasicParser.ConstDeclareMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constDeclareParallel.
    def enterConstDeclareParallel(self, ctx:NeoBasicParser.ConstDeclareParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constDeclareParallel.
    def exitConstDeclareParallel(self, ctx:NeoBasicParser.ConstDeclareParallelContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letSentence.
    def enterLetSentence(self, ctx:NeoBasicParser.LetSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letSentence.
    def exitLetSentence(self, ctx:NeoBasicParser.LetSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letClause.
    def enterLetClause(self, ctx:NeoBasicParser.LetClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letClause.
    def exitLetClause(self, ctx:NeoBasicParser.LetClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letSuite.
    def enterLetSuite(self, ctx:NeoBasicParser.LetSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letSuite.
    def exitLetSuite(self, ctx:NeoBasicParser.LetSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letDeclareBlock.
    def enterLetDeclareBlock(self, ctx:NeoBasicParser.LetDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letDeclareBlock.
    def exitLetDeclareBlock(self, ctx:NeoBasicParser.LetDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letDeclare.
    def enterLetDeclare(self, ctx:NeoBasicParser.LetDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letDeclare.
    def exitLetDeclare(self, ctx:NeoBasicParser.LetDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letDeclareSingle.
    def enterLetDeclareSingle(self, ctx:NeoBasicParser.LetDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letDeclareSingle.
    def exitLetDeclareSingle(self, ctx:NeoBasicParser.LetDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letDeclareMultiple.
    def enterLetDeclareMultiple(self, ctx:NeoBasicParser.LetDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letDeclareMultiple.
    def exitLetDeclareMultiple(self, ctx:NeoBasicParser.LetDeclareMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#letDeclareParallel.
    def enterLetDeclareParallel(self, ctx:NeoBasicParser.LetDeclareParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#letDeclareParallel.
    def exitLetDeclareParallel(self, ctx:NeoBasicParser.LetDeclareParallelContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varSentence.
    def enterVarSentence(self, ctx:NeoBasicParser.VarSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varSentence.
    def exitVarSentence(self, ctx:NeoBasicParser.VarSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varClause.
    def enterVarClause(self, ctx:NeoBasicParser.VarClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varClause.
    def exitVarClause(self, ctx:NeoBasicParser.VarClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varSuite.
    def enterVarSuite(self, ctx:NeoBasicParser.VarSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varSuite.
    def exitVarSuite(self, ctx:NeoBasicParser.VarSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varDeclareBlock.
    def enterVarDeclareBlock(self, ctx:NeoBasicParser.VarDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclareBlock.
    def exitVarDeclareBlock(self, ctx:NeoBasicParser.VarDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varDeclare.
    def enterVarDeclare(self, ctx:NeoBasicParser.VarDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclare.
    def exitVarDeclare(self, ctx:NeoBasicParser.VarDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varDeclareSingle.
    def enterVarDeclareSingle(self, ctx:NeoBasicParser.VarDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclareSingle.
    def exitVarDeclareSingle(self, ctx:NeoBasicParser.VarDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varDeclareMultiple.
    def enterVarDeclareMultiple(self, ctx:NeoBasicParser.VarDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclareMultiple.
    def exitVarDeclareMultiple(self, ctx:NeoBasicParser.VarDeclareMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#varDeclareParallel.
    def enterVarDeclareParallel(self, ctx:NeoBasicParser.VarDeclareParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varDeclareParallel.
    def exitVarDeclareParallel(self, ctx:NeoBasicParser.VarDeclareParallelContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#castSentence.
    def enterCastSentence(self, ctx:NeoBasicParser.CastSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#castSentence.
    def exitCastSentence(self, ctx:NeoBasicParser.CastSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#castClause.
    def enterCastClause(self, ctx:NeoBasicParser.CastClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#castClause.
    def exitCastClause(self, ctx:NeoBasicParser.CastClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#castBody.
    def enterCastBody(self, ctx:NeoBasicParser.CastBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#castBody.
    def exitCastBody(self, ctx:NeoBasicParser.CastBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#factSentence.
    def enterFactSentence(self, ctx:NeoBasicParser.FactSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#factSentence.
    def exitFactSentence(self, ctx:NeoBasicParser.FactSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#factClause.
    def enterFactClause(self, ctx:NeoBasicParser.FactClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#factClause.
    def exitFactClause(self, ctx:NeoBasicParser.FactClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#macroSentence.
    def enterMacroSentence(self, ctx:NeoBasicParser.MacroSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#macroSentence.
    def exitMacroSentence(self, ctx:NeoBasicParser.MacroSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#macroClause.
    def enterMacroClause(self, ctx:NeoBasicParser.MacroClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#macroClause.
    def exitMacroClause(self, ctx:NeoBasicParser.MacroClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#funcSentence.
    def enterFuncSentence(self, ctx:NeoBasicParser.FuncSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#funcSentence.
    def exitFuncSentence(self, ctx:NeoBasicParser.FuncSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#funcClause.
    def enterFuncClause(self, ctx:NeoBasicParser.FuncClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#funcClause.
    def exitFuncClause(self, ctx:NeoBasicParser.FuncClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#feedSentence.
    def enterFeedSentence(self, ctx:NeoBasicParser.FeedSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#feedSentence.
    def exitFeedSentence(self, ctx:NeoBasicParser.FeedSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#feedClause.
    def enterFeedClause(self, ctx:NeoBasicParser.FeedClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#feedClause.
    def exitFeedClause(self, ctx:NeoBasicParser.FeedClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#subSentence.
    def enterSubSentence(self, ctx:NeoBasicParser.SubSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#subSentence.
    def exitSubSentence(self, ctx:NeoBasicParser.SubSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#subClause.
    def enterSubClause(self, ctx:NeoBasicParser.SubClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#subClause.
    def exitSubClause(self, ctx:NeoBasicParser.SubClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#operatorSentence.
    def enterOperatorSentence(self, ctx:NeoBasicParser.OperatorSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#operatorSentence.
    def exitOperatorSentence(self, ctx:NeoBasicParser.OperatorSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#operatorClause.
    def enterOperatorClause(self, ctx:NeoBasicParser.OperatorClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#operatorClause.
    def exitOperatorClause(self, ctx:NeoBasicParser.OperatorClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#operatorIdentifier.
    def enterOperatorIdentifier(self, ctx:NeoBasicParser.OperatorIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#operatorIdentifier.
    def exitOperatorIdentifier(self, ctx:NeoBasicParser.OperatorIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#declarationOperator.
    def enterDeclarationOperator(self, ctx:NeoBasicParser.DeclarationOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#declarationOperator.
    def exitDeclarationOperator(self, ctx:NeoBasicParser.DeclarationOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#eventSentence.
    def enterEventSentence(self, ctx:NeoBasicParser.EventSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#eventSentence.
    def exitEventSentence(self, ctx:NeoBasicParser.EventSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#eventClause.
    def enterEventClause(self, ctx:NeoBasicParser.EventClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#eventClause.
    def exitEventClause(self, ctx:NeoBasicParser.EventClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#bracketedParameters.
    def enterBracketedParameters(self, ctx:NeoBasicParser.BracketedParametersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#bracketedParameters.
    def exitBracketedParameters(self, ctx:NeoBasicParser.BracketedParametersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumSentence.
    def enterEnumSentence(self, ctx:NeoBasicParser.EnumSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumSentence.
    def exitEnumSentence(self, ctx:NeoBasicParser.EnumSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumClause.
    def enterEnumClause(self, ctx:NeoBasicParser.EnumClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumClause.
    def exitEnumClause(self, ctx:NeoBasicParser.EnumClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumType.
    def enterEnumType(self, ctx:NeoBasicParser.EnumTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumType.
    def exitEnumType(self, ctx:NeoBasicParser.EnumTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumBody.
    def enterEnumBody(self, ctx:NeoBasicParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumBody.
    def exitEnumBody(self, ctx:NeoBasicParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumSemex.
    def enterEnumSemex(self, ctx:NeoBasicParser.EnumSemexContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumSemex.
    def exitEnumSemex(self, ctx:NeoBasicParser.EnumSemexContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumSuite.
    def enterEnumSuite(self, ctx:NeoBasicParser.EnumSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumSuite.
    def exitEnumSuite(self, ctx:NeoBasicParser.EnumSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumMembersBlock.
    def enterEnumMembersBlock(self, ctx:NeoBasicParser.EnumMembersBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumMembersBlock.
    def exitEnumMembersBlock(self, ctx:NeoBasicParser.EnumMembersBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumMember.
    def enterEnumMember(self, ctx:NeoBasicParser.EnumMemberContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumMember.
    def exitEnumMember(self, ctx:NeoBasicParser.EnumMemberContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumFieldSingle.
    def enterEnumFieldSingle(self, ctx:NeoBasicParser.EnumFieldSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumFieldSingle.
    def exitEnumFieldSingle(self, ctx:NeoBasicParser.EnumFieldSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#enumFieldMultiple.
    def enterEnumFieldMultiple(self, ctx:NeoBasicParser.EnumFieldMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#enumFieldMultiple.
    def exitEnumFieldMultiple(self, ctx:NeoBasicParser.EnumFieldMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structSentence.
    def enterStructSentence(self, ctx:NeoBasicParser.StructSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structSentence.
    def exitStructSentence(self, ctx:NeoBasicParser.StructSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structClause.
    def enterStructClause(self, ctx:NeoBasicParser.StructClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structClause.
    def exitStructClause(self, ctx:NeoBasicParser.StructClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structBody.
    def enterStructBody(self, ctx:NeoBasicParser.StructBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structBody.
    def exitStructBody(self, ctx:NeoBasicParser.StructBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structSemex.
    def enterStructSemex(self, ctx:NeoBasicParser.StructSemexContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structSemex.
    def exitStructSemex(self, ctx:NeoBasicParser.StructSemexContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structSuite.
    def enterStructSuite(self, ctx:NeoBasicParser.StructSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structSuite.
    def exitStructSuite(self, ctx:NeoBasicParser.StructSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structMembersBlock.
    def enterStructMembersBlock(self, ctx:NeoBasicParser.StructMembersBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structMembersBlock.
    def exitStructMembersBlock(self, ctx:NeoBasicParser.StructMembersBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structMember.
    def enterStructMember(self, ctx:NeoBasicParser.StructMemberContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structMember.
    def exitStructMember(self, ctx:NeoBasicParser.StructMemberContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structFieldSingle.
    def enterStructFieldSingle(self, ctx:NeoBasicParser.StructFieldSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structFieldSingle.
    def exitStructFieldSingle(self, ctx:NeoBasicParser.StructFieldSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#attributeTag.
    def enterAttributeTag(self, ctx:NeoBasicParser.AttributeTagContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#attributeTag.
    def exitAttributeTag(self, ctx:NeoBasicParser.AttributeTagContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structFieldMultiple.
    def enterStructFieldMultiple(self, ctx:NeoBasicParser.StructFieldMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structFieldMultiple.
    def exitStructFieldMultiple(self, ctx:NeoBasicParser.StructFieldMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#structMemberEmbedded.
    def enterStructMemberEmbedded(self, ctx:NeoBasicParser.StructMemberEmbeddedContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#structMemberEmbedded.
    def exitStructMemberEmbedded(self, ctx:NeoBasicParser.StructMemberEmbeddedContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#protoSentence.
    def enterProtoSentence(self, ctx:NeoBasicParser.ProtoSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#protoSentence.
    def exitProtoSentence(self, ctx:NeoBasicParser.ProtoSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#protoClause.
    def enterProtoClause(self, ctx:NeoBasicParser.ProtoClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#protoClause.
    def exitProtoClause(self, ctx:NeoBasicParser.ProtoClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#protoBody.
    def enterProtoBody(self, ctx:NeoBasicParser.ProtoBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#protoBody.
    def exitProtoBody(self, ctx:NeoBasicParser.ProtoBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#traitSentence.
    def enterTraitSentence(self, ctx:NeoBasicParser.TraitSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#traitSentence.
    def exitTraitSentence(self, ctx:NeoBasicParser.TraitSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#traitClause.
    def enterTraitClause(self, ctx:NeoBasicParser.TraitClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#traitClause.
    def exitTraitClause(self, ctx:NeoBasicParser.TraitClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#traitBody.
    def enterTraitBody(self, ctx:NeoBasicParser.TraitBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#traitBody.
    def exitTraitBody(self, ctx:NeoBasicParser.TraitBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classSentence.
    def enterClassSentence(self, ctx:NeoBasicParser.ClassSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classSentence.
    def exitClassSentence(self, ctx:NeoBasicParser.ClassSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classClause.
    def enterClassClause(self, ctx:NeoBasicParser.ClassClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classClause.
    def exitClassClause(self, ctx:NeoBasicParser.ClassClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classBody.
    def enterClassBody(self, ctx:NeoBasicParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classBody.
    def exitClassBody(self, ctx:NeoBasicParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classSemex.
    def enterClassSemex(self, ctx:NeoBasicParser.ClassSemexContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classSemex.
    def exitClassSemex(self, ctx:NeoBasicParser.ClassSemexContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classFieldMultiple.
    def enterClassFieldMultiple(self, ctx:NeoBasicParser.ClassFieldMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classFieldMultiple.
    def exitClassFieldMultiple(self, ctx:NeoBasicParser.ClassFieldMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classFieldSimple.
    def enterClassFieldSimple(self, ctx:NeoBasicParser.ClassFieldSimpleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classFieldSimple.
    def exitClassFieldSimple(self, ctx:NeoBasicParser.ClassFieldSimpleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classSuite.
    def enterClassSuite(self, ctx:NeoBasicParser.ClassSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classSuite.
    def exitClassSuite(self, ctx:NeoBasicParser.ClassSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#objectSentence.
    def enterObjectSentence(self, ctx:NeoBasicParser.ObjectSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#objectSentence.
    def exitObjectSentence(self, ctx:NeoBasicParser.ObjectSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#objectClause.
    def enterObjectClause(self, ctx:NeoBasicParser.ObjectClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#objectClause.
    def exitObjectClause(self, ctx:NeoBasicParser.ObjectClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#objectBody.
    def enterObjectBody(self, ctx:NeoBasicParser.ObjectBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#objectBody.
    def exitObjectBody(self, ctx:NeoBasicParser.ObjectBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#innerDeclareSentence.
    def enterInnerDeclareSentence(self, ctx:NeoBasicParser.InnerDeclareSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#innerDeclareSentence.
    def exitInnerDeclareSentence(self, ctx:NeoBasicParser.InnerDeclareSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constructSentence.
    def enterConstructSentence(self, ctx:NeoBasicParser.ConstructSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constructSentence.
    def exitConstructSentence(self, ctx:NeoBasicParser.ConstructSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#constructClause.
    def enterConstructClause(self, ctx:NeoBasicParser.ConstructClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constructClause.
    def exitConstructClause(self, ctx:NeoBasicParser.ConstructClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classInitializer.
    def enterClassInitializer(self, ctx:NeoBasicParser.ClassInitializerContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classInitializer.
    def exitClassInitializer(self, ctx:NeoBasicParser.ClassInitializerContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classInitializingMembers.
    def enterClassInitializingMembers(self, ctx:NeoBasicParser.ClassInitializingMembersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classInitializingMembers.
    def exitClassInitializingMembers(self, ctx:NeoBasicParser.ClassInitializingMembersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#classInitializingMember.
    def enterClassInitializingMember(self, ctx:NeoBasicParser.ClassInitializingMemberContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#classInitializingMember.
    def exitClassInitializingMember(self, ctx:NeoBasicParser.ClassInitializingMemberContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#destructSentence.
    def enterDestructSentence(self, ctx:NeoBasicParser.DestructSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#destructSentence.
    def exitDestructSentence(self, ctx:NeoBasicParser.DestructSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#destructClause.
    def enterDestructClause(self, ctx:NeoBasicParser.DestructClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#destructClause.
    def exitDestructClause(self, ctx:NeoBasicParser.DestructClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#propertySentence.
    def enterPropertySentence(self, ctx:NeoBasicParser.PropertySentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#propertySentence.
    def exitPropertySentence(self, ctx:NeoBasicParser.PropertySentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#propertyClause.
    def enterPropertyClause(self, ctx:NeoBasicParser.PropertyClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#propertyClause.
    def exitPropertyClause(self, ctx:NeoBasicParser.PropertyClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#propertyBody.
    def enterPropertyBody(self, ctx:NeoBasicParser.PropertyBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#propertyBody.
    def exitPropertyBody(self, ctx:NeoBasicParser.PropertyBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#propertyAccessorSentence.
    def enterPropertyAccessorSentence(self, ctx:NeoBasicParser.PropertyAccessorSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#propertyAccessorSentence.
    def exitPropertyAccessorSentence(self, ctx:NeoBasicParser.PropertyAccessorSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#propertyGetterClause.
    def enterPropertyGetterClause(self, ctx:NeoBasicParser.PropertyGetterClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#propertyGetterClause.
    def exitPropertyGetterClause(self, ctx:NeoBasicParser.PropertyGetterClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#propertySetterClause.
    def enterPropertySetterClause(self, ctx:NeoBasicParser.PropertySetterClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#propertySetterClause.
    def exitPropertySetterClause(self, ctx:NeoBasicParser.PropertySetterClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#statementSentence.
    def enterStatementSentence(self, ctx:NeoBasicParser.StatementSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#statementSentence.
    def exitStatementSentence(self, ctx:NeoBasicParser.StatementSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#statementSuite.
    def enterStatementSuite(self, ctx:NeoBasicParser.StatementSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#statementSuite.
    def exitStatementSuite(self, ctx:NeoBasicParser.StatementSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#statementBlock.
    def enterStatementBlock(self, ctx:NeoBasicParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#statementBlock.
    def exitStatementBlock(self, ctx:NeoBasicParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#clauseStatement.
    def enterClauseStatement(self, ctx:NeoBasicParser.ClauseStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#clauseStatement.
    def exitClauseStatement(self, ctx:NeoBasicParser.ClauseStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#simpleStatement.
    def enterSimpleStatement(self, ctx:NeoBasicParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#simpleStatement.
    def exitSimpleStatement(self, ctx:NeoBasicParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#expressionStatement.
    def enterExpressionStatement(self, ctx:NeoBasicParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expressionStatement.
    def exitExpressionStatement(self, ctx:NeoBasicParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#emptyStatement.
    def enterEmptyStatement(self, ctx:NeoBasicParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#emptyStatement.
    def exitEmptyStatement(self, ctx:NeoBasicParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:NeoBasicParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:NeoBasicParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assignmentSingle.
    def enterAssignmentSingle(self, ctx:NeoBasicParser.AssignmentSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentSingle.
    def exitAssignmentSingle(self, ctx:NeoBasicParser.AssignmentSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assignmentMultiple.
    def enterAssignmentMultiple(self, ctx:NeoBasicParser.AssignmentMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentMultiple.
    def exitAssignmentMultiple(self, ctx:NeoBasicParser.AssignmentMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assignmentParallel.
    def enterAssignmentParallel(self, ctx:NeoBasicParser.AssignmentParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentParallel.
    def exitAssignmentParallel(self, ctx:NeoBasicParser.AssignmentParallelContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#consoleStatement.
    def enterConsoleStatement(self, ctx:NeoBasicParser.ConsoleStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#consoleStatement.
    def exitConsoleStatement(self, ctx:NeoBasicParser.ConsoleStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#atClause.
    def enterAtClause(self, ctx:NeoBasicParser.AtClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#atClause.
    def exitAtClause(self, ctx:NeoBasicParser.AtClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#echoCommand.
    def enterEchoCommand(self, ctx:NeoBasicParser.EchoCommandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#echoCommand.
    def exitEchoCommand(self, ctx:NeoBasicParser.EchoCommandContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#scanCommand.
    def enterScanCommand(self, ctx:NeoBasicParser.ScanCommandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#scanCommand.
    def exitScanCommand(self, ctx:NeoBasicParser.ScanCommandContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#alertCommand.
    def enterAlertCommand(self, ctx:NeoBasicParser.AlertCommandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#alertCommand.
    def exitAlertCommand(self, ctx:NeoBasicParser.AlertCommandContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#entryCommand.
    def enterEntryCommand(self, ctx:NeoBasicParser.EntryCommandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#entryCommand.
    def exitEntryCommand(self, ctx:NeoBasicParser.EntryCommandContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#playCommand.
    def enterPlayCommand(self, ctx:NeoBasicParser.PlayCommandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#playCommand.
    def exitPlayCommand(self, ctx:NeoBasicParser.PlayCommandContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#deterministicStatement.
    def enterDeterministicStatement(self, ctx:NeoBasicParser.DeterministicStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#deterministicStatement.
    def exitDeterministicStatement(self, ctx:NeoBasicParser.DeterministicStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#continueSentence.
    def enterContinueSentence(self, ctx:NeoBasicParser.ContinueSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#continueSentence.
    def exitContinueSentence(self, ctx:NeoBasicParser.ContinueSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#breakSentence.
    def enterBreakSentence(self, ctx:NeoBasicParser.BreakSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#breakSentence.
    def exitBreakSentence(self, ctx:NeoBasicParser.BreakSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#fallthroughSentence.
    def enterFallthroughSentence(self, ctx:NeoBasicParser.FallthroughSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#fallthroughSentence.
    def exitFallthroughSentence(self, ctx:NeoBasicParser.FallthroughSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#deferSentence.
    def enterDeferSentence(self, ctx:NeoBasicParser.DeferSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#deferSentence.
    def exitDeferSentence(self, ctx:NeoBasicParser.DeferSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#returnSentence.
    def enterReturnSentence(self, ctx:NeoBasicParser.ReturnSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#returnSentence.
    def exitReturnSentence(self, ctx:NeoBasicParser.ReturnSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#yieldSentence.
    def enterYieldSentence(self, ctx:NeoBasicParser.YieldSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#yieldSentence.
    def exitYieldSentence(self, ctx:NeoBasicParser.YieldSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#raiseSentence.
    def enterRaiseSentence(self, ctx:NeoBasicParser.RaiseSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#raiseSentence.
    def exitRaiseSentence(self, ctx:NeoBasicParser.RaiseSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#panicSentence.
    def enterPanicSentence(self, ctx:NeoBasicParser.PanicSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#panicSentence.
    def exitPanicSentence(self, ctx:NeoBasicParser.PanicSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#nondeterministicStatement.
    def enterNondeterministicStatement(self, ctx:NeoBasicParser.NondeterministicStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#nondeterministicStatement.
    def exitNondeterministicStatement(self, ctx:NeoBasicParser.NondeterministicStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ifThenSentence.
    def enterIfThenSentence(self, ctx:NeoBasicParser.IfThenSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ifThenSentence.
    def exitIfThenSentence(self, ctx:NeoBasicParser.IfThenSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#goSentence.
    def enterGoSentence(self, ctx:NeoBasicParser.GoSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#goSentence.
    def exitGoSentence(self, ctx:NeoBasicParser.GoSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#awaitSentence.
    def enterAwaitSentence(self, ctx:NeoBasicParser.AwaitSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#awaitSentence.
    def exitAwaitSentence(self, ctx:NeoBasicParser.AwaitSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compoundStatement.
    def enterCompoundStatement(self, ctx:NeoBasicParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compoundStatement.
    def exitCompoundStatement(self, ctx:NeoBasicParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:NeoBasicParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:NeoBasicParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#iterationStatement.
    def enterIterationStatement(self, ctx:NeoBasicParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#iterationStatement.
    def exitIterationStatement(self, ctx:NeoBasicParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#controlFlowStatement.
    def enterControlFlowStatement(self, ctx:NeoBasicParser.ControlFlowStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#controlFlowStatement.
    def exitControlFlowStatement(self, ctx:NeoBasicParser.ControlFlowStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#concurrencyStatement.
    def enterConcurrencyStatement(self, ctx:NeoBasicParser.ConcurrencyStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#concurrencyStatement.
    def exitConcurrencyStatement(self, ctx:NeoBasicParser.ConcurrencyStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ifSentence.
    def enterIfSentence(self, ctx:NeoBasicParser.IfSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ifSentence.
    def exitIfSentence(self, ctx:NeoBasicParser.IfSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ifClause.
    def enterIfClause(self, ctx:NeoBasicParser.IfClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ifClause.
    def exitIfClause(self, ctx:NeoBasicParser.IfClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#elifClause.
    def enterElifClause(self, ctx:NeoBasicParser.ElifClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#elifClause.
    def exitElifClause(self, ctx:NeoBasicParser.ElifClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#elseClause.
    def enterElseClause(self, ctx:NeoBasicParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#elseClause.
    def exitElseClause(self, ctx:NeoBasicParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#matchSentence.
    def enterMatchSentence(self, ctx:NeoBasicParser.MatchSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#matchSentence.
    def exitMatchSentence(self, ctx:NeoBasicParser.MatchSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#matchClause.
    def enterMatchClause(self, ctx:NeoBasicParser.MatchClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#matchClause.
    def exitMatchClause(self, ctx:NeoBasicParser.MatchClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#caseClause.
    def enterCaseClause(self, ctx:NeoBasicParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#caseClause.
    def exitCaseClause(self, ctx:NeoBasicParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#trySentence.
    def enterTrySentence(self, ctx:NeoBasicParser.TrySentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#trySentence.
    def exitTrySentence(self, ctx:NeoBasicParser.TrySentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#tryClause.
    def enterTryClause(self, ctx:NeoBasicParser.TryClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#tryClause.
    def exitTryClause(self, ctx:NeoBasicParser.TryClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#catchClause.
    def enterCatchClause(self, ctx:NeoBasicParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#catchClause.
    def exitCatchClause(self, ctx:NeoBasicParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#switchSentence.
    def enterSwitchSentence(self, ctx:NeoBasicParser.SwitchSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#switchSentence.
    def exitSwitchSentence(self, ctx:NeoBasicParser.SwitchSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#switchClause.
    def enterSwitchClause(self, ctx:NeoBasicParser.SwitchClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#switchClause.
    def exitSwitchClause(self, ctx:NeoBasicParser.SwitchClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#whenClause.
    def enterWhenClause(self, ctx:NeoBasicParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#whenClause.
    def exitWhenClause(self, ctx:NeoBasicParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#defaultClause.
    def enterDefaultClause(self, ctx:NeoBasicParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#defaultClause.
    def exitDefaultClause(self, ctx:NeoBasicParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopSentence.
    def enterLoopSentence(self, ctx:NeoBasicParser.LoopSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopSentence.
    def exitLoopSentence(self, ctx:NeoBasicParser.LoopSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopClause.
    def enterLoopClause(self, ctx:NeoBasicParser.LoopClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopClause.
    def exitLoopClause(self, ctx:NeoBasicParser.LoopClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopBody.
    def enterLoopBody(self, ctx:NeoBasicParser.LoopBodyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopBody.
    def exitLoopBody(self, ctx:NeoBasicParser.LoopBodyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopNoCheck.
    def enterLoopNoCheck(self, ctx:NeoBasicParser.LoopNoCheckContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopNoCheck.
    def exitLoopNoCheck(self, ctx:NeoBasicParser.LoopNoCheckContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopCheckFirst.
    def enterLoopCheckFirst(self, ctx:NeoBasicParser.LoopCheckFirstContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopCheckFirst.
    def exitLoopCheckFirst(self, ctx:NeoBasicParser.LoopCheckFirstContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopCheckLast.
    def enterLoopCheckLast(self, ctx:NeoBasicParser.LoopCheckLastContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopCheckLast.
    def exitLoopCheckLast(self, ctx:NeoBasicParser.LoopCheckLastContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#nextClause.
    def enterNextClause(self, ctx:NeoBasicParser.NextClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#nextClause.
    def exitNextClause(self, ctx:NeoBasicParser.NextClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#uptoClause.
    def enterUptoClause(self, ctx:NeoBasicParser.UptoClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#uptoClause.
    def exitUptoClause(self, ctx:NeoBasicParser.UptoClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#pretestClause.
    def enterPretestClause(self, ctx:NeoBasicParser.PretestClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#pretestClause.
    def exitPretestClause(self, ctx:NeoBasicParser.PretestClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#posttestClause.
    def enterPosttestClause(self, ctx:NeoBasicParser.PosttestClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#posttestClause.
    def exitPosttestClause(self, ctx:NeoBasicParser.PosttestClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopEachClause.
    def enterLoopEachClause(self, ctx:NeoBasicParser.LoopEachClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopEachClause.
    def exitLoopEachClause(self, ctx:NeoBasicParser.LoopEachClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopWhileClause.
    def enterLoopWhileClause(self, ctx:NeoBasicParser.LoopWhileClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopWhileClause.
    def exitLoopWhileClause(self, ctx:NeoBasicParser.LoopWhileClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#loopUntilClause.
    def enterLoopUntilClause(self, ctx:NeoBasicParser.LoopUntilClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#loopUntilClause.
    def exitLoopUntilClause(self, ctx:NeoBasicParser.LoopUntilClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#thenClause.
    def enterThenClause(self, ctx:NeoBasicParser.ThenClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#thenClause.
    def exitThenClause(self, ctx:NeoBasicParser.ThenClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#beginSentence.
    def enterBeginSentence(self, ctx:NeoBasicParser.BeginSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#beginSentence.
    def exitBeginSentence(self, ctx:NeoBasicParser.BeginSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#beginClause.
    def enterBeginClause(self, ctx:NeoBasicParser.BeginClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#beginClause.
    def exitBeginClause(self, ctx:NeoBasicParser.BeginClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#endClause.
    def enterEndClause(self, ctx:NeoBasicParser.EndClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#endClause.
    def exitEndClause(self, ctx:NeoBasicParser.EndClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#withSentence.
    def enterWithSentence(self, ctx:NeoBasicParser.WithSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#withSentence.
    def exitWithSentence(self, ctx:NeoBasicParser.WithSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#withClause.
    def enterWithClause(self, ctx:NeoBasicParser.WithClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#withClause.
    def exitWithClause(self, ctx:NeoBasicParser.WithClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#gosubSentence.
    def enterGosubSentence(self, ctx:NeoBasicParser.GosubSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#gosubSentence.
    def exitGosubSentence(self, ctx:NeoBasicParser.GosubSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#gosubClause.
    def enterGosubClause(self, ctx:NeoBasicParser.GosubClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#gosubClause.
    def exitGosubClause(self, ctx:NeoBasicParser.GosubClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#forkClause.
    def enterForkClause(self, ctx:NeoBasicParser.ForkClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#forkClause.
    def exitForkClause(self, ctx:NeoBasicParser.ForkClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#forEachClause.
    def enterForEachClause(self, ctx:NeoBasicParser.ForEachClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#forEachClause.
    def exitForEachClause(self, ctx:NeoBasicParser.ForEachClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#testingStatement.
    def enterTestingStatement(self, ctx:NeoBasicParser.TestingStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#testingStatement.
    def exitTestingStatement(self, ctx:NeoBasicParser.TestingStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#simpleTestStatement.
    def enterSimpleTestStatement(self, ctx:NeoBasicParser.SimpleTestStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#simpleTestStatement.
    def exitSimpleTestStatement(self, ctx:NeoBasicParser.SimpleTestStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compoundTestStatement.
    def enterCompoundTestStatement(self, ctx:NeoBasicParser.CompoundTestStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compoundTestStatement.
    def exitCompoundTestStatement(self, ctx:NeoBasicParser.CompoundTestStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assertTestStatement.
    def enterAssertTestStatement(self, ctx:NeoBasicParser.AssertTestStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assertTestStatement.
    def exitAssertTestStatement(self, ctx:NeoBasicParser.AssertTestStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assertClause.
    def enterAssertClause(self, ctx:NeoBasicParser.AssertClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assertClause.
    def exitAssertClause(self, ctx:NeoBasicParser.AssertClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unitTestStatement.
    def enterUnitTestStatement(self, ctx:NeoBasicParser.UnitTestStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unitTestStatement.
    def exitUnitTestStatement(self, ctx:NeoBasicParser.UnitTestStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unitClause.
    def enterUnitClause(self, ctx:NeoBasicParser.UnitClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unitClause.
    def exitUnitClause(self, ctx:NeoBasicParser.UnitClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#fromClause.
    def enterFromClause(self, ctx:NeoBasicParser.FromClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#fromClause.
    def exitFromClause(self, ctx:NeoBasicParser.FromClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#onceClause.
    def enterOnceClause(self, ctx:NeoBasicParser.OnceClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#onceClause.
    def exitOnceClause(self, ctx:NeoBasicParser.OnceClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#dataClause.
    def enterDataClause(self, ctx:NeoBasicParser.DataClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#dataClause.
    def exitDataClause(self, ctx:NeoBasicParser.DataClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#dataTable.
    def enterDataTable(self, ctx:NeoBasicParser.DataTableContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#dataTable.
    def exitDataTable(self, ctx:NeoBasicParser.DataTableContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#dataRow.
    def enterDataRow(self, ctx:NeoBasicParser.DataRowContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#dataRow.
    def exitDataRow(self, ctx:NeoBasicParser.DataRowContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#callClause.
    def enterCallClause(self, ctx:NeoBasicParser.CallClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#callClause.
    def exitCallClause(self, ctx:NeoBasicParser.CallClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#hideClause.
    def enterHideClause(self, ctx:NeoBasicParser.HideClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#hideClause.
    def exitHideClause(self, ctx:NeoBasicParser.HideClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#showClause.
    def enterShowClause(self, ctx:NeoBasicParser.ShowClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#showClause.
    def exitShowClause(self, ctx:NeoBasicParser.ShowClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#stayClause.
    def enterStayClause(self, ctx:NeoBasicParser.StayClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#stayClause.
    def exitStayClause(self, ctx:NeoBasicParser.StayClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#passClause.
    def enterPassClause(self, ctx:NeoBasicParser.PassClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#passClause.
    def exitPassClause(self, ctx:NeoBasicParser.PassClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#pastClause.
    def enterPastClause(self, ctx:NeoBasicParser.PastClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#pastClause.
    def exitPastClause(self, ctx:NeoBasicParser.PastClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#failClause.
    def enterFailClause(self, ctx:NeoBasicParser.FailClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#failClause.
    def exitFailClause(self, ctx:NeoBasicParser.FailClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#prefixUnaryOperator.
    def enterPrefixUnaryOperator(self, ctx:NeoBasicParser.PrefixUnaryOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#prefixUnaryOperator.
    def exitPrefixUnaryOperator(self, ctx:NeoBasicParser.PrefixUnaryOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unaryArithmeticOperator.
    def enterUnaryArithmeticOperator(self, ctx:NeoBasicParser.UnaryArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryArithmeticOperator.
    def exitUnaryArithmeticOperator(self, ctx:NeoBasicParser.UnaryArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unaryLogicalOperator.
    def enterUnaryLogicalOperator(self, ctx:NeoBasicParser.UnaryLogicalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryLogicalOperator.
    def exitUnaryLogicalOperator(self, ctx:NeoBasicParser.UnaryLogicalOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unaryArrayOperator.
    def enterUnaryArrayOperator(self, ctx:NeoBasicParser.UnaryArrayOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryArrayOperator.
    def exitUnaryArrayOperator(self, ctx:NeoBasicParser.UnaryArrayOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def enterUnarySpreadOperator(self, ctx:NeoBasicParser.UnarySpreadOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def exitUnarySpreadOperator(self, ctx:NeoBasicParser.UnarySpreadOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unaryCloneOperator.
    def enterUnaryCloneOperator(self, ctx:NeoBasicParser.UnaryCloneOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryCloneOperator.
    def exitUnaryCloneOperator(self, ctx:NeoBasicParser.UnaryCloneOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unaryMoveOperator.
    def enterUnaryMoveOperator(self, ctx:NeoBasicParser.UnaryMoveOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryMoveOperator.
    def exitUnaryMoveOperator(self, ctx:NeoBasicParser.UnaryMoveOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def enterUnaryMetaOperator(self, ctx:NeoBasicParser.UnaryMetaOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def exitUnaryMetaOperator(self, ctx:NeoBasicParser.UnaryMetaOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryArithmeticOperator.
    def enterBinaryArithmeticOperator(self, ctx:NeoBasicParser.BinaryArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryArithmeticOperator.
    def exitBinaryArithmeticOperator(self, ctx:NeoBasicParser.BinaryArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryExponentialOperator.
    def enterBinaryExponentialOperator(self, ctx:NeoBasicParser.BinaryExponentialOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryExponentialOperator.
    def exitBinaryExponentialOperator(self, ctx:NeoBasicParser.BinaryExponentialOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryMultiplicativeOperator.
    def enterBinaryMultiplicativeOperator(self, ctx:NeoBasicParser.BinaryMultiplicativeOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryMultiplicativeOperator.
    def exitBinaryMultiplicativeOperator(self, ctx:NeoBasicParser.BinaryMultiplicativeOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryAdditiveOperator.
    def enterBinaryAdditiveOperator(self, ctx:NeoBasicParser.BinaryAdditiveOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryAdditiveOperator.
    def exitBinaryAdditiveOperator(self, ctx:NeoBasicParser.BinaryAdditiveOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#bitShiftOperator.
    def enterBitShiftOperator(self, ctx:NeoBasicParser.BitShiftOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#bitShiftOperator.
    def exitBitShiftOperator(self, ctx:NeoBasicParser.BitShiftOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryConjunctionOperator.
    def enterBinaryConjunctionOperator(self, ctx:NeoBasicParser.BinaryConjunctionOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryConjunctionOperator.
    def exitBinaryConjunctionOperator(self, ctx:NeoBasicParser.BinaryConjunctionOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryExclusiveDisjunctionOperator.
    def enterBinaryExclusiveDisjunctionOperator(self, ctx:NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryExclusiveDisjunctionOperator.
    def exitBinaryExclusiveDisjunctionOperator(self, ctx:NeoBasicParser.BinaryExclusiveDisjunctionOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryDisjunctionOperator.
    def enterBinaryDisjunctionOperator(self, ctx:NeoBasicParser.BinaryDisjunctionOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryDisjunctionOperator.
    def exitBinaryDisjunctionOperator(self, ctx:NeoBasicParser.BinaryDisjunctionOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryArrayOperator.
    def enterBinaryArrayOperator(self, ctx:NeoBasicParser.BinaryArrayOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryArrayOperator.
    def exitBinaryArrayOperator(self, ctx:NeoBasicParser.BinaryArrayOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryComparisonOperator.
    def enterBinaryComparisonOperator(self, ctx:NeoBasicParser.BinaryComparisonOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryComparisonOperator.
    def exitBinaryComparisonOperator(self, ctx:NeoBasicParser.BinaryComparisonOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryRelationalOperator.
    def enterBinaryRelationalOperator(self, ctx:NeoBasicParser.BinaryRelationalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryRelationalOperator.
    def exitBinaryRelationalOperator(self, ctx:NeoBasicParser.BinaryRelationalOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryConditionalOperator.
    def enterBinaryConditionalOperator(self, ctx:NeoBasicParser.BinaryConditionalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryConditionalOperator.
    def exitBinaryConditionalOperator(self, ctx:NeoBasicParser.BinaryConditionalOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryMonadBindOperator.
    def enterBinaryMonadBindOperator(self, ctx:NeoBasicParser.BinaryMonadBindOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryMonadBindOperator.
    def exitBinaryMonadBindOperator(self, ctx:NeoBasicParser.BinaryMonadBindOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryPipelineOperator.
    def enterBinaryPipelineOperator(self, ctx:NeoBasicParser.BinaryPipelineOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryPipelineOperator.
    def exitBinaryPipelineOperator(self, ctx:NeoBasicParser.BinaryPipelineOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#coalescingOperator.
    def enterCoalescingOperator(self, ctx:NeoBasicParser.CoalescingOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#coalescingOperator.
    def exitCoalescingOperator(self, ctx:NeoBasicParser.CoalescingOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#executionFlowOperator.
    def enterExecutionFlowOperator(self, ctx:NeoBasicParser.ExecutionFlowOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#executionFlowOperator.
    def exitExecutionFlowOperator(self, ctx:NeoBasicParser.ExecutionFlowOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#intervalOperator.
    def enterIntervalOperator(self, ctx:NeoBasicParser.IntervalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#intervalOperator.
    def exitIntervalOperator(self, ctx:NeoBasicParser.IntervalOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#leftIntervalOperator.
    def enterLeftIntervalOperator(self, ctx:NeoBasicParser.LeftIntervalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#leftIntervalOperator.
    def exitLeftIntervalOperator(self, ctx:NeoBasicParser.LeftIntervalOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#rightIntervalOperator.
    def enterRightIntervalOperator(self, ctx:NeoBasicParser.RightIntervalOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#rightIntervalOperator.
    def exitRightIntervalOperator(self, ctx:NeoBasicParser.RightIntervalOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:NeoBasicParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:NeoBasicParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#singleAssignmentOperator.
    def enterSingleAssignmentOperator(self, ctx:NeoBasicParser.SingleAssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#singleAssignmentOperator.
    def exitSingleAssignmentOperator(self, ctx:NeoBasicParser.SingleAssignmentOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unpackingAssignmentOperator.
    def enterUnpackingAssignmentOperator(self, ctx:NeoBasicParser.UnpackingAssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unpackingAssignmentOperator.
    def exitUnpackingAssignmentOperator(self, ctx:NeoBasicParser.UnpackingAssignmentOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compoundAssignmentOperator.
    def enterCompoundAssignmentOperator(self, ctx:NeoBasicParser.CompoundAssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compoundAssignmentOperator.
    def exitCompoundAssignmentOperator(self, ctx:NeoBasicParser.CompoundAssignmentOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#overloadableOperator.
    def enterOverloadableOperator(self, ctx:NeoBasicParser.OverloadableOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#overloadableOperator.
    def exitOverloadableOperator(self, ctx:NeoBasicParser.OverloadableOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#symbolDecorators.
    def enterSymbolDecorators(self, ctx:NeoBasicParser.SymbolDecoratorsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#symbolDecorators.
    def exitSymbolDecorators(self, ctx:NeoBasicParser.SymbolDecoratorsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#symbolDecorator.
    def enterSymbolDecorator(self, ctx:NeoBasicParser.SymbolDecoratorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#symbolDecorator.
    def exitSymbolDecorator(self, ctx:NeoBasicParser.SymbolDecoratorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#annotationDecorator.
    def enterAnnotationDecorator(self, ctx:NeoBasicParser.AnnotationDecoratorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#annotationDecorator.
    def exitAnnotationDecorator(self, ctx:NeoBasicParser.AnnotationDecoratorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#aspectDecorator.
    def enterAspectDecorator(self, ctx:NeoBasicParser.AspectDecoratorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#aspectDecorator.
    def exitAspectDecorator(self, ctx:NeoBasicParser.AspectDecoratorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#taggedValuePairs.
    def enterTaggedValuePairs(self, ctx:NeoBasicParser.TaggedValuePairsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#taggedValuePairs.
    def exitTaggedValuePairs(self, ctx:NeoBasicParser.TaggedValuePairsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#taggedValuePair.
    def enterTaggedValuePair(self, ctx:NeoBasicParser.TaggedValuePairContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#taggedValuePair.
    def exitTaggedValuePair(self, ctx:NeoBasicParser.TaggedValuePairContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#genericTypeParameters.
    def enterGenericTypeParameters(self, ctx:NeoBasicParser.GenericTypeParametersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#genericTypeParameters.
    def exitGenericTypeParameters(self, ctx:NeoBasicParser.GenericTypeParametersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeParameters.
    def enterTypeParameters(self, ctx:NeoBasicParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeParameters.
    def exitTypeParameters(self, ctx:NeoBasicParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typeParameter.
    def enterTypeParameter(self, ctx:NeoBasicParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typeParameter.
    def exitTypeParameter(self, ctx:NeoBasicParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#types.
    def enterTypes(self, ctx:NeoBasicParser.TypesContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#types.
    def exitTypes(self, ctx:NeoBasicParser.TypesContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#type.
    def enterType(self, ctx:NeoBasicParser.TypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#type.
    def exitType(self, ctx:NeoBasicParser.TypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#prefixTypeModifier.
    def enterPrefixTypeModifier(self, ctx:NeoBasicParser.PrefixTypeModifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#prefixTypeModifier.
    def exitPrefixTypeModifier(self, ctx:NeoBasicParser.PrefixTypeModifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#postfixTypeWrapper.
    def enterPostfixTypeWrapper(self, ctx:NeoBasicParser.PostfixTypeWrapperContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#postfixTypeWrapper.
    def exitPostfixTypeWrapper(self, ctx:NeoBasicParser.PostfixTypeWrapperContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#nativeType.
    def enterNativeType(self, ctx:NeoBasicParser.NativeTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#nativeType.
    def exitNativeType(self, ctx:NeoBasicParser.NativeTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#escalarType.
    def enterEscalarType(self, ctx:NeoBasicParser.EscalarTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#escalarType.
    def exitEscalarType(self, ctx:NeoBasicParser.EscalarTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#booleanType.
    def enterBooleanType(self, ctx:NeoBasicParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#booleanType.
    def exitBooleanType(self, ctx:NeoBasicParser.BooleanTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericType.
    def enterNumericType(self, ctx:NeoBasicParser.NumericTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericType.
    def exitNumericType(self, ctx:NeoBasicParser.NumericTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericNatural.
    def enterNumericNatural(self, ctx:NeoBasicParser.NumericNaturalContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericNatural.
    def exitNumericNatural(self, ctx:NeoBasicParser.NumericNaturalContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericInteger.
    def enterNumericInteger(self, ctx:NeoBasicParser.NumericIntegerContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericInteger.
    def exitNumericInteger(self, ctx:NeoBasicParser.NumericIntegerContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericDecimal.
    def enterNumericDecimal(self, ctx:NeoBasicParser.NumericDecimalContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericDecimal.
    def exitNumericDecimal(self, ctx:NeoBasicParser.NumericDecimalContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericReal.
    def enterNumericReal(self, ctx:NeoBasicParser.NumericRealContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericReal.
    def exitNumericReal(self, ctx:NeoBasicParser.NumericRealContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericRatio.
    def enterNumericRatio(self, ctx:NeoBasicParser.NumericRatioContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericRatio.
    def exitNumericRatio(self, ctx:NeoBasicParser.NumericRatioContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericComplex.
    def enterNumericComplex(self, ctx:NeoBasicParser.NumericComplexContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericComplex.
    def exitNumericComplex(self, ctx:NeoBasicParser.NumericComplexContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericQuaternion.
    def enterNumericQuaternion(self, ctx:NeoBasicParser.NumericQuaternionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericQuaternion.
    def exitNumericQuaternion(self, ctx:NeoBasicParser.NumericQuaternionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#temporalType.
    def enterTemporalType(self, ctx:NeoBasicParser.TemporalTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#temporalType.
    def exitTemporalType(self, ctx:NeoBasicParser.TemporalTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#characterType.
    def enterCharacterType(self, ctx:NeoBasicParser.CharacterTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#characterType.
    def exitCharacterType(self, ctx:NeoBasicParser.CharacterTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compoundType.
    def enterCompoundType(self, ctx:NeoBasicParser.CompoundTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compoundType.
    def exitCompoundType(self, ctx:NeoBasicParser.CompoundTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#sequenceType.
    def enterSequenceType(self, ctx:NeoBasicParser.SequenceTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#sequenceType.
    def exitSequenceType(self, ctx:NeoBasicParser.SequenceTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compositeType.
    def enterCompositeType(self, ctx:NeoBasicParser.CompositeTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compositeType.
    def exitCompositeType(self, ctx:NeoBasicParser.CompositeTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#collectionType.
    def enterCollectionType(self, ctx:NeoBasicParser.CollectionTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#collectionType.
    def exitCollectionType(self, ctx:NeoBasicParser.CollectionTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#optionType.
    def enterOptionType(self, ctx:NeoBasicParser.OptionTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#optionType.
    def exitOptionType(self, ctx:NeoBasicParser.OptionTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#metaType.
    def enterMetaType(self, ctx:NeoBasicParser.MetaTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#metaType.
    def exitMetaType(self, ctx:NeoBasicParser.MetaTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procType.
    def enterProcType(self, ctx:NeoBasicParser.ProcTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procType.
    def exitProcType(self, ctx:NeoBasicParser.ProcTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#castType.
    def enterCastType(self, ctx:NeoBasicParser.CastTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#castType.
    def exitCastType(self, ctx:NeoBasicParser.CastTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#factType.
    def enterFactType(self, ctx:NeoBasicParser.FactTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#factType.
    def exitFactType(self, ctx:NeoBasicParser.FactTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#macroType.
    def enterMacroType(self, ctx:NeoBasicParser.MacroTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#macroType.
    def exitMacroType(self, ctx:NeoBasicParser.MacroTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#funcType.
    def enterFuncType(self, ctx:NeoBasicParser.FuncTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#funcType.
    def exitFuncType(self, ctx:NeoBasicParser.FuncTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#feedType.
    def enterFeedType(self, ctx:NeoBasicParser.FeedTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#feedType.
    def exitFeedType(self, ctx:NeoBasicParser.FeedTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#subType.
    def enterSubType(self, ctx:NeoBasicParser.SubTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#subType.
    def exitSubType(self, ctx:NeoBasicParser.SubTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#operatorType.
    def enterOperatorType(self, ctx:NeoBasicParser.OperatorTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#operatorType.
    def exitOperatorType(self, ctx:NeoBasicParser.OperatorTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#eventType.
    def enterEventType(self, ctx:NeoBasicParser.EventTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#eventType.
    def exitEventType(self, ctx:NeoBasicParser.EventTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#getterType.
    def enterGetterType(self, ctx:NeoBasicParser.GetterTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#getterType.
    def exitGetterType(self, ctx:NeoBasicParser.GetterTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#setterType.
    def enterSetterType(self, ctx:NeoBasicParser.SetterTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#setterType.
    def exitSetterType(self, ctx:NeoBasicParser.SetterTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#parenthesizedParameterTypes.
    def enterParenthesizedParameterTypes(self, ctx:NeoBasicParser.ParenthesizedParameterTypesContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#parenthesizedParameterTypes.
    def exitParenthesizedParameterTypes(self, ctx:NeoBasicParser.ParenthesizedParameterTypesContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#bracketedParameterTypes.
    def enterBracketedParameterTypes(self, ctx:NeoBasicParser.BracketedParameterTypesContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#bracketedParameterTypes.
    def exitBracketedParameterTypes(self, ctx:NeoBasicParser.BracketedParameterTypesContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procParameterTypes.
    def enterProcParameterTypes(self, ctx:NeoBasicParser.ProcParameterTypesContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procParameterTypes.
    def exitProcParameterTypes(self, ctx:NeoBasicParser.ProcParameterTypesContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#procParameterType.
    def enterProcParameterType(self, ctx:NeoBasicParser.ProcParameterTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#procParameterType.
    def exitProcParameterType(self, ctx:NeoBasicParser.ProcParameterTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#literal.
    def enterLiteral(self, ctx:NeoBasicParser.LiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#literal.
    def exitLiteral(self, ctx:NeoBasicParser.LiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#escalarLiteral.
    def enterEscalarLiteral(self, ctx:NeoBasicParser.EscalarLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#escalarLiteral.
    def exitEscalarLiteral(self, ctx:NeoBasicParser.EscalarLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:NeoBasicParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:NeoBasicParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#numericLiteral.
    def enterNumericLiteral(self, ctx:NeoBasicParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#numericLiteral.
    def exitNumericLiteral(self, ctx:NeoBasicParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#elapseLiteral.
    def enterElapseLiteral(self, ctx:NeoBasicParser.ElapseLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#elapseLiteral.
    def exitElapseLiteral(self, ctx:NeoBasicParser.ElapseLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#dateLiteral.
    def enterDateLiteral(self, ctx:NeoBasicParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#dateLiteral.
    def exitDateLiteral(self, ctx:NeoBasicParser.DateLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#characterLiteral.
    def enterCharacterLiteral(self, ctx:NeoBasicParser.CharacterLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#characterLiteral.
    def exitCharacterLiteral(self, ctx:NeoBasicParser.CharacterLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#optionLiteral.
    def enterOptionLiteral(self, ctx:NeoBasicParser.OptionLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#optionLiteral.
    def exitOptionLiteral(self, ctx:NeoBasicParser.OptionLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#resultLiteral.
    def enterResultLiteral(self, ctx:NeoBasicParser.ResultLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#resultLiteral.
    def exitResultLiteral(self, ctx:NeoBasicParser.ResultLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#maybeLiteral.
    def enterMaybeLiteral(self, ctx:NeoBasicParser.MaybeLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#maybeLiteral.
    def exitMaybeLiteral(self, ctx:NeoBasicParser.MaybeLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#eitherLiteral.
    def enterEitherLiteral(self, ctx:NeoBasicParser.EitherLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#eitherLiteral.
    def exitEitherLiteral(self, ctx:NeoBasicParser.EitherLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#streamLiteral.
    def enterStreamLiteral(self, ctx:NeoBasicParser.StreamLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#streamLiteral.
    def exitStreamLiteral(self, ctx:NeoBasicParser.StreamLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compoundLiteral.
    def enterCompoundLiteral(self, ctx:NeoBasicParser.CompoundLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compoundLiteral.
    def exitCompoundLiteral(self, ctx:NeoBasicParser.CompoundLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#sequenceLiteral.
    def enterSequenceLiteral(self, ctx:NeoBasicParser.SequenceLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#sequenceLiteral.
    def exitSequenceLiteral(self, ctx:NeoBasicParser.SequenceLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#stringLiteral.
    def enterStringLiteral(self, ctx:NeoBasicParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#stringLiteral.
    def exitStringLiteral(self, ctx:NeoBasicParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#musicalLiteral.
    def enterMusicalLiteral(self, ctx:NeoBasicParser.MusicalLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#musicalLiteral.
    def exitMusicalLiteral(self, ctx:NeoBasicParser.MusicalLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#compositeLiteral.
    def enterCompositeLiteral(self, ctx:NeoBasicParser.CompositeLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compositeLiteral.
    def exitCompositeLiteral(self, ctx:NeoBasicParser.CompositeLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#rangeLiteral.
    def enterRangeLiteral(self, ctx:NeoBasicParser.RangeLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#rangeLiteral.
    def exitRangeLiteral(self, ctx:NeoBasicParser.RangeLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#pairLiteral.
    def enterPairLiteral(self, ctx:NeoBasicParser.PairLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#pairLiteral.
    def exitPairLiteral(self, ctx:NeoBasicParser.PairLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#tupleLiteral.
    def enterTupleLiteral(self, ctx:NeoBasicParser.TupleLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#tupleLiteral.
    def exitTupleLiteral(self, ctx:NeoBasicParser.TupleLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#inetLiteral.
    def enterInetLiteral(self, ctx:NeoBasicParser.InetLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#inetLiteral.
    def exitInetLiteral(self, ctx:NeoBasicParser.InetLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#uriLiteral.
    def enterUriLiteral(self, ctx:NeoBasicParser.UriLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#uriLiteral.
    def exitUriLiteral(self, ctx:NeoBasicParser.UriLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#shellPathLiteral.
    def enterShellPathLiteral(self, ctx:NeoBasicParser.ShellPathLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#shellPathLiteral.
    def exitShellPathLiteral(self, ctx:NeoBasicParser.ShellPathLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#shellPathLiterals.
    def enterShellPathLiterals(self, ctx:NeoBasicParser.ShellPathLiteralsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#shellPathLiterals.
    def exitShellPathLiterals(self, ctx:NeoBasicParser.ShellPathLiteralsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlDocLiteral.
    def enterXmlDocLiteral(self, ctx:NeoBasicParser.XmlDocLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlDocLiteral.
    def exitXmlDocLiteral(self, ctx:NeoBasicParser.XmlDocLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlDocElement.
    def enterXmlDocElement(self, ctx:NeoBasicParser.XmlDocElementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlDocElement.
    def exitXmlDocElement(self, ctx:NeoBasicParser.XmlDocElementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlElementPaired.
    def enterXmlElementPaired(self, ctx:NeoBasicParser.XmlElementPairedContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlElementPaired.
    def exitXmlElementPaired(self, ctx:NeoBasicParser.XmlElementPairedContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlOpeningElement.
    def enterXmlOpeningElement(self, ctx:NeoBasicParser.XmlOpeningElementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlOpeningElement.
    def exitXmlOpeningElement(self, ctx:NeoBasicParser.XmlOpeningElementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlClosingElement.
    def enterXmlClosingElement(self, ctx:NeoBasicParser.XmlClosingElementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlClosingElement.
    def exitXmlClosingElement(self, ctx:NeoBasicParser.XmlClosingElementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlElementSelfClosed.
    def enterXmlElementSelfClosed(self, ctx:NeoBasicParser.XmlElementSelfClosedContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlElementSelfClosed.
    def exitXmlElementSelfClosed(self, ctx:NeoBasicParser.XmlElementSelfClosedContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlDocFragment.
    def enterXmlDocFragment(self, ctx:NeoBasicParser.XmlDocFragmentContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlDocFragment.
    def exitXmlDocFragment(self, ctx:NeoBasicParser.XmlDocFragmentContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlFragmentPaired.
    def enterXmlFragmentPaired(self, ctx:NeoBasicParser.XmlFragmentPairedContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlFragmentPaired.
    def exitXmlFragmentPaired(self, ctx:NeoBasicParser.XmlFragmentPairedContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlFragmentSelfClosed.
    def enterXmlFragmentSelfClosed(self, ctx:NeoBasicParser.XmlFragmentSelfClosedContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlFragmentSelfClosed.
    def exitXmlFragmentSelfClosed(self, ctx:NeoBasicParser.XmlFragmentSelfClosedContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlTagName.
    def enterXmlTagName(self, ctx:NeoBasicParser.XmlTagNameContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlTagName.
    def exitXmlTagName(self, ctx:NeoBasicParser.XmlTagNameContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlAttributes.
    def enterXmlAttributes(self, ctx:NeoBasicParser.XmlAttributesContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlAttributes.
    def exitXmlAttributes(self, ctx:NeoBasicParser.XmlAttributesContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlAttributeValue.
    def enterXmlAttributeValue(self, ctx:NeoBasicParser.XmlAttributeValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlAttributeValue.
    def exitXmlAttributeValue(self, ctx:NeoBasicParser.XmlAttributeValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#xmlChildren.
    def enterXmlChildren(self, ctx:NeoBasicParser.XmlChildrenContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#xmlChildren.
    def exitXmlChildren(self, ctx:NeoBasicParser.XmlChildrenContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#expressionPlaceholder.
    def enterExpressionPlaceholder(self, ctx:NeoBasicParser.ExpressionPlaceholderContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expressionPlaceholder.
    def exitExpressionPlaceholder(self, ctx:NeoBasicParser.ExpressionPlaceholderContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#collectionLiteral.
    def enterCollectionLiteral(self, ctx:NeoBasicParser.CollectionLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#collectionLiteral.
    def exitCollectionLiteral(self, ctx:NeoBasicParser.CollectionLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#collectionLiteralValue.
    def enterCollectionLiteralValue(self, ctx:NeoBasicParser.CollectionLiteralValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#collectionLiteralValue.
    def exitCollectionLiteralValue(self, ctx:NeoBasicParser.CollectionLiteralValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#elements.
    def enterElements(self, ctx:NeoBasicParser.ElementsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#elements.
    def exitElements(self, ctx:NeoBasicParser.ElementsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#element.
    def enterElement(self, ctx:NeoBasicParser.ElementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#element.
    def exitElement(self, ctx:NeoBasicParser.ElementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#elementKey.
    def enterElementKey(self, ctx:NeoBasicParser.ElementKeyContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#elementKey.
    def exitElementKey(self, ctx:NeoBasicParser.ElementKeyContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#elementValue.
    def enterElementValue(self, ctx:NeoBasicParser.ElementValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#elementValue.
    def exitElementValue(self, ctx:NeoBasicParser.ElementValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#arrayAosToSoaLiteral.
    def enterArrayAosToSoaLiteral(self, ctx:NeoBasicParser.ArrayAosToSoaLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#arrayAosToSoaLiteral.
    def exitArrayAosToSoaLiteral(self, ctx:NeoBasicParser.ArrayAosToSoaLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#listComprehension.
    def enterListComprehension(self, ctx:NeoBasicParser.ListComprehensionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#listComprehension.
    def exitListComprehension(self, ctx:NeoBasicParser.ListComprehensionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#comprehensionClause.
    def enterComprehensionClause(self, ctx:NeoBasicParser.ComprehensionClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#comprehensionClause.
    def exitComprehensionClause(self, ctx:NeoBasicParser.ComprehensionClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#objectLiteral.
    def enterObjectLiteral(self, ctx:NeoBasicParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#objectLiteral.
    def exitObjectLiteral(self, ctx:NeoBasicParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#objectLiteralValue.
    def enterObjectLiteralValue(self, ctx:NeoBasicParser.ObjectLiteralValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#objectLiteralValue.
    def exitObjectLiteralValue(self, ctx:NeoBasicParser.ObjectLiteralValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#objectMembers.
    def enterObjectMembers(self, ctx:NeoBasicParser.ObjectMembersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#objectMembers.
    def exitObjectMembers(self, ctx:NeoBasicParser.ObjectMembersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#objectMember.
    def enterObjectMember(self, ctx:NeoBasicParser.ObjectMemberContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#objectMember.
    def exitObjectMember(self, ctx:NeoBasicParser.ObjectMemberContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#memberName.
    def enterMemberName(self, ctx:NeoBasicParser.MemberNameContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#memberName.
    def exitMemberName(self, ctx:NeoBasicParser.MemberNameContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#memberValue.
    def enterMemberValue(self, ctx:NeoBasicParser.MemberValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#memberValue.
    def exitMemberValue(self, ctx:NeoBasicParser.MemberValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#lambdaLiteral.
    def enterLambdaLiteral(self, ctx:NeoBasicParser.LambdaLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#lambdaLiteral.
    def exitLambdaLiteral(self, ctx:NeoBasicParser.LambdaLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#lambdaClause.
    def enterLambdaClause(self, ctx:NeoBasicParser.LambdaClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#lambdaClause.
    def exitLambdaClause(self, ctx:NeoBasicParser.LambdaClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#lambdaStatement.
    def enterLambdaStatement(self, ctx:NeoBasicParser.LambdaStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#lambdaStatement.
    def exitLambdaStatement(self, ctx:NeoBasicParser.LambdaStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#arithmeticComprehension.
    def enterArithmeticComprehension(self, ctx:NeoBasicParser.ArithmeticComprehensionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#arithmeticComprehension.
    def exitArithmeticComprehension(self, ctx:NeoBasicParser.ArithmeticComprehensionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#predeclaredValue.
    def enterPredeclaredValue(self, ctx:NeoBasicParser.PredeclaredValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predeclaredValue.
    def exitPredeclaredValue(self, ctx:NeoBasicParser.PredeclaredValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#predefinedIdentifier.
    def enterPredefinedIdentifier(self, ctx:NeoBasicParser.PredefinedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predefinedIdentifier.
    def exitPredefinedIdentifier(self, ctx:NeoBasicParser.PredefinedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#predefinedShellValue.
    def enterPredefinedShellValue(self, ctx:NeoBasicParser.PredefinedShellValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predefinedShellValue.
    def exitPredefinedShellValue(self, ctx:NeoBasicParser.PredefinedShellValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#predeclaredFunctor.
    def enterPredeclaredFunctor(self, ctx:NeoBasicParser.PredeclaredFunctorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predeclaredFunctor.
    def exitPredeclaredFunctor(self, ctx:NeoBasicParser.PredeclaredFunctorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#predeclaredFact.
    def enterPredeclaredFact(self, ctx:NeoBasicParser.PredeclaredFactContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predeclaredFact.
    def exitPredeclaredFact(self, ctx:NeoBasicParser.PredeclaredFactContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#predeclaredFmap.
    def enterPredeclaredFmap(self, ctx:NeoBasicParser.PredeclaredFmapContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predeclaredFmap.
    def exitPredeclaredFmap(self, ctx:NeoBasicParser.PredeclaredFmapContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#primaryExpressions.
    def enterPrimaryExpressions(self, ctx:NeoBasicParser.PrimaryExpressionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryExpressions.
    def exitPrimaryExpressions(self, ctx:NeoBasicParser.PrimaryExpressionsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:NeoBasicParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:NeoBasicParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#primaryOperand.
    def enterPrimaryOperand(self, ctx:NeoBasicParser.PrimaryOperandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryOperand.
    def exitPrimaryOperand(self, ctx:NeoBasicParser.PrimaryOperandContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#primaryFunctor.
    def enterPrimaryFunctor(self, ctx:NeoBasicParser.PrimaryFunctorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryFunctor.
    def exitPrimaryFunctor(self, ctx:NeoBasicParser.PrimaryFunctorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#sos_Expression.
    def enterSos_Expression(self, ctx:NeoBasicParser.Sos_ExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#sos_Expression.
    def exitSos_Expression(self, ctx:NeoBasicParser.Sos_ExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:NeoBasicParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:NeoBasicParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#arrayIndexing.
    def enterArrayIndexing(self, ctx:NeoBasicParser.ArrayIndexingContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#arrayIndexing.
    def exitArrayIndexing(self, ctx:NeoBasicParser.ArrayIndexingContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#intervalExpression.
    def enterIntervalExpression(self, ctx:NeoBasicParser.IntervalExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#intervalExpression.
    def exitIntervalExpression(self, ctx:NeoBasicParser.IntervalExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#sliceExpression.
    def enterSliceExpression(self, ctx:NeoBasicParser.SliceExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#sliceExpression.
    def exitSliceExpression(self, ctx:NeoBasicParser.SliceExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#formatType.
    def enterFormatType(self, ctx:NeoBasicParser.FormatTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#formatType.
    def exitFormatType(self, ctx:NeoBasicParser.FormatTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#macroOption.
    def enterMacroOption(self, ctx:NeoBasicParser.MacroOptionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#macroOption.
    def exitMacroOption(self, ctx:NeoBasicParser.MacroOptionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#juxtapositionExpression.
    def enterJuxtapositionExpression(self, ctx:NeoBasicParser.JuxtapositionExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#juxtapositionExpression.
    def exitJuxtapositionExpression(self, ctx:NeoBasicParser.JuxtapositionExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#expressions.
    def enterExpressions(self, ctx:NeoBasicParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expressions.
    def exitExpressions(self, ctx:NeoBasicParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#expression.
    def enterExpression(self, ctx:NeoBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expression.
    def exitExpression(self, ctx:NeoBasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#guardsExpression.
    def enterGuardsExpression(self, ctx:NeoBasicParser.GuardsExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#guardsExpression.
    def exitGuardsExpression(self, ctx:NeoBasicParser.GuardsExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#guardClause.
    def enterGuardClause(self, ctx:NeoBasicParser.GuardClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#guardClause.
    def exitGuardClause(self, ctx:NeoBasicParser.GuardClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#guardDefault.
    def enterGuardDefault(self, ctx:NeoBasicParser.GuardDefaultContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#guardDefault.
    def exitGuardDefault(self, ctx:NeoBasicParser.GuardDefaultContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#shellProcess.
    def enterShellProcess(self, ctx:NeoBasicParser.ShellProcessContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#shellProcess.
    def exitShellProcess(self, ctx:NeoBasicParser.ShellProcessContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:NeoBasicParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:NeoBasicParser.AssignmentExpressionContext):
        pass



del NeoBasicParser