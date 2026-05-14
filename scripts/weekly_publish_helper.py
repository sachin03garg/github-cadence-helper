#!/usr/bin/env python3
"""Recommend the next small public change for the portfolio."""

from __future__ import annotations

import argparse


WEEKLY_ACTIONS = {
    1: "Polish the profile README and land the rewritten serverless-rag-demo README.",
    2: "Add repo metadata, pin order notes, and one small cleanup commit to an existing repo.",
    3: "Publish the synthetic instruction dataset and commit the formatting notebook.",
    4: "Add prompt-only baseline notes and open LoRA follow-up issues.",
    5: "Deepen the LoRA SFT scaffold and write the first benchmark note.",
    6: "Add one failure-analysis or model-behavior note to the PEFT repo.",
    7: "Publish the QLoRA tradeoff notebook and update the README with adapter decisions.",
    8: "Add adapter merge/unmerge inference notes and a small follow-up commit.",
    9: "Commit the golden set, regressions, and release-gate logic.",
    10: "Improve benchmark reporting language and add one real limitation note.",
    11: "Publish the latency/throughput benchmark report.",
    12: "Add a small benchmark follow-up rather than a large batch of changes.",
    13: "Add the voice-agent control loop and mock tool data.",
    14: "Open issues for traces, fallback behavior, and handoff handling.",
    15: "Commit fallback paths, traces, and the runbook.",
    16: "Add latency budget notes and one operator-focused improvement.",
    17: "Add a screenshot, diagram, or demo artifact to the strongest repo.",
    18: "Close loose issues and polish language across all README files.",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=int, required=True)
    args = parser.parse_args()
    action = WEEKLY_ACTIONS.get(args.week, "Pick one small visible improvement and publish it cleanly.")
    print(f"Week {args.week}: {action}")


if __name__ == "__main__":
    main()
