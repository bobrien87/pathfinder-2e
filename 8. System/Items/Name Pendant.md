---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Many soldiers wear this metal pendant engraved with their name and critical details. Sadly, they also ascertain the identity of fallen soldiers. Many soldiers find that the pendant helps them stay grounded. When you wear your name pendant, you gain a +1 bonus to saving throws against spells and magical effects with the mental trait.

**Activate—Alert Superior Officer** `pf2:f`

**Frequency** once per day

**Trigger** You gain the [[Dying]] condition

**Effect** The pendent alerts all other allies within 500 feet who are also wearing a name pendant.

**Source:** `= this.source` (`= this.source-type`)
