# github-cadence-helper

This helper repo is for building a real public contribution rhythm without faking activity or backdating commits.

## What It Does

- creates a daily checklist for one small, publishable change
- tracks weekly milestones across your portfolio repos
- seeds issue text for GitHub issues and weekly summaries
- keeps the work spread over time so the contribution graph grows honestly
- turns a bursty one-week portfolio dump into a calmer 4-month technical build story

## Files

- `plans/publishing_calendar.md`: 18-week roadmap
- `templates/daily_checklist.md`: one-day execution template
- `templates/issue_seed.md`: reusable issue format
- `scripts/weekly_publish_helper.py`: prints the next recommended action

## Run

```bash
python3 scripts/weekly_publish_helper.py --week 3
```
