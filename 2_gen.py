import hashlib

def gen_line_md5(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()

md5_gen = gen_line_md5('countries.json')
print(next(md5_gen))
print(next(md5_gen))
print(next(md5_gen))
print(next(md5_gen))
