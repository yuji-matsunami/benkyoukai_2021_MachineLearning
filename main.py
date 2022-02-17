import yaml
import os
import glob
import MeCab
import numpy as np
from typing import Tuple, List, Any
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

def read_file(data_path:str) -> Tuple[List[str], List[int]]:
    dir_names = [d for d in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, d))] # ディレクトリのみを取得
    label_dict = {dir:i for i,dir in enumerate(dir_names)} # ラベルを付けるための辞書を作っておく
    text = []
    label = []
    for dir in dir_names:
        path_list = glob.glob(os.path.join(data_path, dir) + "/*.txt")
        for p in path_list:
            with open(p, 'r', encoding="utf-8") as f:
                next(f)
                next(f)
                title = f.readline().replace("\n","") # 改行を消してタイトルを収集する
                text.append(title)
                label.append(label_dict[dir])

    return text, label

def mecab_process(text:List[str]) -> List[str]:
    mecab = MeCab.Tagger("-Owakati")
    output_list = []
    for title in text:
        wakati = mecab.parse(title)
        output_list.append(wakati)
    return output_list
    
def exchange_vector(text:List[str]) -> Any:
    vectorizer = CountVectorizer()
    return vectorizer.fit_transform(text).toarray()

def main():
    with open("config.yml",encoding='utf-8') as f:
        yml = yaml.safe_load(f)
    data_path = yml["data_path"]
    model = yml["model"]
    text, label = read_file(data_path)
    text_wakati = mecab_process(text)
    X = exchange_vector(text_wakati)
    X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.2, random_state=1) # 教師データとテストデータに分割する
    if model == "SVC":
        clf = SVC(C=1, kernel='rbf')
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        print(f"score:{score}")
    elif model == "logistic":
        clf = LogisticRegression()
    elif model == "RandomForest":
        pass

if __name__ == "__main__":
    main()