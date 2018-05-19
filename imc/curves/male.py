class IMCCurveMale(object):
    """
    IMC based growth curve for males aged 2 to 18 years
    """

    def __init__(self):
        """
        Growth curve based on the IMC of male children with Down Syndrome
        constructor.
        """

        self.title = "IMC based growth curve for males aged 0 to 24 months"

        self.ages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

        self.percentis_5 = [13.83, 13.91, 14.00, 14.12, 14.26, 14.44, 14.71, 15.03,
                            15.37, 15.81, 16.44, 17.08, 17.68, 18.21, 18.66, 19.07,
                            19.48]

        self.percentis_10 = [14.28, 14.38, 14.49, 14.64, 14.81, 15.04, 15.35, 15.73,
                             16.14, 16.66, 17.38, 18.11, 18.79, 19.40, 19.92, 20.41,
                             20.90]

        self.percentis_25 = [15.12, 15.26, 15.42, 15.62, 15.86, 16.17, 16.59, 17.10,
                             17.64, 18.32, 19.20, 20.10, 20.94, 21.68, 22.33, 22.95,
                             23.57]

        self.percentis_50 = [16.19, 16.38, 16.61, 16.91, 17.25, 17.69, 18.28, 18.98,
                             19.72, 20.61, 21.72, 22.83, 23.85, 24.75, 25.54, 26.29,
                             27.05]

        self.percentis_75 = [17.45, 17.72, 18.05, 18.47, 18.96, 19.60, 20.44, 21.42,
                             22.44, 23.60, 24.97, 26.30, 27.49, 28.53, 29.44, 30.31,
                             31.18]

        self.percentis_85 = [18.22, 18.55, 18.94, 19.45, 20.06, 20.84, 21.87, 23.06,
                             24.28, 25.62, 27.14, 28.57, 29.84, 30.94, 31.90, 32.81,
                             33.72]

        self.percentis_90 = [18.79, 19.16, 19.60, 20.19, 20.89, 21.79, 22.99, 24.35,
                             25.72, 27.20, 28.82, 30.31, 31.63, 32.76, 33.74, 34.66,
                             35.59]

        self.percentis_95 = [19.71, 20.16, 20.70, 21.42, 22.28, 23.41, 24.90, 26.60,
                             28.27, 29.96, 31.72, 33.28, 34.62, 35.78, 36.76, 37.67,
                             38.60]

    def make(self):
        """
        Get the values to make the chart
        """

        return {
            'ages': self.ages,
            'title': self.title,
            'percentis_5': self.percentis_5,
            'percentis_10': self.percentis_10,
            'percentis_25': self.percentis_25,
            'percentis_50': self.percentis_50,
            'percentis_75': self.percentis_75,
            'percentis_85': self.percentis_85,
            'percentis_90': self.percentis_90,
            'percentis_95': self.percentis_95
        }
