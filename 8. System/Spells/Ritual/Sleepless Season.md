---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Curse]]", "[[Mental]]"]
cast: "4 hours"
range: "5 miles"
area: "5280-foot square"
duration: "1 week"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You attempt to inflict a curse of sleeplessness upon individuals in the target area to weaken their resolve, possibly making it easier to conquer them. As you successfully complete the ritual, the amethyst pendant crumbles into sand that travels on an unfelt wind to drift down onto the target area. Each living creature in the target area must attempt a Fortitude saving throw against the ritual's casting DC or become unable to gain the benefits of a full night's rest for 1 week. The curse can be removed before that time with cleanse affliction or similar magic.
- **Critical Success** Sleep is unattainable for anyone in the target area who fails the saving throw. As usual, a living creature who goes more than 16 hours without sleeping becomes [[Fatigued]]. A target who becomes fatigued in this way is also [[Enfeebled]] 1; the value of this condition can't be reduced while they're fatigued. For every subsequent day an affected target is fatigued, the value of their enfeebled condition increases by 1 (to a maximum of 4).
- **Success** Sleep can only be caught in short bursts for anyone in the target area who fails the saving throw. As critical success, but a fatigued target doesn't become enfeebled.
- **Failure** The ritual has no effect.
- **Critical Failure** The notion of sleep itself abandons the casters. The casters become fatigued and can't gain the benefits of a full night's rest for 1 month. This is a curse effect.

**Source:** `= this.source` (`= this.source-type`)
