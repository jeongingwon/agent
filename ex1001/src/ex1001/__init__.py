# def main() -> None:
#     print("Hello from ex1001!")

# from 같은경로의 app 파일
# import app 파일 안에있는 main()    

from .app import main

__all__ =["main"]

#  프로젝트를 초기화 해준다