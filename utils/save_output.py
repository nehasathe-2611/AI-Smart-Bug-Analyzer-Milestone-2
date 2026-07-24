import json
import os


def save_analysis(result):

    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    file_path = os.path.join(
        "outputs",
        "analysis_result.json"
    )

    with open(file_path, "w") as file:

        json.dump(
            result,
            file,
            indent=4
        )

    return file_path