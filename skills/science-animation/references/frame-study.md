# Nghiên cứu frame liên tiếp của bốn video

## Bằng chứng và giới hạn

Lượt bổ sung ngày 2026-11-11 dùng bốn bản `reference.mp4` đã có trong `research/animation-reference`. Đã trực tiếp xem bốn contact sheet tổng quan (AI full-review/01, Death sheet-2, personal sheet-1, virotherapy sheet-3) và 11 sheet frame liên tiếp bên dưới. Tổng cộng **132 frame liên tiếp trong các đoạn mẫu**, không phải mọi frame của toàn bộ bốn video.

Tất cả file đọc được báo 30fps. `n` là chỉ số frame giải mã, bắt đầu từ 0. Thời gian ghi dưới ảnh tính bằng `n/30`, giả định tốc độ khung hình cố định; chưa kiểm tra PTS để xác nhận mọi timestamp. Ảnh từng frame được lưu rộng 640px, sheet hiển thị 320px. Chưa kiểm tra độ mượt bằng phát liên tục, âm thanh hoặc project nguồn. Không suy ra easing chính xác, số keyframe gốc hay phần mềm tác giả từ các ảnh này.

Thông tin về phạm vi nghiên cứu cũ được giữ trong [video-study.md](video-study.md); không coi các ảnh cũ chưa mở lại là bằng chứng mới đã kiểm tra.

