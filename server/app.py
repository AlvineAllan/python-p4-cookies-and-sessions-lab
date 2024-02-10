from flask import Flask, jsonify, session

app = Flask(__name__)
app.secret_key = b'a\xdb\xd2\x13\x93\xc1\xe9\x97\xef2\xe3\x004U\xd1Z'

@app.route('/articles/<int:id>')
def show_article(id):
    # Initialize 'page_views' in the session if it's the first request
    session['page_views'] = session.get('page_views', 0)
    
    # Increment 'page_views' by 1 for every request
    session['page_views'] += 1

    # Check if 'page_views' exceeds the limit
    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    # Fetch article data (replace this with your actual implementation)
    article_data = {
        'author': 'John Doe',
        'title': 'Sample Article',
        'content': 'Lorem ipsum dolor sit amet...',
        'preview': 'Lorem ipsum dolor sit amet...',
        'minutes_to_read': 5,
        'date': '2024-02-10'
    }

    # Return article data as JSON response
    return jsonify(article_data)

@app.route('/clear')
def clear_session():
    # Clear session data
    session.clear()
    return jsonify({'message': 'Session data cleared successfully'})

if __name__ == '__main__':
    app.run(debug=True)
