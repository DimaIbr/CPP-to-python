from antlr4 import *
from didLexer import didLexer
from didListener import didListener
from didParser import didParser
import sys

class didPrintListener(didListener):
    def __init__(self):
        self.level = 0;
        self.py_code=open('py_code.py','w')
        self.sign=None

    def enterStart(self, ctx: didParser.StartContext):
        pass
        # Exit a parse tree produced by didParser#start.

    def exitStart(self, ctx: didParser.StartContext):
        pass

        # Enter a parse tree produced by didParser#methodDeclarations.

    def enterMainfunc(self, ctx:didParser.MainfuncContext):
        self.level += 1
        self.py_code.write('if __name__ == \'__main__\':\n')

    # Exit a parse tree produced by didParser#mainfunc.
    def exitMainfunc(self, ctx:didParser.MainfuncContext):
        self.level -= 1

    def enterMethodDeclarations(self, ctx: didParser.MethodDeclarationsContext):
        pass

        # Exit a parse tree produced by didParser#methodDeclarations.

    def exitMethodDeclarations(self, ctx: didParser.MethodDeclarationsContext):
        pass

        # Enter a parse tree produced by didParser#methodDeclaration.

    def enterMethodDeclaration(self, ctx: didParser.MethodDeclarationContext):
        self.py_code.write('\t' * self.level)
        self.py_code.write('def ')
        self.level += 1
        # Exit a parse tree produced by didParser#methodDeclaration.

    def exitMethodDeclaration(self, ctx: didParser.MethodDeclarationContext):
        self.level -= 1


        # Enter a parse tree produced by didParser#methodHeader.

    def enterMethodHeader(self, ctx: didParser.MethodHeaderContext):
        child_gen = ctx.getChildren()
        next(child_gen).getText()
        self.py_code.write(next(child_gen).getText()+'():\n')

        # Exit a parse tree produced by didParser#methodHeader.

    def exitMethodHeader(self, ctx: didParser.MethodHeaderContext):
        pass

        # Enter a parse tree produced by didParser#methodBody.

    def enterMethodBody(self, ctx: didParser.MethodBodyContext):
        pass

        # Exit a parse tree produced by didParser#methodBody.

    def exitMethodBody(self, ctx: didParser.MethodBodyContext):
        pass

        # Enter a parse tree produced by didParser#statment.

    def enterStatment(self, ctx: didParser.StatmentContext):
        pass

        # Exit a parse tree produced by didParser#statment.

    def exitStatment(self, ctx: didParser.StatmentContext):
        pass

        # Enter a parse tree produced by didParser#embeddedStatment.

    def enterEmbeddedStatment(self, ctx: didParser.EmbeddedStatmentContext):
        pass

        # Exit a parse tree produced by didParser#embeddedStatment.

    def exitEmbeddedStatment(self, ctx: didParser.EmbeddedStatmentContext):
        pass

        # Enter a parse tree produced by didParser#methodName.

    def enterMethodName(self, ctx: didParser.MethodNameContext):
        pass

        # Exit a parse tree produced by didParser#methodName.

    def exitMethodName(self, ctx: didParser.MethodNameContext):
        pass

        # Enter a parse tree produced by didParser#localVaraibledDelaration.

    def enterLocalVaraibledDelaration(self, ctx: didParser.LocalVaraibledDelarationContext):
        self.py_code.write('\t' * self.level)
        child_gen = ctx.getChildren()
        next(child_gen).getText()
        self.py_code.write(next(child_gen).getText()+'=')
        next(child_gen).getText()
        self.py_code.write(next(child_gen).getText()+'\n')

        # Exit a parse tree produced by didParser#localVaraibledDelaration.

    def exitLocalVaraibledDelaration(self, ctx: didParser.LocalVaraibledDelarationContext):
        pass

        # Enter a parse tree produced by didParser#methodCall.

    def enterMethodCall(self, ctx: didParser.MethodCallContext):
        self.py_code.write('\t' * self.level)
        for child in ctx.getChildren():
            text=child.getText()
            if text==';':
                continue
            self.py_code.write(text)
        self.py_code.write('\n')
        # Exit a parse tree produced by didParser#methodCall.

    def exitMethodCall(self, ctx: didParser.MethodCallContext):
        pass

        # Enter a parse tree produced by didParser#variableType.

    def enterVariableType(self, ctx: didParser.VariableTypeContext):
        pass

        # Exit a parse tree produced by didParser#variableType.

    def exitVariableType(self, ctx: didParser.VariableTypeContext):
        pass

        # Enter a parse tree produced by didParser#variableName.

    def enterVariableName(self, ctx: didParser.VariableNameContext):
        pass

        # Exit a parse tree produced by didParser#variableName.

    def exitVariableName(self, ctx: didParser.VariableNameContext):
        pass

        # Enter a parse tree produced by didParser#varaibleValue.

    def enterVaraibleValue(self, ctx: didParser.VaraibleValueContext):
        pass

        # Exit a parse tree produced by didParser#varaibleValue.

    def exitVaraibleValue(self, ctx: didParser.VaraibleValueContext):
        pass

    def enterIfStatment(self, ctx: didParser.IfStatmentContext):
        #self.py_code.write('\t' * self.level)
        self.py_code.write('if ')
        self.level+=1
        # Exit a parse tree produced by didParser#ifStatment.

    def exitIfStatment(self, ctx: didParser.IfStatmentContext):
        self.level-=1

    def enterCondition_block(self, ctx:didParser.Condition_blockContext):
        pass

    # Exit a parse tree produced by didParser#condition_block.
    def exitCondition_block(self, ctx:didParser.Condition_blockContext):
        self.py_code.write(':\n')

    def enterAdd(self, ctx:didParser.AddContext):
        child_gen = ctx.getChildren()
        next(child_gen).getText()
        self.py_code.write(next(child_gen).getText())

    # Exit a parse tree produced by didParser#add.
    def exitAdd(self, ctx:didParser.AddContext):
        pass


    # Enter a parse tree produced by didParser#comp.
    def enterComp(self, ctx:didParser.CompContext):
        child_gen = ctx.getChildren()
        next(child_gen).getText()
        self.sign=next(child_gen).getText()

    # Exit a parse tree produced by didParser#comp.
    def exitComp(self, ctx:didParser.CompContext):
        pass


    # Enter a parse tree produced by didParser#mul.
    def enterMul(self, ctx:didParser.MulContext):
        child_gen = ctx.getChildren()
        next(child_gen).getText()
        self.sign=next(child_gen).getText()

    # Exit a parse tree produced by didParser#mul.
    def exitMul(self, ctx:didParser.MulContext):
        pass


    # Enter a parse tree produced by didParser#assi.
    def enterAssi(self, ctx:didParser.AssiContext):
        child_gen = ctx.getChildren()
        next(child_gen).getText()
        self.sign=next(child_gen).getText()

    # Exit a parse tree produced by didParser#assi.
    def exitAssi(self, ctx:didParser.AssiContext):
        pass


    # Enter a parse tree produced by didParser#bin.
    def enterBin(self, ctx:didParser.BinContext):
        child_gen = ctx.getChildren()
        next(child_gen).getText()
        text=next(child_gen).getText()
        if text=="&&":
            self.sign = 'and'
        elif text=="||":
            self.sign = 'or'

    # Exit a parse tree produced by didParser#bin.
    def exitBin(self, ctx:didParser.BinContext):
        pass


    # Enter a parse tree produced by didParser#exprlist.
    def enterExprStatment(self, ctx: didParser.ExprStatmentContext):
        self.py_code.write('\t' * self.level)
        pass

    # Exit a parse tree produced by didParser#exprStatment.
    def exitExprStatment(self, ctx: didParser.ExprStatmentContext):
        pass

    # Enter a parse tree produced by didParser#integer.
    def enterInteger(self, ctx:didParser.IntegerContext):
        self.py_code.write(ctx.getText())
        if self.sign is not None:
            self.py_code.write(self.sign)
            self.sign=None

    # Exit a parse tree produced by didParser#integer.
    def exitInteger(self, ctx:didParser.IntegerContext):
        pass

    # Enter a parse tree produced by didParser#word.
    def enterWord(self, ctx:didParser.WordContext):
        self.py_code.write(ctx.getText())
        if self.sign is not None:
            self.py_code.write(self.sign)
            self.sign=None

    # Exit a parse tree produced by didParser#word.
    def exitWord(self, ctx:didParser.WordContext):
        pass

    def enterBool(self, ctx: didParser.BoolContext):
        if ctx.getText()=='true':
            self.py_code.write('True')
        else:
            self.py_code.write('False')

        if self.sign is not None:
            self.py_code.write(self.sign)
            self.sign = None
        # Exit a parse tree produced by didParser#bool.

    def exitBool(self, ctx: didParser.BoolContext):
        pass

def main():
    input_stream = FileStream("code.txt")
    lexer = didLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = didParser(stream)
    tree = parser.start()
    printer = didPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()