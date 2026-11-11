# Sổ tay chuyển động: từ pose tới từng frame

Các bài dưới đây là **thiết kế mới để luyện tập ở 30fps**, không phải timing đo của video gốc. Mục đích là biến bài học quan sát thành cảnh có thể sản xuất. Xem [frame-study.md](frame-study.md) để biết phần nào đã trực tiếp quan sát.

## 1. Quy tắc thời gian và nội suy

Đặt frame đầu là 0. Một cảnh 90 frame gồm frame 0–89; thời lượng xuất 3 giây ở 30fps, khoảng cách từ tâm frame đầu tới cuối là 89/30 giây. Nếu có key ở frame 90, đó có thể là mốc biên cho cảnh tiếp theo, không phải frame hiển thị cuối của cảnh 90 frame.

Với một đoạn từ `f0` đến `f1`, tính:

```text
u = clamp((frame - f0) / (f1 - f0), 0, 1)
smooth = 3*u*u - 2*u*u*u
value = start + (end - start) * smooth
```

`smooth` phù hợp nhiều động tác đến và dừng; nó không tự tạo trọng lượng hoặc overshoot. Chuyển động đều dùng `u`; bật nhanh rồi giảm tốc có thể thử `1-(1-u)^3`. Với chuỗi key, kiểm tra vận tốc ở điểm nối: mỗi đoạn ease về 0 sẽ tạo cảm giác cứ đi rồi dừng nếu hành động đáng lẽ liên tục.

Không gắn mọi thuộc tính vào một hàm ease. Vị trí, góc, mắt, tay và camera phục vụ các thời điểm khác nhau. Dùng thời gian suy từ frame, không cộng dồn theo thời gian render thực. Random có seed và tham số cố định giúp frame 42 luôn giống nhau khi xuất lại.

## 2. Bài A — protein gắp và đưa hạt qua cổng, 90 frame

Vẽ màng, cổng, protein và một hạt nổi bật theo art recipe. Giữ camera đứng yên để luyện quan hệ nguyên nhân–hậu quả. Đây là ẩn dụ chuyển vận phục vụ bài animation, không phải mô phỏng sinh học được xác minh.

| Frame | Hành động chính | Lớp phụ | Mục đích |
|---:|---|---|---|
| 0–11 | Hạt tiến vào vùng trước cổng; protein chờ | Nền trôi rất nhẹ | Nhận ra tác nhân và vị trí |
| 12–17 | Đầu gắp hướng về hạt | Gốc vẫn gắn màng | Chuẩn bị có hướng |
| 18–29 | Tay đi theo cung tới hạt | Đầu gắp mở | Giữ mục tiêu rõ |
| 30–33 | Hai phần đầu gắp khép | Hạt chuyển sang bám tay | Đánh dấu tiếp xúc |
| 34–45 | Tay kéo hạt về cổng | Khớp phụ theo sau | Cho thấy lực có nguồn |
| 46–51 | Cổng mở | Màng chỉ biến dạng cục bộ | Nguyên nhân trước hậu quả |
| 52–63 | Hạt đi qua vùng cổng | Chỗ đi qua bị che đúng lớp | Không để xuyên hình vô lý |
| 64–69 | Hạt rời đầu gắp, tiếp tục đường đi | Cổng bắt đầu khép | Đổi ràng buộc có chủ đích |
| 70–77 | Protein về gần pose nghỉ | Đầu tay theo sau một chút | Tạo follow-through |
| 78–89 | Giữ kết quả | Nhãn xuất hiện nếu cần | Cho người xem hiểu điều vừa xảy ra |

**Ràng buộc cần kiểm tra:** trước frame 30 hạt ở hệ tọa độ cảnh; 30–63 bám điểm gắn; sau 63 trở lại hệ cảnh. Khi đổi parent, chuyển tọa độ để vị trí toàn cục không nhảy. Giữ chân protein trên socket ở mọi frame. Kiểm tra frame 29/30, 33/34, 63/64 vì đây là chỗ dễ nhảy hoặc xuyên hình.

Nếu code không có IK, dựng 3–5 pose khớp thủ công rồi nội suy góc; không kéo đầu tay và bỏ qua chiều dài các đoạn. Kiểm tra đường đi cả đoạn, vì hai pose đúng vẫn có thể nội suy xuyên màng.

## 3. Bài B — nhân vật nghe một tin và phản ứng, 60 frame

