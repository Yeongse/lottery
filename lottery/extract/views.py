from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import json
import requests
from bs4 import BeautifulSoup
import itertools
  
# ある一回分の結果が, ユーザが入力したすべての組み合わせについて含むかどうか検証(全部含まない時にだけ0を返す)
def is_matched(_target_combinations, _base_data):
    for target_combination in _target_combinations:
        if set(target_combination) < set(_base_data):
            return 1
    return 0

# 回数をkey, 6個の当選番号と1個のボーナス数字の値の配列をvalueにした辞書を返す関数(中は全部str型, 仕切り用の行も含まれている)
def scrape_loto6():
    # 初期設定
    scrape_url = 'http://sougaku.com/loto6/data/list1/'
    html_content = requests.get(scrape_url).content
    soup = BeautifulSoup(html_content, 'html.parser')
    population_data = soup.find('table', class_='bun_box1')

    # 過去の全結果を配列に格納(要素の例: ['第3回', '1', '5', '15', '31', '36', '38', '13', 'C', '4：2', '126', '5：2', '139', '詳細表示'])
    trs_list = []
    for tr in population_data.find_all('tr'):
        tr_list = []
        for td in tr:
            text = td.text.replace('\n','').replace('\t','')
            if text != '':
                tr_list.append(text)
        trs_list.append(tr_list)

    # 辞書の作成
    results = {}
    for tr in trs_list:
        results[tr[0]] = [tr[i] for i in range(1, 8, 1)]

    return results


def index(request):
    return render(request, 'extract/index.html', {})

def loto6(request):
    if request.method == 'POST':
        # 初期設定(スクレイピングによるデータの取得とPOST内容の確認)
        results_all = scrape_loto6()
        targets = request.POST.getlist('targets')
        include = int(request.POST['include'])
        targets_combinations = list(itertools.combinations(targets, include))

        # ユーザが指定した要素を含む結果のみを格納した配列を作成(各要素はgeneration: 第n回とnumbers: [7個の数字]の辞書)
        results_matched = []
        for key in results_all.keys():
            if is_matched(targets_combinations, results_all[key]):
                results_matched.append({'generation': key, 'numbers': results_all[key]})

        return render(request, 'extract/loto6.html', {
            'chosen': targets, 
            'include': include, 
            'results': results_matched
        })
    
    return render(request, 'extract/loto6.html', {
        'choosed': None, 
        'results': None
    })