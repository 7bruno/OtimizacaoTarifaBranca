import statistics  # importa a biblioteca de estatística do python

import PySimpleGUI as sg
import matplotlib.pyplot as plt

global amt
amt:int = 0


while amt <= 0:
    sg.theme('DarkGreen6')  # Add some color to the window

    # Very basic window.  Return values using auto numbered keys

    layout = [
        [sg.Text('Bem vindo ao Tarifa PY!\nPor favor insira os dados abaixo:')],
        [sg.Text('semanas amostradas:', size=(16, 1)), sg.InputText(size=(5, 0))],
        [sg.Text('tarifa fora de ponta:', size=(16, 1)), sg.InputText(size=(5, 0))],
        [sg.Text('tarifa intermediaria:', size=(16, 1)), sg.InputText(size=(5, 0))],
        [sg.Text('tarifa na ponta:', size=(16, 1)), sg.InputText(size=(5, 0))],
        [sg.Text('tarifa convencional:', size=(16, 1)), sg.InputText(size=(5, 0))],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Tarifa PY', layout)
    event, values = window.read()
    amt =int(values[0])
    tfp = float(values[1])
    tint = float(values[2])
    tp = float(values[3])
    tconv = float(values[4])
else:
    window.close()
#listas semanais de cada horario inicializada com a quantidade de amostras necessária
segfp = [0] * amt
segint = [0] * amt
segp = [0] * amt
terfp = [0] * amt
terint = [0] * amt
terp = [0] * amt
quafp = [0] * amt
quaint = [0] * amt
quap = [0] * amt
quifp = [0] * amt
quiint = [0] * amt
quip = [0] * amt
sexfp = [0] * amt
sexint = [0] * amt
sexp = [0] * amt
sabfp = [0] * amt
domfp = [0] * amt

for x in range(amt):   #leitura dos dados do usuario para calculos
    sg.theme('DarkGreen6')
    layout = [
        [sg.Text('Semana {}'.format(x+1))],

        [sg.Text('SEGUNDA FP:', size=(15, 0)), sg.Input(size=(5, 0), key='segundafp'),
         sg.Text('SEGUNDA INT:', size=(15, 0)), sg.Input(size=(5, 0), key='segundaint'),
         sg.Text('SEGUNDA P: ', size=(15, 0)), sg.Input(size=(5, 0), key='segundap')],

        [sg.Text('TERÇA FP:', size=(15, 0)), sg.Input(size=(5, 0), key='tercafp'),
         sg.Text('TERÇA INT:', size=(15, 0)), sg.Input(size=(5, 0), key='tercaint'),
         sg.Text('TERÇA P: ', size=(15, 0)), sg.Input(size=(5, 0), key='tercap')],

        [sg.Text('QUARTA FP:', size=(15, 0)), sg.Input(size=(5, 0), key='quartafp'),
         sg.Text('QUARTA INT:', size=(15, 0)), sg.Input(size=(5, 0), key='quartaint'),
         sg.Text('QUARTA P: ', size=(15, 0)), sg.Input(size=(5, 0), key='quartap')],

        [sg.Text('QUINTA FP:', size=(15, 0)), sg.Input(size=(5, 0), key='quintafp'),
         sg.Text('QUINTA INT:', size=(15, 0)), sg.Input(size=(5, 0), key='quintaint'),
         sg.Text('QUINTA P: ', size=(15, 0)), sg.Input(size=(5, 0), key='quintap')],

        [sg.Text('SEXTA FP:', size=(15, 0)), sg.Input(size=(5, 0), key='sextafp'),
         sg.Text('SEXTA INT:', size=(15, 0)), sg.Input(size=(5, 0), key='sextaint'),
         sg.Text('SEXTA P: ', size=(15, 0)), sg.Input(size=(5, 0), key='sextap')],

        [sg.Text('SABADO:', size=(15, 0)), sg.Input(size=(5, 0), key='sabado'),
         sg.Text('DOMINGO:', size=(15, 0)), sg.Input(size=(5, 0), key='domingo')],
        [sg.Submit(), sg.Cancel()]
    ]

    window2 = sg.Window('Tarifa PY', layout)
    event, values = window2.read()
    segfp[x] = float(values['segundafp'])
    segint[x] = float(values['segundaint'])
    segp[x] =float(values['segundap'])
    terfp[x] = float(values['tercafp'])
    terint[x] = float(values['tercaint'])
    terp[x] = float(values['tercap'])
    quafp[x] = float(values['quartafp'])
    quaint[x] = float(values['quartaint'])
    quap[x] = float(values['quartap'])
    quifp[x] =float(values['quintafp'])
    quiint[x] =float(values['quintaint'])
    quip[x] = float(values['quintap'])
    sexfp[x] = float(values['sextafp'])
    sexint[x] = float(values['sextaint'])
    sexp[x] = float(values['sextap'])
    sabfp[x] = float(values['sabado'])
    domfp[x] = float(values['domingo'])
    window2.close()

#valores médios diario semanais
seg = [statistics.fmean(segfp), statistics.fmean(segint), statistics.fmean(segp)]
ter = [statistics.fmean(terfp), statistics.fmean(terint), statistics.fmean(terp)]
qua = [statistics.fmean(quafp), statistics.fmean(quaint), statistics.fmean(quap)]
qui = [statistics.fmean(quifp), statistics.fmean(quiint), statistics.fmean(quip)]
sex = [statistics.fmean(sexfp), statistics.fmean(sexint), statistics.fmean(sexp)]
sab = statistics.fmean(sabfp)
dom = statistics.fmean(domfp)
#calculo dos consumos
consumodiariofp = statistics.fmean([seg[0],ter[0],qua[0],qui[0],sex[0],sab,dom])
consumodiarioint = statistics.fmean([seg[1],ter[1],qua[1],qui[1],sex[1]])
consumodiariop = statistics.fmean([seg[2],ter[2],qua[2],qui[2],sex[2]])
consumodiariomedio = consumodiariop+consumodiarioint+consumodiariofp
#calculos dos valores de acordo com cada tarifa
valormensalconv = (tconv*consumodiariomedio)*30
valormensaltfbranca = ((tfp*consumodiariofp)+(tint*consumodiarioint)+(tp*consumodiariop))*30
kwhmediotfbranca:float =valormensaltfbranca/ (consumodiariomedio*30)

#inicio da configuração de gráficos
listagfaux1 = ["Tarifa Branca","Tarifa Convencional"]
listagfaux2 = [kwhmediotfbranca,tconv]
plt.bar(listagfaux1, listagfaux2, color = 'green')
plt.xticks(listagfaux1)
plt.ylabel("Valor Médio por Kwh")
plt.xlabel("Tipos de Tarifa")
plt.title("Tarifa Branca x Tarifa Convencional")
plt.show()
listagfaux3 = ["Valor tarifa Branca", "Valor Tarifa Convencional"]
listagfaux4 = [valormensaltfbranca, valormensalconv]
plt.barh(listagfaux3,listagfaux4, color = 'red')
plt.ylabel("Tipos Tarifarios")
plt.xlabel("Valor final em R$")
plt.title("Comparativo do valor final BrancaxConvencional")
plt.show()
#fim da configuração dos gráficos