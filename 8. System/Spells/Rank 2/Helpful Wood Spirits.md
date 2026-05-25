---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Upon casting this spell, a cluster of little wood spirits tumbles into the area. They perform a simple task each round. These spirits are a magical echo of the true spirits that live on the Plane of Wood and can't be attacked, damaged, or otherwise interfered with. These spirits often look like kodama but can appear in any of the countless varieties of wood spirits that inhabit the Plane of Wood.

Choose the kind of aid your wood spirits supply from the list below when you Cast the Spell. The first time each round you Sustain the spell, you can move the area occupied by the apparitions up to 10 feet and you can choose the kind of aid they provide this round.

- **Chores** The wood spirits perform a minor manual task of your choice, such as cleaning, opening a door, picking up an unattended object, or carrying an object from one location to another. The spirits can't pick up or carry an object of greater than 2 Bulk.

- **Distract** The wood spirits distract your foes, clambering all over their feet and bodies and being a nuisance. Creatures in the area are [[Off Guard]] unless they succeed at a Reflex save.

- **Obstacle** The wood spirits fill the area as a chaotic, bouncing mass. The area they occupy is difficult terrain.

- **Search** The wood spirits [[Seek]] in the area they occupy, using your Perception check as their own. You learn anything they do from Seeking in this way.

**Source:** `= this.source` (`= this.source-type`)
