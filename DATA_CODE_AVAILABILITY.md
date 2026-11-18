# Data and code availability template

Use this paragraph once the tagged release and its data have been checked from a fresh clone. Replace the bracketed fields with the release details and adjust the materials listed to match the archive.

> The simulation data and code used in this study are available in the [repository name] GitHub repository, release [tag], at [release URL]. The release includes the switched converter model and simulation settings, frequency-response sweeps, dataset splits, training and evaluation code, and the records used to generate the reported figures and tables. Large data files are stored through Git Large File Storage (Git LFS). The release documentation provides instructions for retrieving the data and reproducing the analyses.

## Release details to fill in

- Repository URL, release tag and URL, and commit identifier.
- Public or reviewer access, with any restrictions stated in the manuscript.
- Licenses for the code and data and attribution for any redistributed material.
- Data manifest with benchmark and split names, LFS-tracked file patterns, and checksums.
- The archived simulator and environment versions, experiment configurations, and reproduction commands.

## Verify the release before citing it

- Check out the release tag from an account with the intended reader or reviewer permissions. Retrieve the LFS objects and confirm the files are complete and match the manifest.
- If the documentation directs readers to a ZIP or tarball, verify that the downloaded archive contains the intended LFS objects. Release archive inclusion is a separate GitHub repository setting. [GitHub documentation on Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) · [GitHub documentation on releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- Rebuild the tables and data-derived figures from the archived inputs and compare them with the journal manuscript.
- Replace the planned-release paragraph in both manuscript editions with the completed paragraph. Cite a DOI as well if the release has been deposited in a DOI-issuing archive. [GitHub documentation on citing repository content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
