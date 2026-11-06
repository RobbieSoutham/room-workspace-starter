# Source-of-truth map

Each topic should have one canonical home. Other documents should link to it rather than keep competing copies.

| Information | Canonical location | Update rule |
|---|---|---|
| Room purpose, boundaries and conventions | `workflows/<room>/CONTEXT.md` | Change when the room's remit or conventions change |
| Active work and next steps | `workflows/<room>/CURRENT.md` | Update as work starts, changes or completes |
| Durable room knowledge | `workflows/<room>/knowledge/` | Add only reusable facts, decisions and procedures |
| Cross-room durable memory | `MEMORY.md` | Keep brief; link to room-owned sources |
| Shared procedures and decision rules | `PROTOCOLS.md` | Version material changes and record the effective date |
| Room names and ownership | `ROOMS.md` | Update when rooms are added, renamed or re-scoped |
| Project repository boundaries and component versioning | `REPOSITORIES.md` and the project's own repository metadata | Keep project source out of this workspace template |

If ownership is unclear, do not silently create a second canonical copy. Resolve the owner, then update this map.
