---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Integrated 1d6 s versatile p]]", "[[Magical]]"]
price: "{'gp': 3700}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking wounding klar* (Hardness 13, HP 100, BT 50) is built with spikes made of beasts' fangs.

**Activate** `pf2:f` (concentrate)

**Frequency** once per round

**Trigger** You or a creature within 30 feet of you suffers bleed damage

**Effect** The sanguine klar regains a number of Hit Points equal to the bleed damage, up to an amount equal to its Hardness.

**Source:** `= this.source` (`= this.source-type`)
