class HeightCurveMaleYears(object):
    """
    Height-based growth curve for males aged 3 to 20 years
    """

    def __init__(self):
        """
        Growth curve based on the height of male children with Down Syndrome
        constructor.
        """

        self.title = "Height-based growth curve for males aged 3 to 20 years"

        self.ages = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        self.percentis_3 = [83.25, 88.28, 93.25, 98.17, 103.12, 108.15, 113.25, 118.43,
                            123.59, 128.45, 132.62, 135.91, 138.37, 140.16, 141.42,
                            142.35, 143.12, 143.83]

        self.percentis_10 = [86.13, 91.35, 96.50, 101.61, 106.74, 111.96, 117.25, 122.59,
                             127.89, 132.84, 137.04, 140.33, 142.78, 144.55, 145.80,
                             146.72, 147.48, 148.17]

        self.percentis_25 = [89.00, 94.41, 99.76, 105.05, 110.37, 115.77, 121.24, 126.76,
                             132.20, 137.23, 141.46, 144.75, 147.19, 148.94, 150.18,
                             151.09, 151.83, 152.52]

        self.percentis_50 = [91.88, 97.48, 103.01, 108.49, 113.99, 119.58, 125.24, 130.93,
                             136.50, 141.61, 145.88, 149.17, 151.59, 153.33, 154.55,
                             155.45, 156.19, 156.87]

        self.percentis_75 = [94.76, 100.55, 106.27, 111.92, 117.61, 123.39, 129.23, 135.09,
                             140.80, 146.00, 150.31, 153.59, 156.00, 157.72, 158.93,
                             159.82, 160.55, 161.22]

        self.percentis_90 = [97.64, 103.62, 109.52, 115.36, 121.24, 127.21, 133.23, 139.26,
                             145.11, 150.39, 154.73, 158.01, 160.40, 162.11, 163.31,
                             164.19, 164.91, 165.57]

        self.percentis_97 = [100.51, 106.69, 112.78, 118.80, 124.86, 131.02, 137.23, 143.43,
                             149.41, 154.78, 159.15, 162.43, 164.81, 166.50, 167.68,
                             168.55, 169.26, 169.92]

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
