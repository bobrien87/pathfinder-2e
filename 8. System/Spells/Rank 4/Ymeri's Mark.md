---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Detection]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "basic Reflex"
duration: "varies"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You place the fiery mark of the Queen of the Inferno on the target, burning into the creature's very essence. The mark gives off a heat that only you can sense; as long as you're on the same plane as the target, you can sense the direction it's in. The target is [[Fatigued]] and can't reduce the value of this condition normally.

You can detonate the mark at any point during its duration by Dismissing the spell. The rune explodes in a @Template[emanation|distance:10] centered on the target that deals 5d6 fire damage with a basic Reflex save. You choose whether the mark's target is included in the explosion.

When you cast the spell, the target attempts a Fortitude save to determine how long the mark lasts. If the spell's duration elapses, the rune doesn't detonate.
- **Critical Success** The target is unaffected.
- **Success** The duration is 1 minute.
- **Failure** The duration is 1 week.
- **Critical Failure** The duration is unlimited.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
