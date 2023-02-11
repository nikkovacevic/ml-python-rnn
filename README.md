# GRU Neural Network Web Service

This repository contains a Flask web service that uses a GRU neural network to make predictions.

## Introduction

This project was developed as a part of a school course on machine learning (RAZVOJ INTELIGENTNIH REŠITEV S STROJNIM UČENJEM). The goal of this project was to build a recurrent neural network for predicting time series, based on weather information and to use the trained model as a web service.

## Contents

- `projekt.ipynb`: A Python Notebook showing the process of data preprocessing, feature engineering, data scaling, spliting the dataset into time series, building and training the model.
- `app.py`: A Python script that implements the web service using the Flask framework.
- `scaler.save`: Saved scaler object used to transform input data.
- `model.h5`: The trained GRU neural network saved as a Keras model.
- `rirsu.postman_collection.json`: Postman Collection file for testing requests.

## Usage

A Docker image of the Flask web service is available on [Docker Hub](https://hub.docker.com/repository/docker/nkovacevic/gru-webservice/general). You can pull the image using the following command:

`docker pull nkovacevic/gru-webservice:latest`

You can run the web service using the following command: 

`docker run -p 5000:5000 nkovacevic/gru-webservice`

This will start the Flask web service on port 5000. Postman request is available in the `rirsu.postman_collection.json` file.
