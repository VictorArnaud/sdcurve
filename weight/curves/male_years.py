class WeightCurveMaleYears(object):
    """
    Weight-based growth curve for males aged 3 to 20 years
    """

    def __init__(self):
        """
        Growth curve based on the weight of male children with Down Syndrome
        constructor.
        """

        self.title = "Weight-based growth curve for males aged 3 to 20 years"

        self.ages = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        self.percentis_3 = [9.44, 10.43, 11.47, 12.58, 13.87, 15.37, 17.09, 19.07,
                            21.32, 23.80, 26.38, 28.90, 31.27, 33.45, 35.46, 37.33,
                            39.14, 40.96]

        self.percentis_10 = [10.90, 12.29, 13.78, 15.44, 17.34, 19.53, 21.98, 24.70,
                             27.67, 30.84, 34.03, 37.05, 39.80, 42.24, 44.40, 46.34,
                             48.16, 49.96]

        self.percentis_25 = [12.37, 14.14, 16.10, 18.29, 20.81, 23.69, 26.88, 30.33,
                             34.02, 37.88, 41.68, 45.20, 48.33, 51.03, 53.34, 55.34,
                             57.17, 58.95]

        self.percentis_50 = [13.83, 15.99, 18.41, 21.14, 24.28, 27.85, 31.77, 35.95,
                             40.37, 44.92, 49.33, 53.36, 56.86, 59.82, 62.28, 64.35,
                             66.19, 67.95]

        self.percentis_75 = [15.29, 17.85, 20.73, 23.99, 27.75, 32.01, 36.66, 41.58,
                             46.73, 51.96, 56.98, 61.51, 65.39, 68.61, 71.22, 73.36,
                             75.20, 76.95]

        self.percentis_90 = [16.76, 19.70, 23.04, 26.85, 31.22, 36.17, 41.55, 47.21,
                             53.08, 59.00, 64.64, 69.66, 73.92, 77.40, 80.16, 82.36,
                             84.22, 85.95]

        self.percentis_97 = [18.22, 21.55, 25.36, 29.70, 34.69, 40.33, 46.44, 52.84,
                             59.43, 66.04, 72.29, 77.82, 82.45, 86.19, 89.10, 91.37,
                             93.23, 94.95]

    def make(self):
        """
        Get the values to make the chart
        """

        return {
            'title': self.title,
            'ages': self.ages,
            'percentis_3': self.percentis_3,
            'percentis_10': self.percentis_10,
            'percentis_25': self.percentis_25,
            'percentis_50': self.percentis_50,
            'percentis_75': self.percentis_75,
            'percentis_90': self.percentis_90,
            'percentis_97': self.percentis_97
        }
