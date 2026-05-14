#!/usr/bin/env python3
"""Recommend the next small public change for the portfolio."""

from __future__ import annotations

import argparse


WEEKLY_ACTIONS = {
    1: "Polish the profile README and land the rewritten serverless-rag-demo README.",
    2: "Publish the synthetic instruction dataset and commit the formatting notebook.",
    3: "Add the LoRA SFT scaffold and write the first benchmark note.",
    4: "Publish the QLoRA tradeoff notebook and update the README with adapter decisions.",
    5: "Commit the golden set, regressions, and release-gate logic.",
    6: "Publish the latency/throughput benchmark report.",
    7: "Add the voice-agent control loop and mock tool data.",
    8: "Commit fallback paths, traces, and the runbook.",
    9: "Add a screenshot, diagram, or demo artifact to the strongest repo.",
    10: "Close loose issues and polish language across all README files.",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=int, required=True)
    args = parser.parse_args()
    action = WEEKLY_ACTIONS.get(args.week, "Pick one small visible improvement and publish it cleanly.")
    print(f"Week {args.week}: {action}")


if __name__ == "__main__":
    main()
