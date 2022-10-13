txt = 'выфавфа лдфва лвфоыащш овдлао авб вфвалзл  выфадл фв лодф лролабв'

res = filter(lambda x: not 'абв' in x, txt.split(' ') )

print(' '.join(list(res)))
