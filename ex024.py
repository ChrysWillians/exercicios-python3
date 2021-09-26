n = str(input('Qual é o nome da sua cidade?: ')).strip().upper()
cidade = n.split()
print('Sua cidade começa com "Santo"? {}'.format('SANTO' in cidade[0]))



