#  :oncoming_automobile: Vehicle_Claim_Fraud_Detection :money_with_wings:

#### Created by Matheus Laranjeira (https://github.com/mathlaranjeira __and__ https://www.linkedin.com/in/matheus-laranjeira-m-sc-1387a859/) & Guilherme Origo Fulop (https://github.com/GuilhermeFulop __and__ https://www.linkedin.com/in/guilherme-origo-fulop/).

<img width="500" height="300" style="display: block; margin-left: auto; margin-right: auto" src="https://www.supergraph.nl/wp-content/uploads/2015/12/insurancefraud.png">

## :blue_book: Intro
Insurance fraud, as defined by the California Department of Insurance, occurs when someone knowingly lies to obtain a benefit or advantage to which they are not otherwise entitled or someone knowingly denies a benefit that is due and to which someone is entitled. According to the Coalition Against Insurance Fraud, insurance fraud, as a whole, occurs in about 10% of property-casualty insurance losses and steals at least $308.6 billion every year from consumers in the United States. Medical care fraud alone accounts for an estimated cost of \$60 billion every year.

Vehicles are also an essential source of insurance fraud, which consists of false or exaggerated claims related to property damage or personal injuries. Some common fraud practices are staged accidents, phantom passengers or exaggerated injuries. With that said, this project focuses on vehicle fraud claims.

## :book: Dataset Information

### :balance_scale: Unbalanced Data

The main characteristic of this dataset is the difference between cases that weren't fraud and those that were fraud. Frauds represent only 6% of the entire dataset. If we train a model this way, the accuracy will be very high, because the model will hit only the not fraud cases and just a few frauds would be prevented. This is not ideal for us, we want a model that predicts correctly almost all frauds in our dataset!

![image](https://user-images.githubusercontent.com/103580606/196768827-425f7c43-fa01-49c1-9022-444091ee35c9.png)

### :bar_chart: Balancing the data

We will show only the better result, which was the undersampling method. for this, we used __ClusterCentroid__, that uses k-means to identify the cluster centroids and replace some values by the centroid value.

![image](https://user-images.githubusercontent.com/103580606/196771303-a74281e3-a6ce-40f1-ba96-7021edb374fc.png)

By the image above, we can see that, at the end, the number of not fraud is equal to the fraud amount.

### :computer: Machine Learning Model

Our best model was __RandomForestClassifier__, first, we have made the hyperparameter tunning, to get the better parameters which will give us the best result.

![image](https://user-images.githubusercontent.com/103580606/196772073-79bfd00b-07f0-42f7-afac-83d847aaac8f.png)

With the model ready, we plot the confudion matrix, and we can see that only 5 frauds were wrongly, while 262 were correctly predicted, a hit rate of 98%!

![image](https://user-images.githubusercontent.com/103580606/196772364-fb2cb5b1-3528-487c-82d8-5ba070c41d21.png)

By some estimatives, by our method, the insurance company could save US$ 434022.47 per year, a 97.75% of ecconomy!

We also make a deploy of the model, you can check it here: https://guilhermefulop-vehicle-claim-fraud-detection-deploymain-hcj60e.streamlitapp.com/

###  :heavy_check_mark: Don't forget!

Please, check out our project, we tested some hypotesis, over and undersampling methods, outilier detection and many more techiniques!
