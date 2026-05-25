---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Acid]]", "[[Consumable]]", "[[Talisman]]", "[[Water]]"]
price: "{'gp': 100}"
usage: "affixed-to-melee-weapon"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a melee weapon

**Activate** R (concentrate)

**Prerequisites** You're an expert with the affixed weapon

**Trigger** A creature in reach of the weapon takes an action with the concentrate trait.

Brine dragons are known to distract their foes at just the right moment, and this blue-green scale appears to have come from one of these creatures. When you activate the scale, it cracks open and releases a spray of caustic saltwater at the triggering creature. The creature takes 2d8 acid damage with a DC 24 [[Reflex]] save. If the creature critically fails at its save, its concentration is broken—the triggering action is disrupted.

**Source:** `= this.source` (`= this.source-type`)
