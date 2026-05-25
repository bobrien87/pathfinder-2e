---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Disarm]]", "[[Finesse]]", "[[Nonlethal]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 350}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fleshy *+1 striking whip* is obviously crafted from the tentacle of some fearsome beast, likely an aqudel, and constantly strobes with small patterns of light.

**Activate** `pf2:1` (concentrate, occult, visual)

**Frequency** once per day

**Requirements** Your last action was a successful Strike, [[Grapple]], or [[Trip]] with the *alghollthu whip*

**Effect** Patterns on the skin of the whip strobe in a rapid pulse. The creature your attack succeeded against must attempt a DC 23 [[Will]] save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Dazzled]] until the end of your next turn.
- **Failure** The target is dazzled until the end of your next turn and [[Stunned]] 1.
- **Critical Failure** The target is dazzled until the end of your next turn and [[Stunned]] 2.

**Craft Requirements** The initial raw materials must include a tentacle from an aqudel.

**Source:** `= this.source` (`= this.source-type`)
