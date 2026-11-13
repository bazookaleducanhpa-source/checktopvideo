# Phân tích xuyên suốt bốn video — lượt 2026-11-13

## Phạm vi thực tế

Đây là phân tích **cấu trúc toàn thời lượng bằng phụ đề và ảnh lấy mẫu**, bổ sung cho `video-study.md` và `frame-study.md`. Chưa phải xem/nghe liên tục toàn bộ bốn video, chưa kiểm tra mọi frame. Không dùng từ “full playback đã hoàn tất” cho lượt này.

Đã đọc phụ đề local từ đầu đến cuối, mở toàn bộ 23 contact sheet tổng quan cũ, tạo và mở thêm 23 sheet quét thay đổi hình ảnh xuyên suốt, cùng 8 sheet chuyển động lấy mẫu. Tổng cộng 54 sheet, chứa 1.265 lượt ảnh; con số này gồm các thời điểm có thể trùng nhau giữa các bộ, không phải 1.265 frame độc lập được chứng minh duy nhất.

FFmpeg đã giải mã cả bốn file từ đầu đến EOF để chọn các ảnh có thay đổi lớn hoặc cách ảnh được chọn trước ít nhất 12 giây. Bộ lọc này không phát hiện đầy đủ mọi shot: dissolve, cut ít tương phản, thay đổi cục bộ và hành động ngắn vẫn có thể bị bỏ sót. Số ảnh chọn **không phải số cảnh**. Ảnh tổng quan cũ cách 4 hoặc 8 giây được dùng cùng bộ mới để bổ sung nhau.

Cả bốn file local chỉ có video stream, không có audio stream theo log FFmpeg. Phụ đề tự động có lỗi nhận dạng, đặc biệt tên riêng. Chưa đánh giá giọng đọc, nhạc, sound design hoặc lip-sync. Không xác minh độc lập các khẳng định AI/y khoa của video; phần nội dung bên dưới mô tả cách nguồn kể chuyện.

