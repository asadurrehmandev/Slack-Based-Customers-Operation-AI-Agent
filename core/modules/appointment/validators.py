from datetime import date, time, datetime


class AppointmentValidator:

    @staticmethod
    def get_effective_date_time_range(
            start_date: date,
            end_date: date | None = None,
            start_time: time | None = None,
            end_time: time | None = None,
            now: datetime | None = None
    ) -> tuple[date, date, time, time] | None:
        """
        Calculate the effective date and time range for an appointment query.

        The function removes dates and times that have already passed.

        Rules:
        - Past dates are moved to today.
        - On today's date, start_time is moved forward to the current time
          if the requested start_time has already passed.
        - Future dates keep the requested start_time and end_time.
        - If the entire requested range has already passed, returns None.
        - If end_date is not provided, only start_date is considered.

        :return:
            Tuple containing:

                (
                    effective_start_date,
                    effective_end_date,
                    effective_start_time,
                    effective_end_time,
                )

            Returns None if no time remains available in the requested range.
        """

        now = now or datetime.now()

        today = now.date()
        current_time = now.time()

        # If no end date is provided, only search the start date.
        if end_date is None:
            end_date = start_date

        # Requested range is completely in the past.
        if end_date < today:
            return None

        # Remove dates before today.
        effective_start_date = max(start_date, today)
        effective_end_date = end_date

        # Default time range.
        effective_start_time = start_time or time.min
        effective_end_time = end_time or time.max

        # If the effective range ends before today, nothing is available.
        if effective_end_date < today:
            return None

        # If the effective range starts today,
        # current time affects the starting time.
        if effective_start_date == today:

            # The requested time window has already ended.
            if current_time >= effective_end_time:
                return None

            # Current time is inside the requested time window.
            if current_time > effective_start_time:
                effective_start_time = current_time

        return (
            effective_start_date,
            effective_end_date,
            effective_start_time,
            effective_end_time,
        )


if __name__ == "__main__":
    from datetime import date, time, datetime


    def test_case(
            name: str,
            start_date: date,
            end_date: date | None = None,
            start_time: time | None = None,
            end_time: time | None = None,
    ):
        result = AppointmentValidator.get_effective_date_time_range(
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
        )

        print("=" * 70)
        print(name)
        print("-" * 70)
        print(f"Start Date : {start_date}")
        print(f"End Date   : {end_date}")
        print(f"Start Time : {start_time}")
        print(f"End Time   : {end_time}")
        print(f"Result     : {result}")


    now = datetime.now()

    print("\nCURRENT SYSTEM TIME")
    print("=" * 70)
    print(f"Date: {now.date()}")
    print(f"Time: {now.time().replace(microsecond=0)}")
    print()

    # ---------------------------------------------------------
    # 1. TODAY - Requested time is completely in the future
    # ---------------------------------------------------------

    test_case(
        name="1. Today - Future Time Window",
        start_date=now.date(),
        end_date=now.date(),
        start_time=time(23, 0),
        end_time=time(23, 59),
    )

    # ---------------------------------------------------------
    # 2. TODAY - Current time is inside requested window
    # ---------------------------------------------------------

    test_case(
        name="2. Today - Current Time Inside Window",
        start_date=now.date(),
        end_date=now.date(),
        start_time=time(0, 0),
        end_time=time(23, 59),
    )

    # ---------------------------------------------------------
    # 3. TODAY - Requested window has already ended
    # ---------------------------------------------------------

    test_case(
        name="3. Today - Time Window Already Passed",
        start_date=now.date(),
        end_date=now.date(),
        start_time=time(0, 0),
        end_time=time(1, 0),
    )

    # ---------------------------------------------------------
    # 4. FUTURE DATE
    # ---------------------------------------------------------

    test_case(
        name="4. Future Date",
        start_date=now.date().replace(
            day=now.day
        ),
        end_date=None,
        start_time=time(9, 0),
        end_time=time(17, 0),
    )

    # ---------------------------------------------------------
    # 5. Future DATE RANGE
    # ---------------------------------------------------------

    test_case(
        name="5. Future Date Range",
        start_date=now.date().replace(
            day=now.day + 1
        ),
        end_date=now.date().replace(
            day=now.day + 3
        ),
        start_time=time(9, 0),
        end_time=time(17, 0),
    )

    # ---------------------------------------------------------
    # 6. Past date range
    # ---------------------------------------------------------

    test_case(
        name="6. Completely Past Date Range",
        start_date=date(2020, 1, 1),
        end_date=date(2020, 1, 5),
        start_time=time(9, 0),
        end_time=time(17, 0),
    )

    # ---------------------------------------------------------
    # 7. Past start date + future end date
    # ---------------------------------------------------------

    test_case(
        name="7. Past Start Date + Future End Date",
        start_date=date(2020, 1, 1),
        end_date=now.date().replace(
            day=now.day + 2
        ),
        start_time=time(9, 0),
        end_time=time(17, 0),
    )

    # ---------------------------------------------------------
    # 8. No start_time / end_time
    # ---------------------------------------------------------

    test_case(
        name="8. No Time Restrictions",
        start_date=now.date(),
        end_date=now.date(),
    )

    # ---------------------------------------------------------
    # 9. Start time only
    # ---------------------------------------------------------

    test_case(
        name="9. Start Time Only",
        start_date=now.date(),
        end_date=now.date(),
        start_time=time(9, 0),
    )

    # ---------------------------------------------------------
    # 10. End time only
    # ---------------------------------------------------------

    test_case(
        name="10. End Time Only",
        start_date=now.date(),
        end_date=now.date(),
        end_time=time(23, 59),
    )
