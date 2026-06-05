import http.server
import json
import os
import sys
import mimetypes
import urllib.parse

PORT = 5500
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(SCRIPT_DIR, 'audio')
AUDIO_EXTENSIONS = {'.mp3', '.mp4', '.wav', '.flac', '.ogg', '.aac', '.m4a', '.wma', '.webm', '.opus'}

class MusicHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SCRIPT_DIR, **kwargs)

    def do_GET(self):
        if self.path == '/api/songs':
            self.handle_api_songs()
            return

        if self.path.startswith('/audio/'):
            self.handle_audio_range()
            return

        super().do_GET()

    def handle_api_songs(self):
        songs = []
        if os.path.isdir(AUDIO_DIR):
            for filename in os.listdir(AUDIO_DIR):
                ext = os.path.splitext(filename)[1].lower()
                if ext in AUDIO_EXTENSIONS:
                    songs.append(filename)
            songs.sort()

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({'songs': songs}, ensure_ascii=False).encode('utf-8'))

    def handle_audio_range(self):
        decoded_path = urllib.parse.unquote(self.path)
        file_path = os.path.join(SCRIPT_DIR, decoded_path.lstrip('/'))

        if not os.path.isfile(file_path):
            self.send_error(404, 'File not found')
            return

        file_size = os.path.getsize(file_path)
        content_type, _ = mimetypes.guess_type(file_path)
        if content_type is None:
            content_type = 'audio/mpeg'

        range_header = self.headers.get('Range')

        if range_header:
            range_str = range_header.replace('bytes=', '')
            parts = range_str.split('-')
            start = int(parts[0]) if parts[0] else 0
            end = int(parts[1]) if len(parts) > 1 and parts[1] else file_size - 1

            if start >= file_size:
                self.send_response(416)
                self.send_header('Content-Range', f'bytes */{file_size}')
                self.end_headers()
                return

            end = min(end, file_size - 1)
            content_length = end - start + 1

            self.send_response(206)
            self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
        else:
            start = 0
            content_length = file_size
            self.send_response(200)

        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(content_length))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        with open(file_path, 'rb') as f:
            f.seek(start)
            remaining = content_length
            chunk_size = 64 * 1024
            while remaining > 0:
                data = f.read(min(chunk_size, remaining))
                if not data:
                    break
                self.wfile.write(data)
                remaining -= len(data)

    def log_message(self, format, *args):
        if '/api/songs' in str(args):
            return
        super().log_message(format, *args)


if __name__ == '__main__':
    print(f'=' * 50)
    print(f'  音乐播放器服务器已启动')
    print(f'  地址: http://localhost:{PORT}')
    print(f'  歌曲文件夹: {AUDIO_DIR}')
    print(f'  支持格式: {", ".join(sorted(AUDIO_EXTENSIONS))}')
    print(f'  按 Ctrl+C 停止服务器')
    print(f'=' * 50)

    server = http.server.HTTPServer(('0.0.0.0', PORT), MusicHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n服务器已停止')
        server.server_close()
