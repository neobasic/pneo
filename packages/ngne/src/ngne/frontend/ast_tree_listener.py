from ngne.parser.NeoBasicParser import NeoBasicParser
from ngne.parser.NeoBasicParserListener import NeoBasicParserListener


# This class defines a complete listener for a parse tree produced by NeoBasicParser.
class AstTreeListener(NeoBasicParserListener):

    # Exit a parse tree produced by NeoBasicParser#sourceCodeProgram.
    def exitSourceCodeProgram(self, ctx: NeoBasicParser.SourceCodeProgramContext):
        print("\n exitSourceCodeProgram:")
        print("\t ctx.children:", ctx.children)

    # Exit a parse tree produced by NeoBasicParser#logicalInstruction.
    def exitLogicalInstruction(self, ctx: NeoBasicParser.LogicalInstructionContext):
        print("\n exitLogicalInstruction:")
        print("\t ctx.children:", ctx.children)

    # Exit a parse tree produced by NeoBasicParser#instructionSentence.
    def exitInstructionSentence(self, ctx: NeoBasicParser.InstructionSentenceContext):
        print("\n exitInstructionSentence:")
        print("\t ctx.children:", ctx.children)

    # Exit a parse tree produced by NeoBasicParser#varClause.
    def exitVarClause(self, ctx: NeoBasicParser.VarClauseContext):
        print("\n exitVarClause:")
        print("\t ctx.children:", ctx.children)

    # Exit a parse tree produced by NeoBasicParser#varDeclare.
    def exitVarDeclare(self, ctx: NeoBasicParser.VarDeclareContext):
        print("\n exitVarDeclare:")
        print("\t ctx.children:", ctx.children)
        print("\t ctx.getChild(1).children:", ctx.getChild(0).children)

    # Exit a parse tree produced by NeoBasicParser#constSentence.
    def exitConstSentence(self, ctx: NeoBasicParser.ConstSentenceContext):
        print("\n exitConstSentence:")
        print("\t ctx.children:", ctx.children)

        children = ctx.children[0].children[1].children[0].children[2].children[0].children[0].children[0].children[
            0].children[0].children

        from pprint import pprint
        pprint(children)

    # Exit a parse tree produced by NeoBasicParser#typeSentence.
    def exitTypeSentence(self, ctx: NeoBasicParser.TypeSentenceContext):
        print("\n exitTypeSentence:")
        print("\t ctx.children:", ctx.children)
