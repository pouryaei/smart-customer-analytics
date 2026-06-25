from src.utils.drift import check_alert


def should_retrain():

    alerts = (
        check_alert()
    )

    if alerts:

        print(
            "Retraining needed"
        )

        return True

    print(
        "Model healthy"
    )

    return False


if __name__ == "__main__":

    should_retrain()