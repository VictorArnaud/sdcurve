class PerimeterCurveFemale(object):
    """
    Cephalic perimeter based growth curve for females aged 0 to 24 months
    """

    def __init__(self):
        """
        Growth curve based on the cephalic perimeter of female children with Down Syndrome
        constructor.
        """

        self.title = "Cephalic Perimeter based growth curve for females aged 0 to 24 months"

        self.ages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                     18, 19, 20, 21, 22, 23, 24]

        self.percentis_3 = [30.50, 32.08, 33.76, 35.09, 36.23, 37.20, 38.03, 38.73,
                            39.31, 39.80, 40.21, 40.55, 40.85, 41.11, 41.34, 41.54,
                            41.73, 41.91, 42.07, 42.22, 42.36, 42.50, 42.63, 42.75,
                            42.86]

        self.percentis_10 = [31.16, 33.16, 34.75, 36.03, 37.11, 38.05, 38.86, 39.53,
                             40.10, 40.57, 40.97, 41.31, 41.61, 41.87, 42.10, 42.31,
                             42.50, 42.68, 42.84, 43.00, 43.15, 43.29, 43.42, 43.55,
                             43.67]

        self.percentis_25 = [31.90, 34.16, 35.69, 36.93, 37.98, 38.89, 39.67, 40.33,
                             40.88, 41.35, 41.74, 42.08, 42.37, 42.62, 42.86, 43.07,
                             43.26, 43.44, 43.61, 43.77, 43.92, 44.06, 44.20, 44.33,
                             44.46]

        self.percentis_50 = [32.80, 35.20, 36.67, 37.87, 38.89, 39.78, 40.54, 41.19,
                             41.73, 42.19, 42.58, 42.91, 43.20, 43.45, 43.68, 43.89,
                             44.09, 44.27, 44.44, 44.60, 44.75, 44.90, 45.04, 45.17,
                             45.30]

        self.percentis_75 = [33.83, 36.16, 37.60, 38.77, 39.77, 40.64, 41.39, 42.03,
                             42.57, 43.02, 43.40, 43.73, 44.01, 44.27, 44.50, 44.70,
                             44.90, 45.08, 45.25, 45.41, 45.56, 45.71, 45.85, 45.98,
                             46.11]

        self.percentis_90 = [34.88, 36.97, 38.39, 39.54, 40.53, 41.39, 42.14, 42.77,
                             43.31, 43.75, 44.13, 44.46, 44.74, 44.99, 45.21, 45.42,
                             45.61, 45.79, 45.96, 46.12, 46.27, 46.42, 46.56, 46.69,
                             46.82]

        self.percentis_97 = [36.07, 37.72, 39.14, 40.28, 41.25, 42.11, 42.86, 43.49,
                             44.02, 44.47, 44.84, 45.17, 45.44, 45.69, 45.91, 46.12,
                             46.31, 46.48, 46.65, 46.81, 46.96, 47.10, 47.24, 47.37,
                             47.50]

    def make(self):
        """
        Get the values to make the chart
        """

        return {
            'ages': self.ages,
            'title': self.title,
            'percentis_3': self.percentis_3,
            'percentis_10': self.percentis_10,
            'percentis_25': self.percentis_25,
            'percentis_50': self.percentis_50,
            'percentis_75': self.percentis_75,
            'percentis_90': self.percentis_90,
            'percentis_97': self.percentis_97
        }
