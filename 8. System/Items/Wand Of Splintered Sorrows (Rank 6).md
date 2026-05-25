---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Magical]]", "[[Manipulate]]", "[[Wand]]", "[[Wood]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden wand is roughly cut, as if it had been crudely chopped from a tree and left forgotten. When held, the wand imparts feelings of deep sorrow.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Splinter Volley]] of the indicated rank. Each splinter contains some of the despair felt by cruelly harvested trees, causing any creature damaged by this spell to become [[Stupefied 2]] for a number of rounds equal to the spell rank. On a critical success on the attack roll, the target also weeps, becoming [[Slowed]] 1 for the same duration.

**Craft Requirements** Supply a casting of *splinter volley* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