| Frame | Mắt | Đầu/thân | Tay |
|---:|---|---|---|
| 0–9 | Nhìn trung tính | Pose nghỉ đọc rõ | Giữ |
| 10–13 | Đồng tử hướng tới người nói | Đầu chưa xoay nhiều | Giữ |
| 14–21 | Giữ mục tiêu | Đầu xoay nhẹ theo mắt | Giữ |
| 22–27 | Mí/mày đổi biểu cảm | Cằm lùi hoặc nghiêng | Bắt đầu nâng |
| 28–37 | Biểu cảm chính | Thân phản ứng biên độ nhỏ | Đến pose diễn đạt |
| 38–45 | Có thể chớp nếu không che khoảnh khắc chính | Vai thả hoặc dừng | Vượt nhẹ rồi trở lại nếu phù hợp |
| 46–59 | Giữ cảm xúc | Ổn định | Giữ pose đủ lâu để đọc |

Một chớp mắt thử có thể gồm 2 frame khép, 1 frame khép hoàn toàn, 3 frame mở. Đây không phải chu kỳ bắt buộc. Đừng chớp mắt đều như đồng hồ; chọn vị trí có lý do trong diễn xuất. Đừng thêm rung thân liên tục cho nhân vật đang mệt hoặc đứng yên tập trung.

Khi quay đầu, điểm nhìn nên chuyển theo mặt chứ không trượt trên canvas. Mũi, mắt xa và tai phải đổi overlap. Nếu pose cần thay artwork, dùng lúc chớp hoặc chuyển động nhanh để giảm cảm giác bật hình, nhưng vẫn kiểm tra silhouette trước/sau.

## 4. Bài C — từ DNA toàn thể tới cận cảnh, 60 frame

Bài học từ personal 07:00–07:02 là giữ dấu hiệu nhận diện và tách nhịp phóng lớn khỏi nhịp tương tác mới.

| Frame | DNA toàn thể | DNA cận | Nhãn/tác nhân |
|---:|---|---|---|
| 0–11 | Giữ ngang | Chưa hiện | Nhãn quy mô đọc được |
| 12–17 | Nhấn vùng giữa | Xuất hiện nhỏ tại cùng neo | Nhãn giảm độ nổi |
| 18–29 | Hai bên ra khỏi vùng nhìn | Mở rộng theo vùng chọn | Bỏ nhãn thuộc quy mô cũ |
| 30–35 | Không còn cần thiết | Ổn định thành bố cục cận | Chưa có hành động mới lớn |
| 36–47 | — | Giữ mốc hình | Tác nhân đi vào |
| 48–59 | — | Chuyển động phụ rất ít | Tác nhân tiến tới vùng tương tác |

Đặt hai asset chung điểm neo. Không scale chữ theo DNA. Dùng mask phù hợp để đoạn nhỏ không hiện như đường dây chạy xuyên asset lớn. Frame giữa transition phải có ít nhất một dấu hiệu màu/hình nối với shot trước. Nếu người xem không biết đang nhìn gì, thêm một hold hoặc vùng đánh dấu trước khi tăng hiệu ứng.

## 5. Bài D — màng hữu cơ nhận một xung lực, 48 frame

Dựng lớp lõi, thân mềm và gai. Thay vì cho cả group scale theo sin, xác định vùng nhận lực và hướng lực.

| Frame | Thân | Nhân/lõi | Gai |
|---:|---|---|---|
| 0–7 | Pose cơ sở | Ổn định | Nghỉ |
| 8–11 | Lõm tại điểm tác động | Ít đổi | Gai gần vùng lực bắt đầu nghiêng |
| 12–17 | Phía đối diện phồng nhẹ | Dịch một phần theo lực | Theo sau thân |
| 18–25 | Bật lại với biên độ thấp hơn | Trở về chậm hơn thân | Vượt nhẹ |
| 26–35 | Giảm biến dạng | Ổn định | Dao động giảm |
| 36–47 | Pose gần ban đầu | Giữ | Dừng dần |

Để làm thử squash toàn thân, có thể dùng `sx=1.06` và `sy=1/sx` nhằm giữ diện tích gần đúng trong 2D. Nhưng đây chỉ là thành phần phụ; lực cục bộ cần dịch điểm biên tương ứng. Không dùng công thức giữ diện tích 2D như thể đã bảo toàn thể tích 3D.

