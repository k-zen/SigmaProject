# -*- coding: utf-8 -*-

import sigmaproject.utils as utils
import pandas as pd
import requests as rq


class NBClassification(object):
    def __init__(self, label: str, value: float = 0.0):
        self.label: str = label
        self.value: float = value

    def __repr__(self):
        return "{0}<{1}>".format(self.label, self.value)


class NBTerm(object):
    def __init__(self, term: str, likelihood: float = 0.0):
        self.term: str = term.lower().strip()
        self.likelihood: float = likelihood

    def __repr__(self):
        return "{0}<{1}>".format(self.term, self.likelihood)


class NBDocument(object):
    def __init__(self, terms: [NBTerm]):
        self.terms: [NBTerm] = terms

    def __repr__(self):
        str = "\t\t\tTerms: {}\n".format(len(self.terms))
        for t in self.terms:
            str += "\t\t\t{}\n".format(t)

        return str


class NBClass(object):
    def __init__(self, label: str):
        self.label: str = label
        self.documents: [NBDocument] = []
        self.prior: float = 0.0
        self.likelihoods: [NBTerm] = []
        """
        A list containing the likelihoods for all terms in the class. 
        """

    def __repr__(self):
        str = "\tClass Label: {}\n".format(self.label)
        str += "\tDocuments: {}\n".format(len(self.documents))
        for d in self.documents:
            str += "\t\t{}\n".format(d)
        str += "\tPrior: {}\n".format(self.prior)
        str += "\tLikelihoods:\n".format(len(self.likelihoods))
        for l in self.likelihoods:
            str += "\t\t{}\n".format(l)

        return str

    def add_create_document(self, message: str) -> None:
        # break the document into terms
        terms = message.split(' ')
        terms = [NBTerm(term=t) for t in terms]
        self.documents.append(NBDocument(terms=terms))

    def compute_likelihood(self, lexicon: [str]) -> None:
        # compute unique and all terms in all documents in the class
        unique_terms = list({t.term for d in self.documents for t in d.terms})
        all_terms = [t.term for d in self.documents for t in d.terms]

        # now for each term in unique compute its likelihood and add to the list of likelihoods
        # likelihood = occurrences of term / all terms
        for t in unique_terms:
            # compute numerator. add 1 to avoid the zero-frequency problem
            numerator = all_terms.count(t) + 1
            # compute denominator. add count of lexicon to avoid zero-frequency problem
            denominator = len(all_terms) + len(lexicon)
            # add to the likelihood list IF not present
            flag = False
            for e in self.likelihoods:
                if e.term == t:
                    flag = True

            if not flag:
                self.likelihoods.append(NBTerm(term=t, likelihood=(numerator / denominator)))

    def get_likelihood(self, term: str) -> None:
        for e in self.likelihoods:
            if e.term == term:
                return e.likelihood

    def get_class_lexicon(self) -> [str]:
        lexicon = []
        for d in self.documents:
            for t in d.terms:
                if t.term not in lexicon:
                    lexicon.append(t.term)

        return lexicon


class NBModel(object):
    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        self.classes: [NBClass] = []
        self.lexicon: [str] = []
        """
        Vocabulary of UNIQUE words in ALL documents.
        """

    def __repr__(self):
        str = "Classes: {}\n".format(len(self.classes))
        for c in self.classes:
            str += "{}\n".format(c)
        str += "Lexicon: {}\n".format(len(self.lexicon))
        str += "{}".format(sorted(self.lexicon))

        return str

    def get_class(self, label: str) -> NBClass:
        for c in self.classes:
            if c.label == label:
                return c

        return None

    def calculate_and_update_prior(self, label: str) -> None:
        N_c = float(len(self.get_class(label=label).documents))  # number of docs in class
        N = 0.0  # number of docs in all classes
        for c in self.classes:
            N += len(c.documents)

        # update prior
        self.get_class(label=label).prior = N_c / N

        if NBModel.DEBUG:
            print("PRIOR for class {0} is {1}.".format(label, N_c / N))
            print("N_c: {0}, N: {1}".format(N_c, N))

    def compute_lexicon(self) -> None:
        """
        Vocabulary should NOT contain duplicates.

        :return: None
        """
        for c in self.classes:
            for d in c.documents:
                for t in d.terms:
                    if t.term not in self.lexicon:
                        self.lexicon.append(t.term)

    def compute_likelihood(self) -> None:
        for c in self.classes:
            c.compute_likelihood(lexicon=self.lexicon)


