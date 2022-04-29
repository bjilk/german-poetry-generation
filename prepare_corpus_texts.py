import json
import os


data_dir = 'data'
src_filename = 'dlk.v5.german.poetry.corpus.full.json'
sm_fn = 'dlk_small_sample.json'

src_path= os.path.join(data_dir, src_filename)
sm_path = os.path.join(data_dir, sm_fn)

with open(src_path, encoding='utf-8') as fp:
    data = json.load(fp)

poems = []

for i, poem in enumerate(data.values()):
    lines = []
    for stanza in poem['poem'].values():
        for line in stanza.values():
            line_text = line['text']
            lines.append(line_text)

    poem_text = {
        'text': '\n'.join(lines)
    }
            
    poems.append(poem_text)

poem_dict = {
    'poems': poems
}
poem_dict_fn = 'dlk_poems_texts.json'
poems_path = os.path.join(data_dir, poem_dict_fn)
print('Writing data')
with open(poems_path, 'w', encoding='utf-8') as fp:
    json.dump(poem_dict, fp)
