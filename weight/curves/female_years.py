class WeightCurveFemaleYears(object):
    """
    Weight-based growth curve for females aged 3 to 20 years
    """

    def __init__(self):
        """
        Growth curve based on the weight of female children with Down Syndrome
        constructor.
        """

        self.title = "Weight-based growth curve for females aged 3 to 20 years"

        self.ages = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        self.percentis_3 = [8.78, 10.02, 11.29, 12.69, 14.30, 16.10, 18.10, 20.22,
                            22.35, 24.37, 26.19, 27.75, 29.06, 30.19, 31.23, 32.21,
                            33.18, 34.15]

        self.percentis_10 = [10.17, 11.74, 13.39, 15.24, 17.37, 19.79, 22.49, 25.36,
                             28.27, 31.04, 33.51, 35.59, 37.31, 38.77, 40.05, 41.23,
                             42.37, 43.48]

        self.percentis_25 = [11.55, 13.46, 15.48, 17.78, 20.43, 23.47, 26.87, 30.51,
                             34.20, 37.70, 40.83, 43.43, 45.56, 47.34, 48.86, 50.25,
                             51.55, 52.82]

        self.percentis_50 = [12.94, 15.18, 17.58, 20.33, 23.50, 27.16, 31.25, 35.66,
                             40.13, 44.37, 48.14, 51.27, 53.82, 55.91, 57.68, 59.26,
                             60.74, 62.16]

        self.percentis_75 = [14.33, 16.90, 19.68, 22.87, 26.57, 30.84, 35.64, 40.80,
                             46.05, 51.04, 55.46, 59.11, 62.07, 64.48, 66.50, 68.28,
                             69.92, 71.50]

        self.percentis_90 = [15.71, 18.62, 21.78, 25.42, 29.64, 34.52, 40.02, 45.95,
                             51.98, 57.70, 62.77, 66.95, 70.33, 73.06, 75.32, 77.29,
                             79.11, 80.84]

        self.percentis_97 = [17.10, 20.34, 23.88, 27.96, 32.71, 38.21, 44.41, 51.10,
                             57.90, 64.37, 70.09, 74.80, 78.58, 81.63, 84.14, 86.31,
                             88.29, 90.18]

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
