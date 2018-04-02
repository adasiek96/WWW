import os
import xlrd
import csv
import codecs
from jinja2 import Environment, PackageLoader, select_autoescape

okregi = []
odn_do_gmin = []
woj_wyn = []
obwody = []

# Nagłówki do kolumn dla okręgów
tab = []
fname = '../data/gminy/gm-okr01.xls'
xl_workbook = xlrd.open_workbook(fname)
xl_sheet = xl_workbook.sheet_by_index(0)
num_cols = xl_sheet.ncols
for col_idx in range(5, num_cols):
    cell_obj = xl_sheet.cell(0, col_idx)
    tab.append(cell_obj.value)

okregi.append(tab)

# Wartości dla okręgów i odnośniki do gmin
file_list = os.listdir('../data/gminy/')
file_list.sort()
for file in file_list:
    fname = '../data/gminy/' + file

    xl_workbook = xlrd.open_workbook(fname)
    xl_sheet = xl_workbook.sheet_by_index(0)

    gminy = []
    num_cols = xl_sheet.ncols
    for row_idx in range(1, xl_sheet.nrows):
        tab = []
        tab2 = []
        for col_idx in range(0, num_cols):
            if col_idx <= 2:
                cell_obj = xl_sheet.cell(row_idx, col_idx)
                if col_idx == 0:
                    tab2.append(int(cell_obj.value))
                else:
                    tab2.append(cell_obj.value)
            elif col_idx >= 5:
                cell_obj = xl_sheet.cell(row_idx, col_idx)
                tab.append(int(cell_obj.value))
        gminy.append(tab)
        odn_do_gmin.append(tab2)

    tab = [sum(x) for x in zip(*gminy)]
    for i in range(17, 29):
        tab.append(round(tab[i - 12] * 100 / tab[4], 2))
    tab.append(round(tab[1] / tab[0] * 100, 2))
    okregi.append(tab)

# Województwa - kody i wyniki
f = open('../data/wojewodztwa.txt')
reader = csv.reader(f, delimiter=" ")
wojewodztwa = list(reader)

# Podział na okręgi
f = open('../data/okręgi.txt')
reader = csv.reader(f, delimiter=",")
okregi_lista = list(reader)

for para in wojewodztwa:
    kod = para[1]
    tab = para
    tab2 = []
    for i in range(0, len(odn_do_gmin)):
        if odn_do_gmin[i][1][0] == kod[0] and odn_do_gmin[i][1][1] == kod[1] \
                and (not tab2 or tab2[-1] != odn_do_gmin[i][0]):
            tab2.append(odn_do_gmin[i][0])
    tab3 = [0] * 17
    for i in tab2:
        tab3 = [x + y for x, y in zip(tab3, okregi[int(i)])]
    tab.append(tab2)
    for i in range(17, 29):
        tab3.append(round(tab3[i - 12] * 100 / tab3[4], 2))
    tab3.append(round(tab3[1] / tab3[0] * 100, 2))
    tab.append(tab3)
    woj_wyn.append(tab)

# Dane do obwodów
for file in os.listdir('../data/obwody/'):
    fname = '../data/obwody/' + file

    xl_workbook = xlrd.open_workbook(fname)
    xl_sheet = xl_workbook.sheet_by_index(0)

    num_cols = xl_sheet.ncols
    for row_idx in range(1, xl_sheet.nrows):
        tab = []
        tab2 = []
        for col_idx in range(0, num_cols):
            cell_obj = xl_sheet.cell(row_idx, col_idx)
            if col_idx == 0 or col_idx == 4 or col_idx >= 7:
                tab.append(int(cell_obj.value))
            else:
                tab.append(cell_obj.value)
        for i in range(12, 24):
            if tab[11] == 0:
                tab.append(0)
            else:
                tab.append(round(tab[i] * 100 / tab[11], 2))
        obwody.append(tab)

env = Environment(
    loader=PackageLoader('generate_html', '../templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('województwa_template.html')

for i in range(len(woj_wyn)):
    g = codecs.open('../output/województwa/' + woj_wyn[i][0] + '.html', 'w', "utf-8")
    odn = [(okregi_lista[item - 1][1], item, okregi_lista[item - 1][1]) for item in woj_wyn[i][2]]

    html = template.render(strz1=" -> ", path1=woj_wyn[i][0],
                           lista_list=[woj_wyn[i][3]], kand=okregi[0], k=7, show='hide',
                           co="okręgów", pref4='../okręgi/', inf=' (okręg nr ', suf=')', odn=odn)
    g.write(html)

template = env.get_template('okręgi_template.html')

for i in range(len(okregi) - 1):
    g = codecs.open('../output/okręgi/' + okregi_lista[i][1] + '.html', 'w', "utf-8")
    lista_p = []
    for j in range(0, len(odn_do_gmin)):
        if i + 1 == odn_do_gmin[j][0]:
            lista_p.append(odn_do_gmin[j])
    lista_p = [(item[2], "", item[2]) for item in lista_p]

    html = template.render(strz1=" -> ", pref1='../województwa/', path1=okregi_lista[i][2],
                           strz2=" -> ", path2=okregi_lista[i][1], path2e=(' (okręg nr ' + str(i + 1) + ')'),
                           lista_list=[okregi[i + 1]], kand=okregi[0], k=7, show='hide',
                           co="gmin", pref4="../gminy/", odn=lista_p)
    g.write(html)

template = env.get_template('gminy_template.html')

temp = list()
obwody_lista = list()

for i in range(len(obwody)):
    obwody[i].append(round(100 * obwody[i][8] / obwody[i][7], 2))
    if temp and temp[-1][2] != obwody[i][2]:
        obwody_lista.append(temp)
        temp = list()
    temp.append(obwody[i])

lista_kandydatow = okregi[0]


def daj_wojewodztwo(kod_w):
    nr = str(kod_w[0]) + str(kod_w[1])
    for triple in wojewodztwa:
        if nr == triple[1]:
            return triple[0]


for i in range(len(obwody_lista)):
    g = codecs.open('../output/gminy/' + obwody_lista[i][0][2] + '.html', 'w', "utf-8")
    path1 = daj_wojewodztwo(obwody_lista[i][0][1])
    path2v = int(obwody_lista[i][0][0])
    path2 = okregi_lista[path2v - 1][1]
    path3 = obwody_lista[i][0][2]
    html = template.render(strz1=' -> ', pref1='../województwa/', path1=path1,
                           strz2=' -> ', pref2='../okręgi/', path2=path2, path2e=' (okręg nr ' + str(path2v) + ')',
                           strz3=' -> ', pref3='', path3=path3,
                           lista_list=obwody_lista[i], kand=lista_kandydatow, k=0)
    g.write(html)