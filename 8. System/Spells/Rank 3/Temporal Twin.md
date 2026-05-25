---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "one willing ally"
duration: "until the end of your next turn"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You pull a fleeting duplicate of your ally from the recent past. The duplicate appears in an unoccupied space of your choice within 30 feet of you and repeats a basic single action the target took since the end of your last turn, such as making a Strike or Interacting to pull a lever. Because the other basic single actions don't produce much of a result on their own, this is typically used for Strike and Interact, though occasionally it could be useful to have a *temporal twin* Stride through a potentially dangerous area to expose a hazard. Immediately after you cast this spell, the target ally spends a reaction to create the duplicate, makes any decisions, and rolls for the repeated action, such as choosing a target for a Strike and making the attack roll. If the ally doesn't have a reaction to spend, *temporal twin* fails. Use the duplicate's location for determining flanking, cover, and the like. Using this spell requires remembering what your ally did, and if you don't remember the details, the GM might not allow you to cast *temporal twin*.

This action can't be used for anything but a basic single action, nor can it use limited resources. The action can have a different target than the original action but must be very similar in form. For example, if the original action were to Interact to pull a lever, the time duplicate could pull a different lever but couldn't turn a doorknob or pick up an item from a table. Being pulled through time to create a twin destabilizes the target's timeline. Once an ally has been the target of *temporal twin*, they're temporarily immune for 1 day.

**Source:** `= this.source` (`= this.source-type`)
