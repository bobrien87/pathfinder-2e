---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]", "[[Metal]]"]
price: "{'gp': 360}"
usage: "held-in-one-or-two-hands"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

In its base form, this armament looks like a smooth bar of soft, gleaming metal shaped like a horseshoe. Its ability to adjust to any battle situation makes it a popular weapon for elite warriors of the Plane of Metal. It can be shaped into a melee weapon using its shifting rune, but it can shift only into weapons primarily made of metal or back to its base shape. In weapon form, it's a *+1 striking shifting* weapon.

**Activate**—Reshape `pf2:1` (concentrate)

**Frequency** once per 10 minutes

**Effect** Strike with the morphing weapon, choosing one of the following benefits to apply to the Strike.

**Reach** Increase the reach by 5 feet.

**Shift** The weapon's damage becomes your choice of bludgeoning, piercing, or slashing instead of its normal type.

**Take** If the Strike hits, you can attempt to [[Disarm]] or [[Steal]] from your target immediately after as a reaction.

**Weigh** Gain a status bonus to the damage roll equal to the weapon's number of damage dice.

**Source:** `= this.source` (`= this.source-type`)
