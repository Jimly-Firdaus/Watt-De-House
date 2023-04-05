# Set the name of the remote repository
REMOTE := origin

# Set the name of the branches
INTO_BRANCH := dev
FROM_BRANCH := feature/simulator

# Update the dev branch with changes from the dev-build branch
main-to-dev:
	git fetch $(REMOTE) $(FROM_BRANCH):$(FROM_BRANCH) --update-head-ok
	git checkout $(INTO_BRANCH)
	git merge $(REMOTE)/$(FROM_BRANCH)
	git push