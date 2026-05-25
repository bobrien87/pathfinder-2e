---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This short bronze rod has the form of a serpent coiled around it. While you hold it, you gain a +1 item bonus to Medicine checks.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Requirements** You have the [[Battle Medicine]] action

**Effect** You use Battle Medicine. The target is temporarily immune to your Battle Medicine for 1 hour instead of 1 day.

**Source:** `= this.source` (`= this.source-type`)
