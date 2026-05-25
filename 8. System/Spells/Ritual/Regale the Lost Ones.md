---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
cast: "4 hours"
targets: "a settlement with a level equal to or lower than twice the ritual's level"
duration: "1 year"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Autumn's shorter days herald an increase in hauntings, which only intensify during winter's cold, dark nights. As fall draws to a close, some of Shenmen's villages hire or set up Tian opera troupes to enact *regale the lost ones* rituals, where they perform dramas drawn from literary classics and historical events that incorporate acting, music, acrobatics, and martial arts.

These ritual performances fulfill a dual purpose; not only do they bring cheer to the living, but they also entertain and placate the "lost ones"—a euphemism for ghosts and other spirits—and seek to reduce the likelihood of attacks from such entities. Performing this ritual during the season of fall reduces the DCs of the ritual's skill checks by 2.

If the ritual is successful, sentient undead and other spirits become less hostile, allowing villagers to focus their efforts on dealing with mindless undead and other more physical threats. This ritual can only be attempted once per year per settlement; additional attempts to *regale the lost ones* in the same settlement automatically result in a critical failure.
- **Critical Success** Haunts and undead in the settlement that are level 3 or lower become easier to defeat. Reduce all Disable DCs for affected haunts in the settlement by 2, and all affected undead within the settlement begin combat [[Frightened]] 1. If the PCs perform this ritual during Act 2 or Act 3, they gain 3 Hope Points.
- **Success** Haunts in the settlement that are level 3 or lower become easier to notice and defeat. Reduce all Disable DCs for affected haunts in the settlement by 1. If the PCs perform this ritual during Act 2 or Act 3, they gain 1 Hope Point.
- **Failure** The ritual has no effect.
- **Critical Failure** Haunts and undead in the settlement that are level 3 or lower become more difficult to notice and defeat. Increase all Disable DCs for affected haunts in the settlement by 2, and all affected undead within the settlement gain the elite adjustment. If the PCs perform this ritual during Act 2 or Act 3, they lose 3 Hope Points.

**Heightened (+1)** Increase the level of affected haunts and undead by 2.

**Source:** `= this.source` (`= this.source-type`)
