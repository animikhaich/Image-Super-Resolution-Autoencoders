# Image Super Resolution Using AutoEncoders

## Introduction & Purpose

This repository was created as an attempt to perform Image Super Resolution using AutoEncoders.

It is well known that GANs are more suited towards applications such as Image Super Resolution, while AutoEncoders are not. 

A very well-written article comparing GANs and AutoEncoders is written by Matthew Stewart, and the same can be found here: [GANs vs. Autoencoders: Comparison of Deep Generative Models](https://towardsdatascience.com/gans-vs-autoencoders-comparison-of-deep-generative-models-985cf15936ea)

However, I was still curious to see the results myself as the question remains: What happens if we do attempt to train?

> I am keeping the documentation brief as this is a Trail Project. Just for a better understanding :)

## Dataset(s)

I attempted to use two datasets:
- [Gender Clssification Dataset (Kaggle)](https://www.kaggle.com/cashutosh/gender-classification-dataset) - I combined male and female images together for this application
- [COCO 2017 Dataset](https://cocodataset.org) - I just used the images

## Dependencies

- Python 3.7.4
- Tensorflow 2.4
- Numpy 1.19.5
- Matplotlib 3.3.4
- OpenCV 4.5.1.48

