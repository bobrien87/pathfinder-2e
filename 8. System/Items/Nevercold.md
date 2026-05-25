---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

Nevercold, sometimes mistakenly referred to as nevercoal, is the charcoal left after wildfires in the First World. True to its name, nevercold remains warm to the touch. If you use nevercold to cast [[Fire Shield]], the spell's duration increases to 5 minutes, the cold resistance you gain from it lasts 1 hour, and you're immune to minor and severe cold for 8 hours.

The catalyst affects 4th-rank *fire shield*.

**Source:** `= this.source` (`= this.source-type`)
