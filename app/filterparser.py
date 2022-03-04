import re
filter:str="And(eq(FirstName,Shannon),NotInList(A360Identifier,(269245105,269053797,269210731)))"

filterOperator:dict={
    "and":"And",
    "or":"Or"
}

filtertype:dict={
    "eq":"Equal", 
    "ne":"NotEqual",
    "startswith":"StartsWith",
    "contains":"Contains",
    "endswith":"EndsWith",
    "lt":"LessThan",
    "le":"LessThanOrEqual",
    "gt":"GreaterThan",
    "ge":"GreaterThanOrEqual",
    "inList":"InList",
    "notinlist":"NotInList",
    "match":"Match",
    "matchall":"MatchAll",
    "matchany":"MatchAny",
    "blank":"Blank",
    "length":"Length",
    "substr":"Substr",
    "upcase":"UpCase",
    "downcase":"DownCase",
    "IsNull":"IsNull",
    "IsNullOrEmpty":"IsNullOrEmpty",
    "IsNotNull":"IsNotNull",
    "IsNotNullOrEmpty":"IsNotNullOrEmpty",
    "Default":"Default"
}


r = re.compile(r'(?:[^,(]|\([^)]*\))+')
fwcs=r.findall(filter)
for str in fwcs:
    print(str)