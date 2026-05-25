---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Force]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause any spells cast on the target to spill out their energy in harmful surges. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** Whenever the target becomes affected by a spell with a duration, the target takes 2d12 persistent,force damage. Each time it takes persistent force damage from *spellwrack*, it reduces the remaining duration of spells affecting it by 1 round. Only a successful [[Arcana]] check against your spell DC can help the target recover from the persistent damage; the curse and the persistent damage end after 1 minute.
- **Failure** As success, but the curse and persistent damage do not end on their own.
- **Critical Failure** As failure, but the persistent force damage is 4d12 persistent,force.

**Source:** `= this.source` (`= this.source-type`)
