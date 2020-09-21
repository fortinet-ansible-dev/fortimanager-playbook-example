#! /usr/bin/python3
from os import listdir
from os.path import isfile, join
import yaml
import sys

def get_metadata(lines):
    data = dict()
    for line in lines:
        stripped_line = line.rstrip('\n')
        stripped_line = stripped_line.strip(' ')
        if not len(stripped_line):
            continue
        if stripped_line[0] != '#':
            break
        stripped_line = stripped_line[1:]
        tokens = stripped_line.split(':')
        if len(tokens) != 2:
            continue
        tokens = [t.strip(' ') for t in tokens]
        data[tokens[0].lower()] = tokens[1]
    if 'label' in data:
        data['label'] = [i.strip(' ') for i in data['label'].split(',')]
    return data

def get_purified_content(lines):
    data = ''
    for line in lines:
        stripped_line = line.rstrip('\n')
        stripped_line = stripped_line.strip(' ')
        if stripped_line == '' or stripped_line[0] == '#':
            continue
        data += line
    return data

even = True
BRANCH='2.0.0'

def print_metadata_in_html(fname, metadata):
    global even
    author_string = ''
    if 'author' in metadata:
        author_string = metadata['author']
    if 'org' in metadata:
        author_string += '<b>(%s)</b>' %(metadata['org'])
    date_string = ''
    if 'date' in metadata:
        date_string = metadata['date']
    label_string = ''
    if 'label' in metadata:
        for label in metadata['label']:
            label_string += '<code class="docutils literal notranslate"><span class="pre">%s</span></code>' % (label)
    print(' <tr class="%s"><td><a target="_blank" href="https://raw.githubusercontent.com/fortinet-ansible-dev/fortimanager-playbook-example/%s/output/%s">%s</a></td>' % ('row-even' if even else 'row-odd', BRANCH, fname, fname))
    print(' <td><code ><span>%s</span></code></td>' % (metadata['desc'] if 'desc' in metadata else ''))
    print(' <td><code ><span class="pre">%s</span></code></td>' % (author_string) )
    print(' <td><code ><span class="pre">%s</span></code></td>' % (date_string) )
    print(' <td>%s</td>' % (label_string))
    print(' </tr>')
    even = not even

def main():
    files = [f for f in listdir('./src') if isfile(join('./src', f))]
    for fname in files:
        fpath = './src/' + fname
        with open(fpath) as f:
            try:
                # validate the content formmat
                fdata = yaml.load(f, Loader=yaml.FullLoader)
            except Exception as e:
                print('invalid ymal format in: ' + fpath)
                print(e)
                sys.exit(-1)
            f.seek(0)
            flines = f.readlines()
            metadata = get_metadata(flines)
            body = get_purified_content(flines)
            with open('./output/' + fname, 'w') as foutput:
                foutput.write(body)
                foutput.flush()
            print_metadata_in_html(fname, metadata)
if __name__ == '__main__':
    main()
