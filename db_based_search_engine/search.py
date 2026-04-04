from flask import Flask,jsonify,request,render_template
from flask_cors import CORS
from db import connection


app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    # return jsonify("Enter the input in URL like this -- > URL?q='input'")
    return render_template('index.html')

@app.route('/search',methods=['GET'])
def search():
    search = request.args.get('q')
    if not search:
        return jsonify({"error":"Use /search?q=your_query"})
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
                "score":i[1]
            })
        return jsonify({"results":format})

if __name__ == "__main__":
    app.run(debug=True)