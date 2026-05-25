---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Deviant]]", "[[Magical]]", "[[Plant]]", "[[Wood]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You're the target of a physical attack.

You grow a shield of woven flowers and branches, then Raise that Shield to defend yourself from the triggering attack. If you would take damage from the attack, you immediately [[Shield Block]]. This is a [[Wooden Shield]] (Hardness 3, HP 12, BT 6). The shield remains in your possession for a number of rounds equal to your level, or until it's destroyed.

**Awakening** The shield becomes stronger. It has Hardness 5, HP 40, BT 20.

**Awakening** The shield takes on a mind of its own and lashes out vengefully when destroyed. When the shield is destroyed, is explodes, dealing 4d6 piercing damage to your attacker, with a [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
