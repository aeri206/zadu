import sys

sys.path.append('../src/zadu')
sys.path.append("../legacy")

import provider as prov

from sklearn.datasets import load_iris, load_digits

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

digits, digits_label = load_digits(return_X_y=True)
iris, iris_label = load_iris(return_X_y=True)

pca = PCA(n_components=2)

digits_pca = pca.fit_transform(digits)
iris_pca = pca.fit_transform(iris)

tsne = TSNE(n_components=2)

digits_tsne = tsne.fit_transform(digits)
iris_tsne = tsne.fit_transform(iris)

from measures.trustworthiness_continuity import trustworthiness_continuity
from measures.class_aware_trustworthiness_continuity import class_aware_trustworthiness_continuity
from measures.mean_relative_rank_error import mean_relative_rank_error
from measures.local_continuity_meta_criteria import local_continuity_meta_criteria
from provider import MDPMetricProvider


print(trustworthiness_continuity(digits, digits_pca, 20))
print(MDPMetricProvider(digits, digits_pca, ["Trustworthiness", "Continuity"], 20).run())

print(class_aware_trustworthiness_continuity(digits, digits_pca, digits_label, 20))

print(mean_relative_rank_error(digits, digits_pca, 20))
print(MDPMetricProvider(digits, digits_pca, ["MRRE_ZX", "MRRE_XZ"], 20).run())

print(local_continuity_meta_criteria(digits, digits_pca, 20))
print(local_continuity_meta_criteria(digits, digits_tsne, 20))
print(local_continuity_meta_criteria(digits, digits_pca, 50))
print(local_continuity_meta_criteria(digits, digits_tsne, 50))

