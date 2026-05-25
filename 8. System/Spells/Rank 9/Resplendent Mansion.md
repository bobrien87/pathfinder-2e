---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Structure]]"]
cast: "1 minute"
range: "500 feet"
duration: "until the next time you make your daily preparations"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a towering mansion up to four stories tall and up to 300 feet on a side. While Casting the Spell, you hold an image of the mansion and its desired appearance in your mind. The mansion can contain as many or as few rooms as you desire, and it's decorated as you imagine it. You can imagine a purpose for each room of the mansion, and the proper accouterments appear within. Any furniture or other mundane fixtures function normally for anyone inside the mansion, but they cease to exist if taken beyond its walls. No fixture created with this spell can create magical effects, but magical devices brought into the mansion function normally.

Your mansion contains the same types and quantities of foodstuffs and servants as created by the [[Planar Palace]] spell.

Each of the mansion's exterior doorways and windows are protected by [[Alarm]] spells. You choose whether each alarm is audible or mental as you Cast the Spell, and each has a different sound (for an audible alarm) or sensation (for a mental one), allowing you to instantly determine which portal has been used.

**Source:** `= this.source` (`= this.source-type`)
