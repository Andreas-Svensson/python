# **Workflow for AI-Projects** 

*Report by Andreas Svensson*

This report explores a theoretical approach to AI-projects using the machine learning algorithm linear regression. In order to narrow the scope and reach a more easily understood explanation, a specific example of predicting house prices with the algorithm is used.

Table of Contents

1. Linear Regression to Predict House Prices  
    1.1  Algorithm Explanation  
    1.2  Algorithm Usage
2. Data Gathering 
3. Formatting Data  
    3.1 Raw Data  
    3.2 Data Preparation  
4. Visualizing and Using Output Data  
    4.1 Presenting Data  
    4.2 Importance of Selecting the Right Data  
5. Conclusion  

## **1.0 Linear Regression**
---
Definition 

Linear regression is a machine learning algorithm which finds likeliness between two or more variables... 

Below follows a more general description which will later be used as a specific example to predict house prices 

### **1.1 Algorithm Explanation** 
The algorithm uses the following formula:  

**Y = a + bX\***

where:  
**Y = Dependent variable**  
The variable being predicted by the algorithm, house price in this example  

**X = Explanatory variable**  
Variable(s) attempting to "explain" the target variable (Y)  
In this example it could be parameters such as living area, amount of floors, etc  

**a = Baseline value**  
Value of the target variable (Y) when explanatory variables (X) are 0  
In this example, the house price when selected variables living area, amount of floors, etc are 0. In other words, the price of a house without any features, the cheapest a house can possibly be.  

**b = Coefficient**  
How much explanatory variables (X) adds to the target variable (Y)  
In this example, how much the price is affected based on living area, amount of floors, etc


### **1.2 Algorithm Usage** 


*Example from datascience*
```py
**IN**:
model3 = lm(price ~ sqft_living + floors + yr_built, data = data)
summary(model3)**OUT**:
Call:
lm(formula = price ~ sqft_living + floors + yr_built, data = data)Residuals:
     Min       1Q   Median       3Q      Max 
-1669759  -134816   -16331   102089  4092350Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
(Intercept)  5.595e+06  1.304e+05   42.92   <2e-16 ***
sqft_living  2.948e+02  2.018e+00  146.10   <2e-16 ***
floors       7.517e+04  3.731e+03   20.15   <2e-16 ***
yr_built    -2.933e+03  6.767e+01  -43.35   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1Residual standard error: 250800 on 21609 degrees of freedom
Multiple R-squared:  0.5335, Adjusted R-squared:  0.5334 
F-statistic:  8237 on 3 and 21609 DF,  p-value: < 2.2e-16
```

**r2 (R-squared)** - 0.5335  
Describes how much of the target variable is explained by the model (from 0 to 1) 

**Adjusted R-squared** - 0.5334  
Should be used instead when multiple explanatory variables are used in the model 

**Residuals**  
TODO Include image for explanation 

**Coefficients**  
The field "Estimate" gives us the a and b values, where Intercept is the a, and the explanatory variables is b(x*) 

**p-value** - 2.2e-16  
Indicates confidence level of estimation


## **3.0 Data Gathering** 

Below follows ways to gather data, and how that data can be formatted in order to achieve optimal results using linear regression. 

If you are employed by a company to solve a task, they might often have the data for you to use.  
Otherwise, some commonly used places for finding datasets to use in machine learning are: 

Google dataset search  
Kaggle  
GitHub  
Government sources  
FiveThirtyEight  
data.world  

If none of the above examples are sufficient, and you are able to generate data yourself, you can also make your own datasets based on generated data. This requires a case where data can be readily created and fed back into the algorithm by the application you are using.

## **4.0 Formatting Data**

Significance of good data in ML 

### 4.1 Raw Data 

Usually has various inconsistencies that need to be resolved before moving on to the next step.

- Missing values 

- Different file formats 

- Outlying data points 

- Inconsistencies in variable values 

- Irrelevant feature variables 

### 4.2 Data Preparation 

- Data transformation 

- Exploratory data analysis  
    Pandas, matplotlib, and seaborn Libraries  

- Data cleaning  
    Pandas, matplotlib, and seaborn Libraries  

- Feature selection  

- Feature engineering  
    libraries such as NumPy allow users to implement mathematical operations effortlessly and perform feature engineering efficiently  

**Scaling** 

```py
def MinMaxScaler(raw_data): # scales values of a list to between 0 and 1

    # finding xmax and xmin values for below equation
    x_max = max(raw_data)
    x_min = min(raw_data)

    # scaling data to between 0-1 using z = (x - xmin) / (xmax - xmin)
    scaled_data = [(x - x_min) / (x_max - x_min) for x in raw_data]

    #scaled_data.sort()
    # return scaled data
    return scaled_data

# raw data containing unscaled values
fruit_weight = [15, 18, 12, 10]
fruit_cost = [1, 2, 3, 5]

# calling scaler function to get scaled values between 0 and 1 returned
print(MinMaxScaler(fruit_weight))
print(MinMaxScaler(fruit_cost))
```

**Tools** 

As is shown in the above steps of data preparation, python is a good tool to utilize for analysing and preparing data for going into a machine learning algorithm. It can also be uesd to implement the machine learning models and work with those, and the output from them.  

Some other useful tools for data preparation are:  
Tableau  
Power BI  
Alteryx  
SAP Data Intelligence Cloud 

## **5.0 Visualizing and Using Output Data**
--- 

### 5.1 Presenting Data 

Text clustering 

Network diagram 

### 5.2 Importance of selecting the right data 

## **6.0 Conclusion**
--- 

Importance of being a good scientist 

Asking the right questions 