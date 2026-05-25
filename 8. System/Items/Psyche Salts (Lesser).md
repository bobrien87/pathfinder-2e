---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #214: The Broken Palace"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A dose of psyche salts is kept in a small, corked vial. When you activate psyche salts, you uncork and pass the open end of the vial near the head of an adjacent creature. The salts within fizz and evaporate, creating a sour-smelling cloud that envelops the creature's head before fading. As they do, the vapors attempt to clear harmful influences from the creature's mind. The creature gains the effect of a 2nd-rank [[Clear Mind]] spell with a +11 counteract check modifier and a +1 item bonus to saving throws against mental effects for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
