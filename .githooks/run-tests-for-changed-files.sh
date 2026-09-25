#!/bin/sh
# Shared by pre-commit and pre-push -- not a hook itself (git only invokes
# files named exactly "pre-commit"/"pre-push"/etc., so this is ignored by
# git and only run when those hooks source/call it).
#
# Usage: run-tests-for-changed-files.sh [exercise|stage]
#   exercise (default) -- test ONLY the specific exercise(s) that changed
#   stage               -- test the WHOLE stage for any exercise that
#                          changed in it (every exercise in that stage,
#                          not just the one(s) that changed)
#
# Either way, a changed exams/examNN/solution.py or
# challenges/challengeNN/solution.py always tests as just that one exam/
# challenge -- neither is split into smaller units, so there's no wider
# target for "stage" granularity to expand it to.
#
# Reads a list of changed file paths (one per line) on stdin, maps each
# one to its test id at the requested granularity, and runs "python
# tools/cli.py test <id>" once per unique id found -- never the full
# suite. Exits non-zero if any of those runs fail; exits 0 (nothing to
# test) if no matching file appears in the input at all.

granularity="${1:-exercise}"

# An exercise folder is named "exerciseXX" (the Capstone stage) or, on
# every stage using the tier-named convention, "tierN_<name>XX" -- the
# tier number prefix keeps a plain directory listing sorted in learning
# order: tier0_hello_world (Setup, stage01 only), tier1_basicXX,
# tier2_midXX, tier3_advancedXX, tier4_testing (stages 1-7 only).
EX_NAME='exercise[0-9][0-9]\|tier[0-9]_[a-z_]*[0-9]*'

case "$granularity" in
    exercise)
        # stage01/exercise03/whatever.py -> stage01_exercise03
        # stage01/basic01/whatever.py -> stage01_basic01
        ids=$(sed -n \
            -e "s#^exercises/\\(stage[0-9][0-9]\\)/\\($EX_NAME\\)/.*\\.py\$#\\1_\\2#p" \
            -e 's#^exams/\(exam[0-9][0-9]\)/solution\.py$#\1#p' \
            -e 's#^challenges/\(challenge[0-9][0-9]\)/solution\.py$#\1#p' \
            | sort -u)
        ;;
    stage)
        # stage01/exercise03/whatever.py -> stage01 (every exercise in it)
        ids=$(sed -n \
            -e "s#^exercises/\\(stage[0-9][0-9]\\)/\\($EX_NAME\\)/.*\\.py\$#\\1#p" \
            -e 's#^exams/\(exam[0-9][0-9]\)/solution\.py$#\1#p' \
            -e 's#^challenges/\(challenge[0-9][0-9]\)/solution\.py$#\1#p' \
            | sort -u)
        ;;
    *)
        echo "run-tests-for-changed-files.sh: unknown granularity '$granularity' (expected 'exercise' or 'stage')" >&2
        exit 1
        ;;
esac

if [ -z "$ids" ]; then
    echo "No exercises/stageNN/exerciseXX/*.py, exams/examNN/solution.py, or challenges/challengeNN/solution.py changed -- nothing to test."
    exit 0
fi

overall_status=0
for id in $ids; do
    echo ""
    echo "==> python tools/cli.py test $id"
    python tools/cli.py test "$id"
    status=$?
    if [ $status -ne 0 ]; then
        overall_status=1
    fi
done

exit $overall_status
