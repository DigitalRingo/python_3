string = "у пФЫрФЫВРОогОЛДОШПСЗраФЫВммРФЗЫиПРИсДОСтов пФЫВеПАДреУКЩЧСШрыЫЛЬЛЫв"
print(string)
result: str = ""
for s in string:
    if not s.isupper():
        result = result + s
print(result)
