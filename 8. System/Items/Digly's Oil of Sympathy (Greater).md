---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This thick, red liquid has a pungent—but not unpleasant—smell. You pour the oil onto a weapon when activating it. If the weapon has damaged a creature within the last 10 minutes, the most recent creature damaged by the weapon regains @Damage[(6d10+20)[healing]] Hit Points. The creature is then temporarily immune to *Digly's oil of sympathy* for 10 minutes.

The magic relies on the malice behind the attack, so the weapon must have been used against an enemy of the attacker. In other words, someone can't voluntarily take damage from a friend's weapon, then heal from it—a fact that made it very difficult for Sir Kenelm Digly to test the oil during its development.

**Source:** `= this.source` (`= this.source-type`)
