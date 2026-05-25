---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "5-foot emanation"
targets: "you and allies in the area"
duration: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You recall memories of hedonistic rites to send yourself into an infectious frenzy, dancing and howling wildly to encourage your companions to join in. You and your allies gain a +1 status bonus to saving throws against mental effects while in the area. Whenever someone benefiting from this bonus critically succeeds at a saving throw against an enemy's mental effect, its revelry increases, granting it a +1 status bonus to attack rolls and damage rolls for 1 round.

> [!danger] Effect: Spell Effect: Frenzied Revelry

**Heightened (4th)** The emanation's radius is 10 feet, and the status bonus to saves is +2.

**Heightened (7th)** The emanation's radius is 15 feet, and the status bonus to saves is +3.

**Source:** `= this.source` (`= this.source-type`)
