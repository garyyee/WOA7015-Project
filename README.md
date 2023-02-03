# WOA7015-Project
This is a group project for WOA7015 course of Advanced Machine Learning

## Group 7
1. Lee Wai Key (17194567)
2. Nasib Ullah (S2019652)
3. Yuhuan He (S2165922)
4. Gary Siew Wah Yee (S2190954)


## ABSTRACT
<p align="justify">
To investigate the feasibility of estimating heart rate in neonates using respiratory signals, as a non-intrusive alternative to ECG and pulse oximetry as a non-invasive alternative method for estimating heart rate in neonates. samples of neonatal respiratory (RESP) and electrocardiography (ECG) signals were collected and analyzed to extract features related to heart rate. Required preprocessing, subsampling and denoising were performed, and transformed all the data to the same scale, so the given data helped the model to learn well, and the machine learning model was then trained to estimate heart rate using these features. the final output of this model is estimating the accurate heart rate of neonates using respiratory signals. The performance of the proposed method was evaluated by comparing the estimated heart rate with the reference heart rate obtained from ECG. The results showed that there is a strong correlation between the respiratory signal and heart rate in neonates and that the proposed method can provide reliable and accurate estimates of heart rate with a low mean absolute error and high correlation coefficient with the reference heart rate. These findings suggest that the proposed method could be a valuable non-invasive alternative for measuring heart rate in neonates, which could reduce the risk of skin damage in premature infants and improve the accuracy of heart rate measurements. However, it is our further plan to research furthermore on this method to validate these findings on a larger scale and real-time usage.</p>
<p align="center">
<br><img src="picture/Neonate.png" width="200">     <img src="picture/ECG.png" width="200"> </p>



## Problem Statement
Heart and respiratory rates are crucial clinical indicators in monitoring a person’s health status, especially the neonates. The common methods of measuring heart rate in neonates are electrocardiography (ECG) and pulse oximetry, which are intrusive methods. 

## Objective
To investigate the feasibility of estimating heart rate in neonates using respiratory signals, as a non-intrusive alternative to ECG and pulse oximetry.

## Literature Review
1. Non-invasive sensor methods used in monitoring newborn babies after birth, a clinical perspective.
2. Heart Rate Monitoring in Newborn Babies: A Systematic Review.
3. Wearable technology for baby monitoring: a review.
4. EEG, behavioural and physiological recordings following a painful procedure in human neonates.

## Conclusions
1.  We constructed a high-precision machine learning model to predict neonatal heart rate by characterizing the relationship between respiratory signals and the heart rate of newborns.
2. By comparing with the reference heart rate from ECG, our method has a low mean absolute error and a good correlation coefficient score with the reference heart rate.
3. This method may be a valuable non-invasive alternative method for measuring neonatal heart rate.
4. More sample data are needed to increase the generalization ability of the model.

## Model Result
<p align="center">
<br><img src="picture/Model Result.png">
