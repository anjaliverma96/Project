# Project Charter 

**Vision**: Engage people looking for entertainment and fun, in humor with jokes and content that
					match their interests. Help them discover jokes they might not have found otherwise
					and ultimately spread happiness thereby increasing user base for the app.

**Mission**: Build an app for joke recommendations and drive app usage by enabling users to rank jokes on a visual analog scale. Produce updated recommendations based on their inputs(i.e. explicit preferences) using collaborative filtering(i.e. similarity to other users) recommendation model trained on Jester Dataset.

**Success criteria**: 
- Machine Learning Performance Metric : **AUC** - Area Under the ROC Curve that plots true
positive rate against false positive rate. This metric was chosen for model evaluation since we are concerned with whether users like the recommended joke or not rather than the accuracy of predicted user ratings for a joke. For the model to be successful, the goal would be to achieve a mean AUC score (across all users in test set) in the range 0.7 to 0.9 (though this is subject to change and can be ascertained only after optimizing/tuning model parameters ).

- Business Performance Metric : **Engagement** ~ measured by how frequently users come back to the app. Success is defined as having achieved a million plus downloads with 80% of the users visiting the app atleast once a day and is indicative of personalized recommendations that suit the sense of humor of the users.

# Planning
## Theme 1 
         

 - **Epic 1** : **Model Building**
	 -	Story 1 : **Define the model objective** ~ why the model is being built and understand the end goal the model would achieve
	 -	Story 2 : **Gather the data** ~ Extract interaction matrix between users and jokes from the Jester dataset and transform data into format expected for a recommendation system
	 - Story 3 : **Data Cleaning** ~ Handle any inconsistencies or missing values and prepare the data for modeling
	 - Story 4 : **Feature Engineering** ~ Explore and create new attributes about the user-joke interaction that could potentially be used in the recommender
	 - Story 5 : Split the data into **training** and **test** sets and train 2 different models
		-Story 5.1 : Train a **Baseline** model whose underlying algorithm is to recommend items that are popular
		-Story 5.2 : Train a **Collaborative Filtering** model using **Lightfm** package in python where the underlying algorithm is to suggest jokes that similar users like
	 
 - **Epic 2** : **Model Selection and Evaluation**
	 - Story 1 : Decide on loss functions and metrics to evaluate performance of the two models
	 - Story 2 : Tune/Optimize model hyperparameters using cross-validation to arrive at the best fitted model
	 - Story 3 : Evaluate each model using the decided metrics (such as AUC) using both the training and test datasets. Select the model with the best performance metric(highest AUC) for the test set

 - **Epic 3** : **Model Validation, Reproducibilty and Collaboration**
	 - Story 1 : **Logging** ~ Manage complexity, communicate code to potential collaborators or developers, and debug software
	 - Story 2 : Write **Unit Tests** and **Configure reproducibility tests** that can be run to test each stage of model development
	 - Story 3 : **Version Control**: Create a Github repository for potential collaboration
	 - Story 4 : **Documentation**: Make code readable and reproducible by documenting code   	
 - **Epic 4** : **App development**
	 - Story 1 : Present the app and results of recommender to users with the help of Flask (deployed on AWS). (Put code in a scalable environment)
	 - Story 2 : Update app with feedback from users
	

# Backlog 

 - Theme1.Epic1.Story1 - 2 points
 
 - Theme1.Epic1.Story2 -  2 points
 - Theme1.Epic1.Story3 -  4 points
 - Theme1.Epic1.Story4 -  4 points
 - Theme1.Epic1.Story5.1 - 4 points
 - Theme1.Epic1.Story5.2 - 4 points
 - Theme1.Epic2.Story1 -  2 points
 - Theme1.Epic2.Story2 -  4 points
 - Theme1.Epic2.Story3 -  1 point
 - Theme1.Epic3.Story1 -  4 points
 - Theme1.Epic3.Story2 -   8 points
 - Theme1.Epic3.Story3 -   2 points
 - Theme1.Epic3.Story4 -   2 points
 - Theme1.Epic4.Story1 -   8 points

# Icebox	

 - Theme1.Epic4.Story2
