# Sổ tay dựng artwork: từ khối tới cảnh hoàn chỉnh

## Cách đọc và phạm vi

Đây là cách dựng mới rút ra từ những hình đã quan sát trong bốn video, không phải bản giải mã project của tác giả. Tên lớp, tọa độ, mã màu, số điểm Bézier và tỷ lệ bên dưới là **đề xuất thực hành**. Mốc đối chiếu và ảnh nằm trong [video-study.md](video-study.md) và [frame-study.md](frame-study.md).

Mục lục: ngôn ngữ hình • tế bào • màng và protein • người • DNA • môi trường máy móc • mặt cắt mô • màu và ánh sáng • kiểm tra.

## 1. Ngôn ngữ hình: vì sao hình nhiều màu vẫn đọc được

Trong các mẫu, hình được phân thành ba cấp: silhouette nhận diện, mảng cấu trúc bên trong, điểm nhấn nhỏ. Mắt hoặc tâm phản ứng thường được dành vùng tương phản riêng. Cảnh bệnh viện sáng và ít hiệu ứng hơn cảnh vi mô; cảnh robot mở đầu dùng vùng sáng sau silhouette rất tối. Vì thế không có một preset neon phù hợp mọi shot.

Quy trình dựng một artboard:

1. Vẽ ba thumbnail trắng đen, mỗi thumbnail chỉ gồm nền, chủ thể và đối tượng tương tác. Chọn bản nhìn rõ quan hệ nhất ở chiều rộng 240px.
2. Đặt khối lớn trước. Một cảnh cơ chế cần khoảng trống cho đường đi, không chỉ khoảng trống cho chữ.
3. Chia hình lớn thành các mảng có nhiệm vụ: ranh giới, cơ quan, điểm nối, mặt, đạo cụ. Không thêm hạt cho tới khi bước này rõ.
4. Dùng ba mức sáng để tách chủ thể, nền và điểm nhấn. Hai màu khác hue nhưng cùng độ sáng vẫn có thể dính nhau.
5. Thêm chi tiết theo cụm. Một vùng nghỉ ít chi tiết cạnh một vùng dày làm chi tiết có giá trị hơn việc rải đều.
6. Đặt artwork vào pose cực trị sớm. Hình đẹp khi đứng yên có thể hở vai, lệch mắt hoặc đứt màng lúc xoay.

### Đường Bézier sạch

Đặt anchor tại cực trên/dưới/trái/phải và nơi đổi độ cong. Với đường cong mềm, hai tay nắm tại một điểm nên cùng tiếp tuyến; không dùng hàng chục anchor để chữa một khối đơn giản. Góc nhọn chỉ xuất hiện khi silhouette cần gai, cạnh máy hoặc gấp khúc. Kiểm tra đường biên ở tỷ lệ thật, không chỉ phóng 800%.

Nếu morph hai path, giữ cùng số điểm, thứ tự điểm và chiều đi quanh đường biên. Gắn điểm tương ứng theo bộ phận; tự động nối điểm gần nhất dễ làm đường viền xoắn. Với hai silhouette rất khác nhau, vẽ pose trung gian hoặc dùng che khuất/cắt cảnh sẽ dễ kiểm soát hơn.

## 2. Tế bào nguyên bản có thể diễn xuất

Xem [hình minh họa sáu bước](../assets/cell-construction.svg), artwork vector nguyên bản đi kèm skill. Có thể mở trực tiếp bằng trình duyệt hoặc phần mềm vector; các group minh họa bộ phận, chưa phải rig hoàn chỉnh.

Đối chiếu: Death khoảng 07:40–07:48; virotherapy khoảng 08:00. Mẫu cho thấy lớp màng, vùng chất bên trong, nhân và chi tiết có độ tương phản khác nhau. Không phải mọi tế bào đều phải có mắt.

### Các bước vẽ trên ô 400 × 400

