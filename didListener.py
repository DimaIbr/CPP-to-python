# Generated from did.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .didParser import didParser
else:
    from didParser import didParser

# This class defines a complete listener for a parse tree produced by didParser.
class didListener(ParseTreeListener):

    # Enter a parse tree produced by didParser#start.
    def enterStart(self, ctx:didParser.StartContext):
        pass

    # Exit a parse tree produced by didParser#start.
    def exitStart(self, ctx:didParser.StartContext):
        pass


    # Enter a parse tree produced by didParser#mainfunc.
    def enterMainfunc(self, ctx:didParser.MainfuncContext):
        pass

    # Exit a parse tree produced by didParser#mainfunc.
    def exitMainfunc(self, ctx:didParser.MainfuncContext):
        pass


    # Enter a parse tree produced by didParser#methodDeclarations.
    def enterMethodDeclarations(self, ctx:didParser.MethodDeclarationsContext):
        pass

    # Exit a parse tree produced by didParser#methodDeclarations.
    def exitMethodDeclarations(self, ctx:didParser.MethodDeclarationsContext):
        pass


    # Enter a parse tree produced by didParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:didParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by didParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:didParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by didParser#methodHeader.
    def enterMethodHeader(self, ctx:didParser.MethodHeaderContext):
        pass

    # Exit a parse tree produced by didParser#methodHeader.
    def exitMethodHeader(self, ctx:didParser.MethodHeaderContext):
        pass


    # Enter a parse tree produced by didParser#methodBody.
    def enterMethodBody(self, ctx:didParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by didParser#methodBody.
    def exitMethodBody(self, ctx:didParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by didParser#statment.
    def enterStatment(self, ctx:didParser.StatmentContext):
        pass

    # Exit a parse tree produced by didParser#statment.
    def exitStatment(self, ctx:didParser.StatmentContext):
        pass


    # Enter a parse tree produced by didParser#embeddedStatment.
    def enterEmbeddedStatment(self, ctx:didParser.EmbeddedStatmentContext):
        pass

    # Exit a parse tree produced by didParser#embeddedStatment.
    def exitEmbeddedStatment(self, ctx:didParser.EmbeddedStatmentContext):
        pass


    # Enter a parse tree produced by didParser#methodName.
    def enterMethodName(self, ctx:didParser.MethodNameContext):
        pass

    # Exit a parse tree produced by didParser#methodName.
    def exitMethodName(self, ctx:didParser.MethodNameContext):
        pass


    # Enter a parse tree produced by didParser#localVaraibledDelaration.
    def enterLocalVaraibledDelaration(self, ctx:didParser.LocalVaraibledDelarationContext):
        pass

    # Exit a parse tree produced by didParser#localVaraibledDelaration.
    def exitLocalVaraibledDelaration(self, ctx:didParser.LocalVaraibledDelarationContext):
        pass


    # Enter a parse tree produced by didParser#methodCall.
    def enterMethodCall(self, ctx:didParser.MethodCallContext):
        pass

    # Exit a parse tree produced by didParser#methodCall.
    def exitMethodCall(self, ctx:didParser.MethodCallContext):
        pass


    # Enter a parse tree produced by didParser#variableType.
    def enterVariableType(self, ctx:didParser.VariableTypeContext):
        pass

    # Exit a parse tree produced by didParser#variableType.
    def exitVariableType(self, ctx:didParser.VariableTypeContext):
        pass


    # Enter a parse tree produced by didParser#variableName.
    def enterVariableName(self, ctx:didParser.VariableNameContext):
        pass

    # Exit a parse tree produced by didParser#variableName.
    def exitVariableName(self, ctx:didParser.VariableNameContext):
        pass


    # Enter a parse tree produced by didParser#varaibleValue.
    def enterVaraibleValue(self, ctx:didParser.VaraibleValueContext):
        pass

    # Exit a parse tree produced by didParser#varaibleValue.
    def exitVaraibleValue(self, ctx:didParser.VaraibleValueContext):
        pass


    # Enter a parse tree produced by didParser#exprStatment.
    def enterExprStatment(self, ctx:didParser.ExprStatmentContext):
        pass

    # Exit a parse tree produced by didParser#exprStatment.
    def exitExprStatment(self, ctx:didParser.ExprStatmentContext):
        pass


    # Enter a parse tree produced by didParser#condition_block.
    def enterCondition_block(self, ctx:didParser.Condition_blockContext):
        pass

    # Exit a parse tree produced by didParser#condition_block.
    def exitCondition_block(self, ctx:didParser.Condition_blockContext):
        pass


    # Enter a parse tree produced by didParser#add.
    def enterAdd(self, ctx:didParser.AddContext):
        pass

    # Exit a parse tree produced by didParser#add.
    def exitAdd(self, ctx:didParser.AddContext):
        pass


    # Enter a parse tree produced by didParser#comp.
    def enterComp(self, ctx:didParser.CompContext):
        pass

    # Exit a parse tree produced by didParser#comp.
    def exitComp(self, ctx:didParser.CompContext):
        pass


    # Enter a parse tree produced by didParser#bool.
    def enterBool(self, ctx:didParser.BoolContext):
        pass

    # Exit a parse tree produced by didParser#bool.
    def exitBool(self, ctx:didParser.BoolContext):
        pass


    # Enter a parse tree produced by didParser#mul.
    def enterMul(self, ctx:didParser.MulContext):
        pass

    # Exit a parse tree produced by didParser#mul.
    def exitMul(self, ctx:didParser.MulContext):
        pass


    # Enter a parse tree produced by didParser#assi.
    def enterAssi(self, ctx:didParser.AssiContext):
        pass

    # Exit a parse tree produced by didParser#assi.
    def exitAssi(self, ctx:didParser.AssiContext):
        pass


    # Enter a parse tree produced by didParser#bin.
    def enterBin(self, ctx:didParser.BinContext):
        pass

    # Exit a parse tree produced by didParser#bin.
    def exitBin(self, ctx:didParser.BinContext):
        pass


    # Enter a parse tree produced by didParser#integer.
    def enterInteger(self, ctx:didParser.IntegerContext):
        pass

    # Exit a parse tree produced by didParser#integer.
    def exitInteger(self, ctx:didParser.IntegerContext):
        pass


    # Enter a parse tree produced by didParser#ifStatment.
    def enterIfStatment(self, ctx:didParser.IfStatmentContext):
        pass

    # Exit a parse tree produced by didParser#ifStatment.
    def exitIfStatment(self, ctx:didParser.IfStatmentContext):
        pass


    # Enter a parse tree produced by didParser#word.
    def enterWord(self, ctx:didParser.WordContext):
        pass

    # Exit a parse tree produced by didParser#word.
    def exitWord(self, ctx:didParser.WordContext):
        pass



del didParser