.PHONY: check package render sync test

check:
	python3 scripts/validate_pack.py
	python3 -m unittest discover -s tests -v

package: check
	python3 scripts/package_plugin.py

render:
	python3 scripts/render_catalog.py

sync: render
	python3 scripts/sync_pack.py

test:
	python3 -m unittest discover -s tests -v
