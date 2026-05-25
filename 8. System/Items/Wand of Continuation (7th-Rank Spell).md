---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 15000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand increases a spell's duration. Yellow embers spiral over its surface until the spell ends.

**Activate** Cast a Spell; The activation takes `pf2:2` if the spell normally takes `pf2:1` to cast, or `pf2:3` if the spell normally takes `pf2:2`

**Frequency** Once per day, plus overcharge

**Effect** You Cast the Spell, and its duration is increased by half.

**Craft Requirements** Supply a casting of a spell of the appropriate rank. The spell must have a casting time of `pf2:1` or `pf2:2` and a duration no less than 10 minutes and no greater than 1 hour.

**Source:** `= this.source` (`= this.source-type`)
