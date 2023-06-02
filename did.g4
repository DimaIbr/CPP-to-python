grammar did;

SPACE: [ \t\r\n]+ -> channel(HIDDEN);
start : methodDeclarations mainfunc EOF;
mainfunc: 'void main()' methodBody;
methodDeclarations : methodDeclaration+;
methodDeclaration : methodHeader methodBody;
methodHeader :'void'|variableType methodName '(' ')';
methodBody : '{' statment* '}';
statment : embeddedStatment ';'?;
embeddedStatment
	:localVaraibledDelaration
	|methodCall
	|exprStatment
//	|forStatment
    ;

methodName : WORD;

localVaraibledDelaration : variableType variableName ('=' varaibleValue);
methodCall : methodName '(' ')';
variableType  :'int'|'byte'|'string'|'bool';
variableName : WORD;
varaibleValue
    :BooleanLiteral
    |IntegerLiteral
    |StringLiteral;

BooleanLiteral : 'true'|'false';
IntegerLiteral : [0-9]+;
StringLiteral :'"' (ESC|.)*? '"';
fragment  ESC: '\\"' | '\\\\' ;

exprStatment : expr;

condition_block
: '(' expr ')';

expr
    : expr ('*' | '/') expr #mul
    | expr ('+' | '-') expr #add
    | expr ('<' | '<=' | '>=' | '>' | '==') expr #comp
    | expr '=' expr #assi
    | expr ( '&&' | '||') expr #bin
    | 'if' condition_block methodBody ('else' methodBody)? #ifStatment
    |IntegerLiteral #integer
    |WORD #word
    |BooleanLiteral #bool
    ;

WORD :[a-zA-Z]+;