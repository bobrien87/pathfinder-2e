---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Cold]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 4500}"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fur-lined *+2 greater resilient cold-resistant hide armor* is favored by warriors in the Crown of the World. In addition to providing excellent protection from extreme elements, the armor also enables you to erect massive walls of ice.

**Activate—Endure** `pf2:3` (concentration, manipulate, primal)

**Frequency** once per day

**Effect** You cast 5th-rank [[Environmental Endurance]] on yourself.

**Activate—Freeze Enemy** `pf2:3` (cold, concentration, manipulate, primal)

**Frequency** once per day

**Effect** You cast [[Wall of Ice]].

**Craft Requirements** Supply a casting of *environmental endurance* (5th rank) and *wall of ice*.

**Source:** `= this.source` (`= this.source-type`)
