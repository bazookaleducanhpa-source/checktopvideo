# Cách vẽ và dựng animation giải thích khoa học

Các thông số dưới đây là điểm khởi đầu đề xuất cho sản xuất mới, không phải số đo hoặc bí quyết lấy từ project gốc.

## 1. Chốt ý của cảnh trước khi vẽ

Viết một câu: “Ai/cái gì làm gì, khiến điều gì thay đổi?”. Ví dụ trung tính: “Một tín hiệu tới cổng, cổng mở và các hạt đi qua”. Chia thành ba trạng thái trước–hành động–sau. Đặt một tiêu điểm, rồi chọn góc nhìn nhìn rõ quan hệ ấy.

Storyboard ghi: thời gian dự kiến, lời thoại, chủ thể, hành động, camera, phần thay đổi, cách nối sang cảnh sau. Đoạn lời thoại cần đọc số liệu nên có khoảng giữ hình; không đặt chuyển cảnh lớn ngay lúc đọc một con số quan trọng.

## 2. Vẽ từ silhouette tới chi tiết

1. Dùng hình tròn, ellipse, capsule và đường Bézier để tạo khối chính. Nhìn bản một màu ở kích thước nhỏ: có nhận ra chủ thể không?
2. Tạo bất đối xứng có chủ đích cho nhân vật sinh học; giữ đối xứng và góc cạnh hơn cho máy móc nếu phù hợp câu chuyện.
3. Chia hình thành 3 mức: khối lớn, bộ phận trung bình, chi tiết nhỏ. Chi tiết không được làm mất ranh giới khối chính.
4. Thêm vùng sáng và bóng dưới dạng mảng màu lớn. Gradient chỉ dùng để tăng thể tích hoặc trọng tâm; không phủ glow lên mọi cạnh.
5. Vẽ mắt, mí và miệng thành lớp riêng. Bộ biểu cảm tối thiểu hữu ích: bình thường, chú ý, nghi ngờ, bất ngờ, mệt; lựa chọn theo câu chuyện.

Ví dụ một tế bào nguyên bản: viền ngoài không đều → thân → màng trong → nhân lệch tâm → vài bào quan → đốm sáng → bộ mặt. Đặt mặt ở vùng ít chi tiết, không để particle đi ngang che mắt.

## 3. Màu sắc theo vai trò

Lập bảng màu có tên vai trò: nền, chủ thể, đối tượng tương tác, cảnh báo, nhãn. Giữ cùng một đối tượng cùng màu qua nhiều cảnh. Đừng dùng màu cảnh báo cho đồ trang trí cạnh một hành động quan trọng.

Ba hướng khởi đầu tự chọn:
- Cơ chế vi mô: nền indigo, chủ thể vàng/cam, tác nhân cyan, nguy cơ hồng đậm.
- Cảnh người: nền kem/mint, người hồng/tím, đạo cụ màu tương phản vừa phải.
- Hệ thống: nền navy, đường nối xanh nhạt, nhóm chính violet, trạng thái nguy hiểm đỏ.

Đây là gợi ý định hướng, không phải palette được đo từ video. Kiểm tra grayscale: chủ thể vẫn phải nổi bật bằng độ sáng và hình khối.

## 4. Chia lớp để có thể chuyển động

Cấu trúc cảnh hữu ích: background → far scenery → midground → actor root → body/head/face/limbs → foreground → particles → labels. Mắt, miệng, tay và điểm gắn đạo cụ có pivot riêng. Không làm méo chữ khi scale actor.

Tế bào: nhân và thân có thể đi theo root, còn màng và gai có độ trễ riêng. Người: vai, khuỷu, cổ tay và cổ cần vị trí nhất quán. Chuyển mặt chính diện sang nghiêng thường cần pose vẽ riêng; chỉ co chiều ngang sẽ làm mặt méo.

Thêm chiều sâu bằng chồng lấp, thay tỷ lệ, độ tương phản xa–gần và parallax. Giữ một nguồn sáng có chủ đích. Blur tiền cảnh có thể dẫn mắt nhưng không được che hành động chính.

