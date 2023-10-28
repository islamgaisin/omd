import math


class CountVectorizer:
    """
    В файле приведена реализация класса CountVectorizer,
    с помощью которого можно получить терм-документную матрицу
    """

    def __init__(self):
        """
        Инициализатор класа CountVectorizer.
        features - словарь (не множество, потому что важен порядок) для
                   хранения всех слов в корпусе
        count_matrix - терм-документная матрица,
                       которую необходимо получить
        """
        self.features = {}
        self.count_matrix = []

    def fit_transform(self, corpus: list) -> list:
        """
        Функция принимает список предложений и
        возвращает терм-документную матрицу
        :param corpus: список предложений (каждое предложение - строка,
                       состоящая из слов, разделенных пробелом)
        :return: возвращается список, представляющий собой
                 терм-документную матрицу
        """
        self.features = {}
        self.count_matrix = []
        corpus = list(map(lambda x: x.lower().split(), corpus))
        self.__fit(corpus)
        self.__transform(corpus)
        return self.count_matrix

    def __fit(self, corpus: list):
        """
        Функция наполняет self.features (определяет все
        уникальные слова, которые есть в тексте)
        :param corpus: список предложений (каждое предложение -
                       список слов, полученный из исходного предложения
                       с помощью split())
        :return: функция ничего не возвращает
        """
        for sentence in corpus:
            for word in sentence:
                self.features[word] = 1

    def __transform(self, corpus: list):
        """
        Функция непосредственно составляет терм-документную матрицу,
        используя имеющийся набор слов в корпусе
        :param corpus: список предложений (каждое предложение -
                       список слов, полученный из исходного предложения
                       с помощью split())
        :return: функция ничего не возвращает
        """
        feature_keys = list(self.features.keys())
        for sentence in corpus:
            words_frequency = [0] * len(self.features)
            for i in range(len(self.features)):
                words_frequency[i] = sentence.count(feature_keys[i])
            self.count_matrix.append(words_frequency)

    def get_feature_names(self) -> list:
        """
        Функция возвращает все уникальные слова, которые есть в корпусе
        :return: список строк, каждая строка - слово из корпуса
        """
        return list(self.features.keys())


class TfidfTransformer:
    """
    Инициализатор класса TfidfTransformer
    tfidf_matrix - матрица с рассчитанными значениями tfidf
    """

    def __init__(self):
        self.tfidf_matrix = []

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Функция получает tfidf-матрицу из терм-документной матрицы, полученной
        от класса CountVectorizer
        :param count_matrix: терм-документная матрица, которая была
                             создана из корпуса с помощью класса
                             CountVectorizer
        :return: возвращается tfidf-матрица
        """
        tf_matrix = self.__tf_transform(count_matrix)
        idf_matrix = self.__idf_transform(count_matrix)
        number_of_docs = len(count_matrix)
        number_of_feature_names = len(count_matrix[0])
        for i in range(number_of_docs):
            tfidf_doc = [0.0] * number_of_feature_names
            for j in range(number_of_feature_names):
                tfidf_doc[j] = round(tf_matrix[i][j] * idf_matrix[j], 3)
            self.tfidf_matrix.append(tfidf_doc)
        return self.tfidf_matrix

    def __tf_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Функция подсчитывает значение term frequency, используя
        терм-документную матрицу
        :param count_matrix: терм-документная матрица, которая была
                             создана из корпуса с помощью класса
                             CountVectorizer
        :return: возвращается матрица с tf-значениями
        """
        tf_matrix = []
        number_of_feature_names = len(count_matrix[0])
        for doc in count_matrix:
            tf_doc = [0.0] * number_of_feature_names
            number_of_words_in_doc = sum(doc)
            for i in range(number_of_feature_names):
                tf_doc[i] = doc[i] / number_of_words_in_doc
            tf_matrix.append(tf_doc)
        return tf_matrix

    def __idf_transform(self, count_matrix: list[list[int]]) -> list[float]:
        """
        Функция подсчитывает значение inverse document-frequency, используя
        терм-документную матрицу
        :param count_matrix: терм-документная матрица, которая была
                             создана из корпуса с помощью класса
                             CountVectorizer
        :return: возвращается матрица с idf-значениями
        """
        number_of_docs = len(count_matrix)
        number_of_feature_names = len(count_matrix[0])
        docs_with_word = [0] * number_of_feature_names
        for doc in count_matrix:
            for i in range(number_of_feature_names):
                if doc[i] != 0:
                    docs_with_word[i] += 1
        idf_matrix = []
        for elem in docs_with_word:
            idf_matrix.append(math.log((number_of_docs + 1) / (elem + 1)) + 1)
        return idf_matrix


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        """
        Инициализатор класса TfidfVectorizer
        tfidf_matrix - матрица с рассчитанными значениями tfidf
        transformer - экземпляр класса TfidfTransformer, предназначен
                      для получения tfidf-матрицы
        """
        super().__init__()
        self.tfidf_matrix = []
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Функция принимает список предложений и
        возвращает tfidf-матрицу
        :param corpus: список предложений (каждое предложение - строка,
                       состоящая из слов, разделенных пробелом)
        :return: возвращается список, представляющий собой
                 tfidf-матрицу
        """
        self.count_matrix = super().fit_transform(corpus)
        self.tfidf_matrix = self.transformer.fit_transform(self.count_matrix)
        return self.tfidf_matrix


def solution():
    """
    Функция, проверяющаяя корректность реализации
    класса CountVectorizer
    :return: функция ничего не возвращает
    """
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    print(vectorizer.fit_transform(corpus))


if __name__ == '__main__':
    solution()
