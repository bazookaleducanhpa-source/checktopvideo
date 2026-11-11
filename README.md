# Signal — Viral Radar

## Artwork và animation khoa học

- `skills/science-animation/`: hướng dẫn dựng hình, phân tích cảnh và timing.
- `artwork/science-samples/`: SVG, PNG và script vẽ; `v2/` chứa bản cải thiện.
- `artwork/science-samples/animation/`: video thử 30 giây.
- `artwork/science-samples/sequence-v3/`: video 36 giây với 9 cảnh và ba đoạn 12 giây.

Các script dựng hình dùng Python với `Pillow`, `resvg-py`, `imageio-ffmpeg`. Chạy lần lượt `draw_samples.py`, `refine_samples.py`, rồi `animate.py` hoặc `sequence.py` từ thư mục `artwork/science-samples/`. Script animation hiện dùng font Arial tại `C:/Windows/Fonts/`; cần đổi đường dẫn font nếu chạy trên hệ điều hành khác. Video là bài thử hình ảnh cách điệu, chưa có âm thanh.

Thư mục nghiên cứu `research/` và footage tham khảo không được đưa vào Git. Các liên kết ảnh nghiên cứu trong skill yêu cầu tư liệu local; hướng dẫn vẽ và artwork nguyên bản vẫn có trong repository.

## Chạy ứng dụng

Chạy local với Node.js 22+, không cần cài dependency.

1. Copy .env.example thành .env, điền YOUTUBE_API_KEY (bật YouTube Data API v3 trong Google Cloud).
2. Chạy npm start trong thư mục này, mở http://localhost:3000.
3. Thêm @handle, channel ID hoặc URL kênh rồi cập nhật.

Tối đa 30 kênh, 50 video gần nhất/kênh. Tự cập nhật 30 phút khi server chạy. Hai snapshot cách nhau ít nhất 5 phút mới tính view/giờ. Lịch sử giữ tối đa 30 ngày hoặc 3000 điểm/video. Lưu local trong data/state.json; key chỉ đọc phía server.

Outlier so sánh view/giờ từ lúc đăng với trung vị video còn lại cùng kênh. Chưa chuẩn hóa theo tuổi hoặc Shorts/live, không phải xác suất viral. Không đo tổng tăng trưởng toàn bộ kênh. Không có CTR/retention/địa lý của kênh khác.

DeepSeek phân tích transcript, hook, cấu trúc, giả thuyết viral và đề cương gốc cho Mỹ. Có ô phân tích độc lập không cần YouTube key. Chưa tải transcript tự động, xác minh tin tức bằng web hoặc tổng hợp chủ đề. Chưa kiểm chứng dữ liệu API thật nếu thiếu key. Không có dữ liệu giả.

Server chỉ lắng nghe loopback. Không dùng trực tiếp cho hosting công khai. Chạy npm test để kiểm tra phép tính.

Docs: https://developers.google.com/youtube/v3/docs/videos/list
Captions: https://developers.google.com/youtube/v3/guides/implementation/captions

## DeepSeek
Điền DEEPSEEK_API_KEY trong .env, giữ DEEPSEEK_MODEL=deepseek-flash hoặc model tài khoản hỗ trợ. Khởi động lại bằng npm start. Mở cổng PORT trong .env (máy này là 3210). Không dán key vào chat hoặc transcript. Key chỉ nằm phía server. Khi bấm phân tích, dữ liệu video và transcript được gửi đến DeepSeek; có tính phí theo tài khoản API. Kết quả AI là giả thuyết, không thay thế kiểm chứng nguồn tin.
Tài liệu tích hợp: https://api-docs.deepseek.com/en/
