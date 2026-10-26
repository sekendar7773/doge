from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' এবং নির্দিষ্ট পোর্ট দিয়ে রান করা হচ্ছে যাতে ফোন থেকে এক্সেস করা যায়
    app.run(host='0.0.0.0', port=5000, debug=True)