import os
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import numpy as np
from sklearn.externals import joblib
import pymongo
import pandas as pd

app = Flask(__name__)
api = Api(app)
cbc_model = joblib.load('cbc_kmeans.joblib')
liver_model = joblib.load('liver_kmeans.joblib')
cholesterol_model = joblib.load('cholesterol_kmeans.joblib')
diabetes_model = joblib.load('diabetes_kmeans.joblib')
data = []


def loadData():
    myclient = pymongo.MongoClient("mongodb://sih:sih@35.244.56.63:27017/")
    mydb = myclient["ocr"]
    mycol = mydb["ocr"]
    myquery = {"type": "health"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        for y in x['data']:
            data.append({y['test']: y['value']})


loadData()
# print(data)
# print(len(data))

class Hello(Resource):
    def get(self):
        return jsonify({
            'Message': 'Hello User'
        })


class PredBlood(Resource):
    def get(self):
        diffBaso = 0.22
        diffEos = 0.972
        diffLymph = 19.395
        diffMono = 9.4427
        diffNeut = 61.255
        absBaso = 0.014580
        absEos = 0.059160
        absLymph = 1.16
        absMono = 0.559450
        absNeut = 3.24885
        hemoglobin = 10.47
        mch = 28.335
        mchc = 29.51
        mcv = 90.8
        mpv = 11.795
        packedCellVolume = 33.3
        plateletCount = 147.15
        rbcCount = 3.45
        rdw = 13.85
        tlc = 5.103
        for x in data:
            try:
                if x['%Baso']:
                    diffBaso = x['%Baso']    
            except:
                pass
        for x in data:
            try:
                if x['%Eos']:
                    diffEos = x['%Eos']
            except:
                pass
        for x in data:
            try:
                if x['%Lymph']:
                    diffLymph = x['%Lymph']
            except:
                pass
        for x in data:
            try:
                if x['%Mono']:
                    diffMono = x['%Mono']
            except:
                pass
        for x in data:
            try:
                if x['%Neut']:
                    diffNeut = x['%Neut']
            except:
                pass
        for x in data:
            try:
                if x['AbsBaso']:
                    absBaso = x['AbsBaso']
            except:
                pass
        for x in data:
            try:
                if x['AbsEos']:
                    absEos = x['AbsEos']
            except:
                pass
        for x in data:
            try:
                if x['AbsLymph']:
                    absLymph = x['AbsLymph']
            except:
                pass
        for x in data:
            try:
                if x['AbsMono']:
                    absMono = x['AbsMono']
            except:
                pass
        for x in data:
            try:
                if x['AbsNeut']:
                    absNeut = x['AbsNeut']
            except:
                pass
        for x in data:
            try:
                if x['Hemoglobin']:
                    hemoglobin = x['Hemoglobin']
            except:
                pass
        for x in data:
            try:
                if x['MCH']:
                    mch = x['MCH']
            except:
                pass
        for x in data:
            try:
                if x['MCHC']:
                    mchc = x['MCHC']
            except:
                pass
        for x in data:
            try:
                if x['MCV']:
                    mcv = x['MCV']
            except:
                pass
        for x in data:
            try:
                if x['MPV']:
                    mpv = x['MPV']
            except:
                pass
        for x in data:
            try:
                if x['Packed Cell Volume']:
                    packedCellVolume = x['Packed Cell Volume']
            except:
                pass
        for x in data:
            try:
                if x['Platelet Count']:
                    plateletCount = x['Platelet Count']
            except:
                pass
        for x in data:
            try:
                if x['RBC Count']:
                    rbcCount = x['RBC Count']
            except:
                pass
        for x in data:
            try:
                if x['RDW']:
                    rdw = x['RDW']
            except:
                pass
        for x in data:
            try:
                if x['TLC']:
                    tlc = x['TLC']
            except:
                pass
        
        pred = int(cbc_model.predict([[diffBaso, diffEos, diffLymph, diffMono, diffNeut,
                                       absBaso, absEos, absLymph, absMono, absNeut,
                                       hemoglobin, mch, mchc, mcv, mpv, packedCellVolume,
                                       plateletCount, rbcCount, rdw, tlc]]))

        if pred == 0:
            msg = 'You are healthy'
        elif pred == 1:
            msg = 'low blood count'
        else:
            msg = 'high blood count'

        return jsonify({
            'Prediction': pred,
            'Message': msg
        })


class PredLiver(Resource):
    def get(self):
        for x in data:
            try:
                if x['bilirubin total']:
                    tbili = x['bilirubin total']
            except:
                pass
        for x in data:
            try:
                if x['bilirubin direct']:
                    dbili = x['bilirubin direct']
            except:
                pass
        for x in data:
            try:
                if x['bilirubin indirect']:
                    ibili = x['bilirubin indirect']
            except:
                pass
        for x in data:
            try:
                if x['ast (sgot) *']:
                    ast = x['ast (sgot) *']
            except:
                pass
        for x in data:
            try:
                if x['alt (sgpt) *']:
                    alt = x['alt (sgpt) *']
            except:
                pass
        for x in data:
            try:
                if x['alkaline phosphatase (alp) *']:
                    alkPhos = x['alkaline phosphatase (alp) *']
            except:
                pass
        for x in data:
            try:
                if x['total protein']:
                    prot = x['total protein']
            except:
                pass
        for x in data:
            try:
                if x['albumin']:
                    albumin = x['albumin']
            except:
                pass
        for x in data:
            try:
                if x['calcium, total *']:
                    ca = x['calcium, total *']
            except:
                pass
        for x in data:
            try:
                if x['sodium *']:
                    na = x['sodium *']
            except:
                pass
        for x in data:
            try:
                if x['potassium *']:
                    k = x['potassium *']
            except:
                pass
        for x in data:
            try:
                if x['creatinine']:
                    cr = x['creatinine']
            except:
                pass
        bun = 16.152550
        cl = 103.963000
        glob = 2.952450
        glu = 103.505500
        pred = int(liver_model.predict([[alt, ast, albumin, alkPhos, bun,
                                     ca, cl, cr, dbili, glob, glu, ibili,
                                    k, na, prot, tbili]]))
        if pred == 0:
            msg = 'Liver is healthy'
        else:
            msg = 'Take care please'

        return jsonify({
            'Prediction': pred,
            'Message': msg
        })


class PredCholesterol(Resource):
    def get(self):
        cholesterol = 167.8725
        hdlc = 41.808150
        ldlc = 116.052513
        triglyc = 280.4103
        vldlc = 21.126420
        chdl_ratio = 3.84444
        nhdlc = 159.255
        for x in data:
            try:
                if x['cholesterol']:
                    cholesterol = x['cholesterol']
            except:
                pass
        for x in data:
            try:
                if x['hdl cholesterol']:
                    hdlc = x['hdl cholesterol']
            except:
                pass
        for x in data:
            try:
                if x['direct ldl cholesterol']:
                    ldlc = x['direct ldl cholesterol']
            except:
                pass    
        for x in data:
            try:
                if x['triglycerides']:
                    triglyc = x['triglycerides']
            except:
                pass
        for x in data:
            try:
                if x['very low density lipoprotein']:
                    vldlc = x['very low density lipoprotein']
            except:
                pass
        for x in data:
            try:
                if x['chol/hdl ratio']:
                    chdl_ratio = x['chol/hdl ratio']
            except:
                pass
        for x in data:
            try:
                if x['non hdl cholesterol']:
                    nhdlc = x['non hdl cholesterol']
            except:
                pass
        pred = int(cholesterol_model.predict([[cholesterol, hdlc, ldlc,
                                              triglyc, vldlc, chdl_ratio, nhdlc]]))

        if pred == 1:
            msg = 'High Cholesterol'
        else:
            msg = 'Low Cholesterol'

        return jsonify({
            'Prediction': pred,
            'Message': msg
        })


class PredDiabetes(Resource):
    def get(self):
        hba1c = 6.1
        eag = 127.773750
        for x in data:
            try:
                if x['glycosylated hemoglobin(hba1c)']:
                    hba1c = x['glycosylated hemoglobin(hba1c)']
            except:
                pass
        for x in data:
            try:
                if x['mean plasma glucose']:
                    eag = x['mean plasma glucose']
            except:
                pass
        pred = int(diabetes_model.predict([[hba1c, eag]]))

        if pred == 0:
            msg = 'diagnosing diabetes'
        elif pred == 1:
            msg = 'non-diabetic'
        else:
            msg = 'you\'re at risk'
        return jsonify({
            'Prediction': pred,
            'Message': msg
        })


api.add_resource(Hello, '/')
api.add_resource(PredBlood, '/predict/blood')
api.add_resource(PredLiver, '/predict/liver')
api.add_resource(PredCholesterol, '/predict/cholesterol')
api.add_resource(PredDiabetes, '/predict/diabetes')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