Với đường biên theo góc, thử `r(theta,t)=r0(theta)+A(t)*w(theta)*sin(phase(theta,t))`; `w` giới hạn vùng ảnh hưởng, `A` giảm theo thời gian. Chọn biên độ đủ nhỏ để không tự cắt path; kiểm tra ở điểm lõm, gai và chỗ nối mask. Các lớp phía trong không cần có cùng pha hoặc biên độ, nhưng phải giữ quan hệ bao chứa.

## 6. Particles có nhiệm vụ

Phân loại trước khi tạo:

- **Hạt cơ chế:** có điểm xuất phát/đích, đường đi và sự kiện tiếp xúc. Tốc độ và mật độ không được làm sai điều giải thích.
- **Hạt môi trường:** ít tương phản, thường chậm và nhỏ; có thể trôi lệch pha.
- **Hạt sự kiện:** phát ra theo một sự kiện; hướng và thời điểm cho thấy lực, sau đó giảm hoặc ra khỏi khung.

Cho mỗi hạt một thời điểm sinh, đời sống, vị trí đầu, vận tốc và seed. Tính trạng thái từ tuổi hạt. Khi loop, tránh reset cả đám cùng frame. Khi camera phóng lớn, xác định hạt nằm trong world hay screen space; chọn sai sẽ làm hạt dính vào màn hình hoặc phóng to vô lý.

Đừng dùng particle làm lý do để chuyển động mọi vùng. Khi cần khán giả đọc một nhãn, giảm hạt quanh nhãn hoặc giữ một vùng sạch.

## 7. Camera, cut và overlap

Camera nên trả lời một câu hỏi: đang ở đâu, phần nào quan trọng, quan hệ lớn–nhỏ ra sao. Giữ camera ổn định khi chuyển động đối tượng đã đủ giải thích. Nếu pan, chừa khoảng phía hướng chuyển động. Đặt điểm dừng sao cho hình cuối là một bố cục đẹp riêng, không chỉ là kết quả ngẫu nhiên của tween.

Với parallax 2D, cho các mặt phẳng gần/xa dịch khác nhau nhưng giữ thứ tự chiều sâu. Không áp dụng các hệ số khác nhau lên bộ phận của cùng một vật cứng. Khi vật tiền cảnh che cut, cần thật sự che toàn bộ vùng sẽ đổi hình tại frame cắt; kiểm tra bốn góc màn hình.

Với match shape, khớp vị trí, hướng, tỷ lệ và ít nhất một tín hiệu màu. Crossfade hai hình phức tạp thường tạo ảnh kép khó đọc; có thể cut ở thời điểm silhouette gần nhau hoặc dùng một lớp che có lý do.

## 8. Kiểm tra từng frame có mục tiêu

Kiểm tra các frame trước/sau tiếp xúc, đổi parent, đổi artwork, bắt đầu/kết thúc mask, cực trị biến dạng và cut. Sau đó phát cả đoạn để xem cảm giác chuyển động. Hai việc này bổ sung cho nhau.

| Lỗi | Nguyên nhân thường gặp | Sửa |
|---|---|---|
| Động tác đều và vô lực | Spacing tuyến tính ở mọi thuộc tính | Thêm pose chuẩn bị, thay spacing, cho thời gian dừng |
| Trượt khi cầm vật | Đạo cụ không ở hệ tọa độ tay | Chuyển parent giữ world transform |
| Khớp lộ khe | Thiếu overlap hoặc pivot lệch | Vẽ phần dư ở khớp, chỉnh pivot |
| Morph xoắn | Topology/điểm tương ứng sai | Ghép anchor theo bộ phận hoặc vẽ pose trung gian |
| Giật tại loop | Giá trị hoặc vận tốc hai đầu không nối | Kiểm tra cả vị trí và đạo hàm tại biên |
| Nhấp nháy hạt | Random mới mỗi frame | Seed và tính trực tiếp theo thời gian |
| Người xem lạc tỷ lệ | Không có mốc xuyên transition | Giữ một vật nhận diện và bố cục cuối rõ |
| Chữ khó đọc | Chữ di chuyển/scale cùng camera | Tách lớp overlay, cho khoảng giữ |

Khi báo kết quả, ghi rõ đã xem frame tĩnh, sheet hay playback; âm thanh đã nghe hay chưa. Không nói “mượt 30fps” chỉ vì đã xuất file 30fps.
