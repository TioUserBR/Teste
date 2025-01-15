from flask import Flask, request, render_template, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    video_url = request.args.get('url')  # Obtém o URL do vídeo da query string
    saved_time = request.cookies.get('video_time', 0)  # Obtém o tempo salvo nos cookies
    return render_template('video_player.html', video_url=video_url, saved_time=saved_time)

@app.route('/save_time', methods=['POST'])
def save_time():
    time = request.json.get('time', 0)  # Recebe o tempo atual do vídeo
    response = make_response(jsonify({"message": "Time saved"}))
    response.set_cookie('video_time', str(time), max_age=7 * 24 * 60 * 60)  # Salva o tempo por 7 dias
    return response

if __name__ == '__main__':
    app.run(debug=True)
