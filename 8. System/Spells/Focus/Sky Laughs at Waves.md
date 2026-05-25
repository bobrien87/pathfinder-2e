---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Magus]]", "[[Manipulate]]"]
cast: "`pf2:1`"
requirements: "You're wielding a one-handed weapon in the sword group."
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** You're wielding a one-handed weapon in the sword group.

You soar and leave the world's squabbles behind before your violent intentions ground you once more. Fly up to your Speed, then make a Strike with your sword against an adjacent creature at the end of your movement. If you don't have any other means of flying, you fall after the Strike. If you can't end your movement adjacent to an enemy, this spell is disrupted.

**Source:** `= this.source` (`= this.source-type`)