class NaiveBayesTextClassifier(object):
    """
    Text classifier using the Naïve Bayes Classifier.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """
    SHOW_MODEL = False
    MAKE_SUBSET_FOR_TRAINING = False
    TRAINING_SUBSET_SIZE = 2
    """
    boolean: Flag to enable only a subset of the entire dataset.
    """
    MAKE_SUBSET_FOR_TESTING = True
    TESTING_SUBSET_SIZE = 40
    """
    boolean: Flag to enable only a subset of the entire dataset.
    """

    def __init__(self):
        self.model: NBModel = NBModel()
        pass

    def train(self,
              training_set: [str] = [],
              debug: bool = False) -> NBModel:
        """
        Function to create a statistical model used in the classification function.

        :param training_set: An array of strings containing the path to the training data (Index 0) \
            and the training labels (Index 1).
        :param debug: Flag to enable/disable debug mode.

        :return: NBModel
        """
        # parse the training data and labels and convert them into pandas Series
        # TODO: change to support dynamic files
        training_data = rq.get('http://www.apkc.net/data/csc_578d/assignment01/problem04/traindata.txt').text.splitlines()
        if training_data is not None:
            t_data_series = pd.Series(training_data)
            if NaiveBayesTextClassifier.DEBUG:
                print("Training Data:")
                print(t_data_series)

        training_labels = rq.get('http://www.apkc.net/data/csc_578d/assignment01/problem04/trainlabels.txt').text.splitlines()
        if training_labels is not None:
            t_labels_series = pd.Series(training_labels)
            if NaiveBayesTextClassifier.DEBUG:
                print("Training Labels:")
                print(t_labels_series)

        # combine both series into a DataFrame
        t_data_matrix = pd.DataFrame({
            'message': t_data_series,
            'label': t_labels_series
        })

        # make a subset of the entire training set for debugging purposes
        if NaiveBayesTextClassifier.MAKE_SUBSET_FOR_TRAINING:
            _0_messages = t_data_matrix.loc[t_data_matrix.label == '0', 'message'][0:NaiveBayesTextClassifier.TRAINING_SUBSET_SIZE]
            _0_labels = ['0' for _ in _0_messages]
            _1_messages = t_data_matrix.loc[t_data_matrix.label == '1', 'message'][0:NaiveBayesTextClassifier.TRAINING_SUBSET_SIZE]
            _1_labels = ['1' for _ in _1_messages]
            # replace the DataFrame
            t_data_matrix = pd.DataFrame({
                'message': pd.concat([
                    pd.Series(list(_0_messages)),
                    pd.Series(list(_1_messages))
                ]),
                'label': pd.concat([
                    pd.Series(_0_labels),
                    pd.Series(_1_labels)
                ])
            })
            print(t_data_matrix)

        if NaiveBayesTextClassifier.DEBUG:
            print("DataFrame: (Future: Class 1, Wise Saying: Class 0)")
            print(t_data_matrix)

        # iterate the documents and count vocabulary
        for i, r in t_data_matrix.iterrows():
            if i == 2:  # for debug
                break

            document = str(r['message'])
            vocabulary = document.split(' ')
            label = r['label']

            if NaiveBayesTextClassifier.DEBUG:
                print("Document: {}".format(document))
                print("Class: {}".format(label))
                print("Vocabulary: {}".format(len(vocabulary)))
                print('---')

        # construct the model
        # 1. save classes, documents, terms
        for label in t_data_matrix.label.unique():  # this returns an ndarray
            self.model.classes.append(NBClass(label=label))

            # save all messages for each class
            tmp = t_data_matrix.loc[t_data_matrix.label == label, 'message']
            cls = self.model.get_class(label)
            for _, m in tmp.items():
                cls.add_create_document(str(m))

        # 2. calculate priors
        for label in t_data_matrix.label.unique():  # this returns an ndarray
            self.model.calculate_and_update_prior(label)

        # 3. compute lexicon
        self.model.compute_lexicon()

        # 4. compute likelihoods
        self.model.compute_likelihood()

        # print for debug
        if NaiveBayesTextClassifier.SHOW_MODEL:
            print('')
            print('++++++')
            print(self.model)

        return self.model

    def classify(
            self,
            model: NBModel,
            testing_set: [str] = [],
            debug: bool = False) -> None:
        """
        Function to classify text phrases into bins or classes using the Naïve Bayes classifier algorithm. It
        will use the statistical model created with the training function.

        :param testing_set: An array of strings containing the path to the data data (Index 0) \
            and the labels (Index 1).
        :param debug: Flag to enable/disable debug mode.

        :return: None
        """
        # parse the training data and labels and convert them into pandas Series
        # TODO: change to support dynamic files
        testing_data = rq.get('http://www.apkc.net/data/csc_578d/assignment01/problem04/traindata.txt').text.splitlines()
        if testing_data is not None:
            t_data_series = pd.Series(testing_data)
            if NaiveBayesTextClassifier.DEBUG:
                print("Testing Data:")
                print(t_data_series)

        testing_labels = rq.get('http://www.apkc.net/data/csc_578d/assignment01/problem04/trainlabels.txt').text.splitlines()
        if testing_labels is not None:
            t_labels_series = pd.Series(testing_labels)
            if NaiveBayesTextClassifier.DEBUG:
                print("Testing Labels:")
                print(t_labels_series)

        # combine both series into a DataFrame
        t_data_matrix = pd.DataFrame({
            'message': t_data_series,
            'label': t_labels_series
        })

        # make a subset of the entire training set for debugging purposes
        if NaiveBayesTextClassifier.MAKE_SUBSET_FOR_TESTING:
            _0_messages = t_data_matrix.loc[t_data_matrix.label == '0', 'message'][0:NaiveBayesTextClassifier.TESTING_SUBSET_SIZE]
            _0_labels = ['0' for _ in _0_messages]
            _1_messages = t_data_matrix.loc[t_data_matrix.label == '1', 'message'][0:NaiveBayesTextClassifier.TESTING_SUBSET_SIZE]
            _1_labels = ['1' for _ in _1_messages]
            # replace the DataFrame
            t_data_matrix = pd.DataFrame({
                'message': pd.concat([
                    pd.Series(list(_0_messages)),
                    pd.Series(list(_1_messages))
                ]),
                'label': pd.concat([
                    pd.Series(_0_labels),
                    pd.Series(_1_labels)
                ])
            })
            # print(t_data_matrix)

        correct = 0
        class_0_lexicon = model.classes[0].get_class_lexicon()
        class_1_lexicon = model.classes[1].get_class_lexicon()

        # compute the odds for each class
        for _, r in t_data_matrix.iterrows():
            document = str(r['message'])
            vocabulary = document.split(' ')
            label = r['label']

            final_vocabulary = []

            # the vocabulary MUST be common to both classes otherwise the algorithm is unbalanced
            # and it doesn't work, so we should intersect terms to both classes
            common_vocabulary = []
            for t in class_0_lexicon:
                if class_1_lexicon.count(t) > 0:
                    common_vocabulary.append(t)

            for t in vocabulary:
                if common_vocabulary.count(t) > 0:
                    final_vocabulary.append(t)

            # compute probability for each class
            argmax = []
            for c in model.classes:
                factors: str = ""
                v = c.prior
                factors += "{}*".format(v)
                for t in final_vocabulary:
                    likelihood = c.get_likelihood(term=t)
                    if likelihood is not None:
                        v *= likelihood
                        factors += "{}*".format(likelihood)

                if len(final_vocabulary) == 0:
                    v = 0

                argmax.append(NBClassification(label=c.label, value=v))

            # compute accuracy
            max_label = max(argmax, key=lambda e: e.value).label
            result = utils.Colors.FAIL + 'FALSE' + utils.Colors.ENDC
            if max_label == label:
                correct += 1
                result = utils.Colors.BOLD + 'TRUE' + utils.Colors.ENDC

            print(utils.Colors.BOLD + "Message:" + utils.Colors.ENDC + " {} ".format(document) + "{}".format(result))

        print(utils.Colors.BOLD + "=======" + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "RESULT:" + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "> Classifier Accuracy: \"{0}%\"".format((correct / t_data_matrix.shape[0]) * 100) + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "=======" + utils.Colors.ENDC)
