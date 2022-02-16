# 勉強会課題

## livedoorニュースコーパスを用いて記事の分類を行う

- コーパスは各自でダウンロードしてください
  - [コーパスはこちら](https://www.rondhuit.com/download.html)
- ダウンロードしたコーパスはdatasetフォルダ内にいれてください

### 以下のライブラリをインストールして環境を作ってください

- (注)anacondaを利用している人はcondaコマンドでインストールしてください
```
$pip install pyyaml
$pip install scikit-learn
$pip install numpy
$pip install mecab
```

### configファイルで複数のモデルで実験できます