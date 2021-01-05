from bs4 import BeautifulSoup
import regex
import requests
from matplotlib.figure import Figure
import time

def getArray(resp,reg):
    strArray = ""
    for e in resp:
        strArray += str(e) 
    array = regex.findall(reg,strArray)
    if array[0] == "Equipa":
        return array[1:]
    else:
        return array

def getScrapLigaNOS():
    request = requests.get("https://liganos.pt").text
    soup = BeautifulSoup(request,'lxml')
    strSoup = str(soup)
    #resp = soup.find_all('div', class_= "tablepos")
    equipasResp = soup.find_all('div', class_= "team")
    pointsResp = soup.find_all('div', class_= "points")
    playedGamesResp = soup.find_all('div', class_= "played")
    winGamesResp = soup.find_all('div', class_= "win")
    drawGamesResp = soup.find_all('div', class_= "drawn")
    lostGamesResp = soup.find_all('div', class_= "lost")
    scoredResp = soup.find_all('div', class_= "scored")
    sufferedResp = soup.find_all('div', class_= "suffered")
    points = getArray(pointsResp,r'[0-9]+')
    played = getArray(playedGamesResp,r'[0-9]+')
    teams = getArray(equipasResp,r'(?<=>)[a-zA-Z\u00C0-\u017F\s\.]+(?=<)')
    win = getArray(winGamesResp,r'[0-9]+')
    draw = getArray(drawGamesResp,r'[0-9]+')
    lost = getArray(lostGamesResp,r'[0-9]+')
    scored = getArray(scoredResp,r'[0-9]+')
    suffered = getArray(sufferedResp,r'[0-9]+')
    finalDic = {}
    for i in range(len(teams)):
        finalDic[teams[i]] = {"jj": played[i],  'win': win[i], 'draw': draw[i], 'lost': lost[i],'scored': scored[i],'suffered': suffered[i],'points': points[i]}
    return finalDic
    
valores = []
tempos = []


def obterValorOil():
    global tempos
    global valores
    request = requests.get("https://finance.yahoo.com/quote/GC=F?p=GC=F").text  #preco do ouro em direto
    soup = BeautifulSoup(request,'lxml')
    resp = soup.find('span',class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    if not valores :
        addValores(tempos,valores,resp)
    elif resp.text != valores[-1]:  #só insiro um novo valor quando este for diferente do ultimo a ter sido inserido
        addValores(tempos,valores,resp)
    if len(valores)>150:
        valores = valores[50:]
        tempos = tempos[50:]
    # with open("scrapResults.txt","w") as f:
    #     for i in range(len(valores)):
    #         f.write(f"{valores[i]} {tempos[i]}\n")
    return {"valores":valores, "tempos":tempos} 



def addValores(tempos,valores,resp):
    valores += [resp.text]
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    tempos += [current_time]

def create_figure(x,y):
    fig = Figure()   
    ax = fig.add_subplot(1,1,1)
    # ax.style.use('dark-background')

    ax.set(xlabel='time (s)', ylabel='value ($)', title='Gold Price')
    ax.grid()
    ax.grid(False)
    ax.plot(x,y)
    if len(x) >= 8:
        xtick = ax.xaxis.get_ticklabels()
        ytick = ax.yaxis.get_ticklabels()

        intervaloX = len(xtick)//4
        intervaloY = len(ytick)//4

        # ytick = ax.yaxis.get_ticklabels()
        # for e in xtick: e.set_visible(False) #esconder todas
        # for e in ytick: e.set_visible(False) #esconder todas
        # for e in xtick[::len(xtick)//4]:
        #     e.set_visible(True)
        # for e in ytick[::len(ytick)//4]:
        #     e.set_visible(True)   
        for n, label in enumerate(ax.xaxis.get_ticklabels()): #reduzir o numero de label a serem apresentadas
            if n % intervaloX != 0:
                label.set_visible(False)
        for n, label in enumerate(ax.yaxis.get_ticklabels()): #reduzir o numero de label a serem apresentadas
            if n % intervaloY != 0:
                label.set_visible(False)
  
    return fig


   