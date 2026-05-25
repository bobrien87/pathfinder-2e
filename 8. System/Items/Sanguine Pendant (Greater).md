---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 17000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This clear crystal pendant contains a drop of blood from a sorcerer that expands and contracts as you cast spells. A sanguine pendant is associated with a specific sorcerer bloodline, and only sorcerers with that bloodline can invest this item. This item gains the trait matching the tradition of that bloodline. The pendant grants a +3 item bonus to both of your bloodline skills.

**Activate—Blood's Call** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast a bloodline spell. If you don't spend this Focus Point by the end of this turn, it's lost.

**Craft Requirements** You're a sorcerer with the associated bloodline.

**Source:** `= this.source` (`= this.source-type`)
