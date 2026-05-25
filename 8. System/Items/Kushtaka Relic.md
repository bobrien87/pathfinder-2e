---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 525}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add one action)

These relics come in many forms, as the only requirement is they were owned by a human who transformed into a kushtaka. Used as a catalyst for [[Spirit Blast]] against a target possessing another creature, a *kushtaka relic* attempts to banish such a spirit. A creature who fails the Fortitude save against *spirit blast* has its grasp on its possessed target weakened. The result of the possessed creature's next Will save against the possession effect is improved by one degree. A creature who is possessing another and critically fails the Fortitude save against *spirit blast* takes damage and then is banished from the body it was possessing.

**Source:** `= this.source` (`= this.source-type`)
