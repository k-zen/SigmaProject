# -*- coding: utf-8 -*-

import pandas as pd
import requests as rq

from colorama import Back, Style


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
    USE_FILTERED: bool = False

    def __init__(self, raw_terms: [NBTerm], filtered_terms: [NBTerm]):
        self.raw_terms: [NBTerm] = raw_terms  # stopwords included
        self.filtered_terms: [NBTerm] = filtered_terms  # stopwords removed

    def __repr__(self):
        str = "\t\t\tTerms: {}\n".format(len(self.get_terms()))
        for t in self.get_terms():
            str += "\t\t\t{}\n".format(t)

        return str

    def get_terms(self):
        if NBDocument.USE_FILTERED:
            return self.filtered_terms
        else:
            return self.raw_terms


class NBClass(object):
    def __init__(self, label: str):
        self.label: str = label
        self.documents: [NBDocument] = []
        self.prior: float = 0.0
        self.likelihoods: [NBTerm] = []
        self.name: str = ""
        if self.label == '0':
            self.name = 'Wise Saying'
        elif self.label == '1':
            self.name = 'Future'

    def __repr__(self):
        str = "\tClass Label: {}\n".format(self.label)
        str += "\tDocuments: {}\n".format(len(self.documents))
        for d in self.documents:
            str += "\t\t{}\n".format(d)
        str += "\tPrior: {}\n".format(self.prior)
        str += "\tLikelihoods: {}\n".format(len(self.likelihoods))
        for l in self.likelihoods:
            str += "\t\t{}\n".format(l)

        return str

    def add_create_document(self, message: str) -> None:
        # break the document into terms
        terms = message.split(' ')
        raw_terms = [NBTerm(term=t) for t in terms]
        filtered_terms = raw_terms  # legacy, no use
        self.documents.append(NBDocument(raw_terms=raw_terms, filtered_terms=filtered_terms))

    def compute_likelihood(self, lexicon: [str]) -> None:
        # this will include ALL terms in the class, INCLUDED repeated terms!!!
        class_terms = [t.term for d in self.documents for t in d.get_terms()]  # ALL TERMS!!!

        # now for each term in lexicon compute its likelihood and add to the list of likelihoods
        # likelihood = occurrences of term / all terms
        for t in lexicon:
            # compute numerator. add 1 to avoid the zero-frequency problem
            numerator = class_terms.count(t) + 1
            # compute denominator. add count of lexicon to avoid zero-frequency problem
            denominator = len(class_terms) + len(lexicon)
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
            for t in d.get_terms():
                if t.term not in lexicon:
                    lexicon.append(t.term)

        return lexicon

    @staticmethod
    def get_class_name(label: str):
        if label == '0':
            return 'Wise Saying'
        elif label == '1':
            return 'Future'

        return 'None'


class NBModel(object):
    DEBUG = False

    def __init__(self):
        self.classes: [NBClass] = []
        self.lexicon: [str] = []  # vocabulary of UNIQUE words in ALL documents

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

        # +++ DEBUG
        if NBModel.DEBUG:
            print("PRIOR for class {0} is {1}.".format(label, N_c / N))
            print("N_c: {0}, N: {1}".format(N_c, N))

    def compute_lexicon(self) -> None:
        # vocabulary should NOT contain duplicates
        for c in self.classes:
            for d in c.documents:
                for t in d.get_terms():
                    if t.term not in self.lexicon:
                        self.lexicon.append(t.term)

    def compute_likelihood(self) -> None:
        for c in self.classes:
            c.compute_likelihood(lexicon=self.lexicon)


