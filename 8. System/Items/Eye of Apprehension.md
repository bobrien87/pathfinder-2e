---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Fortune]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 400}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You are about to roll Perception for initiative but haven't rolled yet

**Requirements** You are a master in Perception

This round piece of cymophane's silky inclusion makes it look like a cat's eye. While affixed, it makes you jittery.

When you activate it, roll Perception twice and use the higher result.

**Source:** `= this.source` (`= this.source-type`)
