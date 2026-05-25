---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple doll is made with scraps of cloth tied or sewn together into a basic humanoid shape, but its appearance belies its strange power over the actions of others. The head and limbs of the doll constantly droop and sway slightly, never able to remain in one position for very long. Whoever holds a *floppy rag doll* can feel it squirming in their grasp.

**Activate—Loose Limbs** `pf2:1` (manipulate, visual)

**Frequency** once per hour

**Effect** You brandish the *floppy rag doll* at a creature within 30 feet who can see you and shake it about. The creature's own limbs begin moving wildly in a similar fashion, and they must attempt a DC 19 [[Will]] save saving throw.
- **Critical Success** The target is unaffected.
- **Success** The target can't use reactions until the end your turn.
- **Failure** The target is [[Clumsy]] 1 and can't use reactions until the beginning of your next turn.
- **Critical Failure** As failure, but [[Clumsy]] 2

**Source:** `= this.source` (`= this.source-type`)
