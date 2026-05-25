---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
targets: "1 living creature"
defense: "Fortitude"
duration: "1 week"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You curse the target with a hunger no food can sate. You can Dismiss the spell. The target must attempt a Fortitude save.
- **Critical Success** The creature is unaffected and is temporarily immune for 1 hour.
- **Success** The creature is [[Fatigued]] for 1 round.
- **Failure** The creature is immediately afflicted by hunger as if it hadn't eaten food in days. It becomes fatigued and takes 1d4 damage each day that can't be healed until it sates its hunger. No amount of eating can sate the creature's hunger during the spell's duration.
- **Critical Failure** As failure, but the creature takes 2d4 damage each day from unbearable hunger.

**Heightened (+1)** The hunger becomes more intolerable, increasing the damage each day by 1d4, or by 2d4 on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
