@echo off
REM 가상 환경을 사용하는 경우 가상 환경 활성화 (필요 시)
REM call D:\2023\crawl\env\bldg_down\Scripts\activate.bat
cd /d "D:\2023\crawl\env\bldg_down\Scripts\"
call activate.bat

REM Python 스크립트가 있는 디렉터리로 이동
cd /d "D:\2023\crawl\"

REM Python 스크립트 실행
python bldg_download.py

REM call D:\2023\crawl\env\bldg_down\Scripts\activate.bat
cd /d "D:\2023\crawl\env\bldg_down\Scripts\"
call deactivate.bat

REM 스크립트 실행 후 창 유지 (원하지 않으면 제거 가능)
pause
