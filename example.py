"""New independent fictional-fact illustration. No model or financial engine."""
import json

FACT = {"sample_id": "SYNTH-01", "field": "display_amount_usd", "value": 123400, "source_id": "syn-source-01"}


def check_claim(claim):
    if type(claim) is not dict or set(claim) != set(FACT):
        return "UNVERIFIED: MISSING_OR_EXTRA_FIELD"
    if claim["source_id"] != FACT["source_id"]:
        return "UNVERIFIED: UNKNOWN_SOURCE"
    if any(type(claim[k]) is not type(v) or claim[k] != v for k, v in FACT.items()):
        return "UNVERIFIED: UNSUPPORTED_CLAIM"
    return "SUPPORTED_SYNTHETIC_FACT"


if __name__ == "__main__":
    print(json.dumps({"provenance": "SCRIPTED / INVENTED; NOT LIVE MODEL OUTPUT",
                      "supported": check_claim(dict(FACT)),
                      "wrong_value_real_source": check_claim(dict(FACT, value=777700)),
                      "limits": "Generic illustration only; no appraisal, credit or private-engine validation."}, indent=2))
