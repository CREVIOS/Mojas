# Disclaimer

Main Strcuture function ist added, so please wait before final version in two days. It is undergoing some update...

# Mojas
--> A Bengali Programming Language where all syntax in Bengali language and it is written python

## Introduction
A programming language of Bengali syntax is created using python, which has functions, variables, statements, basic binary operations, and more.  The funniest part of this language is that I used an interpreter to make an interpreter.

## Motivation
The primary motivation I developed behind this language after witnessing the difficulties of teaching Bangladeshi schoolchildren programming. They are more comfortable learning everything in their mother tongue. In 2018, I taught my neighbor’s (13 years old) programming and faced difficulties teaching him. Later I found that he could understand the logic and syntax more clearly in Bengali than in English. So, I started developing a language in Bengali, and we know that we are all more comfortable in talking and understanding in the mother tongue.

So, first, this language will be used to teach them the basic programming structure and logic behind the essential operation. After that, we can quickly move to teach them C, Python, or Julia language.

## Seatbacks
As I wrote an interpreted language, it will be great to write it in a compiled language (like C, C++, or Swift) because the performance lost in the language of my interpreter and the interpreter that is interpreting my interpreter will compound. If it was a compiled language that I am creating, a slower language (like Python or JavaScript) would be good. Compile-time may be bad, but in my opinion, that isn’t nearly as big a deal as bad run time. But I wrote mojas in python; until now, it is interpreted language, and I am trying to convert it into a compiled one.

### English Grammar of Mojas 
```
expr			: KEYWORD:VAR IDENTIFIER EQ expr
			: comp-expr ((KEYWORD:AND|KEYWORD:OR) comp-expr)*

comp-expr		: NOT comp-expr
			: arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*

arith-expr	        :	term ((PLUS|MINUS) term)*

term			: factor ((MUL|DIV) factor)*

factor			: (PLUS|MINUS) factor
			: power

power			: call (POW factor)*

call			: atom (LPAREN (expr (COMMA expr)*)? RPAREN)?

atom 			: INT|FLOAT|STRING|IDENTIFIER
				: LPAREN expr RPAREN
				: if-expr
				: for-expr
				: while-expr
				: func-def

if-expr			: KEYWORD:IF expr KEYWORD:THEN expr (KEYWORD:ELIF expr KEYWORD:THEN expr)* (KEYWORD:ELSE expr)?

for-expr		: KEYWORD:FOR IDENTIFIER EQ expr KEYWORD:TO expr  (KEYWORD:STEP expr)? KEYWORD:THEN expr

while-expr	        : KEYWORD:WHILE expr KEYWORD:THEN expr

func-def		: KEYWORD:FUN IDENTIFIER? LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN ARROW expr
```            
### Statements
```
:: Mojas >>> চলক  কম = 2020
Output: 2020
:: Mojas >>> চলক  কমচ = যদি কম >= 2000 তারপর 2002 তারদি কম <= 2021 তারপর 2019  নহিলে 2050
Output: 2002
```


### For Loop
```
:: Mojas >>> চলক ক = 1
Output: 1
:: Mojas >>> যে চ = 1 থেকে 5 তারপর  চলক ক = চ*ক
:: Mojas >>> ক
Output: 24
:: Mojas >>> চলক ক1 = ক
Output: 24
:: Mojas >>> যে চ = 1 থেকে 5 ধাপ 2 তারপর  চলক ক1 = (চ^চ)+ ক1   // calculation    \sum_{1}^{4}{x^2+k} 
:: Mojas >>> ক1
Output: 52   
:: Mojas >>> চলক কক = 1 
Output: 1
:: Mojas >>> যে চ = 2 থেকে 11 ধাপ 1 তারপর  চলক কক = চ+কক  // calculation of  \sum_{1}^{10}x
:: Mojas >>> কক
Output: 55
```

### Functions 
```
:: Mojas >>> মজা যোগ(ক,খ) -> ক+খ // Declaring-Function function-name(a,b) -> a+b
:: Mojas >>> যোগ(1001,1020) // function-name(1000,1020)
Output: 2021
:: Mojas >>> মজা আমরা(ক,খ,গ,ঘ) -> ((ক+খ)^গ)+ঘ   // Declaring-Function function-name(a,b,c,d) -> ((a+b)^c)+d
:: Mojas >>>আমরা(1,2,3,4)   //function-name(1,2,3,4)
Output: 31
```
### Strings

```
:: Mojas >>> "এটি একটি লাইন"
Output: "এটি একটি লাইন"
:: Mojas >>> "লাইন" * 3
Output: "লাইনলাইনলাইন"
:: Mojas >>> মজা অনি(ক,নাম)-> "এটি" * ক + নাম
Output: <function অনি>
:: Mojas >>> অনি(5,"লাইন")
Output: "এটিএটিএটিএটিএটিলাইন"
:: Mojas >>> অনি(15,"লাইন")
Output: "এটিএটিএটিএটিএটিএটিএটিএটিএটিএটিএটিএটিএটিএটিএটিলাইন"
```
