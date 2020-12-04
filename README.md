# Attention on Attention for Image Captioning

This repository includes the implementation for the project for course CS685: Natural Language Processing.

## Requirements

- Python 3.6
- Java 1.8.0
- PyTorch 1.0
- cider (already been added as a submodule)
- coco-caption (already been added as a submodule)
- tensorboardX


## Prepare data

Data is available [here](https://drive.google.com/drive/folders/1LMzL4C30SCEaJzYwtJ-wrDLbr2DWcl-M?usp=sharing).

All the necessary data for a pointer-generator network has been prepared in the above drive folder.

## Training

### AoANet

```bash
$ CUDA_VISIBLE_DEVICES=0 sh train.sh
```

### BUTD
```bash
$ CUDA_VISIBLE_DEVICES=0 sh train-butd.sh
```

See `opts.py` for more configurable options.

## Evaluation

Create a vocab to index mapping for test files by running:
```
python scripts/make_ocr_data.py --wtoi_json data/wtoi.json --ocr_json data/ptrgen_test_ocr.json --out_folder data/vizwiz_test_vocab_ix
```


### AoANet
```bash
$ CUDA_VISIBLE_DEVICES=0 python eval.py --model log/log_ptrgen/model-best.pth --infos_path log/log_ptrgen/infos_aoanet-best.pkl --input_json data/ptrgen_talk_vizwiz_withtest.json --dump_images 0 --dump_json 1 --num_images 8000 --beam_size 2 --batch_size 32 --split test --input_fc_dir data/vizwiz_test_fc --input_att_dir data/vizwiz_test_att --input_box_dir data/vizwiz_test_box --input_text_dir data/vizwiz_test_text --input_text_ix_dir data/vizwiz_test_vocab_ix --verbose_loss=1 --ocr_vocab_size 10357 --no_text_ids no_text_ids_test.npy --use_text 1
```

### BUTD
```bash
$ CUDA_VISIBLE_DEVICES=0 python eval.py --model log/log_td/model-best.pth --infos_path log/log_td/infos_aoanet-best.pkl  --dump_images 0 --dump_json 1 --num_images -1 --language_eval 1 --beam_size 2 --batch_size 100 --split test
```


## Performance
Our Extended Vocabulary model as well as the Pointer-Generator network beat the AoANet model CIDEr and SPICE scores.

## Acknowledgements

This repository is based on [self-critical.pytorch](https://github.com/ruotianluo/self-critical.pytorch) and [AoANet](https://github.com/husthuaan/AoANet), and you may refer to it for more details about the code.
