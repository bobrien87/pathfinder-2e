---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "30 feet"
duration: "sustained"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a simple illusory sound or vision. A sound adds the auditory trait to the spell and the sound can't include intelligible words or elaborate music. A vision adds the visual trait, can be no larger than a 5-foot cube, and is clearly crude and undetailed if viewed from within 15 feet. When you Cast or Sustain the Spell, you can attempt to [[Create a Diversion]] with the illusion, gaining a +2 circumstance bonus to your Deception check. If the attempt fails against a creature, that creature disbelieves the *figment*.

> [!danger] Effect: Spell Effect: Figment

**Source:** `= this.source` (`= this.source-type`)
