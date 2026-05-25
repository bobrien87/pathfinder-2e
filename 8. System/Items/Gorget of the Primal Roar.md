---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1250}"
usage: "worncollar"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This engraved duskwood gorget seems to vibrate with ferocity, granting you a +2 item bonus to Intimidation checks.

**Activate—Primal Roar** A (auditory, concentrate, emotion, fear, mental)

**Frequency** once during the duration of each polymorph effect

**Requirements** You're in a non-humanoid form via a polymorph effect

**Effect** You unleash a bestial roar, attempting a single [[Intimidation]] check compared to the Will DCs of all enemies within 30 feet to impose the effects below.
- **Critical Success** The creature is [[Frightened]] 2.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is unaffected.

**Source:** `= this.source` (`= this.source-type`)
