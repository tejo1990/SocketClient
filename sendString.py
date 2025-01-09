import socket
import json
from pprint import pprint

def receive_json_data(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # 서버에 연결
            s.connect((host, port))
            print(f"서버 {host}:{port}에 연결되었습니다.")

            # 'data' 문자열 전송
            input_string = input("전송할 문자열을 입력하세요: ")
            s.sendall(input_string.encode())
            print(f"'{input_string}' 문자열을 서버로 전송했습니다.")

            # 서버로부터 데이터 수신
            received_data = b''
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                received_data += chunk

            # 받은 데이터를 JSON으로 파싱
            json_data = json.loads(received_data.decode('utf-8'))
            print("\n받은 JSON 데이터:")
            pprint(json_data)  # 보기 좋게 출력

        except json.JSONDecodeError:
            print("받은 데이터를 JSON으로 파싱할 수 없습니다.")
            print("받은 원시 데이터:", received_data.decode('utf-8'))
        except ConnectionRefusedError:
            print(f"서버 {host}:{port}에 연결할 수 없습니다.")
        except Exception as e:
            print(f"오류 발생: {e}")

if __name__ == "__main__":
    SERVER_HOST = 'localhost'  # 서버 IP 주소
    SERVER_PORT = 7775         # 서버 포트 번호

    receive_json_data(SERVER_HOST, SERVER_PORT)
    
    # 사용자 입력을 기다려 프로그램이 즉시 종료되지 않도록 함
    input("\n프로그램을 종료하려면 Enter 키를 누르세요...")
