from tqdm import tqdm
import evalplus.sanitize
from shapely.geometry import Polygon


def test_code(test_cases: list[dict], extra_imports: str = "") -> list[bool]:
    results = []

    for test_case in tqdm(test_cases, desc="Testing code"):
        globals = {}
        try:
            exec(extra_imports, globals)
            exec(test_case["code"], globals)
        except Exception as e:
            print(f"Error while executing code: {e}")
            results.append(["Execution error"] * len(test_case["tests"]))
            continue

        case_results = []
        for test in test_case["tests"]:
            try:
                res = globals[test_case["entrypoint"]](**test["inputs"])
                if test_case["id"] == "10" and isinstance(res, Polygon):  # When creating H3 polygons, we can get both polygon and list of points
                    case_results.append(bool(res.equals(test["expected_output"])))
                elif test_case["id"].startswith("16"):  # Tolerance of 0.001 for trajectory length
                    case_results.append(bool(abs(res - test["expected_output"]) < 0.001))
                elif test_case["id"].startswith("18"):  # Tolerance of 0.001 for trajectory duration
                    case_results.append(bool(abs(res - test["expected_output"]) < 0.001))
                elif test_case["id"].startswith("19"):  # We have a tolerance for geocoding polygon (over 0.9 IoU)
                    case_results.append(bool(res.intersection(test["expected_output"]).area / res.union(test["expected_output"]).area > 0.9))
                elif test_case["id"].startswith("20"):  # We add some toleration for geocoding result
                    x_diff = abs(res.x - test["expected_output"][0])
                    y_diff = abs(res.y - test["expected_output"][1])
                    case_results.append(bool(x_diff < 0.01 and y_diff < 0.01))
                else:
                    case_results.append(bool(res == test["expected_output"]))
            except Exception as e:
                res = str(e)
                print(f"Error while executing test: {e}")
                case_results.append(f"Error: {e}")
            print(f"(id={test_case['id']})Expected: {test['expected_output']}, got: {res}")
        results.append(case_results)

    return results


def remove_additional_functions(code: str) -> str:
    lines = code.split("\n")

    first_found = False

    for idx, line in enumerate(lines):
        if "def " in line:
            if first_found:
                break
            first_found = True

    return "\n".join(lines[:idx])


def sanitize_code(codes: list[str], entrypoints: list[str]) -> list[str]:
    return [
        remove_additional_functions(evalplus.sanitize.sanitize(code, entrypoint))
        for code, entrypoint in zip(codes, entrypoints)
    ]

def sanitize_single(code: str, entrypoint: str) -> str:
    return remove_additional_functions(evalplus.sanitize.sanitize(code, entrypoint))
