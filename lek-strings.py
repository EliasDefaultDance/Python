firstName = "Elias"
middleName = "Erik"
lastName = "Dahlgren"
nickName = "Kenzio"
Domain = "@elev.ga.ntig"
topDomain = ".se"

#print(middleName, firstName, lastName, nickName)

tecken = """paranteser (), 
hakparanteser[],
måsvingar{} ,
kolon:,
semikolon;,
komma ,\" dubbelfnutt, \' enkelfnutt"""

skolmail = firstName.lower() + "."
skolmail += lastName.lower()
skolmail += Domain.lower()
skolmail += topDomain.lower()

print(skolmail)