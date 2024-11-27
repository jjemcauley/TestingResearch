def predicate_and_clause_test(a, b, c):
    if(a > 0 and b > 0):
        return "Predicate 1 met"
    if(c > a + b):
        return "Predicate 2 met"
    if(a < b + c or a % 2 == 0):
        return "Predicate 3 met"
    if(b < a and c + b == a):
        return "Predicate 4 met"
    if(a == b + c and c % 2 == 0):
        return "Predicate 5 met"
    if(a > b and c < 10 and b < 10):
        return "Predicate 6 met"

