ỨNG DỤNG QUẢN LÝ THÔNG TIN SINH VIÊN
1. Bài làm về gì
Ứng dụng được xây dựng nhằm mục đích quản lý thông tin sinh viên thông qua một hệ thống web đơn giản, hỗ trợ thực hiện các chức năng cơ bản như:
- Thêm mới sinh viên
- Chỉnh sửa thông tin sinh viên
- Xóa sinh viên
- Tìm kiếm sinh viên theo mã số
- Liệt kê toàn bộ danh sách sinh viên
Ngoài ra, ứng dụng còn được thiết kế theo mô hình hai ứng dụng tách biệt:
- App 1 đóng vai trò như máy chủ (server), chịu trách nhiệm xử lý dữ liệu, cung cấp API và lưu trữ thông tin trong cơ sở dữ liệu.
- App 2 đóng vai trò như máy khách (client), được sử dụng để gửi yêu cầu tìm kiếm sinh viên từ xa, phù hợp với mô hình mạng nội bộ (LAN).
2. Sử dụng công nghệ, thuật toán, ngôn ngữ lập trình
Ngôn ngữ và công nghệ:
- Python 3.11 – Ngôn ngữ chính của toàn bộ ứng dụng
- Flask – Framework dùng để xây dựng web backend và API RESTful
- HTML, CSS (basic) – Giao diện người dùng
- JavaScript (DOM) – Hỗ trợ tương tác và tìm kiếm động
- SQL Server – Cơ sở dữ liệu lưu trữ thông tin sinh viên
- PyODBC – Thư viện kết nối giữa Python và SQL Server
Kết nối liên ứng dụng:
- App 2 sử dụng thư viện requests của Python để gọi tới API của App 1 thông qua địa chỉ IP nội bộ
- App 1 chạy bằng Flask với host="0.0.0.0" để chấp nhận kết nối từ các máy khác trong mạng LAN
3. Một số giao diện cơ bản
- Giao diện App 1 – Quản lý sinh viên:
  <img width="1845" height="914" alt="image" src="https://github.com/user-attachments/assets/c8c893ff-84b2-44ae-8f9e-e17e3b31f459" />
- Giao diện App 2 – Tìm kiếm từ xa:
  <img width="1864" height="914" alt="image" src="https://github.com/user-attachments/assets/9a04c7d5-d48d-4087-9696-7642afcc5377" />
4. Mục tiêu của đề tài
- Làm quen với cách xây dựng ứng dụng quản lý thực tế trên nền tảng web.
- Áp dụng kiến thức về ngôn ngữ Python và framework Flask để xử lý backend và API.
- Tương tác với cơ sở dữ liệu SQL Server để lưu trữ và truy vấn thông tin sinh viên.
- Thực hành cách triển khai mô hình client-server qua mạng LAN, nơi App 1 hoạt động như server và App 2 là ứng dụng tìm kiếm từ xa.
- Hiểu rõ quy trình CRUD (Create – Read – Update – Delete) và xử lý dữ liệu từ form nhập liệu trong môi trường web.
5. Hướng dẫn sử dụng
- Clone mã nguồn từ github: https://github.com/BinhNeymar2004/QLSinhVien-2-app.git
- Khởi động App 1 (máy chủ): python app1.py
- Khởi động App 2 (máy khách): python app2.py
- Mở trình duyệt và truy cập: http://localhost:5000
