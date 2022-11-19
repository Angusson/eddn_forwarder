from python:3.9

run apt update && apt upgrade -y
# run apt install -y \
# 	python3-dev \
# 	build-essential \
# 	libgl1

workdir /app
copy requirements.txt .
run pip install -r requirements.txt

copy . .

cmd ["python", "src/eddn_forwarder.py"]
