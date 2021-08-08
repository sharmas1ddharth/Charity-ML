## Project: Finding Donors for CharityML

In this project, I have applied several Machine learning models to accurately model individual's income. I have choosen best candidate model based on preliminary result using GridSearchCV to further optimize algorithm to best model the data. Goal of implementation is to predict if Individual makes more than 50K or less. This sort of task arise in an non profit setting where organisation surive on donations.
Having this prediction would help non profit to better understand how large of donation to request or whether or not to reach out to begin with.


## Technologies:


This project requires **[Python 3.x](https://www.python.org)** and the following Python libraries installed:


- [NumPy](http://www.numpy.org/)

- [Pandas](http://pandas.pydata.org)

- [matplotlib](http://matplotlib.org/)

- [scikit-learn](http://scikit-learn.org/stable/)



You will also need to have software installed to run and execute an 
[iPython Notebook](http://ipython.org/notebook.html)







## Data


The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Census+Income). The datset was donated by Ron Kohavi and Barry Becker, after being published in the article "Scaling Up the Accuracy of Naive-Bayes Classifiers: A Decision-Tree Hybrid". You can find the article by Ron Kohavi [online](https://www.aaai.org/Papers/KDD/1996/KDD96-033.pdf).


**Features**

- `age`: Age

- `workclass`: Working Class (Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked)

- `education_level`: Level of Education (Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, 
   Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool)

- `education-num`: Number of educational years completed
- `marital-status`: Marital status (Married-civ-spouse, Divorced, Never-married, Separated, 
   Widowed, Married-spouse-absent, Married-AF-spouse)

- `occupation`: Work Occupation (Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, 
   Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces)

- `relationship`: Relationship Status (Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried)

- `race`: Race (White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black)

- `sex`: Sex (Female, Male)

- `capital-gain`: Monetary Capital Gains

- `capital-loss`: Monetary Capital Losses

- `hours-per-week`: Average Hours Per Week Worked

- `native-country`: Native Country (United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, 
   Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, 
   Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, 
   Hong, Holand-Netherlands)

**Target Variable**
- `income`: Income Class (<=50K, >50K)


## Implementation
- Starting with data exploration I analysed all features and data type of columns (Categorical, Ordinal or binary). 
- After analyzing data, I found that there is skewed data. So, I did some data preprocessing to transform skewed continous features to log distribution to spreadout extreme values. 
- After this scaling is done on features using minmaxscalar to achieve normalization. This ensures each feature is treated equally when applying 
  supervised learning.
- All categorical features are one hot encoded to numerical values before feeding to ML model.  
- Cross Validation train_test_split is done on features and income to prepare training and testing datasets.
- Model benchmark is established using Naive predictor.
- Model performance metrics is defined accuracy and F-beta score.
- Various supervised ML alogrithm from scikit learn are used to train model. 
- Results are evaluated and performance metrics for these supervised learning models are plotted. 
- Best model is choosen and further tunned to optimize metrics to get final model evaluation.
- At last Feature Importance and relevence is discussed and implemented to show how feature selection can make difference. 


## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.
3. Data processing/transformation scripts are being kept [here]
4. etc...
5. Follow setup [instructions](Link to file)