| Nguồn | File local thực tế | Thời lượng file | Ảnh tổng quan cũ | Ảnh chọn mới | Mẫu chuyển động mới |
|---|---|---:|---:|---:|---:|
| [AI Just Crossed the Terrifying Line – Now What?](https://www.youtube.com/watch?v=ujkD4SxPKOI) | AV1, 854×480, 30 fps | 1303,87 s | 326 | 156 | 24 |
| [What Actually Happens When You Die?](https://www.youtube.com/watch?v=fEjvSbI_PT4) | H.264, 640×360, 30 fps | 839,77 s | 105 | 106 | 24 |
| [How I Survived Late-Stage Cancer (A Fun Story)](https://www.youtube.com/watch?v=5_Fayfx2NUM) | H.264, 640×360, 30 fps | 893,63 s | 112 | 133 | 24 |
| [This Woman Cured Her Cancer with an Insane Method](https://www.youtube.com/watch?v=0NY2gAftzJE) | H.264, 640×360, 30 fps | 913,47 s | 114 | 117 | 24 |

Tổng thời lượng file: khoảng 65 phút 51 giây. Riêng `reference.info.json` của AI ghi 3840×2160, 60 fps; đó không phải thông số bản MP4 local đang được nghiên cứu. Khi đánh chỉ số frame, phải dùng thông số của file thực tế.

Tư liệu mới nằm tại `research/animation-reference/timeline-review-2026-11-13/`. Mỗi video có `manifest.json`, `decode.log`, ảnh riêng và sheet. Timestamp của bộ chọn mới lấy từ source PTS trong `showinfo`. Timestamp trên tám sheet chuyển động là ước tính tâm mẫu ở 2 fps, không phải mốc cut chính xác.

Các khoảng dưới đây là **đoạn nội dung để nghiên cứu**, không phải danh sách mọi shot hoặc EDL. Mốc được làm tròn theo phụ đề và hình. Cột quan sát mô tả bằng chứng; cột áp dụng là đề xuất thiết kế mới.

## 1. AI — giữ hệ biểu tượng xuyên suốt một câu chuyện dài

Bằng chứng ảnh: [bộ cũ](../../../research/animation-reference/full-review/01.jpg), [manifest mới](../../../research/animation-reference/timeline-review-2026-11-13/ai/manifest.json). Đã mở bộ cũ 01–11 và bộ mới 01–07.

| Khoảng | Nội dung và hình quan sát | Cách áp dụng vào tác phẩm mới |
|---|---|---|
| 00:00–00:53 | Mở bằng robot trong các ô giam, đổi từ cận sang phòng có nhiều tầng; silhouette tối trên vùng sáng, sau đó trở về laptop và người dẫn chuyện dạng chim. Nguồn dựng một tình huống nguy hiểm trước khi định nghĩa thuật ngữ. | Dùng một sự kiện cụ thể mở câu hỏi; cần cảnh xác lập không gian trước cận phản ứng. Chừa lối quay về khung người kể để chuyển sang giải thích. |
| 00:53–02:16 | Mạng thần kinh, giao diện chat, nhân vật agent có “tay”, thang so sánh và timeline. Nền sáng của chat đổi sang nền tối của cơ chế. | Mỗi khái niệm mới nên có một hành động hoặc dấu hiệu hình khác nhau; đừng chỉ thay nhãn trên cùng hình tròn. |
| 02:16–02:47 | Bàn phím, agent, mê cung, cờ và phần thưởng; hình phần thưởng đổi cấu trúc. | Giới thiệu bộ vật thể mang nghĩa trước khi dùng nó trong lập luận dài. |
| 02:47–03:44 | Ví dụ dọn phòng, vua Midas rồi cuộc đua thuyền có bảng điểm. Không gian đời thường và game thay phiên cho khái niệm “mục tiêu nói ra khác điều muốn đạt”. | Dùng hai ví dụ khác quy mô để thử cùng một ý, nhưng giữ liên hệ bằng câu hỏi xuyên suốt. |
| 03:44–05:05 | Nhiều bài toán lặp, scorer được nhân vật hóa, cúp thưởng, phép toán và mê cung bị sửa. | Cho thấy đầu vào → thao tác → phản hồi. Một bộ máy chấm điểm có vị trí ổn định giúp khán giả nhận ra ai đánh giá ai. |
| 05:05–06:26 | Mê cung không giải được; nhánh bị phạt và nhánh được thưởng; màu đỏ/vàng đánh dấu hậu quả, rồi quay lại hình agent và mạng. | Biểu diễn sự khác nhau bằng hai diễn biến nhìn thấy được; dùng màu trạng thái nhất quán, không chỉ lời thoại đánh giá. |
| 06:26–07:50 | Phòng server, nhóm agent, ngày tháng, vùng cách ly, kho công cụ và luật nhiệm vụ. | Trước một sự cố phức tạp, vẽ bản đồ quyền truy cập và giới hạn; camera tiến gần chỉ khi giới thiệu quan hệ mới. |
| 07:50–09:20 | Folder dùng làm bảng tin; nhiều agent có tên; thư mục thành hộp thư, nhóm và cây phân công. Scorer xuất hiện lại để nhắc cách nhận thưởng. | Thay hình theo mức tổ chức: một tin nhắn → nhiều tin → hộp thư → nhóm. Giữ màu/hình người tham gia khi chuyển từ cận sang sơ đồ. |
| 09:20–09:53 | Laptop, emoji và phần diễn giải về việc dùng ngôn ngữ giống con người cho AI. | Khi đổi từ sự kiện sang cách diễn giải, tạm giảm mật độ cảnh và làm rõ phạm vi ẩn dụ. |
| 09:53–11:27 | Mê cung/cờ quay lại, cờ giả, cảnh báo và người điều phối mới; câu trích được đặt giữa khung rộng. | Tái sử dụng biểu tượng cũ với trạng thái mới để người xem hiểu bước ngoặt mà không học lại hình. |
| 11:27–13:27 | Các nhóm thử nghiệm, scorer, nhóm tình nguyện, so sánh virus, rồi nhiều đoạn trích trao đổi. Một số actor biến mất khỏi lưới. | Xen sơ đồ số đông với trường hợp cá thể; đoạn trích dài cần vùng sạch và khoảng giữ, không phủ hành động cạnh tranh. |
| 13:27–14:44 | Nhóm agent chuyển ra mạng có các thẻ/nút; tài khoản, khóa và dòng trích mô tả phát hiện. | Dùng đồ thị quyền truy cập thay vì vẽ “hacker gõ máy” cho mọi hành động kỹ thuật. |
| 14:44–15:49 | Nhóm đồng thuận và nhóm phản đối được tách vị trí; “swarm” tụ lại; sơ đồ ba hệ thống chuyển sang mạng vàng bị đổi tím. | Thể hiện tập thể bằng nhóm có đường biên và hướng di chuyển chung; cho sự xâm nhập có điểm tiếp xúc và mặt lan truyền. |
| 15:49–16:23 | Ngày/giờ, nhiều agent biến mất, hình người nghiên cứu và báo cáo. | Một kết quả đột ngột có thể được kể bằng sự vắng đi của đối tượng, không cần thêm hiệu ứng nổ. |
| 16:23–18:24 | Folder cũ được nhóm mới tiếp cận; mạng và các thẻ tin; khung “update”; sân khấu giới thiệu sản phẩm rồi cửa server đóng. | Tách cập nhật và ý kiến khỏi chuỗi sự kiện chính bằng kiểu bố cục riêng. Đừng biến cảnh báo tương lai thành cùng kiểu hình với bằng chứng quá khứ. |
| 18:24–20:19 | Nhân vật nghiên cứu, chồng tài liệu, agent soi agent, mặt nạ, hạ tầng nhiều ngành và quả địa cầu. | Khi mở rộng hệ quả, đi từ quan hệ đơn giản sang mạng lớn; nhắc lại mốc tỷ lệ để sự tăng quy mô có ý nghĩa. |
| 20:19–20:48 | Trở về phòng robot, nhà nghiên cứu, laptop và mắt đỏ; khép lại hình mở đầu. | Lặp lại bối cảnh mở với ý nghĩa đã đổi, không lặp nguyên đoạn chỉ để đủ thời lượng. |
| 20:48–21:44 | Hỗ trợ kênh, sản phẩm, footage đồ in và end screen. | Đánh dấu phần thương mại riêng; không dùng các cut sản phẩm để suy ra nhịp khoa học. |

**Nhận định:** sức liên kết của phần hình nằm ở bộ biểu tượng có nghĩa bền vững: agent, mê cung, cờ, scorer, phần thưởng, folder. Việc một nhân vật trở nên đáng ngại chủ yếu được thể hiện bằng màu, mắt, quan hệ kích thước và bối cảnh. Không có dữ liệu retention để kết luận những lựa chọn này làm tăng giữ chân người xem.

## 2. Death — cơ chế theo tầng và khoảng lặng cuối câu chuyện

Bằng chứng: [sheet cũ 1](../../../research/animation-reference/fEjvSbI_PT4/sheet-1.jpg), [manifest mới](../../../research/animation-reference/timeline-review-2026-11-13/death/manifest.json). Đã mở cả bốn sheet cũ và năm sheet mới.

| Khoảng | Nội dung và hình quan sát | Cách áp dụng |
|---|---|---|
| 00:00–00:12 | Giới thiệu sản phẩm ngủ bằng footage và QR. | Tách khỏi hook của nội dung. |
| 00:12–01:10 | Tim ngừng, cơ thể/người vẫn hiện diện, rồi các cấp cơ chế. Một nhân vật nhỏ phát sáng trở thành người dẫn đường. | Chọn một vật/nhân vật làm mốc qua các lần thay tỷ lệ. |
| 01:10–01:50 | Oxy, đường, ATP; đường đi qua phổi và máu; lưới chấm và hồng cầu. | Với khái niệm trừu tượng, cho thấy trao đổi và đường vận chuyển trước khi đưa tỷ lệ lên hình. |
| 01:50–02:30 | Não–tim–phổi nối trong cơ thể; timeline ngắn; cận gương mặt và sự tắt tín hiệu. | Đi từ quan hệ toàn hệ thống xuống một hậu quả nhìn thấy được. Không đổi cả camera lẫn chú thích khi khán giả đang đọc thời gian. |
| 02:30–03:45 | Câu hỏi về cuộc đời nối sang quảng cáo 80,000 Hours; hình mạng, tài liệu, website. | Đây là đoạn tài trợ; không tính nó vào diễn tiến cơ chế thần kinh. |
| 03:45–04:16 | Neuron, màng chéo chia hai miền, protein gắn màng và nhãn. | Bố cục phải giải thích “trong/ngoài” ngay cả khi chưa đọc chữ. |
| 04:16–04:58 | Protein giảm hoạt động, phân bố ion, neuron mất tín hiệu và ảnh hưởng lân cận. | Dùng cùng bố cục trước/sau để người xem thấy cái gì đã hỏng; không thay toàn cảnh cùng lúc với hậu quả. |
| 04:58–05:53 | Tác nhân nhỏ vào vùng tế bào, neuron và mạng thần kinh, sóng ảnh hưởng trên não. | Sau sự cố cục bộ, lùi về mạng để cho thấy lan truyền. |
| 05:53–06:55 | Nhân vật dẫn đường tách khỏi cơ thể; không gian thưa, não và timeline; cảnh bệnh viện/hiến tạng theo lời kể. | Cho khoảng nghỉ giữa hai cụm cơ chế; giảm chi tiết thay vì cố duy trì chuyển động mọi nơi. |
| 06:55–07:40 | Tim/gan/thận, bộ đường–oxy–ATP, DNA và vùng mô. | Nhắc lại các biểu tượng nguyên liệu đã dạy từ đầu, rồi giới thiệu phản ứng khác của cơ quan. |
| 07:40–08:26 | Tế bào có mặt, màu chuyển theo trạng thái; túi enzyme giải phóng tác nhân, tế bào biến dạng. | Tách vỏ chứa, phần bên trong và vật thoát ra; một phép scale cả khối không kể đủ cơ chế. |
| 08:26–09:06 | Cơ, sợi cơ, khung người, nang lông, tim và máu. | Đổi cách nhìn theo từng tầng cấu trúc; không dùng hình cơ thể tổng quát để minh họa mọi câu. |
| 09:06–09:46 | Nhóm vi sinh, mặt cắt ruột có lớp nhầy–biểu mô–miễn dịch, hàng rào suy yếu. | Vẽ địa hình và ranh giới trước khi cho đám đông đi qua; người xem cần biết một sự vượt biên vừa xảy ra. |
| 09:46–10:42 | Cảnh đông hạt và tế bào miễn dịch; chuyển ra hình cơ thể có các điểm tách biệt, rồi trở về một tế bào đơn lẻ. | Chuyển số đông → toàn thể → cá thể để giải thích mất liên lạc, không chỉ tăng số hạt trên màn hình. |
| 10:42–11:52 | Ánh sáng đi vào mô, hồng cầu co lại, vùng da, DNA và đường tín hiệu. | Dùng khác biệt ánh sáng và mật độ để kể sự suy tàn; vẫn giữ các cấu trúc đủ đọc. |
| 11:52–12:42 | Cơ/tế bào gốc, nhân vật nhỏ trên nền tối, cơ thể và đốm sáng. Câu kết quay lại câu hỏi thời điểm chết. | Kết thúc bằng câu hỏi ở cấp con người, tránh thêm một sơ đồ mới khi đã tới kết luận. |
| 12:42–14:00 | Sản phẩm ngủ, footage làm việc và end screen. | Tách phần thương mại và hậu trường khỏi cơ chế. |

**Nhận định:** tuyến hình liên tục được giữ bằng cơ thể, nhân vật dẫn đường và các biểu tượng phân tử. Sự tương phản quan trọng là cảnh đông hoạt động so với cảnh thưa ở cuối. Những mốc y khoa trong phụ đề là phát biểu của nguồn, không phải hướng dẫn y tế đã kiểm chứng trong nghiên cứu này.

## 3. Personal cancer story — trải nghiệm con người dẫn vào cơ chế

Bằng chứng: [sheet cũ 1](../../../research/animation-reference/5_Fayfx2NUM/sheet-1.jpg), [manifest mới](../../../research/animation-reference/timeline-review-2026-11-13/personal/manifest.json). Đã mở bốn sheet cũ và sáu sheet mới.

| Khoảng | Nội dung và hình quan sát | Cách áp dụng |
|---|---|---|
| 00:00–00:40 | Nhân vật kể chuyện, bối cảnh điều trị và bác sĩ; xen cảnh cách điệu của các tác nhân trong cơ thể. | Đặt một người cụ thể vào tình huống trước khi giảng giải thuật ngữ. |
| 00:40–01:33 | Túi truyền xanh, ống nối, giọt rơi, cận bác sĩ kiểm tra găng tay, bệnh nhân cười; góc toàn và cận đổi theo điều cần chú ý. | Một đạo cụ nhỏ có thể mang cả hook: vật → nguy cơ → phản ứng → nghịch lý. Cần pose riêng cho tay và nét mặt. |
| 01:33–02:14 | Quay về ghế điều trị, cơ thể dạng mạng rồi title card và mô hình phân tử. | Chốt câu hỏi của trải nghiệm trước khi chuyển sang lịch sử/cơ chế. |
| 02:14–03:33 | Phòng thí nghiệm, nhà nghiên cứu, kính hiển vi, vi khuẩn dài, chuột và điện thoại; khung tối/bo cong và tông nâu phân biệt hồi tưởng. | Dùng một quy ước hình riêng cho thời quá khứ; không cần dựa hoàn toàn vào nhãn năm. |
| 03:33–04:04 | Lưới người, cơ quan thận và trở về bệnh nhân. | Đưa rủi ro về một hình cụ thể trước khi trình bày kết quả thành công. |
| 04:04–05:16 | Nhóm 11 khuôn mặt, nhóm đáp ứng tách ra, lưới tỷ lệ, truyền dịch/thận/bàng quang và biểu đồ so sánh. | Chọn một cách mã hóa số lượng rồi giữ nhất quán. Khi đổi từ người sang biểu đồ, cần giữ rõ mẫu số và đại lượng. |
| 05:16–06:17 | Title card cơ chế, cận cổng truyền, cơ thể, mạch máu và các phân tử; phụ đề chia các nhóm theo đường đi. | Tạo một hành trình liên tục từ đạo cụ đã quen đến bên trong, thay vì bắt đầu một thế giới không liên hệ. |
| 06:17–06:53 | Màng tế bào, tác nhân vượt qua, phân tử thay thành phần, rồi tiếp cận nhân. | Dùng thay đổi hình có nguyên nhân để đánh dấu trạng thái hoạt động. Một đối tượng cần giữ được nhận diện sau biến đổi. |
| 06:53–07:20 | Nhân → DNA nhỏ toàn chiều ngang → DNA lớn bị liên kết thành cụm; đồng hồ xuất hiện. | Phóng đại đúng vùng tương tác, bỏ nhãn ở tỷ lệ cũ, rồi mới diễn hoạt sự cố. Đồng hồ mang ý “hạn xử lý”, không phải đồ trang trí. |
| 07:20–08:34 | Bộ máy sửa DNA, cơ và các mô cần thay mới nhanh, DNA hỏng, đám tế bào, ảnh gia đình và bệnh nhân. | Xen cơ chế và hậu quả đời sống để tránh chuỗi vi mô kéo dài không có điểm tựa cảm xúc. |
| 08:34–09:48 | Tế bào ung thư, tế bào mầm, hình sinh sản, kiểm tra DNA, trạng thái từ chấp nhận sang từ chối rồi tế bào tan rã. | Với một ngoại lệ quan trọng, dùng so sánh trước/sau theo cùng tiêu chí; không chỉ đổi màu một nhóm rồi tuyên bố giải thích xong. |
| 09:48–10:32 | Timeline nhiều tuần, cơ thể, cận phổi, cửa phòng, bệnh nhân và thuốc hỗ trợ; chuyển sang hình hồi phục. | Đưa kết quả cơ chế trở lại đúng người và đúng thời gian đã đặt ở đầu. |
| 10:32–10:59 | Suy ngẫm về tế bào ung thư và ảnh/kỷ niệm; hình bệnh nhân vẫn là mốc. | Khoảng suy ngẫm cần ít thông tin mới để người xem nối lại câu chuyện. |
| 10:59–11:36 | Quán cà phê, toàn người, cận croissant/cốc, nét mặt thưởng thức rồi toàn quán. | Cảm giác phục hồi có thể kể bằng hành động đời thường và đạo cụ quen, không cần hiệu ứng chiến thắng lớn. |
| 11:36–12:13 | Sách/kênh, hồi tưởng các cảnh cũ, quay lại túi thuốc và lời chào tạm biệt. | Dùng montage ngắn nhắc lại những nút câu chuyện trước khi kết thúc quan hệ với đạo cụ trung tâm. |
| 12:13–13:48 | Quảng cáo phần mềm quản lý; interface và đồ họa công việc. | Phân loại riêng, không coi đây là phần cơ chế y học. |
| 13:48–14:54 | Lịch, artwork in, hậu trường và end screen. | Phân loại riêng. |

**Nhận định:** đây là tài liệu hữu ích nhất trong bốn video để học diễn xuất người và nối cảnh đời thường với vi mô. Giá trị không nằm ở việc cho mắt chớp liên tục, mà ở chọn đúng đối tượng nhìn, tay kiểm tra gì, thân tựa vào đâu và hậu quả của sự kiện vừa xảy ra.

## 4. Virotherapy — hành động mở đầu, giải thích ngược và cân nhắc cuối

Bằng chứng: [sheet cũ 1](../../../research/animation-reference/0NY2gAftzJE/sheet-1.jpg), [manifest mới](../../../research/animation-reference/timeline-review-2026-11-13/virotherapy/manifest.json). Đã mở bốn sheet cũ và năm sheet mới.

| Khoảng | Nội dung và hình quan sát | Cách áp dụng |
|---|---|---|
| 00:00–00:29 | Kim xuyên vào mô, nhiều tác nhân, rồi giới thiệu nhân vật qua màn hình trong bối cảnh sản xuất video. | Cho thấy hành động trung tâm ngay đầu; sau đó cung cấp ai và vì sao, thay vì mở bằng định nghĩa dài. |
| 00:29–01:54 | Nhân vật, điều trị trước đó, mô bị ảnh hưởng, biểu tượng tác dụng phụ, khối u trở lại, phòng thí nghiệm và ý định dùng virus. | Tách trạng thái trước/sau bằng quy mô, ánh sáng và quan hệ nhân vật–khối u. |
| 01:54–02:40 | Hồi tưởng nghiên cứu, virus và tế bào bình thường, tác nhân miễn dịch. | Giải thích phản ứng bình thường trước khi đưa ra trường hợp hỏng. |
| 02:40–03:26 | Vùng tế bào ung thư khác màu, hàng rào quanh khối, virus và mảnh vỡ thu hút tác nhân khác. | Giữ hình khác nhau cho ba nhóm; chuyển biến phải thay đổi được ranh giới hoặc hành vi. |
| 03:26–04:33 | Bác sĩ, sơ đồ ba phía, các bệnh nhân khác nhau, hình truyền thuốc và miễn dịch. | Sau cảnh hành động, lùi ra sơ đồ để giải thích vì sao cơ chế không đơn giản. |
| 04:33–05:00 | Nhân vật cùng đồng nghiệp trong lab, nhiều góc nhìn làm việc. | Chuẩn bị hành động bằng vật thể và nguồn lực cụ thể. |
| 05:00–06:23 | Đoạn NordVPN nối từ chữ “virus”, nhiều giao diện và thiết bị. | Đây là sponsor; tách khỏi phần lập luận sinh học. |
| 06:23–06:57 | Nuôi cấy, hỗn hợp tác nhân và hai ống nghiệm để so mức tinh sạch. | Dùng cùng vật chứa, đổi phần bên trong để so sánh; giữ số liệu như phát biểu của nguồn. |
| 06:57–07:28 | Các thẻ virus và thẻ phiên bản khác nhau trên nền sáng. | Chọn thẻ so sánh khi câu chuyện chuyển sang lựa chọn, tránh giữ kiểu “chiến trường” cho mọi loại thông tin. |
| 07:28–07:46 | Montage chuẩn bị, ống tiêm và lịch theo tuần. | Tách quá trình sản xuất khỏi thời gian áp dụng; timeline giúp nén nhiều ngày mà vẫn dễ hiểu. |
| 07:46–08:12 | Kim tiêm và khối u; khối lớn lên, nhiều gai hơn rồi thay đổi; có tín hiệu tua ngược. | Đặt một kết quả bất ngờ trước, sau đó quay lại lý giải. Không dùng phóng to đơn thuần cho biến đổi cơ thể phức tạp. |
| 08:12–08:48 | Trở lại lớp tế bào, các tế bào đổi trạng thái rồi vỡ, hàng rào và tế bào miễn dịch lân cận. | Hiện nguyên nhân theo thứ tự: tác nhân tới → đối tượng đổi → dấu vết thoát ra → bên ngoài phản ứng. |
| 08:48–09:16 | Cận các tế bào miễn dịch phản ứng, ký hiệu báo động, lớp xanh che rồi lộ các silhouette phía sau. | Chuyển cảnh có thể chính là sự thay đổi thông tin: lớp che rút đi làm lộ thứ trước đó bị giấu. |
| 09:16–09:56 | Khung đen rồi trận cảnh rộng, ba nhóm tác nhân, cận tấn công và timeline trở lại. | Cảnh đông vẫn cần phe, hướng và mục tiêu; xen tổng thể với cận để không biến thành particle ngẫu nhiên. |
| 09:56–10:40 | Khối u ở trạng thái mới, virus khác, thẻ lựa chọn, bệnh nhân sốt và phản ứng tiếp. | Dùng lại bộ thẻ đã dạy khi có lựa chọn mới; đổi palette/shape tác nhân để người xem không nhầm vai. |
| 10:40–11:24 | Đồ thị theo tuần, mô trước/sau, khối được đưa vào đĩa, nhân vật và thời gian theo dõi. | Sau ẩn dụ hành động cần trả về thước đo và kết quả cụ thể. Đồ thị phải có đơn vị và thời gian đọc. |
| 11:24–12:28 | Câu hỏi, màn hình phản hồi trái chiều, hai nhân vật, thẻ ưu/nhược và thanh đánh đổi. | Đổi hẳn cách trình bày khi bàn lựa chọn: ít diễn viên hơn, nền sáng hơn, hai phía dễ so sánh. |
| 12:28–13:16 | Các giai đoạn, bệnh nhân/mức độ bệnh và thời điểm điều trị theo lời nguồn. | Hiển thị điều kiện áp dụng thay vì chỉ một cảnh thắng lợi chung. |
| 13:16–14:22 | Nhiều loại tác nhân/thuốc, quay lại nhân vật, thí nghiệm và đường đi tương lai. | Kết luận bằng phạm vi và câu hỏi nghiên cứu; không biến một trường hợp thành lời hứa phổ quát. |
| 14:22–15:14 | Poster, footage sản phẩm, end screen. | Tách phần thương mại. |

**Nhận định:** cấu trúc nổi bật là hành động → kết quả bất ngờ → tua lại cơ chế → đo kết quả → cân nhắc đánh đổi. Ba nhóm tác nhân được đọc nhờ silhouette và màu, không chỉ nhờ nhãn. Đây là nghiên cứu cách kể; không dùng phần mô tả nguồn làm hướng dẫn tự điều trị.

## 5. Bốn đoạn chuyển động kiểm tra bổ sung

Mỗi đoạn dài 12 giây, lấy 24 ảnh ở 2 fps. Chỉ đủ phân tích các trạng thái và diễn tiến lớn; không đủ đo easing, frame tiếp xúc chính xác, chớp mắt ngắn hoặc vận tốc gốc.

### AI, 15:22–15:34: lan truyền màu có nguồn

Ảnh: [A](../../../research/animation-reference/timeline-review-2026-11-13/motion/ai/sheet-1.jpg), [B](../../../research/animation-reference/timeline-review-2026-11-13/motion/ai/sheet-2.jpg).

- Quan sát: cụm đen/đỏ đi trong mạng vàng; gần 15:27 bắt đầu có vùng tím tại điểm chạm. Tím lan lên/xuống cấu trúc rồi sang các nhánh khác. Những cột xa vẫn khác độ sáng.
- Suy luận triển khai: graph gồm node/edge và thời gian kích hoạt riêng, mặt nạ màu chạy dọc nhánh, tách mặt phẳng gần/xa. Không biết tác giả thực sự dùng mask, keyframe hay mô phỏng.
- Bài học: muốn kể sự lan truyền phải có nơi khởi phát và thứ tự, không đổi màu toàn mạng cùng một frame. Khi camera thay đổi, cần giữ được điểm tiếp xúc để người xem theo dõi.

### Death, 08:08–08:20: giải phóng tác nhân và đổi quy mô

Ảnh: [A](../../../research/animation-reference/timeline-review-2026-11-13/motion/death/sheet-1.jpg), [B](../../../research/animation-reference/timeline-review-2026-11-13/motion/death/sheet-2.jpg).

- Quan sát: đầu đoạn cận một tác nhân hình tam giác có nhãn. Sau đó xuất hiện cả nhóm trong túi vàng; đường viền túi biến dạng và có khoảng hở, các tác nhân ra ngoài. Khoảng 08:16–08:17 chuyển sang một tế bào lớn đang biến dạng.
- Suy luận triển khai: asset cận và asset nhóm riêng; path vỏ có trạng thái kín/mở; vật con đổi ràng buộc từ trong túi sang không gian cảnh. Cảnh tế bào sau có lõi/biên/phần nhô ra tách nhau.
- Bài học: thứ tự giải thích là nhận diện vật → vị trí chứa → vỏ hỏng → vật thoát → hậu quả ở tỷ lệ lớn hơn. Đừng bỏ nhịp nhận diện để nhồi thêm chuyển động.

### Personal, 01:00–01:12: phản ứng bác sĩ

Ảnh: [A](../../../research/animation-reference/timeline-review-2026-11-13/motion/personal/sheet-1.jpg), [B](../../../research/animation-reference/timeline-review-2026-11-13/motion/personal/sheet-2.jpg).

- Quan sát: giọt riêng trên nền tối, sau đó cắt sang mặt và găng tay. Miệng đổi từ bình thường sang lo ngại, hai tay đổi vị trí không hoàn toàn đồng pha, đầu/hướng mặt đổi khi kiểm tra. Cuối mẫu miệng nhỏ lại và có trạng thái mắt khép.
- Suy luận triển khai: đầu, tóc, mắt, mày, miệng, hai cánh tay và bàn tay cần điều khiển riêng. Cần nhiều pose tay để hướng lòng bàn tay thay đổi hợp lý.
- Bài học: diễn xuất gắn với việc “kiểm tra giọt đã rơi vào đâu”, không phải cho toàn người lắc theo sin. Mẫu 2 fps không chứng minh chính xác mắt dẫn đầu trước bao nhiêu frame.

### Virotherapy, 09:00–09:12: báo động rồi lộ vùng bị che

Ảnh: [A](../../../research/animation-reference/timeline-review-2026-11-13/motion/virotherapy/sheet-1.jpg), [B](../../../research/animation-reference/timeline-review-2026-11-13/motion/virotherapy/sheet-2.jpg).

- Quan sát: cụm tế bào có màu nóng lên và ký hiệu báo động; khoảng 09:03 chuyển sang các mảng xanh lớn cùng hạt nhỏ. Khoảng trống giữa mảng tăng lên, lộ những silhouette tím và cấu trúc phía sau.
- Suy luận triển khai: nhiều lớp occluder hữu cơ có mask/biến dạng riêng, nền sau có độ tương phản tăng dần; hạt chỉ làm dấu chuyển động.
- Bài học: chuyển cảnh có nghĩa vì cho người xem biết thứ trước đây bị che đã lộ ra. Không cần phủ crossfade lên hai cảnh phức tạp.

## 6. Những điều cần đưa vào cách dựng tiếp theo

| Quyết định | Bằng chứng giúp chọn | Thực hành đề xuất |
|---|---|---|
| Giữ vật thể nối câu chuyện | Folder/cờ của AI; túi truyền của Personal; người dẫn đường của Death | Chọn 1–2 vật xuyên suốt và lập bảng trạng thái trước khi dựng storyboard. |
| Đổi kiểu cảnh theo nhiệm vụ | Virotherapy chuyển từ chiến trường sang đồ thị rồi thanh đánh đổi | Mỗi đoạn ghi rõ nhiệm vụ: trải nghiệm, cơ chế, số lượng, lựa chọn hay kết luận. |
| Chuyển quy mô có mốc | Cổng truyền → cơ thể → mạch → màng → nhân → DNA | Lập chuỗi mốc nhận diện; cận mới phải trả lời điều mà toàn cảnh không nhìn thấy. |
| Dùng khung giữ để đọc | Các câu trích AI và biểu đồ ở hai video ung thư | Đặt nhãn khi hành động chính đã ổn định; cho thời gian đọc theo nội dung, không chia mọi cảnh bằng nhau. |
| Diễn hoạt có nguyên nhân | Giọt rơi → bác sĩ kiểm tra; tiếp xúc → mạng đổi màu | Viết ba trạng thái trước, tác động, sau; chỉ thêm chuyển động phụ sau khi ba trạng thái rõ. |
| Biến dạng nhiều lớp | Túi enzyme, tế bào, khối u | Tách lõi tương đối cứng, màng mềm, appendage và vật bên trong. |
| Phân biệt số đông và cá thể | Swarm AI; miễn dịch phân tán trong Death | Cho một actor tiêu biểu trước, rồi nhân rộng; quay lại cá thể khi cần cảm xúc. |
| Kết thúc bằng điều đã đặt ra | Robot phòng giam; cốc cà phê; nhân vật dẫn đường | Nhắc lại vật/không gian mở đầu với trạng thái mới; tránh thêm cơ chế hoàn toàn mới ở câu cuối. |

Một storyboard mới cần ghi: khoảng lời thoại, nhiệm vụ cảnh, tiêu điểm, chủ thể, hành động, hậu quả, scale, điểm neo nối cảnh, pose cực trị và cách kiểm tra. Độ dài cảnh lấy từ hành động/lời thoại. Không suy ra một “công thức 4 giây/cảnh” từ những video này.

### Đối chiếu với bản thử hiện có trong repo

Đây là nhận xét từ code đã đọc, chưa phải đánh giá playback lại bản render trong lượt này.

- `sequence.py` đã có chín kiểu cảnh khác nhau, nhưng chia đều bốn giây; cần chọn nhịp theo hành động và ý nghĩa thay vì chỉ theo số scene.
- Chuỗi lab → giọt → tế bào → cổng → đường hầm → DNA → mạng → mô → lab có nhiều tỷ lệ, nhưng cần kịch bản giải thích rõ vì sao đi từ DNA sang mạng rồi mô. Đa dạng hình không tự tạo quan hệ nhân quả.
- `animate.py` có chuỗi khớp giữ chiều dài và khóa gốc protein; đây là nền tốt cho tiếp xúc. Nên giữ kiểm tra ràng buộc và mở rộng pose có mục đích.
- Các biến dạng dạng scale/sin hữu ích làm chuyển động phụ, nhưng chưa thay thế được biến dạng cục bộ và diễn xuất như các mẫu mới đã xem.
- Biểu đồ ở cảnh lab cuối cần đại lượng/đơn vị nếu dùng để truyền đạt kết quả thực. Nếu chỉ là hình thử, phải tiếp tục gọi là motion study.

## 7. Những gì chưa thể kết luận

Chưa có playback liên tục hoặc nghe soundtrack; chưa có EDL mọi shot; chưa đo đường cong easing hoặc số key gốc; chưa có bằng chứng về rig/phần mềm toàn bộ pipeline. Footage hậu trường cho thấy người làm và giao diện phần mềm ở một số khoảnh khắc, nhưng không đủ gán mọi cảnh cho một công cụ.

Chưa có CTR, retention, địa lý hoặc lịch sử tăng view trong lượt nghiên cứu này. Vì vậy, các lựa chọn hình ảnh trên là bài học về cách trình bày, không phải nguyên nhân viral đã được chứng minh.

Để đáp ứng đầy đủ yêu cầu **xem/nghe full**, vẫn cần một lượt xem video có âm thanh hỗ trợ toàn thời lượng và ghi phạm vi kiểm tra của công cụ đó. Không đánh dấu bước này hoàn tất chỉ vì FFmpeg đã giải mã tới cuối file.