## 5. Tạo chuyển động có trọng lượng

Vẽ pose bắt đầu, pose cực trị và pose dừng trước khi thêm in-between. Chọn đường đi hình cung cho cử động hữu cơ; máy móc có thể đi theo đường thẳng và dừng rõ.

Một công thức thử ở 30fps: chuẩn bị 4–8 frame, hành động 8–16 frame, ổn định 4–8 frame. Đây chỉ là bài tập, phải chỉnh theo hành động và lời thoại. Gaze có thể dẫn đầu chuyển đầu một chút; tay hoặc màng kéo theo sau. Squash/stretch nhẹ nên giữ cảm giác thể tích bằng cách tăng một trục và giảm trục kia.

Tránh mọi vật lắc cùng nhịp. Cho mỗi actor một pha khác nhau; giảm biên độ nền. Hạt nền đi chậm, hạt thể hiện sự kiện đi theo hướng có ý nghĩa. Chuyển động của hạt không được ngẫu nhiên hoàn toàn nếu đang giải thích dòng vận chuyển.

Đối với biến dạng khối u hoặc sinh vật: điều khiển các điểm đường viền và bộ phận riêng. Scale toàn khối chỉ là một thành phần, không thay thế biến dạng silhouette.

## 6. Camera và chuyển cảnh

- Macro → micro: đánh dấu một vùng trên chủ thể, tiến vào vùng ấy, giữ một hình quen thuộc rồi mới lộ cấu trúc mới.
- Match shape: hình tròn/đường dây ở cảnh trước trở thành chi tiết liên quan ở cảnh sau.
- Occlusion: một vật đi qua trước camera che chuyển cảnh.
- Pan theo nhân vật: đưa mắt tới quan hệ tiếp theo, không di chuyển chỉ để hình luôn bận rộn.
- Hard cut: dùng khi đổi thời gian, luận điểm hoặc cần tương phản. Không cần biến mọi lần đổi cảnh thành morph.

Phần kết có thể nhắc lại một vật thể từ mở đầu nhưng ở trạng thái mới. Đây là cách làm câu chuyện khép kín bằng hình ảnh.

## 7. Lộ trình bài tập áp dụng

1. Vẽ một chủ thể nguyên bản với 5 biểu cảm; kiểm tra silhouette và màu ở kích thước nhỏ.
2. Dựng cảnh 6–10 giây: chủ thể nhận tín hiệu, phản ứng, rồi ổn định. Chỉ một hành động chính.
3. Dựng cảnh 10–15 giây: toàn cảnh → cận cảnh → cơ chế bên trong; giữ mốc nhận diện qua thay đổi tỷ lệ.
4. Dựng 20–30 giây có ba cảnh: vấn đề → cơ chế → kết quả. Xem có hiểu được quan hệ khi tắt âm thanh không.
5. Sau khi có style và motion đạt yêu cầu, mở rộng thành storyboard cho video dài, tái sử dụng bộ asset thay vì tạo hình mới không nhất quán ở mỗi cảnh.

## 8. Kiểm tra chất lượng

- Hình tĩnh: một tiêu điểm rõ; silhouette đọc được; nhãn không che hành động; màu có nghĩa.
- Chuyển động: không giật tại điểm nối; pivot không trượt; không xuyên hình; camera không gây mất phương hướng.
- Diễn giải: người xem biết đang ở tỷ lệ nào; nguyên nhân xuất hiện trước hậu quả; biểu đồ có trục/đơn vị khi cần.
- Đầu ra: kiểm tra frame đầu/cuối, đoạn chuyển cảnh, độ đồng bộ âm thanh và bản render thực. Không lấy contact sheet làm bằng chứng đã xem mượt mọi frame.
- Nguyên bản: tạo nhân vật, kịch bản và bố cục riêng; tư liệu tải về chỉ để nghiên cứu.
