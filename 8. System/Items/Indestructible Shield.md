---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]"]
price: "{'gp': 24000}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *indestructible shield* is a *high-grade greater reinforcing adamantine shield* (Hardness 17, HP 136) that can withstand just about any damage. It can be damaged only by a [[Disintegrate]] spell (roll damage as if against a creature that failed its save) or by an artifact tied to destruction.

**Craft Requirements** The raw materials must include at least 4,400 gp of adamantine.

**Source:** `= this.source` (`= this.source-type`)
