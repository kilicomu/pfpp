#!/usr/bin/env bash

set -e

declare -a HOOKS=(
  "applypatch-msg"
  "commit-msg"
  "fsmonitor-watchman"
  "post-update"
  "pre-applypatch"
  "pre-commit"
  "pre-push"
  "pre-rebase"
  "pre-receive"
  "prepare-commit-msg"
  "update"
)

REPO_ROOT="$(git rev-parse --show-toplevel)"

for HOOK in "${HOOKS[@]}"; do
  if [[ -f "${REPO_ROOT}/hooks/${HOOK}" ]]; then
    1>&2 echo "INFO: Found hook script ${REPO_ROOT}/hooks/${HOOK} - installing..."
    ln --force --symbolic "${REPO_ROOT}/hooks/${HOOK}" "${REPO_ROOT}/.git/hooks/${HOOK}"
  fi
done
