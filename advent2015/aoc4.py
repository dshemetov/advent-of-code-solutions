import md5

for i in range(10000000):
    m = md5.new()
    m.update("iwrupvqb" + str(i))
    if m.hexdigest()[0:6] == "000000":
        break

print(m.hexdigest())
print(i)
