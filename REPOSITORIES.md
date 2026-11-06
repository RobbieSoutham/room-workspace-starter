# Repository layout

This repository is the **workspace layer**: room boundaries, agent instructions, source-of-truth pointers and shared procedures. Keep application or research project source code in its own project repository.

```text
workspace/                       # this repository
  workflows/                     # room context and coordination notes
project-one/                     # separate project repository
  component-a/                   # optional independently versioned component
  component-b/                   # optional independently versioned component
```

When a project repository contains independently maintained components, use Git submodules and commit their pinned revisions in the parent project. Add them with `git submodule add <repository-url> <path>` and document the expected clone command (`git clone --recurse-submodules`).

If the components are not independently released, owned or reused, keep them as ordinary directories in the project repository. Avoid placing another repository's `.git` directory inside a project without declaring it as a submodule: the parent will not track that component's files or revision.

Keep this template generic. Do not add a specific project as a submodule here; project repositories should sit alongside the workspace repository or in a separate projects directory, and room documents should link to them.
