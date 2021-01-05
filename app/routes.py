from app import app
from app.models import test, regexpy, afd, scrap

from flask import render_template,flash, url_for,Response,redirect, jsonify,request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io, requests, threading, random
from apscheduler.schedulers.background import BackgroundScheduler


import threading

sched = BackgroundScheduler(daemon=True)
sched.add_job(scrap.obterValorOil,'interval',seconds=10)
sched.start()

@app.route('/',methods=["POST","GET"])
@app.route('/index',methods=["POST","GET"])
def index():
    return render_template("inicio.html", value=3)

@app.route('/webscrap')
def plots():
    tabelaClass = scrap.getScrapLigaNOS()
    return render_template("webscrap.html", tabelaClass = tabelaClass)

@app.route('/regex',methods=["GET","POST"])
def regex():
    if request.method == "GET":
        return render_template("regex.html", results = None)
    else:       
        output = regexpy.checkRegex(request.form)
        return render_template("regex.html", results= output)

@app.route('/automato', methods = ["GET","POST"])
def automato():
    if request.method == "GET":
        return render_template("automato.html")
    else:
        output = afd.checkAutomato(request.form["sequencia"])
        return render_template("automato.html", result = output)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getPlot')
def plot_png():
    fig = scrap.create_figure(scrap.tempos, scrap.valores)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/getImage')
def imageTest():
    return "<img class='flexImg bigImg'src='/getPlot' alt=''>"
