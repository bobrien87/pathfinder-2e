---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You can't be seen. You're [[Undetected]] to everyone. Creatures can [[Seek]] to detect you; if a creature succeeds at its Perception check against your Stealth DC, you become [[Hidden]] to that creature until you [[Sneak]] to become undetected again. If you become invisible while someone can already see you, you start out hidden to them (instead of undetected) until you successfully Sneak. You can't become [[Observed]] while invisible except via special abilities or magic.

**Source:** `= this.source` (`= this.source-type`)
