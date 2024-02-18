def externo(a, b):
    def interno(c, d):
        return c + d
    return interno(a, b)

res = externo(5, 10)

print(res)