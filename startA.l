identifier ^[A|a][0-9a-zA-Z]+

%%
{identifier} printf("Identifier starting with a");
%%
main()
{
yylex();
}
int yywrap()
{
return 1;
}

