---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
traits: ["[[Curse]]", "[[Mental]]"]
cast: "1 day"
range: "10 feet"
targets: "1 creature of a level no greater than double the geas ritual's rank"
duration: "see text"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You enforce a magic rule on a willing target, forcing it to either perform or refrain from carrying out a certain act. A *geas* to perform an act is usually conditional, such as, "Always offer hospitality to strangers seeking a place to stay." An unconditional *geas* to perform a certain act doesn't require the target to perform that act exclusively, though it must prioritize the task above all leisurely pursuits. The most common *geas* to refrain from carrying out an act is a specification to avoid violating a contract. In those cases, the secondary caster usually takes charge of making sure the wording of the contract is attuned correctly with the ritual's magic. Because the target is willing, *geas* can have a duration that lasts for as long as the target agrees to. If the target is unable to fulfill the *geas*, it becomes [[Sickened]] 1, and the sickened condition increases by 1 for each consecutive day it is prevented from following the *geas*, to a maximum of sickened 4. The sickened condition ends immediately when it follows the *geas* again; it can't remove the sickened condition in any other way. Only powerful magic such as a [[Wish]] ritual can remove the effects of *geas* from a willing target.
- **Critical Success** The *geas* succeeds, and the target receives a +1 status bonus to skill checks that directly uphold the *geas* (at the GM's discretion).
- **Success** The *geas* succeeds.
- **Failure** The *geas* fails.
- **Critical Failure** The *geas* fails, and you are instead affected by the *geas* you were attempting to place on the target. You are considered an unwilling target, so the *geas* can be counteracted with a [[Cleanse Affliction]] spell.

**Heightened (5th)** You can use *geas* on an unwilling creature; it can attempt a Will save to negate the effect. If the target fails this Will save, the *geas* lasts up to 1 week. A *cleanse affliction* spell can counteract a *geas* on an unwilling creature, in addition to powerful magic such as a *wish* ritual. A clever unwilling creature can subvert the *geas* by contriving situations that prevent it from complying, but in that case it becomes [[Sickened]] (as described above).

**Heightened (7th)** As 5th rank, but the *geas* lasts for up to 1 year on an unwilling creature.

**Heightened (9th)** As 5th rank, but the *geas* lasts for a duration you choose (even unlimited) on an unwilling creature.

**Source:** `= this.source` (`= this.source-type`)
