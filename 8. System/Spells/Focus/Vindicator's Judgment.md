---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:1`"
range: "60 feet"
targets: "your hunted prey"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You pronounce a terrible judgment upon your quarry that causes all of your attacks and divine spells to strike with deadly efficacy. The target takes extra damage from your attacks, depending on the result of its Fortitude save. The spell ends immediately if the target is no longer your hunted prey.
- **Critical Success** The target is unaffected.
- **Success** The target has weakness 5 to the next Strike you make against it or damaging divine spell you cast that includes it as a target before the end of your next turn.
- **Failure** The target has weakness 5 to all Strikes you make against it or damaging divine spells you cast that includes it as a target for the duration of the spell.
- **Critical Failure** As failure, but the target is [[Off Guard]] against the first Strike or divine spell attack you make against it each round for the duration of the spell.

**Heightened (7th)** The weakness is 10.

**Heightened (9th)** The weakness is 15.

**Source:** `= this.source` (`= this.source-type`)
