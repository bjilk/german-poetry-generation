import json
import os


home_dir = os.environ['HOME']
data_dir = os.path.join(home_dir, 'data')
src_filename = 'dlk.v5.german.poetry.corpus.full.json'
sm_fn = 'dlk_small_sample.json'

src_path= os.path.join(data_dir, src_filename)
sm_path = os.path.join(data_dir, sm_fn)

use_small_sample = False

with open(src_path, encoding='utf-8') as fp:
    data = json.load(fp)

if use_small_sample:
    sm = {}
    if os.path.exists(sm_path):
        with open(sm_path, 'r') as fp:
            sm = json.load(fp)
    else:
        for idx, poem in list(data.items())[:50]:
            sm[idx] = poem

        with open(sm_path, 'w') as fp:
            json.dump(sm, fp)

poems = []

data = sm if use_small_sample else data
   
for poem in data.values():
    lines = []
    for stanza in poem['poem'].values():
        for line in stanza.values():
            line_tokens = {
                'tokens': [t.replace('·', '') for t in line['tokens']]
            }
            line_tokens['tokens'].append('\n')
            lines.append(line_tokens)
    token_lists = [line['tokens'] for line in lines]
    poem_tokens = []
    for line in token_lists:
        poem_tokens.extend(line)

    poem_tokens = {
        'tokens': poem_tokens
    }
            
    poems.append(poem_tokens)

poem_dict = {
    'poems': poems
}
poem_dict_fn = 'dlk_poems.json'
poems_path = os.path.join(data_dir, poem_dict_fn)
with open(poems_path, 'w', encoding='utf-8') as fp:
    json.dump(poem_dict, fp)
