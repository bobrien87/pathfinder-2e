---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "wornbracers"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Etchings of powerful bears decorate these brass bracers. You gain a +3 item bonus to Athletics checks and a +2 circumstance bonus to Athletics checks to lift a heavy object, [[Escape]], and [[Force Open]]. When you invest the bracers, you either increase your Strength modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate—Bear Hug** `pf2:1` (manipulate)

Attempt to [[Grapple]] a creature. If you succeed, you crush the creature in your grasp, dealing @Damage[(@actor.abilities.str.mod)[bludgeoning]]{bludgeoning} damage to it equal to your Strength modifier. If you critically succeeded, the damage is equal to double your Strength modifier, and the creature suffocates as long as it remains [[Grabbed]] or [[Restrained]] by you.

**Source:** `= this.source` (`= this.source-type`)
