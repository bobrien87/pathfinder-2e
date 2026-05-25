---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
traits: ["[[Illusion]]"]
cast: "1 hour"
range: "touch"
targets: "yourself and up to 5 willing creatures"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You project the targets into an immersive mindscape or cause them to exit one. You must be aware the mindscape exists, though you don't need to know specifics. The casters must be in physical contact with one another in a circle for the duration of the casting and all targets must be selected from these casters. Your bodies typically remain behind in stasis when you enter a mindscape, though some mindscapes pull you entirely into them upon entrance. If you enter a mindscape, you can leave only by using another mindscape door ritual, finding an exit within the nature of the mindscape, or when the mindscape ceases to exist. When exiting a mindscape, you typically return to your bodies or to the location where you entered the mindscape. If the mindscape's creator wants to prevent anyone from entering or exiting, the DC of the primary check is the creator's Will DC if that would be higher than the ritual's normal DC.
- **Critical Success** You transport the creatures as you intended and can leave a portal that lasts for an unlimited duration. It typically looks like an ordinary door or passage appropriate to the mindscape. Any target of the spell can enter or exit through this portal as they would an ordinary door. If you wish, you can make the door passable by anyone.
- **Success** You transport the creatures as you intended.
- **Failure** You fail to enter or exit the mindscape.
- **Critical Failure** Something goes horribly wrong. The GM decides whether mental feedback deals 9d6 mental damage to all ritual casters (DC 26 [[Will]] save) or 1d4 casters are unwillingly pulled into the mindscape (or ejected from it).

**Heightened (8th)** The ritual targets up to 100 willing creatures, the critical failure damage increases to 20d6, and the critical failure save DC increases to 40.

**Source:** `= this.source` (`= this.source-type`)
