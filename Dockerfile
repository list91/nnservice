FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
libglib2.0-0 \
libgl1 \
python3-pip

# RUN pip install fastapi==0.111.1 \
# opencv_python==4.10.0.84 --break-system-packages
# RUN pip install --upgrade pip --break-system-packages
# RUN pip install fastapi opencv_python --break-system-packages

COPY . /app

WORKDIR /app

RUN pip install "uvicorn[standard]" --break-system-packages

# RUN pip install tensorflow==2.17.0 tensorflow_hub==0.16.1 --break-system-packages
RUN pip install -r requirements.txt --break-system-packages
    

# RUN apt install python3.12-venv -y
# RUN . venv/bin/activate
# CMD ["source", "venv/bin/activate", "&&", "uvicorn", "main:app", "--host", "172.17.0.2"]
CMD ["uvicorn", "main:app", "--host", "172.17.0.2"]


# Открываем порт 8000 для внешнего доступа
# EXPOSE 8000

