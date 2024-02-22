// GCD+.g4 - ANTLR Grammar file for GCD+ language

grammar GCDplus;

program: statement+;

statement: element | config | entity | interaction | dataBinding | security | crossPlatform | cloud | devOps | testing | futures | devTools | documentation | license | contributing;

element: '+' nameConfig? property* '+'
    | '#' identifierConfig? property* '#'
    | '$' identifierConfig property* '$'
    | identifierConfig property* '\n' ('+'|'#'|'$') ;

config: '$config' property* '$';

entity: '$entities' property* '$';

interaction: '$interact' property* '$';

dataBinding: '$data' property* '$';

security: '$security' property* '$';

crossPlatform: '$crossPlatform' property* '$';

cloud: '$cloud' property* '$';

devOps: '$devOps' property* '$';

testing: '$testing' property* '$';

futures: '$futures' property* '$';

devTools: '$devTools' property* '$';

documentation: '$docs' property* '$';

license: '$license' property* '$';

contributing: '$contributing' property* '$';

property: identifierConfig valueConfig?;

nameConfig: 'name' identifierConfig;
identifierConfig: 'identifier' identifierConfig;
valueConfig: 'value' stringValueConfig;
stringValueConfig: STRING;

STRING: '"' ~[\r\n"]* '"';

WS: [ \t\n\r]+ -> skip;
