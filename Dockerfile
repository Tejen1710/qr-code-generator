FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m -u 10001 -s /sbin/nologin myuser \
    && mkdir -p /app/logs /app/qr_codes \
    && chown -R myuser:myuser /app

COPY --chown=myuser:myuser . .

USER myuser

ENTRYPOINT ["python", "main.py"]
CMD ["--url", "http://github.com/Tejen1710"]
