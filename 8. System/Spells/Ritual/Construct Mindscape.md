---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
traits: ["[[Illusion]]"]
cast: "1 day"
duration: "1 day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an entirely mental environment called an immersive mindscape. It can have any appearance you and the secondary casters imagine and hold in your minds as you execute the ritual. A mindscape is typically veiled, disguising its nature as a mental construct, but you can choose to make it overt. Even a veiled mindscape has some signs it's not a real place that can be revealed through close inspection or by spending a long time there. Most mindscapes are incapable of physically harming those inside. Even though the mindscape you create is limited in dimension, it appears to have a convincing environment around it, such as a sky and clouds.
- **Critical Success** You create a mindscape approximately a half-mile in length and width, and 50 feet in height (large enough to contain a typical village). The GM might allow you to make it larger if it has little detail, such as a grassy plain. You and any secondary casters of your choice can enter it and you can leave a doorway that you and any creatures you designate can pass through.
- **Success** As critical success, but the mindscape is approximately 25 feet in length, width, and height (like a modest house).
- **Failure** You can't hold the image together and it falls apart.
- **Critical Failure** Your secret desires horribly warp the mindscape into a distorted mirror of what you intended.

**Heightened (6th)** The duration is 1 week.

**Heightened (9th)** The duration is 1 year, and the area on a critical success is 1 mile in length and width.

**Heightened (10th)** The duration is unlimited, and the area on a critical success is 1 mile in length and width. The cost increases to 2,000 gp.

**Source:** `= this.source` (`= this.source-type`)
