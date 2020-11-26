import os
import json
import argparse
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ocr_json', required=False, default=None, help='OCR json')
    parser.add_argument('--wtoi_json', required=False, default=None, help='word to index file')
    parser.add_argument('--out_folder', required=False, default=None, help='folder to store vocab indices per image')

    args = parser.parse_args()
    params = vars(args)  # convert to ordinary dict

    out_folder = params['out_folder']
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder)

    wtoi = json.load(open(params['wtoi_json'], 'r'))
    ocr = json.load(open(params['ocr_json'], 'r'))
    unk_ix = wtoi['UNK']
    print('Length of OCR json: ', len(ocr))
    max_length = 20
    for img, words in ocr.items():
        ixs = []
        for w in words[:max_length]:
            ixs.append(wtoi.get(w, unk_ix))
        outpath = os.path.join(params['out_folder'], img+".npy")
        np.save(outpath, ixs)