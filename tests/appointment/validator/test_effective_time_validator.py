from datetime import datetime, time, timedelta

import pytest

from core.modules.appointment.validators import AppointmentValidator

NOW = datetime.now()

TODAY = NOW.date()
TOMORROW = TODAY + timedelta(days=1)
FUTURE_DATE = TODAY + timedelta(days=5)
PAST_DATE = TODAY - timedelta(days=5)

PAST_START = (NOW - timedelta(hours=3)).time()
PAST_END = (NOW - timedelta(hours=1)).time()

CURRENT_TIME = NOW.time()

FUTURE_START = (NOW + timedelta(hours=1)).time()
FUTURE_END = (NOW + timedelta(hours=3)).time()

FUTURE_START_PLUS_5 = (NOW + timedelta(minutes=5)).time()
FUTURE_END_MINUS_5 = (NOW + timedelta(hours=3, minutes=-5)).time()

TEST_CASES = [
    (
        "Future Time | Today",
        TODAY,
        TODAY,
        FUTURE_START,
        FUTURE_END,
        (
            TODAY,
            TODAY,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Past Time | Today",
        TODAY,
        TODAY,
        PAST_START,
        PAST_END,
        None,
    ),

    (
        "Current Time | Today",
        TODAY,
        TODAY,
        PAST_START,
        FUTURE_END,
        (
            TODAY,
            TODAY,
            CURRENT_TIME,
            FUTURE_END,
        ),
    ),

    (
        "Time Exactly At Start | Today",
        TODAY,
        TODAY,
        CURRENT_TIME,
        FUTURE_END,
        (
            TODAY,
            TODAY,
            CURRENT_TIME,
            FUTURE_END,
        ),
    ),

    (
        "Time Exactly At End | Today",
        TODAY,
        TODAY,
        PAST_START,
        CURRENT_TIME,
        None,
    ),
    (
        "Missing Time | Today",
        TODAY,
        TODAY,
        None,
        None,
        (
            TODAY,
            TODAY,
            CURRENT_TIME,
            time.max,
        ),
    ),

    (
        "Missing Start Time | Today",
        TODAY,
        TODAY,
        None,
        FUTURE_END,
        (
            TODAY,
            TODAY,
            CURRENT_TIME,
            FUTURE_END,
        ),
    ),

    (
        "Missing End Time | Today",
        TODAY,
        TODAY,
        FUTURE_START,
        None,
        (
            TODAY,
            TODAY,
            FUTURE_START,
            time.max,
        ),
    ),

    (
        "Future Time | Tomorrow",
        TOMORROW,
        TOMORROW,
        FUTURE_START,
        FUTURE_END,
        (
            TOMORROW,
            TOMORROW,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Future Time | Future Date",
        FUTURE_DATE,
        FUTURE_DATE,
        FUTURE_START,
        FUTURE_END,
        (
            FUTURE_DATE,
            FUTURE_DATE,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Future Date | No Time",
        FUTURE_DATE,
        FUTURE_DATE,
        None,
        None,
        (
            FUTURE_DATE,
            FUTURE_DATE,
            time.min,
            time.max,
        ),
    ),

    (
        "Past Date | No Time",
        PAST_DATE,
        PAST_DATE,
        None,
        None,
        None,
    ),

    (
        "Past Date | Today",
        PAST_DATE,
        TODAY,
        FUTURE_START,
        FUTURE_END,
        (
            TODAY,
            TODAY,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Past Date | Future Date",
        PAST_DATE,
        FUTURE_DATE,
        FUTURE_START,
        FUTURE_END,
        (
            TODAY,
            FUTURE_DATE,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Past Date Range | Future Date",
        PAST_DATE,
        FUTURE_DATE,
        FUTURE_START,
        FUTURE_END,
        (
            TODAY,
            FUTURE_DATE,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Today | Future Date Range",
        TODAY,
        FUTURE_DATE,
        FUTURE_START,
        FUTURE_END,
        (
            TODAY,
            FUTURE_DATE,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Future Date Range | Future Time",
        TOMORROW,
        FUTURE_DATE,
        FUTURE_START,
        FUTURE_END,
        (
            TOMORROW,
            FUTURE_DATE,
            FUTURE_START,
            FUTURE_END,
        ),
    ),

    (
        "Future Date Range | No Time",
        TOMORROW,
        FUTURE_DATE,
        None,
        None,
        (
            TOMORROW,
            FUTURE_DATE,
            time.min,
            time.max,
        ),
    ),

    (
        "Entire Range | Past",
        PAST_DATE,
        TODAY - timedelta(days=1),
        FUTURE_START,
        FUTURE_END,
        None,
    ),

    (
        "Partial Range | Past + Future",
        PAST_DATE,
        FUTURE_DATE,
        PAST_START,
        FUTURE_END,
        (
            TODAY,
            FUTURE_DATE,
            CURRENT_TIME,
            FUTURE_END,
        ),
    )
]


@pytest.mark.parametrize(
    "test_name,start_date,end_date,start_time,end_time,expected",
    TEST_CASES
)
def test_get_effective_time(
        test_name,
        start_date,
        end_date,
        start_time,
        end_time,
        expected
):
    result = AppointmentValidator.get_effective_date_time_range(
        start_time=start_time,
        end_time=end_time,
        start_date=start_date,
        end_date=end_date,
        now=NOW
    )

    assert result == expected