1. **Silhouette:** phác một khối lệch tâm quanh (200,210), rộng khoảng 270, cao 230. Tạo 5–7 thùy lớn khác kích thước; tránh biến thành hình sao đều.
2. **Màng ngoài:** dùng path khép kín màu tối. Giữ các lõm đủ rộng để khi thu nhỏ không thành răng cưa.
3. **Màng trong:** vẽ path nhỏ hơn, nhưng chỉnh tay quanh các lõm; phép scale đơn thuần không tạo độ dày màng đều.
4. **Bào tương:** một mảng sáng hơn ở trung tâm. Chừa một khoảng ít chi tiết nơi đặt mặt hoặc điểm tương tác.
5. **Nhân:** khối tròn lệch tâm, khoảng 1/4–1/3 bề ngang tế bào. Thêm một mảng tối và một đốm sáng lớn thay vì nhiều chấm lấp lánh.
6. **Bào quan:** chia thành 2–3 cụm, mỗi cụm 2–5 hình. Thay đổi tỷ lệ có kiểm soát; không random kích thước từng pixel.
7. **Mặt nếu cần:** đặt mắt trên một nhóm riêng. Khoảng cách mắt và vị trí miệng giữ ổn định ở các pose; biểu cảm chủ yếu từ mí, mày và hướng nhìn.
8. **Độ sâu:** thêm mảng sáng cong ôm khối bên trên và mảng tối phía dưới. Chỉ thêm viền sáng nơi có nguồn sáng hoặc cần tách nền.

Thứ tự lớp gợi ý:

```text
cell_root (vị trí, góc tổng thể)
  rear_appendages
  outer_membrane
  cytoplasm
  organelles_back
  nucleus
  organelles_front
  face_root (eyes / lids / brows / mouth)
  highlight
  front_appendages
```

Cho màng biến dạng riêng; nhân giữ thể tích tương đối ổn định và có độ trễ nhẹ. Bộ mặt đi theo thân nhưng không nhận toàn bộ méo cục bộ của màng. Gai gắn vào điểm trên biên, không đặt tuyệt đối trên canvas rồi để thân trôi khỏi gai.

**Lỗi hay gặp:** nhân, hạt và màng đều sáng như nhau → giảm tương phản hạt trước; hình giống miếng sticker → thêm overlap và một mảng bóng theo khối; màng giống cao su vô trọng lượng → giảm biên độ và chỉ tác động quanh vùng nhận lực.

## 3. Màng tế bào và protein dạng khớp

Đối chiếu trực tiếp: Death 04:08. Màng hồng chạy chéo, chia miền tím phía trên và vàng phía dưới; đối tượng xanh gắn vào màng. Đây là bố cục giải thích được “bên trong/bên ngoài” bằng không gian trước khi đọc nhãn.

1. Vẽ một đường dẫn chéo qua khung. Tạo dải màng theo đường dẫn, không xoay từng hình lipid ngẫu nhiên.
2. Một đơn vị lipid gồm đầu tròn và phần đuôi; nhân bản theo tiếp tuyến đường dẫn. Hai hàng đầu hướng về hai phía ngoài của dải.
3. Cắt một khoảng dành cho cổng. Đặt cổng trong cùng hệ tọa độ với màng để pan/zoom không làm cổng trượt.
4. Vẽ protein bằng các đoạn capsule và khớp tròn. Đầu gắp có silhouette riêng, nhìn rõ trạng thái mở/đóng.
5. Giấu phần gốc sau màng bằng lớp che; đặt phần hoạt động trước màng. Layer order quyết định cảm giác xuyên qua màng.
6. Đặt hạt tự do ở ba tầng: nền mờ, tầng hành động rõ, tiền cảnh ít và lớn hơn. Hạt liên quan cơ chế cần màu/hình nhất quán qua cổng.
7. Đặt nhãn trong khoảng trống; đường chỉ kết thúc ở cấu trúc, không xuyên qua khớp đang hoạt động.

Rig thử: `membrane_root → socket → upper_segment → elbow → lower_segment → gripper`. Pivot của đoạn con nằm tại đầu đoạn cha. Chuyển động đầu gắp phải giữ chiều dài đoạn tay, trừ khi cố ý dùng biến dạng hoạt hình.

## 4. Nhân vật người: mềm, rõ, có cảm xúc

Đối chiếu: personal cancer story 00:04–01:32. Da và áo được cách điệu bằng màu khác thực tế; mắt, mày, miệng và tư thế vẫn giúp hiểu cảm xúc. Độ tin cậy đến từ diễn xuất nhất quán, không phải giải phẫu nhiều chi tiết.

### Dựng đầu và mặt

