---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
cast: "1 hour"
duration: "1 month"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You entreat the thunderbird in the Tusk Mountains to come to your aid. While performing this ritual, the secondary casters can appeal to the thunderbird's pride or tempestuous nature to gain a +2 circumstance bonus to their checks.
- **Critical Success** The thunderbird is helpful to the casters for the duration.
- **Success** The thunderbird is friendly to the casters for the duration.
- **Failure** The thunderbird ignores the entreaty and remains indifferent.
- **Critical Failure** The thunderbird takes offense and permanently departs the area.

**Source:** `= this.source` (`= this.source-type`)
