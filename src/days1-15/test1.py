with open('./.umirc.js', 'r+', encoding='utf-8') as f:
    print(f.read())
    for line, index in f.readline():
        print(line)
        f.write(index + ':' + line )
print('done')