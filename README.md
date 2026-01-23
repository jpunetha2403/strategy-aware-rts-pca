# strategy-aware-rts-pca
# Beyond Performance Symmetry: Strategy-Aware Movement Analysis for RTS

This repository contains the analysis code used to demonstrate how outcome-equivalent movements can be achieved using divergent motor control strategies, exposing limitations of outcome-based Return-to-Sport (RTS) assessments.

## Overview
Traditional RTS metrics focus on performance outcomes (e.g., symmetry indices), but fail to capture how movements are executed. Using unsupervised dimensionality reduction and clustering on wearable sensor data, this work illustrates the dissociation between movement magnitude and movement control — referred to as the *illusion of symmetry*.

## Dataset
This analysis uses the publicly available **UCI Human Activity Recognition (HAR)** dataset.

Dataset link:  
https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

## Methods
- Feature standardisation
- Principal Component Analysis (PCA)
- Unsupervised k-means clustering
- Silhouette score validation
- Strategy interpretation using magnitude–control dissociation

## Repository Structure
- `notebooks/` — End-to-end reproducible analysis
- `src/` — Modular analysis functions
- `figures/` — Example outputs used in the presentation
- `data/` — Placeholder (raw data not redistributed)

## Key Concept
Passing a functional performance test does not guarantee symmetric movement strategy. True RTS readiness requires symmetry in both outcome and control.

## Reproducibility
All analyses were performed using Python 3.10 and standard scientific libraries. See `requirements.txt`.

## License
This project is released under the MIT License.
