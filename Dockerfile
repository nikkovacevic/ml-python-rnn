FROM python:3.8-slim

# install required libraries
RUN pip install --upgrade pip
RUN pip install numpy pandas scikit-learn keras tensorflow flask gunicorn

# copy the application code
COPY . /0projekt
WORKDIR /0projekt

#copy the scaler file
COPY scaler.save /0projekt

#copy the model file
COPY model.h5 /0projekt

# set the entrypoint
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8000", "app:app" ]