---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 200}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

On certain rare occasions, when a particularly despoiled tree or a powerful demonic fungal infestation (such as a Jeharlu Spore) is destroyed, the grimy black ash that remains behind functions as a catalyst called black ash. A [[Wall of Thorns]] empowered with this catalyst gains the fungus trait and appears diseased and toxic, with greasy filaments of dripping fungus growing through its vines. A creature damaged by this wall's thorns takes an additional 2d6 persistent,poison.

**Source:** `= this.source` (`= this.source-type`)
