---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
cast: "1 hour"
range: "20 feet"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You officiate the creation of a magical bond between two or more willing creatures, who are secondary casters of the ritual and must share genuine affection for one another. As part of the ritual, all members of the bond receive a ring, amulet, or similar token to symbolize their shared connection. They lose the effects of the ritual when not wearing the token, and the bond is broken if either token is destroyed.

Creatures benefiting from a successful heartbond ritual can later participate in a heightened version of the ritual without requiring new checks by spending the required time and paying the difference of the two costs. A creature can be under the effects of multiple heartbond rituals at once.
- **Critical Success** Once per day, each bonded creature can use a 2-action activity, which has the concentrate trait, to learn the present state of one other bonded creature. The creature knows the other creature's direction and distance and any conditions affecting them. Each participant can cast message as a divine innate spell at will, but can target only another participant.
- **Success** As a critical success, except the bonded creatures can't cast message as a divine innate spell.
- **Failure** The ritual has no effect.
- **Critical Failure** Magical backlash creates discordant energy among the participants. For 1 week, each secondary caster is [[Clumsy]] 2 and [[Stupefied 2]] whenever they are within 30 feet of another secondary caster.

**Heightened (6th)** The cost increases to 300 gp per secondary caster. On a success, secondary casters permanently gain the effects of a 6th-rank telepathy spell, but only with each other

**Source:** `= this.source` (`= this.source-type`)
