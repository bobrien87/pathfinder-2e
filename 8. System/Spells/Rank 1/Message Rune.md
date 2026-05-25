---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]", "[[Mental]]"]
cast: "5 minutes"
range: "touch"
targets: "1 flat unattended surface or non-magical object of light Bulk"
duration: "1 day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You record a message up to 5 minutes long and inscribe a special rune on any flat unattended surface or small object within reach. The nature of the rune's appearance is up to you, but it's visible to everyone, and it must be no smaller than 2 inches in diameter. You also specify a trigger that creatures must meet to activate the rune.

For the duration of the spell, creatures that meet the criteria of the trigger can touch the rune to hear the recorded message in their head as though you were speaking to them telepathically. You know when someone is listening to the message, but you don't know who's listening to it. You can Dismiss the spell.

**Heightened (+2)** The duration increases for every 2 ranks, becoming 1 week, 1 month, 1 year, or unlimited respectively.

**Source:** `= this.source` (`= this.source-type`)
