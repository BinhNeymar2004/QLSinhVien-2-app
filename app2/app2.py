from flask import Flask, render_template
import requests

app = Flask(__name__)

# Trang giao diện tìm kiếm
@app.route('/')
def index():
    return render_template('search.html')

# API: Tìm kiếm sinh viên theo mã sinh viên
@app.route('/api/search/<ma_sv>', methods=['GET'])
def tim_kiem_sinh_vien(ma_sv):
    try:
        # Gọi API từ app1
        response = requests.get(f'http://localhost:5000/api/sinhvien/{ma_sv}')
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Không tìm thấy sinh viên'}, 404
    except requests.exceptions.RequestException:
        return {'message': 'Không thể kết nối tới API'}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)