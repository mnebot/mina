**Ngôn ngữ: Tiếng Việt · [Quay lại trang chọn ngôn ngữ](../readme.md)**

# Trợ lý nhà thông minh đa ngôn ngữ


**Đọc bằng:** [Tiếng Việt](Read.vi.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Dự án này mô tả cách triển khai một hệ sinh thái nhà thông minh cục bộ trên Raspberry Pi, đi kèm trợ lý giọng nói đa ngôn ngữ.

## Nguồn gốc tên Mina

**Mina** bắt nguồn từ gốc từ *minna* trong tiếng Germanic cổ, có nghĩa là “ký ức”, “tình cảm” hoặc “kỷ niệm”. Tên này cũng xuất hiện trong những ngôn ngữ khác: trong tiếng Ba Tư, *mīnā* gắn với “ánh sáng” hoặc “thủy tinh xanh”; trong tiếng Nhật, *mina* có nghĩa là “mọi người” hoặc “tất cả cùng nhau”.

Những cách diễn giải này tượng trưng cho **ký ức chung và cộng đồng**, những giá trị phù hợp với một trợ lý đồng hành và hỗ trợ cuộc sống thường nhật trong gia đình.

Về âm thanh, Mina là một cái tên nhẹ nhàng nhưng rõ ràng. Tên được phát âm theo từng âm tiết là `Mi-na` và ít có khả năng bị nhầm với những từ thường dùng trong gia đình.

## Mục tiêu

Xây dựng một hệ thống nhà thông minh riêng tư, đáng tin cậy và nhanh chóng, cho phép điều khiển các thiết bị trong nhà bằng lệnh thoại mà không bắt buộc phải phụ thuộc vào dịch vụ đám mây.

Kiến trúc kết hợp:

- Xử lý cục bộ các lệnh nhà thông minh và bảo vệ quyền riêng tư.
- Dùng Ollama để xử lý cục bộ các câu hỏi thông thường.
- Dùng mô hình đám mây cho câu hỏi phức tạp và thông tin cập nhật.

## Phần cứng

- Khuyến nghị Raspberry Pi 5 với RAM 8 GB. Khả năng tương thích có giới hạn đến Raspberry Pi 3B+.
- Dùng SSD NVMe, không dùng thẻ SD. Khả năng hỗ trợ thẻ SD có giới hạn.
- Micro và loa USB hai chiều.
- Các thiết bị nhà thông minh tương thích với Zigbee, Matter, Philips Hue hoặc Wi-Fi cục bộ.
- Làm mát chủ động để tránh giảm hiệu năng do quá nhiệt.

## Kiến trúc

1. Home Assistant OS quản lý thiết bị và các quy trình tự động hóa.
2. openWakeWord phát hiện từ đánh thức ngay trên thiết bị.
3. Whisper chuyển lời nói thành văn bản bằng ngôn ngữ đang hoạt động thông qua Wyoming.
4. Bộ xử lý ý định thực thi các lệnh nhà thông minh cục bộ.
5. Piper tổng hợp câu trả lời bằng giọng nói tiếng Catalan.
6. Ollama trả lời câu hỏi thông thường mà không gửi dữ liệu lên Internet.
7. Chỉ những yêu cầu được nêu rõ là cần AI nâng cao mới được gửi đến AI đám mây.

## Các tính năng dự kiến

- Điều khiển đèn, ổ cắm, điều hòa, rèm và các thiết bị khác bằng giọng nói.
- Bí danh đa ngôn ngữ.
- Bộ hẹn giờ điều khiển bằng giọng nói.
- Tra cứu thời tiết tại địa phương.
- Phát và điều khiển nhạc.
- Chuyển dự phòng riêng tư sang mô hình Ollama.
- Nhận diện người nói qua giọng nói.
- Ghi nhớ ngữ cảnh dài hạn.
- Tùy chọn chuyển yêu cầu sang mô hình AI đám mây.
- Sao lưu và giám sát hiệu năng.

## Nguyên tắc thiết kế

- Các lệnh nhà thông minh phải hoạt động ngay cả khi không có kết nối Internet.
- Ưu tiên bộ xử lý ý định cục bộ hơn LLM.
- Ưu tiên xử lý dữ liệu âm thanh và các cuộc trò chuyện riêng tư ngay trên thiết bị.
- Chỉ dùng mô hình đám mây cho yêu cầu được nêu rõ hoặc câu hỏi phức tạp, và chỉ khi người dùng chủ động bật tính năng này trong lúc cấu hình trợ lý.
- Hệ thống phải duy trì nhiệt độ và độ trễ ổn định khi hoạt động liên tục dưới tải.

## Trạng thái dự án

Hiện dự án được xác định dưới dạng danh sách công việc chức năng. Các cấu hình cụ thể, quy trình tự động hóa và tập lệnh triển khai sẽ được bổ sung khi các câu chuyện người dùng hoàn tất.
