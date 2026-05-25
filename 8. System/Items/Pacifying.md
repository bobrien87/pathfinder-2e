---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 150}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune turns weapons into instruments of peacemaking.

**Activate** R (concentrate, mental)

**Trigger** You damage a creature with the etched weapon

**Effect** The damaged creature must succeed at a DC 20 [[Will]] save or be pacified. A pacified creature takes a –2 penalty to attack rolls on any attacks that aren't nonlethal for 1 minute, and the creature also experiences a clear psychic warning that they should stop making attacks that could kill.

**Source:** `= this.source` (`= this.source-type`)
