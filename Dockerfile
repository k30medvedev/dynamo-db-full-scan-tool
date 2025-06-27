FROM python:3.13-slim

WORKDIR /app

COPY *.py ./
COPY requirements.txt ./
COPY styles.css ./
COPY VERSION ./
COPY pages/ pages/

RUN pip install --no-cache-dir -r requirements.txt

ARG VERSION
ENV APP_VERSION=${VERSION}

ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ENABLECORS=false

EXPOSE 8501

CMD ["streamlit", "run", "Home.py"]

ENV STREAMLIT_LOG_LEVEL=debug