---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Fatal d12]]", "[[Magical]]"]
price: "{'gp': 140}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking greatpick* bears a head studded with the tusks of a trollhound.

**Activate—Ravenous Strike** `pf2:2` (magical, manipulate)

**Effect** You Strike with the *trollhound pick*, transferring a portion of a trollhound's legendary appetite to the target. A living enemy who takes damage from the attack must attempt a DC 19 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature suffers hunger pangs, becoming [[Off Guard]] for 1 round.
- **Failure** The creature experiences gnawing hunger, becoming off-guard for 1 round and [[Enfeebled]] 1 for 1 minute. If the creature consumes any amount of food or drink (including imbibing a potion), the enfeebled condition ends.
- **Critical Failure** As failure, but the creature is [[Enfeebled]] 2 and each instance of consuming food or drink reduces the penalty by 1.

**Craft Requirements** The initial raw materials must include the teeth and tongue from a trollhound.

**Source:** `= this.source` (`= this.source-type`)
