Họ và Tên : Nguyễn Thị Mỹ Duyên

MSSV: K205480106033

Môn học: Lập trình Python

Tên đề tài : Hệ thống đề xuất phim cho người dùng

1. xây dựng cơ sở dữ liệu

Bảng : Phim  bao gồm :ID(pk) ,Tiêu đề ,Thể loại ,Ngày phát hành ,Mô tả ,Xếp hạng .

Stored Procedures (SP_): SP_GetTopRatedMovies để lấy danh sách các bộ phim có điểm đánh giá cao nhất từ cơ sở dữ liệu.

2. Sử dụng Python và FastAPI để tạo một API để lấy dữ liệu từ trang web dịch vụ phim trực tuyến TMDB API.

Thuật toán:
-	 Gọi API của dịch vụ phim để lấy dữ liệu về phim.
-	Xử lý dữ liệu (lấy các thông tin cần thiết như tiêu đề, thể loại, ngày phát hành, mô tả).
-	Lưu dữ liệu vào cơ sở dữ liệu MSSQL.
-	API trong PYTHON sử dụng fasst API:
Tạo API để người dùng khác có thể lấy dữ liệu phim, đánh giá phim, và nhận đề xuất phim. 

 3. Sử dụng Node-red
    
- Gọi API từ Python: Sử dụng node HTTP request để gọi API FastAPI để lấy dữ liệu phim.
- Xử lý dữ liệu: Sử dụng các node function để xử lý dữ liệu nếu cần.
- Gọi stored procedure: Sử dụng node MSSQL để gọi các stored procedure, truyền tham số vào và lưu dữ liệu vào cơ sở dữ liệu.
  
4. Web
-	Xây dựng một ứng dụng web để hiển thị dữ liệu từ cơ sở dữ liệu.
-	Hiển thị biểu đồ dữ liệu phim. 


