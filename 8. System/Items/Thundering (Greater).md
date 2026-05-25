---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]", "[[Sonic]]"]
price: "{'gp': 6500}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *thundering* weapon lets out a peal of thunder when it hits, dealing an extra 1d6 sonic damage on a successful Strike. On a critical hit, the target must succeed at a DC 34 [[Fortitude]] save or be [[Deafened]] permanently.

Sonic damage dealt by this weapon ignores the target's sonic resistance.

**Source:** `= this.source` (`= this.source-type`)
