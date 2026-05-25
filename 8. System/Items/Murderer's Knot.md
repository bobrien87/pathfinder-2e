---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 66}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You damage an [[Off Guard]] creature with a Strike using the affixed weapon

This black strand of leather is tied to look like a peace knot when the weapon is worn, but it doesn't hamper drawing the weapon. When you activate the knot, the creature you damaged takes 1d6 bleed damage and is off-guard until the bleed ends.

If you have the [[Twist the Knife]] feat, the talisman instead deals persistent bleed damage equal to your sneak attack damage.

**Source:** `= this.source` (`= this.source-type`)
