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


    # Enter a parse tree produced by NeoBasicParser#shebangInterpreter.
    def enterShebangInterpreter(self, ctx:NeoBasicParser.ShebangInterpreterContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#shebangInterpreter.
    def exitShebangInterpreter(self, ctx:NeoBasicParser.ShebangInterpreterContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#logicalInstructionSuite.
    def enterLogicalInstructionSuite(self, ctx:NeoBasicParser.LogicalInstructionSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#logicalInstructionSuite.
    def exitLogicalInstructionSuite(self, ctx:NeoBasicParser.LogicalInstructionSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#logicalInstructions.
    def enterLogicalInstructions(self, ctx:NeoBasicParser.LogicalInstructionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#logicalInstructions.
    def exitLogicalInstructions(self, ctx:NeoBasicParser.LogicalInstructionsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#logicalInstruction.
    def enterLogicalInstruction(self, ctx:NeoBasicParser.LogicalInstructionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#logicalInstruction.
    def exitLogicalInstruction(self, ctx:NeoBasicParser.LogicalInstructionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#instructionSentence.
    def enterInstructionSentence(self, ctx:NeoBasicParser.InstructionSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#instructionSentence.
    def exitInstructionSentence(self, ctx:NeoBasicParser.InstructionSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#directive.
    def enterDirective(self, ctx:NeoBasicParser.DirectiveContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#directive.
    def exitDirective(self, ctx:NeoBasicParser.DirectiveContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#pragmaDirective.
    def enterPragmaDirective(self, ctx:NeoBasicParser.PragmaDirectiveContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#pragmaDirective.
    def exitPragmaDirective(self, ctx:NeoBasicParser.PragmaDirectiveContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#canaryTestingDirective.
    def enterCanaryTestingDirective(self, ctx:NeoBasicParser.CanaryTestingDirectiveContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#canaryTestingDirective.
    def exitCanaryTestingDirective(self, ctx:NeoBasicParser.CanaryTestingDirectiveContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#testStatement.
    def enterTestStatement(self, ctx:NeoBasicParser.TestStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#testStatement.
    def exitTestStatement(self, ctx:NeoBasicParser.TestStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assertStatement.
    def enterAssertStatement(self, ctx:NeoBasicParser.AssertStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assertStatement.
    def exitAssertStatement(self, ctx:NeoBasicParser.AssertStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#declaration.
    def enterDeclaration(self, ctx:NeoBasicParser.DeclarationContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#declaration.
    def exitDeclaration(self, ctx:NeoBasicParser.DeclarationContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#moduleSentence.
    def enterModuleSentence(self, ctx:NeoBasicParser.ModuleSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#moduleSentence.
    def exitModuleSentence(self, ctx:NeoBasicParser.ModuleSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#moduleClause.
    def enterModuleClause(self, ctx:NeoBasicParser.ModuleClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#moduleClause.
    def exitModuleClause(self, ctx:NeoBasicParser.ModuleClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#appletSentence.
    def enterAppletSentence(self, ctx:NeoBasicParser.AppletSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#appletSentence.
    def exitAppletSentence(self, ctx:NeoBasicParser.AppletSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#appletClause.
    def enterAppletClause(self, ctx:NeoBasicParser.AppletClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#appletClause.
    def exitAppletClause(self, ctx:NeoBasicParser.AppletClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#notabeneSentence.
    def enterNotabeneSentence(self, ctx:NeoBasicParser.NotabeneSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#notabeneSentence.
    def exitNotabeneSentence(self, ctx:NeoBasicParser.NotabeneSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#notabeneClause.
    def enterNotabeneClause(self, ctx:NeoBasicParser.NotabeneClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#notabeneClause.
    def exitNotabeneClause(self, ctx:NeoBasicParser.NotabeneClauseContext):
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


    # Enter a parse tree produced by NeoBasicParser#undefDeclare.
    def enterUndefDeclare(self, ctx:NeoBasicParser.UndefDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#undefDeclare.
    def exitUndefDeclare(self, ctx:NeoBasicParser.UndefDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:NeoBasicParser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:NeoBasicParser.AccessSpecifierContext):
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


    # Enter a parse tree produced by NeoBasicParser#constSpecifier.
    def enterConstSpecifier(self, ctx:NeoBasicParser.ConstSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#constSpecifier.
    def exitConstSpecifier(self, ctx:NeoBasicParser.ConstSpecifierContext):
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


    # Enter a parse tree produced by NeoBasicParser#ivalSentence.
    def enterIvalSentence(self, ctx:NeoBasicParser.IvalSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalSentence.
    def exitIvalSentence(self, ctx:NeoBasicParser.IvalSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalClause.
    def enterIvalClause(self, ctx:NeoBasicParser.IvalClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalClause.
    def exitIvalClause(self, ctx:NeoBasicParser.IvalClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalSpecifier.
    def enterIvalSpecifier(self, ctx:NeoBasicParser.IvalSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalSpecifier.
    def exitIvalSpecifier(self, ctx:NeoBasicParser.IvalSpecifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalSuite.
    def enterIvalSuite(self, ctx:NeoBasicParser.IvalSuiteContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalSuite.
    def exitIvalSuite(self, ctx:NeoBasicParser.IvalSuiteContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalDeclareBlock.
    def enterIvalDeclareBlock(self, ctx:NeoBasicParser.IvalDeclareBlockContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalDeclareBlock.
    def exitIvalDeclareBlock(self, ctx:NeoBasicParser.IvalDeclareBlockContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalDeclare.
    def enterIvalDeclare(self, ctx:NeoBasicParser.IvalDeclareContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalDeclare.
    def exitIvalDeclare(self, ctx:NeoBasicParser.IvalDeclareContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalDeclareSingle.
    def enterIvalDeclareSingle(self, ctx:NeoBasicParser.IvalDeclareSingleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalDeclareSingle.
    def exitIvalDeclareSingle(self, ctx:NeoBasicParser.IvalDeclareSingleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalDeclareMultiple.
    def enterIvalDeclareMultiple(self, ctx:NeoBasicParser.IvalDeclareMultipleContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalDeclareMultiple.
    def exitIvalDeclareMultiple(self, ctx:NeoBasicParser.IvalDeclareMultipleContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ivalDeclareParallel.
    def enterIvalDeclareParallel(self, ctx:NeoBasicParser.IvalDeclareParallelContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ivalDeclareParallel.
    def exitIvalDeclareParallel(self, ctx:NeoBasicParser.IvalDeclareParallelContext):
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


    # Enter a parse tree produced by NeoBasicParser#varSpecifier.
    def enterVarSpecifier(self, ctx:NeoBasicParser.VarSpecifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#varSpecifier.
    def exitVarSpecifier(self, ctx:NeoBasicParser.VarSpecifierContext):
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


    # Enter a parse tree produced by NeoBasicParser#statement.
    def enterStatement(self, ctx:NeoBasicParser.StatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#statement.
    def exitStatement(self, ctx:NeoBasicParser.StatementContext):
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


    # Enter a parse tree produced by NeoBasicParser#compoundStatement.
    def enterCompoundStatement(self, ctx:NeoBasicParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#compoundStatement.
    def exitCompoundStatement(self, ctx:NeoBasicParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#controlFlowStatement.
    def enterControlFlowStatement(self, ctx:NeoBasicParser.ControlFlowStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#controlFlowStatement.
    def exitControlFlowStatement(self, ctx:NeoBasicParser.ControlFlowStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:NeoBasicParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:NeoBasicParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#otherwiseSentence.
    def enterOtherwiseSentence(self, ctx:NeoBasicParser.OtherwiseSentenceContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#otherwiseSentence.
    def exitOtherwiseSentence(self, ctx:NeoBasicParser.OtherwiseSentenceContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ifStatement.
    def enterIfStatement(self, ctx:NeoBasicParser.IfStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ifStatement.
    def exitIfStatement(self, ctx:NeoBasicParser.IfStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#ifThenClause.
    def enterIfThenClause(self, ctx:NeoBasicParser.IfThenClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#ifThenClause.
    def exitIfThenClause(self, ctx:NeoBasicParser.IfThenClauseContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unlessStatement.
    def enterUnlessStatement(self, ctx:NeoBasicParser.UnlessStatementContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unlessStatement.
    def exitUnlessStatement(self, ctx:NeoBasicParser.UnlessStatementContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unlessClause.
    def enterUnlessClause(self, ctx:NeoBasicParser.UnlessClauseContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unlessClause.
    def exitUnlessClause(self, ctx:NeoBasicParser.UnlessClauseContext):
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


    # Enter a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def enterUnarySpreadOperator(self, ctx:NeoBasicParser.UnarySpreadOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unarySpreadOperator.
    def exitUnarySpreadOperator(self, ctx:NeoBasicParser.UnarySpreadOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def enterUnaryMetaOperator(self, ctx:NeoBasicParser.UnaryMetaOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#unaryMetaOperator.
    def exitUnaryMetaOperator(self, ctx:NeoBasicParser.UnaryMetaOperatorContext):
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


    # Enter a parse tree produced by NeoBasicParser#executionFlowOperator.
    def enterExecutionFlowOperator(self, ctx:NeoBasicParser.ExecutionFlowOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#executionFlowOperator.
    def exitExecutionFlowOperator(self, ctx:NeoBasicParser.ExecutionFlowOperatorContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#binaryCoalescingOperator.
    def enterBinaryCoalescingOperator(self, ctx:NeoBasicParser.BinaryCoalescingOperatorContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#binaryCoalescingOperator.
    def exitBinaryCoalescingOperator(self, ctx:NeoBasicParser.BinaryCoalescingOperatorContext):
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


    # Enter a parse tree produced by NeoBasicParser#labelIdentifier.
    def enterLabelIdentifier(self, ctx:NeoBasicParser.LabelIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#labelIdentifier.
    def exitLabelIdentifier(self, ctx:NeoBasicParser.LabelIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#symbolIdentifier.
    def enterSymbolIdentifier(self, ctx:NeoBasicParser.SymbolIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#symbolIdentifier.
    def exitSymbolIdentifier(self, ctx:NeoBasicParser.SymbolIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typedIdentifier.
    def enterTypedIdentifier(self, ctx:NeoBasicParser.TypedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typedIdentifier.
    def exitTypedIdentifier(self, ctx:NeoBasicParser.TypedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:NeoBasicParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:NeoBasicParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#identifiers.
    def enterIdentifiers(self, ctx:NeoBasicParser.IdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#identifiers.
    def exitIdentifiers(self, ctx:NeoBasicParser.IdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#symbolIdentifiers.
    def enterSymbolIdentifiers(self, ctx:NeoBasicParser.SymbolIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#symbolIdentifiers.
    def exitSymbolIdentifiers(self, ctx:NeoBasicParser.SymbolIdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#typedIdentifiers.
    def enterTypedIdentifiers(self, ctx:NeoBasicParser.TypedIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#typedIdentifiers.
    def exitTypedIdentifiers(self, ctx:NeoBasicParser.TypedIdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def enterQualifiedIdentifiers(self, ctx:NeoBasicParser.QualifiedIdentifiersContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#qualifiedIdentifiers.
    def exitQualifiedIdentifiers(self, ctx:NeoBasicParser.QualifiedIdentifiersContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#type.
    def enterType(self, ctx:NeoBasicParser.TypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#type.
    def exitType(self, ctx:NeoBasicParser.TypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#nativeType.
    def enterNativeType(self, ctx:NeoBasicParser.NativeTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#nativeType.
    def exitNativeType(self, ctx:NeoBasicParser.NativeTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#posfixTypeWrapper.
    def enterPosfixTypeWrapper(self, ctx:NeoBasicParser.PosfixTypeWrapperContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#posfixTypeWrapper.
    def exitPosfixTypeWrapper(self, ctx:NeoBasicParser.PosfixTypeWrapperContext):
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


    # Enter a parse tree produced by NeoBasicParser#optionalType.
    def enterOptionalType(self, ctx:NeoBasicParser.OptionalTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#optionalType.
    def exitOptionalType(self, ctx:NeoBasicParser.OptionalTypeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#metaType.
    def enterMetaType(self, ctx:NeoBasicParser.MetaTypeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#metaType.
    def exitMetaType(self, ctx:NeoBasicParser.MetaTypeContext):
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


    # Enter a parse tree produced by NeoBasicParser#shellPathLiteral.
    def enterShellPathLiteral(self, ctx:NeoBasicParser.ShellPathLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#shellPathLiteral.
    def exitShellPathLiteral(self, ctx:NeoBasicParser.ShellPathLiteralContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#optionalLiteral.
    def enterOptionalLiteral(self, ctx:NeoBasicParser.OptionalLiteralContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#optionalLiteral.
    def exitOptionalLiteral(self, ctx:NeoBasicParser.OptionalLiteralContext):
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


    # Enter a parse tree produced by NeoBasicParser#predeclaredValue.
    def enterPredeclaredValue(self, ctx:NeoBasicParser.PredeclaredValueContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#predeclaredValue.
    def exitPredeclaredValue(self, ctx:NeoBasicParser.PredeclaredValueContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#operand.
    def enterOperand(self, ctx:NeoBasicParser.OperandContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#operand.
    def exitOperand(self, ctx:NeoBasicParser.OperandContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:NeoBasicParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:NeoBasicParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#slicingRange.
    def enterSlicingRange(self, ctx:NeoBasicParser.SlicingRangeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#slicingRange.
    def exitSlicingRange(self, ctx:NeoBasicParser.SlicingRangeContext):
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


    # Enter a parse tree produced by NeoBasicParser#factScope.
    def enterFactScope(self, ctx:NeoBasicParser.FactScopeContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#factScope.
    def exitFactScope(self, ctx:NeoBasicParser.FactScopeContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#expression.
    def enterExpression(self, ctx:NeoBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expression.
    def exitExpression(self, ctx:NeoBasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#sos_Expression.
    def enterSos_Expression(self, ctx:NeoBasicParser.Sos_ExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#sos_Expression.
    def exitSos_Expression(self, ctx:NeoBasicParser.Sos_ExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:NeoBasicParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:NeoBasicParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#condicionalExpression.
    def enterCondicionalExpression(self, ctx:NeoBasicParser.CondicionalExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#condicionalExpression.
    def exitCondicionalExpression(self, ctx:NeoBasicParser.CondicionalExpressionContext):
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


    # Enter a parse tree produced by NeoBasicParser#macroExpression.
    def enterMacroExpression(self, ctx:NeoBasicParser.MacroExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#macroExpression.
    def exitMacroExpression(self, ctx:NeoBasicParser.MacroExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#macroCall.
    def enterMacroCall(self, ctx:NeoBasicParser.MacroCallContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#macroCall.
    def exitMacroCall(self, ctx:NeoBasicParser.MacroCallContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:NeoBasicParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:NeoBasicParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#primaryExpressions.
    def enterPrimaryExpressions(self, ctx:NeoBasicParser.PrimaryExpressionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#primaryExpressions.
    def exitPrimaryExpressions(self, ctx:NeoBasicParser.PrimaryExpressionsContext):
        pass


    # Enter a parse tree produced by NeoBasicParser#expressions.
    def enterExpressions(self, ctx:NeoBasicParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by NeoBasicParser#expressions.
    def exitExpressions(self, ctx:NeoBasicParser.ExpressionsContext):
        pass



del NeoBasicParser