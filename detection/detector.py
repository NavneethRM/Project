from abc import ABC, abstractmethod


class Detector(ABC):

    @abstractmethod
    def detect(self, flow):
        """Return Alert or None"""
        pass


class DetectionEngine:

    def __init__(self):
        self.detectors = []

    def register(self, detector):
        self.detectors.append(detector)

    def run(self, flow):

        alerts = []

        for detector in self.detectors:

            alert = detector.detect(flow)

            if alert is not None:
                alerts.append(alert)

        return alerts