| Nguồn | Frame đã xem | Khoảng gần đúng | Tài liệu ảnh |
|---|---:|---|---|
| [AI](https://www.youtube.com/watch?v=ujkD4SxPKOI&t=18s) | 540–563 | 18.000–18.767s | [sheet 1](../../../research/animation-reference/dense-study/ai/sheet-01.jpg), [sheet 2](../../../research/animation-reference/dense-study/ai/sheet-02.jpg) |
| [Death](https://www.youtube.com/watch?v=fEjvSbI_PT4&t=248s) | 7440–7463 | 248.000–248.767s | [sheet 1](../../../research/animation-reference/dense-study/death/sheet-01.jpg), [sheet 2](../../../research/animation-reference/dense-study/death/sheet-02.jpg) |
| [Personal cancer story](https://www.youtube.com/watch?v=5_Fayfx2NUM&t=420s) | 12600–12659 | 420.000–421.967s | [A1](../../../research/animation-reference/dense-study/personal/sheet-01.jpg), [A2](../../../research/animation-reference/dense-study/personal/sheet-02.jpg), [B1](../../../research/animation-reference/dense-study/personal-transition/sheet-01.jpg), [B2](../../../research/animation-reference/dense-study/personal-transition/sheet-02.jpg), [B3](../../../research/animation-reference/dense-study/personal-transition/sheet-03.jpg) |
| [Virotherapy](https://www.youtube.com/watch?v=0NY2gAftzJE&t=480s) | 14400–14423 | 480.000–480.767s | [sheet 1](../../../research/animation-reference/dense-study/virotherapy/sheet-01.jpg), [sheet 2](../../../research/animation-reference/dense-study/virotherapy/sheet-02.jpg) |

Các bảng gom frame theo diễn biến để đọc dễ hơn. Toàn bộ frame riêng và chỉ số tương ứng nằm trong `manifest.json` cạnh mỗi sheet. Bảng không gán một “keyframe” cho frame nguồn: ảnh render không cho biết frame nào tác giả đặt key.

## 1. AI: dùng ánh sáng và silhouette để tổ chức cảnh đông

**Quan sát:** phòng nhìn chéo từ trên, nhiều ô sáng đỏ và thiết bị quanh sàn. Tâm cảnh là hình đen trên vùng sáng vàng. Các mảng đen gấp khúc từ mép trên thay đổi mạnh trong nửa đầu mẫu; cuối mẫu còn lại khối đen ở giữa. Cảnh vẫn nhận ra được dù chủ thể gần như không có chi tiết bên trong.

| Frame | Thay đổi nhìn thấy | Bài học áp dụng |
|---|---|---|
| 540–543 | Mảng gấp khúc lớn nối vùng trên với tâm; nền phòng vẫn đọc được | Tách hành động bằng độ sáng và đường biên |
| 544–547 | Hình gấp khúc đổi hướng/vị trí quanh tâm | Vẽ pose silhouette riêng cho biến đổi mạnh |
| 548–551 | Đường nối phía trên thu hẹp và đổi hình | Giảm khối phụ khi chuyển sự chú ý về chủ thể |
| 552–554 | Phần nối ngắn dần, còn đoạn gấp phía trên | Một đường dẫn mắt có thể rút khỏi cảnh sau khi hoàn thành vai trò |
| 555–559 | Không còn phần nối dài trong hình; khối giữa biến đổi | Giữ vùng sáng để chủ thể không hòa nền |
| 560–563 | Khối giữa có hình ngang hơn so với đầu đoạn | Cho silhouette diễn đạt trạng thái, không phụ thuộc mặt |

**Suy luận triển khai:** có thể dựng bằng các lớp nền phối cảnh, pool ánh sáng, silhouette biến dạng và hiệu ứng phụ. Không đủ bằng chứng xác định là rig 2D, 3D hay tổ hợp. Không đo được quỹ đạo camera riêng từ mẫu này.

**Cách tự vẽ:** làm bản phòng ba mặt phẳng, đặt một hình nguyên bản màu rất tối ở tâm, vẽ 4 pose lớn của hiệu ứng. Kiểm tra khi tắt glow: hình vẫn rõ nhờ nền sáng. Sau đó mới thêm rim light và đèn xung quanh.

## 2. Death: màng cố định quan hệ, protein thay pose

**Quan sát:** dải màng hồng chạy chéo và phân chia hai nền màu. Cổng xanh lá nằm trong màng. Cấu trúc xanh dương có nhiều đoạn và khớp thay tư thế quanh cổng; hạt xung quanh di chuyển. Cuối đoạn có các thành phần nhãn nhỏ bắt đầu xuất hiện.

| Frame | Thay đổi nhìn thấy | Bài học áp dụng |
|---|---|---|
| 7440–7443 | Đoạn xanh phía trên chuyển từ vươn ngang sang cao hơn | Vị trí khớp và đường cong hành động cần rõ |
| 7444–7447 | Dáng đầu gắp phía trên gọn hơn; nhánh dưới vẫn gắn vào màng | Khóa điểm gắn, cho đầu tự do di chuyển |
| 7448–7451 | Các đoạn khớp đổi góc trong khi hai miền màu giữ ý nghĩa | Cấu trúc nền ổn định giúp đọc cử động nhỏ |
| 7452–7455 | Nhánh phía dưới duỗi chéo xuống phải | Dùng cung chuyển động để tránh pose cứng |
| 7456–7459 | Đầu trên mở hơn, đầu dưới tiếp tục đổi tư thế | Hai nhánh không cần cùng pha |
| 7460–7463 | Xuất hiện mảnh nhãn ở trái và trên màng | Chữ là lớp bổ trợ; cơ chế đã nhìn thấy trước đó |

**Suy luận triển khai:** chuỗi khớp hoặc pose vẽ riêng đều có thể tái tạo hành vi tương tự. Mẫu không chứng minh một cơ chế sinh học cụ thể; phân tích ở đây chỉ nói về staging và chuyển động.

**Cách tự dựng:** vẽ dải màng và cổng trong cùng root, tách mỗi đoạn protein, đặt pivot ở khớp. Tạo ba pose tiếp cận–tương tác–rời. Cho hạt quan trọng bám đầu gắp tại thời điểm tương tác, rồi tách ra; không để hạt trôi ngẫu nhiên xuyên qua protein.

## 3. Personal: giữ nhận diện DNA khi thay asset theo tỷ lệ

**Quan sát:** nền kem gần như trống; chuỗi DNA nhỏ nằm ngang và có đường đo bên dưới. Một hình nhỏ ở phía trên. Chuỗi lớn bắt đầu hiện ở giữa, mở rộng và uốn thành một dải lớn. Sau khi bố cục cận ổn định, đối tượng nhỏ nhiều màu đi xuống từ trên.

| Frame | Thay đổi nhìn thấy | Bài học áp dụng |
|---|---|---|
| 12600–12615 | Chuỗi nhỏ và đường đo được giữ gần như ổn định | Cho người xem thời gian đọc quy mô trước chuyển cảnh |
| 12616–12619 | Vùng giữa chuỗi bắt đầu thay đổi nhỏ | Cần frame dày để tìm đúng lúc bắt đầu transition |
| 12620–12623 | Đoạn DNA lớn nhô lên rõ hơn ở tâm | Tạo mốc thị giác nối cảnh toàn với cận |
| 12624–12627 | Đoạn lớn mở rộng, hai phần chuỗi nhỏ còn hai bên | Không cần toàn cảnh cùng phóng to |
| 12628–12631 | DNA lớn chiếm phần lớn khung, đường đo và chuỗi nhỏ rút khỏi vùng nhìn | Loại thông tin của mức tỷ lệ cũ khi bước sang cơ chế mới |
| 12632–12635 | Chuỗi lớn uốn vòng; bố cục bắt đầu ổn định | Dừng chuyển đổi trước hành động tiếp theo |
| 12636–12643 | DNA giữ hình lớn, đối tượng nhỏ xuất hiện từ mép trên | Tách nhịp chuyển cảnh và nhịp giới thiệu tác nhân |
| 12644–12651 | Đối tượng nhiều màu đi xuống, DNA tiếp tục là mốc | Dẫn mắt tới quan hệ giữa tác nhân và nền cơ chế |
| 12652–12659 | Đối tượng tiến gần hơn, chưa thấy toàn bộ kết quả trong mẫu | Không suy diễn kết quả tiếp xúc nằm ngoài đoạn đã xem |

**Suy luận triển khai:** có thể dùng hai mức chi tiết của DNA, vùng che ở giữa và scale từng lớp. Không thể kết luận video dùng morph path hay dựng camera. Việc nhận diện được DNA trong cả hai bố cục quan trọng hơn lựa chọn công cụ.

**Cách tự dựng:** giữ màu/hướng xoắn, vẽ riêng DNA toàn thể và cận cảnh. Canh điểm neo trung tâm. Cho asset cận mở rộng từ vùng có ý nghĩa; giảm nhãn đo của cảnh cũ. Đợi hình ổn định rồi mới đưa tác nhân vào.

## 4. Virotherapy: khối hữu cơ nhiều tầng

**Quan sát:** khối trung tâm có biên tối, lớp xanh dương/cyan, vùng tím và lõi hồng; ngoài khối có gai và nhánh. Nền đỏ tím sáng hơn sát chủ thể. Trong 24 frame, đường viền và các cụm nhỏ thay đổi nhẹ; hình tổng thể được giữ giữa khung.

| Frame | Thay đổi nhìn thấy | Bài học áp dụng |
|---|---|---|
| 14400–14405 | Biên, gai và lõi giữ nhận diện trong khi vị trí tương đối thay đổi nhẹ | Chia asset thành nhiều phần có liên quan |
| 14406–14411 | Các thùy và vùng màu bên trong không chỉ là một hình đứng yên | Biến dạng cục bộ giữ cảm giác hữu cơ |
| 14412–14417 | Mẫu tiếp tục biến đổi nhẹ mà không thay bố cục lớn | Chuyển động nhỏ đủ duy trì sức sống khi đang giải thích |
| 14418–14423 | Khối vẫn ở tâm, gai và chấm không lấn át lõi | Giữ hierarchy ngay cả ở artwork dày chi tiết |

Mẫu ngắn và ảnh sheet thu nhỏ **không đủ để đo chu kỳ, tần số, mức squash hoặc độ trễ từng gai**. Muốn định lượng cần mở ảnh riêng, đánh dấu landmark và lấy đoạn dài hơn.

**Cách tự dựng:** dựng lõi và 6–8 thùy lớn, gắn gai lên các thùy; dùng tham số biến dạng cục bộ thay vì scale cả group. Giữ khu vực thông tin chính ít méo. Chi tiết nhỏ đi theo vật chủ, không rung độc lập từng frame.

## 5. Quy trình mở rộng nghiên cứu tới từng shot/frame

1. Dùng contact sheet thưa để tìm shot cần học. Chỉ gọi đó là bản đồ tổng quan, vì có thể bỏ sót cut ngắn.
2. Chọn khoảng có đủ chuẩn bị, hành động và ổn định. Chụp từng frame liên tiếp; đừng dùng bộ lọc `fps=8` rồi gọi là mọi frame.
3. Ghi `n`, thời gian, pose, điểm neo, overlap, biến dạng, nhãn, camera và mức tin cậy. Một cột riêng dành cho cách triển khai đề xuất.
4. Nếu cần đo easing, theo dõi cùng landmark và tách chuyển động camera trước. Tính khoảng cách giữa các frame; không ước lượng cubic-bezier bằng mắt rồi ghi như dữ kiện.
5. Xem đoạn phát ở tốc độ thường và chậm để đánh giá nhịp. Muốn nói lip-sync hoặc nhạc/cut phải nghe âm thanh tương ứng.
6. Muốn tuyên bố kiểm tra toàn bộ video cần manifest phủ đủ mọi frame, nhật ký kiểm tra và xử lý cả các khoảng chưa xem. Hiện bộ nghiên cứu này chưa đạt phạm vi đó.

Lệnh chạy từ thư mục dự án, theo quy tắc RTK của workspace:

```powershell
rtk proxy python skills/science-animation/scripts/frame_probe.py research/animation-reference/fEjvSbI_PT4/reference.mp4 research/animation-reference/dense-study/death-next --start-frame 7464 --count 60
```

Script giải mã từ đầu để chọn đúng chỉ số frame; có thể chậm ở video dài. Không resample fps, không xóa thư mục cũ, giới hạn tối đa 240 frame/lần để nghiên cứu từng đoạn. Với nguồn VFR, chỉ số frame vẫn hữu ích nhưng timestamp ước tính cần thay bằng PTS trước khi dùng để trích dẫn thời gian chính xác.
