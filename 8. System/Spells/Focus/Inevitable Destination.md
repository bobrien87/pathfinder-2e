---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "you and 1 enemy"
defense: "Will"
duration: "2 rounds"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You twist the paths of the target, ensuring that each one leads to you. The target attempts a Will saving throw.
- **Critical Success** The spell has no effect.
- **Success** Your pull hampers the target's footsteps. It takes a –10-foot circumstance penalty to its Speeds until the end of its next turn.
- **Failure** The target can't move any farther from you than it was when you Cast the Spell, though it can move in such a way that it maintains an equal distance. If you move farther away from the target than the initial distance, the spell ends. The targeted foe can attempt to [[Escape]] against your spell DC. If it succeeds, the spell ends.
- **Critical Failure** As failure, plus the target is pulled 10 feet closer to you and falls [[Prone]], tripping in its haste to move toward you.

**Source:** `= this.source` (`= this.source-type`)
