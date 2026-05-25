---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 1250, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This semaphore set consists of two hardwood poles painted white, with finely crafted silk flags bisected by yellow and red fields. A tiny stylized black serpent with its tongue extended is depicted on the top outer corner of each flag. The semaphore of slanders, in addition to being a functioning semaphore set, can be used to send false signals to any enemy forces observing the signaler, providing a +2 item bonus to Deception checks to do so, and allies are always aware of this ruse.

**Activate—Insidious Insinuation** `pf2:2` (concentrate, emotion, fear, manipulate, mental, visual)

**Frequency** once per day

**Effect** You activate the semaphore to mislead the enemy. Choose a creature within 60 feet to attempt a DC 28 [[Will]] save saving throw.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Frightened]] 1.
- **Failure** The target is frightened 1 and is [[Off Guard]] for 1 round.
- **Critical Failure** The target is [[Frightened]] 2 and off-guard for 2 rounds.

**Source:** `= this.source` (`= this.source-type`)
