import numpy as np
import pandas as pd

from sklearn import linear_model

from sklearn.metrics import mean_squared_error, r2_score ,max_error

import matplotlib.pyplot as plt
import seaborn as sns

import fonctions.perso_stats as perso_stats

def regression_lineaire(data,colonne_cible,intercept=True):
    """
    crée un modele de regression lineaire.
    arg :
        train : dataframe ou serie ou array données d entrainement         
        target dataframe ou serie ou array         
        
    return :
        regr : model sklearn de regression lineaire
    """
    #sklearn version
    #prepa data
    target = data.pop(colonne_cible)

    #reshape si series (sklean n aime pas trop les pandas series)
    
    if isinstance(data,pd.Series):
        data = np.array(data)
        data =data.reshape(-1,1)

    #creation model regression lineaire
    regr = linear_model.LinearRegression(fit_intercept=intercept) #version sklean
    
    #entrainement du model
    regr.fit(data,target)    
        
    pred = regr.predict(data)

    if intercept:
        print("intercept (const dans statmodels)",regr.intercept_)

    # The coefficients
    print("Coefficients: \n", regr.coef_)    
    # The mean squared error
    print("Erreur des moindres carrés train : %.2f" % mean_squared_error(target, pred))
    # The coefficient of determination: 1 is perfect prediction
    # https://stackoverflow.com/questions/54614157/scikit-learn-statsmodels-which-r-squared-is-correct
    print("Coefficient de determination train : %.2f" % r2_score(target, pred))
    #erreur max :
    print("erreur max train: ",max_error(target, pred))
    
    fig,ax = plt.subplots()
    erreur_train =pred-target
    sns.histplot(erreur_train,ax=ax)
    ax.set_title("distribution des erreurs")    
    
    plt.show()

    #test normalité
    print("\n test de Normalité des erreurs")
    perso_stats.test_loi_normale(erreur_train.sample(5000))
    print("\n") 

    return(regr)
