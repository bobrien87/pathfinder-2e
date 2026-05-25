---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[Extradimensional]]", "[[Healing]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "1 minute"
range: "30 feet"
targets: "you and up to 6 willing creatures"
duration: "10 minutes"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a pathway to paradise, visible only to you and your allies through a dense cloud of magical mist. You and the other targets within range are transported through this mist to an extradimensional paradise of idyllic geographical features. Creatures within this paradise don't need to eat or drink. For each minute you spend within this paradise, all creatures within experience the benefits of 24 hours passing, gaining the healing benefits of a full night's rest, as well as the elapse of any afflictions or spells with day-long intervals. However, for any afflictions or spells with intervals measured in shorter periods of time, only one of those intervals passes for every minute spent within the paradise. This means that at the end of a minute, a creature can attempt a saving throw against a disease whose interval is 1 day, a poison whose interval is 1 minute, and a harmful spell that allows a saving throw each round. Each saving throw attempted while within the paradise gains a +4 status bonus.

You and your allies can act normally while within the paradise and can use the time to cast spells, Refocus, or perform other exploration activities that take less than 10 minutes. When the spell ends, you and all other targets depart the paradise, returning through the mists to your previous locations or in the nearest unoccupied spaces. You can Dismiss this spell.

**Source:** `= this.source` (`= this.source-type`)