class NaiveBayesTextClassifier(object):
    """
    Text classifier using the Naïve Bayes Classifier. This classifier supports only 2 classes, so it's a
    binary classifier.
    """

    DEBUG = False
    SHOW_MODEL = False
    MAKE_SUBSET_FOR_TRAINING = False
    TRAINING_SUBSET_SIZE = 2
    MAKE_SUBSET_FOR_TESTING = False
    TESTING_SUBSET_SIZE = 2

    def __init__(self):
        self.model: NBModel = NBModel()
        pass

    def train(self, training_set: [str] = [], debug: bool = False) -> NBModel:
        # parse the training data and labels and convert them into pandas Series
        training_data = rq.get(
            'http://www.apkc.net/data/csc_578d/assignment01/problem04/traindata.txt'
        ).text.splitlines()
        if training_data is not None:
            t_data_series = pd.Series(training_data)

        training_labels = rq.get(
            'http://www.apkc.net/data/csc_578d/assignment01/problem04/trainlabels.txt'
        ).text.splitlines()
        if training_labels is not None:
            t_labels_series = pd.Series(training_labels)

        # combine both series into a DataFrame
        t_data_matrix = pd.DataFrame({
            'message': t_data_series,
            'label': t_labels_series
        })

        # make a custom subset of the entire training set for debugging purposes
        if NaiveBayesTextClassifier.MAKE_SUBSET_FOR_TRAINING:
            _0_messages = t_data_matrix.loc[
                              t_data_matrix.label == '0',
                              'message'][0:NaiveBayesTextClassifier.TRAINING_SUBSET_SIZE
                          ]
            _0_labels = ['0' for _ in _0_messages]
            _1_messages = t_data_matrix.loc[
                              t_data_matrix.label == '1',
                              'message'][0:NaiveBayesTextClassifier.TRAINING_SUBSET_SIZE
                          ]
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

        # +++ DEBUG
        if NaiveBayesTextClassifier.DEBUG:
            print("DataFrame: (Future: Class 1, Wise Saying: Class 0)")
            print(t_data_matrix)

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

        # +++ DEBUG
        if NaiveBayesTextClassifier.SHOW_MODEL:
            print('')
            print('++++++')
            print(self.model)

        return self.model

    def classify(self, model: NBModel, testing_set: [str] = [], debug: bool = False) -> None:
        # parse the training data and labels and convert them into pandas Series
        testing_data = rq.get(
            'http://www.apkc.net/data/csc_578d/assignment01/problem04/testdata.txt'
        ).text.splitlines()
        if testing_data is not None:
            t_data_series = pd.Series(testing_data)

        testing_labels = rq.get(
            'http://www.apkc.net/data/csc_578d/assignment01/problem04/testlabels.txt'
        ).text.splitlines()
        if testing_labels is not None:
            t_labels_series = pd.Series(testing_labels)

        # combine both series into a DataFrame
        t_data_matrix = pd.DataFrame({
            'message': t_data_series,
            'label': t_labels_series
        })

        # make a subset of the entire training set for debugging purposes
        if NaiveBayesTextClassifier.MAKE_SUBSET_FOR_TESTING:
            _0_messages = t_data_matrix.loc[
                              t_data_matrix.label == '0',
                              'message'][0:NaiveBayesTextClassifier.TESTING_SUBSET_SIZE
                          ]
            _0_labels = ['0' for _ in _0_messages]
            _1_messages = t_data_matrix.loc[
                              t_data_matrix.label == '1',
                              'message'][0:NaiveBayesTextClassifier.TESTING_SUBSET_SIZE
                          ]
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

        # compute the odds for each class
        correct_instances = 0
        for _, r in t_data_matrix.iterrows():
            document = str(r['message'])
            vocabulary = document.split(' ')
            label = r['label']

            # compute probability for each class
            argmax = []
            for c in model.classes:
                factors: str = ""
                v = c.prior
                factors += "{} *".format(v)
                for t in vocabulary:
                    likelihood = c.get_likelihood(term=t)
                    if likelihood is not None:
                        v *= likelihood
                        factors += " {} *".format(likelihood)

                if len(vocabulary) == 0:
                    v = 0

                argmax.append(NBClassification(label=c.label, value=v))

                if NaiveBayesTextClassifier.DEBUG:
                    print("Class {2} => {0} = {1}".format(factors.strip('*'), v, c.label))

            # compute accuracy
            max_label = max(argmax, key=lambda e: e.value).label
            result = Style.BRIGHT + Back.RED + 'INCORRECT' + Style.RESET_ALL
            if max_label == label:
                correct_instances += 1
                result = Style.BRIGHT + Back.GREEN + 'CORRECT' + Style.RESET_ALL

            txt = ''
            txt += "- {} ".format(document)
            txt += Style.BRIGHT + " [{0}:{1}] ".format(NBClass.get_class_name(max_label), max_label) + Style.RESET_ALL
            txt += " {} ".format(result)
            print(txt)

        print(Style.BRIGHT + "=======" + Style.RESET_ALL)
        print(Style.BRIGHT + "RESULT:" + Style.RESET_ALL)
        print(Style.BRIGHT + "> Classifier Accuracy: \"{0}%\"".format(
            (correct_instances / t_data_matrix.shape[0]) * 100
        ) + Style.RESET_ALL)
        print(Style.BRIGHT + "=======" + Style.RESET_ALL)
