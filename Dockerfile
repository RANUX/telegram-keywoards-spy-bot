FROM python:3.11-slim
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip install --user -r requirements.txt
# run app
CMD ["python", "telegram_bot.py"]