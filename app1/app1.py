from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)  # Cho phép app2 gọi API

# Cấu hình kết nối SQL Server với Windows Authentication
app.config['SQLALCHEMY_DATABASE_URI'] = r'mssql+pyodbc://@MSI\BTL_OLAP2/QLSinhVien2?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model Sinh viên
class SinhVien(db.Model):
    __tablename__ = 'SinhVien'
    MaSV = db.Column(db.String(10), primary_key=True)
    HoTen = db.Column(db.String(100), nullable=False)
    NgaySinh = db.Column(db.Date, nullable=True)
    GioiTinh = db.Column(db.String(10), nullable=True)
    DiaChi = db.Column(db.String(200), nullable=True)
    TenLop = db.Column(db.String(100), nullable=True)
    TenKhoa = db.Column(db.String(100), nullable=True)

# Tạo bảng trong CSDL (nếu chưa có)
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Lỗi tạo bảng: {e}")

# Trang giao diện chính
@app.route('/')
def index():
    return render_template('index.html')

# API: Thêm sinh viên
@app.route('/api/sinhvien', methods=['POST'])
def them_sinh_vien():
    data = request.get_json()
    if not data or not all(key in data for key in ['MaSV', 'HoTen']):
        return jsonify({'message': 'Thiếu thông tin bắt buộc (MaSV, HoTen)'}), 400
    
    sinh_vien = SinhVien(
        MaSV=data['MaSV'],
        HoTen=data['HoTen'],
        NgaySinh=data.get('NgaySinh'),
        GioiTinh=data.get('GioiTinh'),
        DiaChi=data.get('DiaChi'),
        TenLop=data.get('TenLop'),
        TenKhoa=data.get('TenKhoa')
    )
    
    try:
        db.session.add(sinh_vien)
        db.session.commit()
        return jsonify({'message': 'Thêm sinh viên thành công', 'MaSV': data['MaSV']}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Lỗi: {str(e)}'}), 400

# API: Sửa sinh viên
@app.route('/api/sinhvien/<ma_sv>', methods=['PUT'])
def sua_sinh_vien(ma_sv):
    sinh_vien = SinhVien.query.filter_by(MaSV=ma_sv).first()
    if not sinh_vien:
        return jsonify({'message': 'Không tìm thấy sinh viên'}), 404
    
    data = request.get_json()
    sinh_vien.HoTen = data.get('HoTen', sinh_vien.HoTen)
    sinh_vien.NgaySinh = data.get('NgaySinh', sinh_vien.NgaySinh)
    sinh_vien.GioiTinh = data.get('GioiTinh', sinh_vien.GioiTinh)
    sinh_vien.DiaChi = data.get('DiaChi', sinh_vien.DiaChi)
    sinh_vien.TenLop = data.get('TenLop', sinh_vien.TenLop)
    sinh_vien.TenKhoa = data.get('TenKhoa', sinh_vien.TenKhoa)
    
    try:
        db.session.commit()
        return jsonify({'message': 'Sửa sinh viên thành công'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Lỗi: {str(e)}'}), 400

# API: Xóa sinh viên
@app.route('/api/sinhvien/<ma_sv>', methods=['DELETE'])
def xoa_sinh_vien(ma_sv):
    sinh_vien = SinhVien.query.filter_by(MaSV=ma_sv).first()
    if not sinh_vien:
        return jsonify({'message': 'Không tìm thấy sinh viên'}), 404
    
    try:
        db.session.delete(sinh_vien)
        db.session.commit()
        return jsonify({'message': 'Xóa sinh viên thành công'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Lỗi: {str(e)}'}), 400

# API: Liệt kê danh sách sinh viên
@app.route('/api/sinhvien', methods=['GET'])
def liet_ke_sinh_vien():
    try:
        sinh_vien_list = SinhVien.query.all()
        result = [{
            'MaSV': sv.MaSV,
            'HoTen': sv.HoTen,
            'NgaySinh': sv.NgaySinh.isoformat() if sv.NgaySinh else None,
            'GioiTinh': sv.GioiTinh,
            'DiaChi': sv.DiaChi,
            'TenLop': sv.TenLop,
            'TenKhoa': sv.TenKhoa
        } for sv in sinh_vien_list]
        return jsonify(result)
    except Exception as e:
        return jsonify({'message': f'Lỗi: {str(e)}'}), 500

# API: Tìm kiếm theo mã sinh viên
@app.route('/api/sinhvien/<ma_sv>', methods=['GET'])
def tim_kiem_sinh_vien(ma_sv):
    try:
        sinh_vien = SinhVien.query.filter_by(MaSV=ma_sv).first()
        if not sinh_vien:
            return jsonify({'message': 'Không tìm thấy sinh viên'}), 404
        
        return jsonify({
            'MaSV': sinh_vien.MaSV,
            'HoTen': sinh_vien.HoTen,
            'NgaySinh': sinh_vien.NgaySinh.isoformat() if sinh_vien.NgaySinh else None,
            'GioiTinh': sinh_vien.GioiTinh,
            'DiaChi': sinh_vien.DiaChi,
            'TenLop': sinh_vien.TenLop,
            'TenKhoa': sinh_vien.TenKhoa
        })
    except Exception as e:
        return jsonify({'message': f'Lỗi: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
