---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "10"
cast: "1 day"
targets: "the mindscape"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

After you gather the anchors that make up the mindscape's structure, or in the case of anchors too immense to move, when you gain control over the region surrounding the anchors, you can perform this ritual to tear the mindscape apart from within. The ritual takes but a day to attempt, so those who would oppose such a destructive doom would do well to challenge the enemy by doing what they can to protect their mindscape's anchors. At the GM's discretion, the most powerful of mindscapes, such as those created by a deity, might be immune to this ritual's effects.

Over the course of this ritual's casting, you and the secondary casters unravel the basic and fundamental ideas of the mindscape's anchors. As you do so, flashes of memory tied to the anchor you target flood your mind, before the anchor itself dissipates. The mindscape might react with hostility to this process, manifesting creatures or swaying primary inhabitants to stop you. Regardless of how many anchors in all must be dismantled, it always takes a day to perform this ritual.
- **Critical Success** The mindscape is destroyed, and you and the secondary casters are returned to the plane from which you hailed before entering the mindscape.
- **Success** The mindscape is destroyed, but you and the secondary casters are scattered randomly to locations on other planes.
- **Failure** The mindscape is not destroyed, and you and the and the secondary casters are scattered randomly to locations on other planes.
- **Critical Failure** The mindscape is not destroyed, and you and the secondary casters become [[Drained]] 3 and are then each plunged into separate mindscapes. You remain trapped therein until you engineer each of your own escapes. You forget the destroy mindscape ritual and must discover it again if you wish to pursue this goal once more.

**Source:** `= this.source` (`= this.source-type`)
