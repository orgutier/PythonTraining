#!/bin/sh
# Shared by pre-commit and pre-push -- not a hook itself (git only invokes
# files named exactly "pre-commit"/"pre-push"/etc., so this is ignored by
# git and only run when those hooks source/call it).
#
# Reads a list of changed file paths (one per line) on stdin, maps any
# exercises/weekNN/exerciseXX/*.py (including solution.py itself and any
# helper submodule next to it) or challenges/challengeNN/solution.py to its
# test id, and runs "python tools/cli.py test <id>" once per unique id
# found -- not the full suite. Exits non-zero if any of those runs fail;
# exits 0 (nothing to test) if no matching file appears in the input at all.

ids=$(sed -n \
    -e 's#^exercises/\(week[0-9][0-9]\)/exercise[0-9][0-9]/.*\.py$#\1#p' \
    -e 's#^exercises/\(week[0-9][0-9]\)/solution\.py$#\1#p' \
    -e 's#^challenges/\(challenge[0-9][0-9]\)/solution\.py$#\1#p' \
    | sort -u)

if [ -z "$ids" ]; then
    echo "No exercises/weekNN/exerciseXX/*.py or challenges/challengeNN/solution.py changed -- nothing to test."
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
