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
                if word not in self.features:
                    self.features[word] = 0
                self.features[word] += 1

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
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)


if __name__ == '__main__':
    solution()
