from flask import Flask,jsonify,request
from db import connection


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify("Enter the input in URL like this -- > URL?q='input'")

@app.route('/search',methods=['GET'])
def search():
    search = request.args.get('q')
    if not search:
        return jsonify('''Enter the input in URL like this -- > URL?q='input' ''')
    search = search.lower().strip()

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM contentable where content like %s",(f"%{search}%",))
    retrieval = cursor.fetchall()
    result = []
    for i in retrieval:
        wordcount = i[0].count(search)
        result.append((i[0],wordcount))

    result.sort(key=lambda x:x[1],reverse=True)
    cursor.close()
    conn.close()

    if len(result) == 0:
        return jsonify(f"No Results found for {search.capitalize()}")
    else:
        format = []
        for i in result:
            format.append({
                "content":i[0],
                'Score':i[1]
            })
        return jsonify(format)

if __name__ == "__main__":
    app.run(debug=True)