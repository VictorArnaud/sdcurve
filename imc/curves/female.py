class IMCCurveFemale(object):
    """
    IMC based growth curve for females aged 2 to 18 years
    """

    def __init__(self):
        """
        Growth curve based on the IMC of female children with Down Syndrome
        constructor.
        """

        self.title = "IMC based growth curve for females aged 2 to 18 years"

        self.ages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

        self.percentis_5 = [13.11, 13.14, 13.20, 13.32, 13.50, 13.78, 14.14, 14.61,
                            15.18, 15.82, 16.46, 17.03, 17.48, 17.83, 18.10, 18.33,
                            18.57]

        self.percentis_10 = [13.67, 13.75, 13.87, 14.05, 14.30, 14.65, 15.10, 15.65,
                             16.32, 17.06, 17.80, 18.45, 18.97, 19.38, 19.70, 19.98,
                             20.26]

        self.percentis_25 = [14.67, 14.85, 15.07, 15.36, 15.74, 16.22, 16.82, 17.54,
                             18.38, 19.30, 20.20, 21.01, 21.67, 22.19, 22.60, 22.96,
                             23.32]

        self.percentis_50 = [15.87, 16.16, 16.52, 16.95, 17.49, 18.14, 18.93, 19.84,
                             20.90, 22.04, 23.15, 24.15, 24.97, 25.63, 26.15, 26.61,
                             27.06]

        self.percentis_75 = [17.17, 17.60, 18.10, 18.70, 19.41, 20.27, 21.25, 22.39,
                             23.68, 25.06, 26.42, 27.63, 28.63, 29.43, 30.07, 30.64,
                             31.19]

        self.percentis_85 = [17.91, 18.42, 19.01, 19.71, 20.53, 21.49, 22.60, 23.86,
                             25.29, 26.81, 28.30, 29.64, 30.74, 31.63, 32.34, 32.96,
                             33.57]

        self.percentis_90 = [18.43, 19.01, 19.66, 20.42, 21.31, 22.36, 23.55, 24.90,
                             26.42, 28.05, 29.64, 31.06, 32.24, 33.18, 33.94, 34.61,
                             35.25]

        self.percentis_95 = [19.23, 19.90, 20.65, 21.52, 22.53, 23.70, 25.03, 26.51,
                             28.18, 29.96, 31.70, 33.26, 34.55, 35.58, 36.42, 37.14,
                             37.84]

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
