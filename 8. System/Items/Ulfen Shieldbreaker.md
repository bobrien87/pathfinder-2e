---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Sweep]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The axe and shield are signature weapons of war and powerful cultural symbols for the Ulfen people. Duels among Ulfen warriors that don't end in death are traditionally called when one of the combatants' shield shatters, leading experienced warriors to take as much pride in the resilience of their shields as the sharpness of their axes. This has led to something of an ongoing rivalry between Ulfen armorers seeking to craft unbreakable shields and those seeking to forge unstoppable weapons, with this distinctively bearded *+1 striking battle axe* representing the current pinnacle of the latter group's craft.

When you damage a raised shield with an *Ulfen shieldbreaker*, your attack ignores the shield's first 3 points of Hardness. If the damage is not fully mitigated by any remaining Hardness, the shield takes an additional 1d6 slashing damage from the attack. This damage ignores all Hardness.

**Activate—Battering Blow** `pf2:f`

**Trigger** Your melee Strike with the Ulfen shieldbreaker reduces an enemy's shield below its Broken Threshold

**Effect** The force of your blow threatens to knock your opponent to the ground. Attempt an Athletics check to [[Trip]] the target of the triggering attack. If your attack was powerful enough to destroy the shield outright, you gain a +2 circumstance bonus to the roll.

**Source:** `= this.source` (`= this.source-type`)
