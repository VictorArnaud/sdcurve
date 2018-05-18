class PerimeterCurveMale(object):
    """
    Cephalic perimeter based growth curve for males aged 0 to 24 months
    """

    def __init__(self):
        """
        Growth curve based on the cephalic perimeter of male children with Down Syndrome
        constructor.
        """

        self.title = "Cephalic Perimeter based growth curve for males aged 0 to 24 months"

        self.ages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                     19, 20, 21, 22, 23, 24]

        self.percentis_3 = [30.13, 33.11, 34.99, 36.31, 37.34, 38.17, 38.85, 39.41,
                            39.88, 40.29, 40.64, 40.95, 41.22, 41.46, 41.68, 41.88,
                            42.06, 42.22, 42.37, 42.51, 42.64, 42.76, 42.87, 42.98,
                            43.08]

        self.percentis_10 = [30.84, 33.95, 35.91, 37.29, 38.37, 39.24, 39.94, 40.53,
                             41.02, 41.45, 41.82, 42.14, 42.42, 42.68, 42.91, 43.11,
                             43.30, 43.47, 43.63, 43.78, 43.91, 44.04, 44.15, 44.26,
                             44.37]

        self.percentis_25 = [31.71, 34.83, 36.83, 38.23, 39.32, 40.21, 40.93, 41.52,
                             42.03, 42.46, 42.83, 43.16, 43.45, 43.71, 43.94, 44.15,
                             44.34, 44.52, 44.68, 44.82, 44.96, 45.09, 45.21, 45.32,
                             45.43]

        self.percentis_50 = [32.89, 35.86, 37.81, 39.20, 40.29, 41.17, 41.89, 42.48,
                             42.99, 43.42, 43.79, 44.12, 44.41, 44.67, 44.90, 45.11,
                             45.30, 45.47, 45.63, 45.77, 45.91, 46.04, 46.16, 46.27,
                             46.37]

        self.percentis_75 = [34.16, 36.88, 38.77, 40.13, 41.21, 42.08, 42.79, 43.38,
                             43.88, 44.31, 44.68, 45.00, 45.29, 45.55, 45.78, 45.98,
                             46.17, 46.34, 46.50, 46.64, 46.78, 46.90, 47.02, 47.13,
                             47.23]

        self.percentis_90 = [35.20, 37.75, 39.60, 40.95, 42.02, 42.89, 43.60, 44.19,
                             44.69, 45.12, 45.49, 45.81, 46.10, 46.35, 46.58, 46.79,
                             46.97, 47.14, 47.30, 47.45, 47.58, 47.71, 47.82, 47.93,
                             48.04]

        self.percentis_97 = [36.15, 38.57, 40.39, 41.74, 42.81, 43.68, 44.39, 44.98,
                             45.48, 45.91, 46.28, 46.61, 46.89, 47.15, 47.38, 47.59,
                             47.77, 47.94, 48.10, 48.25, 48.38, 48.51, 48.62, 48.73,
                             48.84]

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
