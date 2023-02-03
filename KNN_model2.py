import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import GridSearchCV

# read training data and split training data into train_x and train_y
totalData = pd.read_csv('featured_data.csv')[:7000]
trainFeature = ['ncodpers', 'ind_empleado', 'sexo', 'age', 'ind_nuevo', 'indrel', 'indrel_1mes',
                'tiprel_1mes', 'indresi', 'indext', 'indfall', 'renta']
trainClassification = ['ind_ahor_fin_ult1', 'ind_aval_fin_ult1', 'ind_cco_fin_ult1', 'ind_cder_fin_ult1',
                       'ind_cno_fin_ult1', 'ind_ctju_fin_ult1', 'ind_ctma_fin_ult1', 'ind_ctop_fin_ult1',
                       'ind_ctpp_fin_ult1', 'ind_deco_fin_ult1', 'ind_deme_fin_ult1', 'ind_dela_fin_ult1',
                       'ind_ecue_fin_ult1', 'ind_fond_fin_ult1', 'ind_hip_fin_ult1', 'ind_plan_fin_ult1',
                       'ind_pres_fin_ult1', 'ind_reca_fin_ult1', 'ind_tjcr_fin_ult1', 'ind_valo_fin_ult1',
                       'ind_viv_fin_ult1', 'ind_nomina_ult1', 'ind_nom_pens_ult1', 'ind_recibo_ult1']
trainX = totalData.loc[:, trainFeature]
# iterate over all category in train_y and each time use GridSearchCV to find the best parameter and accuracy
for category in trainClassification:
    trainY = totalData.loc[:, [category]]
    numOfClass = len(trainY[category].unique())
    numOfOne = len(trainY[trainY[category] == 1])
    numOfZero = len(trainY[trainY[category] == 0])
    # when current category has two values and the amount of each value is larger than 5, fit the model
    if numOfClass > 1 and numOfOne > 5 and numOfZero > 5:
        k_range = range(1, 5)
        weight_options = ['uniform', 'distance']
        param_grid = {'n_neighbors': k_range, 'weights': weight_options}  # the grid of parameter 
        grid_search = GridSearchCV(KNN(), param_grid=param_grid, cv=5)
        grid_search.fit(trainX, trainY.values.ravel())
        print(category)
        print(grid_search.best_score_)
        print(grid_search.best_params_)
