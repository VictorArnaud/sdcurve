class HeightCurveFemaleYears(object):
    """
    Height-based growth curve for females aged 3 to 20 years
    """

    def __init__(self):
        """
        Growth curve based on the height of female children with Down Syndrome
        constructor.
        """

        self.title = "Height-based growth curve for females aged 3 to 20 years"

        self.ages = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        self.percentis_3 = [81.24, 86.54, 91.92, 97.51, 103.27, 108.92, 114.19,
                            118.90, 122.97, 126.35, 129.02, 131.03, 132.48,
                            133.51, 134.24, 134.77, 135.18, 135.53]

        self.percentis_10 = [84.02, 89.43, 94.94, 100.66, 106.56, 112.34, 117.71,
                             122.48, 126.59, 129.97, 132.63, 134.62, 136.06,
                             137.08, 137.80, 138.33, 138.73, 139.07]

        self.percentis_25 = [86.79, 92.33, 97.96, 103.81, 109.85, 115.76, 121.23,
                             126.07, 130.20, 133.59, 136.24, 138.22, 139.64,
                             140.65, 141.36, 141.88, 142.28, 142.62]

        self.percentis_50 = [89.57, 95.22, 100.97, 106.96, 113.14, 119.18, 124.75,
                             129.65, 133.82, 137.21, 139.85, 141.81, 143.22,
                             144.21, 144.92, 145.44, 145.83, 146.17]

        self.percentis_75 = [92.34, 98.12, 103.99, 110.11, 116.44, 122.60, 128.27,
                             133.24, 137.43, 140.83, 143.46, 145.40, 146.80,
                             147.78, 148.48, 148.99, 149.38, 149.71]

        self.percentis_90 = [95.12, 101.01, 107.01, 113.26, 119.73, 126.02, 131.79,
                             136.82, 141.05, 144.45, 147.07, 149.00, 150.37,
                             151.35, 152.05, 152.55, 152.93, 153.26]

        self.percentis_97 = [97.90, 103.91, 110.02, 116.42, 123.02, 129.44, 135.31,
                             140.41, 144.66, 148.07, 150.68, 152.59, 153.95,
                             154.92, 155.61, 156.10, 156.48, 156.81]

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