1. Vẽ khối sọ oval và hàm hơi thu. Kẻ đường giữa và đường mắt theo góc đầu.
2. Đặt tai tại vùng đường mắt–mũi, rồi tóc thành một silhouette lớn và vài mảng phụ. Không vẽ từng sợi.
3. Dựng mắt bằng trắng mắt, đồng tử và mí có mask. Khi nhắm, mí che mắt; tránh scale cả mắt thành một chấm nhỏ.
4. Lông mày là đường cong có độ dày rõ. Đổi độ nghiêng và khoảng cách tới mắt tạo khác biệt lớn hơn thêm nếp nhăn.
5. Miệng dùng các pose riêng: khép, mở hẹp, mở rộng, cười, căng. Với lời thoại cần lip-sync, chọn viseme theo âm thanh thực; không lặp ba miệng theo chu kỳ đều.
6. Vẽ thêm góc 3/4 và nghiêng khi shot cần. Mắt xa nhỏ/hẹp hơn, mũi chồng lên vùng mặt; không co ngang toàn đầu để giả xoay 90 độ.

| Trạng thái | Mắt/mày | Miệng | Pose phụ trợ |
|---|---|---|---|
| Chú ý | Nhìn về tác nhân, mày nhấc nhẹ | Khép hoặc hé | Đầu dẫn hướng |
| Bối rối | Hai mày không đối xứng | Một khóe kéo | Đầu nghiêng nhẹ |
| Mệt | Mí thấp, mày ít lực | Lỏng, ít biên độ | Vai hạ, thân tựa |
| Bất ngờ | Mắt mở, mày nhấc | Mở tròn | Thân lùi sau một nhịp |
| Nhẹ nhõm | Mí mềm | Cười nhẹ | Vai thả, nhịp chuyển chậm |

### Thân, tay và đạo cụ

Vẽ thân như một khối áo rõ, tay bằng các đoạn thuôn có phần chồng lên nhau tại khớp. Đặt bàn tay riêng với các pose nắm/chỉ/mở. Tay cầm đồ vật cần điểm gắn trên lòng bàn tay; đạo cụ đi theo điểm ấy cho tới frame buông. Khi nằm trên giường, đệm và chăn phải che đúng lớp chân/thân, bóng tiếp xúc gắn với chỗ tựa.

Đạo cụ y tế nên được giản lược để đọc được hành động. Không suy ra hướng dẫn điều trị hay liều dùng từ cách điệu của hình.

## 5. DNA và chuyển đổi tỷ lệ

Đối chiếu trực tiếp: personal 07:00–07:02. DNA nhỏ nằm ngang trên nền sáng trở thành DNA lớn uốn cong; nền ít chi tiết giúp nhận ra hình liên tục.

1. Vẽ đường trục của chuỗi. Để giải thích chiều dài, giữ trục thẳng; để giải thích tương tác cục bộ, dùng đường cong lớn.
2. Tạo hai đường xoắn quanh trục với pha đối nhau. Các thanh nối cùng nhịp dọc trục.
3. Phân đoạn trước/sau tại điểm giao để có overlap rõ. Hai màu gần nhau về vai trò nhưng khác độ sáng giúp tách hai dải.
4. Khi hình rất nhỏ, giảm chi tiết thành biểu tượng sóng đôi. Khi cận, thay bằng asset có thanh nối và đường viền rõ; dùng cùng màu và hướng xoắn để nối nhận diện.
5. Nhãn đo chiều dài thuộc cảnh toàn thể; khi đi vào cơ chế cận cảnh, đưa nhãn ra trước khi nó phóng to chiếm màn hình.

Không nhất thiết morph mọi điểm từ chuỗi nhỏ sang lớn. Có thể dùng hai asset với vùng che và khoảng overlap ngắn. Đây là lựa chọn triển khai, không phải khẳng định về cách video gốc được làm.

## 6. Cảnh máy móc, robot và mạng lưới

Đối chiếu trực tiếp: AI khoảng 00:02–00:58 và mẫu 00:18. Bố cục phòng có mặt sàn, hai vách và nhiều đơn vị lặp; chủ thể tối được tách bởi vùng sáng vàng phía sau.

1. Chốt mặt phẳng sàn và vách trước. Vẽ đường dẫn phối cảnh thống nhất cho ô tường và thiết bị; không trộn góc nhìn của từng asset.
2. Tạo một module cửa/ô sáng với biến thể bật, tắt, cảnh báo. Tái dùng module theo hàng, giảm kích thước theo mặt phẳng.
3. Robot gồm thân hộp bo góc, màn mặt lõm, mắt phát sáng và tay chân thành khối riêng. Mắt có lõi sáng nhỏ, vùng màu và glow ngoài; glow không thay thế hình mắt.
4. Dành vùng sáng lớn sau nhân vật nếu silhouette tối. Giảm chi tiết đúng vùng tiếp xúc để tay/chân vẫn đọc được.
5. Vẽ dây và đường mạch theo tuyến có điểm đến. Mạng lưới giải thích cần cho thấy node và quan hệ; không dùng mạng trang trí vô nghĩa.
6. Tách `room`, `devices`, `actor`, `light_pool`, `foreground_occluder`. Parallax chỉ dùng khi phù hợp mặt phẳng; chuyển động camera không được phá điểm tụ.

