#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
serve.py — Web server đơn giản cho Ngân Hàng Câu Hỏi Toán Lớp 9
Chạy: python serve.py
Sau đó mở: http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
import threading

PORT = 8000
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, fmt, *args):
        # Gọn log, bỏ qua các request tài nguyên nhỏ
        if '.css' in args[0] or '.js' in args[0] or '.ico' in args[0]:
            return
        print(f"  [{self.client_address[0]}] {args[0][:80]}")

def open_browser():
    import time
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    print("=" * 55)
    print("  📐 Ngân Hàng Câu Hỏi Toán Lớp 9 – Lạng Sơn")
    print("=" * 55)
    print(f"  ✓ Server đang chạy tại: http://localhost:{PORT}")
    print(f"  ✓ Thư mục phục vụ:      {DIR}")
    print(f"  → Trình duyệt sẽ tự mở...")
    print(f"  → Nhấn Ctrl+C để dừng server")
    print("=" * 55)

    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server đã dừng.")
