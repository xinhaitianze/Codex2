h = 1
line = "abs        s"
if 'bs' in line[:3]:
            print(f'line {h}')
            print(line)
            print('^' * len(line))
            print("ERROR: unknown instruction,  'abs' ?")