FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir streamlit

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
