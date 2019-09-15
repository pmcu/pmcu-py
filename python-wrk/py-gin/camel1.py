import camelcase

c = camelcase.CamelCase()

txt = """hello world
agus d'ól sé pionta agus
bhí sé deas agus bó bhuí.
"""

print(c.hump(txt))
