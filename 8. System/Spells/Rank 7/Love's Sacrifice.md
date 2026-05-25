---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "one creature"
defense: "Will"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You take damage that would reduce you to 0 Hit Points.

You cry out for aid, and a creature near you feels compelled to throw itself in front of the threat as the ultimate expression of their love. A target that genuinely loves the caster without magical compulsion, at their player's or the GM's discretion, fails the save.
- **Critical Success** The target is unaffected.
- **Success** The creature moves adjacent to you, moving further than its Speed if necessary as the magic compels it to exceed its limits. It takes half the damage you would have taken, while you take the rest. If you would be reduced to 0 Hit Points, you're reduced to 1 instead.
- **Failure** As success, except they take the full damage. If the damage reduces them to 0 Hit Points, they immediately die; this is a death effect.

*PFS Note:* This spell can only be cast on a friendly NPC with GM approval, and on a PC with their player's approval.

**Source:** `= this.source` (`= this.source-type`)
