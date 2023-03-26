FROM python:3.11-slim

# Install zsh
RUN apt-get update && apt-get install -y zsh

WORKDIR /app

# Update this line to match the new file structure
COPY ./app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

# Update this line to match the new file structure
COPY ./app /app

EXPOSE 5001

CMD ["python", "app.py"]
