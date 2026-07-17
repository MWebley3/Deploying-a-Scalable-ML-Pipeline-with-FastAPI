# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a RandomForestClassifier trained to predict whether an individual's income is <=50K or >50K using demographic and employment features from the Adult Census dataset. Categorical variables are one‑hot encoded, and the target label is binarized.

## Intended Use
The model is intended for educational use in demonstrating a machine learning pipeline and API deployment. It should not be used for real‑world decisions such as hiring, lending, or insurance.
## Training Data
The model was trained on the Adult Census Income dataset using an 80/20 train‑test split. Features include workclass, education, marital status, occupation, relationship, race, sex, and native country.
## Evaluation Data
The model was evaluated using precision, recall, and F1 score, which measure classification performance on the held-out test set.
## Metrics
_Please include the metrics used and your model's performance on those metrics._

Precision: 0.7419

Recall: 0.6384

F1 Score: 0.6863

These metrics indicate that the model performs reasonably well at identifying individuals earning more than $50K, though recall is affected by the dataset’s class imbalance.

## Ethical Considerations
The dataset contains sensitive demographic attributes and may reflect historical biases. Predictions should not be used to make decisions affecting individuals.
## Caveats and Recommendations
The model is trained only on U.S. census data, is affected by class imbalance, and may not generalize to other populations. Use this model only for demonstration. Monitor slice performance and avoid using predictions in any real‑world decision‑making context.