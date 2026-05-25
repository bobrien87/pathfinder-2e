---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]", "[[Unholy]]"]
price: "{'gp': 7}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

These bones from different types of demons can be used to form temporary barriers. When you crush the bone fragments and blow the resulting dust around yourself as you cast [[Shield]], the shield appears as a bone bulwark shaped like the demon's face.

When use Shield Block with the spell, the barrier explodes into many bone fragments. The shards cause 1d4 bleed damage to each creature adjacent to you that fails a DC 16 [[Reflex]] save. This persistent bleed damage is unholy and can be stopped with an Interact action to remove the shards.

**Source:** `= this.source` (`= this.source-type`)
