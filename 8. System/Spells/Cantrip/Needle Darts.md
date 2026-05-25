---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shape three needles out of a piece of metal in your possession and send them flying in a tight group toward one target. Make a spell attack roll against your target's AC. The needles deal 3d4 piercing damage and might cause bleeding.

The needles impart any special properties of the metal that forms them; for instance, cold iron needles deal additional damage to creatures with weakness to cold iron. All the needles are made of the same metal, and the metal returns to you after the attack.
- **Critical Success** The target takes double damage and @Damage[(@item.level)[bleed]] damage.
- **Success** The target takes full damage.

**Heightened (+1)** You send one additional needle, increasing the regular damage by 1d4 and increasing the persistent bleed damage on a critical hit by 1.

**Source:** `= this.source` (`= this.source-type`)
