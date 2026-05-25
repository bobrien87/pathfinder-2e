---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
targets: "1 living creature"
defense: "Fortitude"
duration: "1 day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You curse the target with a thirst no drink can quench. You can Dismiss the spell. The target must attempt a Fortitude save.
- **Critical Success** The creature is unaffected and is temporarily immune for 1 hour.
- **Success** The creature is [[Fatigued]] for 1 round.
- **Failure** The creature is immediately afflicted by thirst as if it hadn't had a drink in days. It becomes Fatigued and takes 1d4 damage each hour that can't be healed until it quenches its thirst. No amount of drinking can quench the creature's thirst during the spell's duration.
- **Critical Failure** As failure but the creature takes 2d4 damage each hour.

**Heightened (+3)** The thirst becomes more unbearable, increasing the damage each hour by 1d4, or by 2d4 on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
