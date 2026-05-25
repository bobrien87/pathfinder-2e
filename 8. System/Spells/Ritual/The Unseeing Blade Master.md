---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Trial]]"]
cast: "1 day"
source: "Pathfinder Lost Omens Tian Xia World Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

There are many legends of blade masters who, not wanting to rely on flawed mortal eyes, learned to fight through reliance on both their other keen senses and knowledge from the universe itself. Those who intentionally seek out the path often do so by running through forms in thick clouds of incense.

Making a Strike against an enemy you can see is anathema to this ritual and immediately ends its benefits. If the ritual is ended in this way, you must conduct an [[Atone]] ritual before attempting this ritual again.
- **Critical Success** As success, except you can instead defeat an enemy in single combat that both uses a sword and is higher level than you.
- **Success** You call a blessing into your sword to guide you on the path and are bound by the ritual's anathema. Once you've used that sword against 20 enemies, each significant enough to grant XP, you gain the [[Blind Fight]] feat.
- **Failure** The incense is dispersed by a strange gust of wind and you learn nothing.
- **Critical Failure** The sword you're intending to use for the ritual becomes broken. If you aren't permanently blind, you're instead [[Blinded]] for 1 month and can't repeat this ritual during that time.

**Source:** `= this.source` (`= this.source-type`)
