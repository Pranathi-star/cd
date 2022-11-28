%{
/*first program*/
%}
Oct [o][0-7]+
Hex [o][x|X][0-9A-F]+
%%
{Hex} printf("this is hexadecimal number");
{Oct} printf("this is an octal number");
%%
main()
{
yylex();
}
int yywrap()
{
return 1;
}
