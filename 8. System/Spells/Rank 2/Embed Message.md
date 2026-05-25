---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 object or willing creature"
duration: "unlimited"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You specify a trigger and a message up to 25 words long. When the specified trigger occurs within 30 feet of the target, illusory text of your message circles the target accompanied by a disembodied voice. You can choose a language you know for the text and speech, and can choose what the voice sounds like. Once the message is completed, the spell ends.

**Heightened (4th)** You can add a simple sensory component to emphasize the message, such as an odor, visual effect, or physical sensation. This addition is obviously illusory and part of the message, lasting only while the message is being read.

**Heightened (6th)** As 4th rank, but you can choose how many times the spell repeats the message before it ends; there is no limit to the number of repetitions.

**Source:** `= this.source` (`= this.source-type`)
