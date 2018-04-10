# =====================================
# Kakao Plus Friend 2.0
# Toolkit
# Author: Taekyung Kim(kimtk@suwon.ac.kr)
# Last update: 2018-03-18
#======================================
# == LIBRARY ========================================
from flask import Flask, request, jsonify
from msg_set import all_msgs,msg_home
# == INIT APP SERVER ===============================
app=Flask(__name__)
app.debug=True
# == INTERACTION ===================================
@app.route("/")
def index():
    return "hello world"
@app.route("/keyboard")
def startKb():
    return jsonify(msg_home.home())
@app.route("/message",methods=['POST',])
def worker():
    user_msg=request.get_json()
    #user_key=user_msg['user_key']
    user_content=user_msg['content']
    considered_message=[m for m in all_msgs if m.question == user_content]
    if len(considered_message) > 0:
        msg=considered_message[0]
        response_to_kakaotalk=msg.echo()
        return jsonify(response_to_kakaotalk)
    else:
        return jsonify(msg_home.echo())
# == RUN SERVER ===================================
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001)