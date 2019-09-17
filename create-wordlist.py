import argparse
from os import path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create wordlist suited for your current target.')
    parser.add_argument('-w', '--wordlists', nargs='+',
                    help='wordlists to use', required=True)
    parser.add_argument('-wb', '--wordlists_base', nargs='?',
                    help='base path for the wordlists', required=False, default='')
    parser.add_argument('-b', '--base', nargs='+',
                    help='base path on the website. Words from wordlists will te attached to every base path provided', required=False, default=['/'])
    parser.add_argument('-o', '--outfile', nargs='?',
                    help='outfile', required=False, default='wordlist.txt')
    args = parser.parse_args()

    wordlists = args.wordlists
    wordlists_base = args.wordlists_base
    paths_base = list(map(lambda x: x if x[0] == '/' else '/' + x, args.base))
    outfile_path = args.outfile


    res = set()
    for wordlist in wordlists:
        with open(path.join(wordlists_base, wordlist), 'r') as infile:
            words = infile.read().split('\n')
        for path_base in paths_base:
            for word in words:
                try:
                    word = word if word[0] != '/' else word[1:]
                except IndexError:
                    pass
                res.add(path.join(path_base, word))
                # res.append(path.join())

    print(res)
    with open(outfile_path, 'w') as outfile:
        print('\n'.join(res), file=outfile)