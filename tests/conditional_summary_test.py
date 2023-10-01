from copy import deepcopy
from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from action import Action

BUTTON_ACTIONS = [
    {
        "summary": [
            {"summary": "summary1", "before": "10:00:00"},
            {"summary": "summary2", "before": "19:00:00"},
        ]
    }
]


class ConditionalSummary(TestCase):
    def setUp(self):
        self.action = Action({"events": []})

    @patch("action.datetime")
    def test_first_interval(self, fake_datetime):
        fake_datetime.now = Mock(return_value=datetime.strptime("00:00:00", "%H:%M:%S"))
        assert self.action.set_summary_by_time(deepcopy(BUTTON_ACTIONS)) == [
            {"summary": "summary1"}
        ]

    @patch("action.datetime")
    def test_interval(self, fake_datetime):
        fake_datetime.now = Mock(return_value=datetime.strptime("19:00:00", "%H:%M:%S"))
        assert self.action.set_summary_by_time(deepcopy(BUTTON_ACTIONS)) == [
            {"summary": "summary2"}
        ]
