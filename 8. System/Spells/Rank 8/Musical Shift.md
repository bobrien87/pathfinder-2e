---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "20-foot emanation"
duration: "1 minute (sustained)"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a quick series of wrist flicks, music fills the air. While the music can be heard as if it were performed normally at a distance, creatures in the spell's area become affected in more significant ways. When you cast musical shift, select a key signature (to affect enemies) and a time signature (to affect allies) from the options below; all creatures within the area are affected as indicated. You can change the key signature or time signature as part of the action you take when you Sustain the spell.

**Flat** (key signature) Whenever an enemy critically fails at a Strike, saving throw, or skill check, they fall [[Prone]] in addition to other effects from the critical failure.

**Natural** (key signature) Enemies take a –2 status penalty to attack rolls.

**Sharp** (key signature) Whenever an enemy takes piercing or slashing damage, they also take 2d6 persistent bleed damage.

**Double** (time signature) You and your allies become [[Quickened]] and can use the extra action each round only for [[Leap]], Stand, Step, or Stride actions.

**Quadruple** (time signature) You and your allies gain a +2 status bonus to attack rolls.

**Triple** (time signature) You and your allies gain a +2 status bonus to Armor Class and Reflex saving throws.

> [!danger] Effect: Spell Effect: Musical Shift

**Source:** `= this.source` (`= this.source-type`)
