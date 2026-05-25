---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Flexible]]", "[[Invested]]", "[[Magical]]", "[[Noisy]]"]
price: "{'gp': 430}"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 chain mail* is most commonly worn by mid-level leaders in charge of squads or platoons of soldiers and was designed to enable them to relay and receive tactical information from their commanders.

**Activate—Mail Delivery** `pf2:1` (concentrate, manipulate, occult)

**Frequency** once per hour

**Effect** You cast [[Message]] as a 3rd-rank spell.

**Craft Requirements** Supply a casting of *message* (3rd rank).

**Source:** `= this.source` (`= this.source-type`)
