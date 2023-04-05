# Set the name of the remote repository
REMOTE := origin

# Set the name of the branches
INTO_BRANCH := feature/data-input
FROM_BRANCH := dev

# Update the dev branch with changes from the dev-build branch
dev-to-data-input:
	git fetch $(REMOTE) $(FROM_BRANCH):$(FROM_BRANCH) --update-head-ok
	git checkout $(INTO_BRANCH)
	git merge $(REMOTE)/$(FROM_BRANCH)
	git push