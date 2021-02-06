from flask import jsonify
response={'data':[0,0,0,0,0],'prediction_label':{'survived':1,'not survived':0}}


jsonify(response)