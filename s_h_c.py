from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_string', methods=['POST'])
def post_string():
    try:
        data = request.get_json()
        if not data or 'input_string' not in data:
            return jsonify({'error': 'Missing input_string'}), 400
        
        input_string = data['input_string']
        return jsonify({'message': 'String received', 'input': input_string}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
