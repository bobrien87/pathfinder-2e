---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 275}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` envision

**Trigger** You are [[Dying]] at the beginning of your turn.

Carved from an arboreal's knuckle, this wooden torus can be activated despite your being [[Unconscious]]. The knot then sprouts several roots that arch over your body like a spider's legs. These lift you a few inches off the ground before Striding and carrying you with them. The roots prioritize taking you away from obvious harm, though as a reaction, an ally who speaks Arboreal can command the roots to carry you to a particular point within range.

After moving, the roots continue protecting you; this counts as Raising a Shield, giving you a +1 circumstance bonus to AC until the beginning of your next turn. The roots use the [[Shield Block]] reaction against the first physical attack against you, after which the roots crumble.

The roots carry you up to 15 feet and have Hardness 10.

**Source:** `= this.source` (`= this.source-type`)