Một phòng 2D có chiều sâu có thể dùng các mặt phẳng phối cảnh vẽ sẵn. Chỉ dùng 3D khi thay đổi góc camera khiến mặt khuất cần hiện ra. Không thể kết luận phần mềm dựng từ ảnh đã render.

## 7. Mô, khối u và đám đông tế bào

Vẽ biên chung của vùng mô trước, rồi đặt các tế bào theo vùng, không rải hình tròn độc lập khắp canvas. Cho hàng trước che một phần hàng sau; kích thước và tương phản giảm về xa. Giữ vài biến thể silhouette để tránh cảm giác lát gạch.

Khối hữu cơ có nhiều lớp cần các đường biên liên quan nhưng không đồng dạng tuyệt đối. Vùng lõi, vùng trung gian và gai phản ứng khác nhau. Trong mẫu virotherapy 08:00, khối không chỉ to/nhỏ; đường viền và cụm bên trong thay đổi tương quan. Bài dựng nên tách lõi, thùy, gai và hạt.

Khi thể hiện lan truyền, đánh dấu trạng thái từng tế bào rồi cho thay đổi đi qua không gian. Không đổi màu cả đám đồng thời nếu câu chuyện nói tác nhân lan từ một nơi. Khi chuyển sang số liệu, giảm trang trí và dành vùng rõ cho trục, đơn vị, chú thích.

## 8. Màu, ánh sáng và độ hoàn thiện

Palette thử cho tác phẩm mới, **không phải mã màu đo từ video**:

| Vai trò | Cơ chế tối | Cảnh người sáng |
|---|---|---|
| Nền | `#151333` | `#FFF3CA` |
| Mảng phụ | `#3E2472` | `#B8E7DD` |
| Chủ thể | `#F5B83D` | `#C9569B` |
| Đối tượng tương tác | `#36C9DB` | `#397DAD` |
| Điểm cảnh báo | `#EF527F` | `#C54160` |

Vẽ bóng bằng mảng màu có hue riêng, không chỉ phủ đen bán trong suốt lên mọi thứ. Với khối cong, mảng sáng cũng cong theo khối. Tạo ánh sáng tập trung từ ngoài vào trong: vùng ảnh hưởng rộng ít đậm → viền màu hẹp → lõi sáng nhỏ. Nếu mọi thứ đều glow, bỏ glow ở phần phụ trước khi tăng glow chủ thể.

Texture chỉ thêm sau khi hình và ánh sáng đã đọc được. Giữ texture bám theo vật thể; noise chạy ngẫu nhiên mỗi frame dễ thành nhấp nháy. Gradient nền nên hướng mắt tới hành động, không tạo một điểm sáng mạnh cạnh khung làm người xem nhìn sai chỗ.

## 9. Chẩn đoán hình chưa đẹp

| Hiện tượng | Kiểm tra | Cách sửa trước tiên |
|---|---|---|
| Nhiều chi tiết nhưng không rõ | Thu xuống 240px | Bỏ chi tiết phụ, làm rõ silhouette |
| Màu chói, phẳng | Xem grayscale | Tách độ sáng nền/chủ thể |
| Khớp như bị gãy | Xem pose cực trị | Chỉnh pivot, phần chồng và pose bàn tay |
| Vật thể nổi như sticker | Xem chỗ tiếp xúc | Thêm overlap, bóng tiếp xúc có hướng |
| Biến dạng như thạch | So thân với nhân/mặt | Giảm biên độ, tách phần cứng/mềm |
| Cảnh vô hồn dù chuyển động nhiều | Tắt hiệu ứng và hạt | Vẽ lại pose phản ứng và hướng nhìn |
| Chuyển cảnh đẹp nhưng khó hiểu | Dừng trước/sau cut | Giữ mốc nhận diện hoặc thêm shot nối |

Hoàn thiện theo thứ tự: ý nghĩa → bố cục → silhouette → pose → màu → chuyển động → ánh sáng → chi tiết. Đừng dành phần lớn thời gian cho hạt và glow khi hành động chính còn khó đọc.
