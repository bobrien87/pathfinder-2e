---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
traits: ["[[Mental]]"]
cast: "1 day"
range: "30 feet"
targets: "1 creature"
duration: "unlimited"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Severing ties with a member of a cult courts danger and threatens to undermine the secrecy of the group, whether that secrecy protects its worshippers or enables them to operate in the shadows. Many cults end their association with a wayward member on the edge of a blade, but there are options that preserve both secrecy and the life of the expelled member. An oblivious expulsion removes knowledge of the cult but is time-consuming enough that a cult usually reserves it for only the most well-regarded members who nevertheless need to be removed-or for sleeper agents the cult wishes to place among society and activate later.

It's difficult to cast this ritual unless the target is willing or [[Restrained]]. If the creature is unwilling to accept the ritual, it can attempt a Will save to negate the effect. The effects of the ritual depend on the results of your Occultism check.
- **Critical Success** The ritual removes all memories of the cult's activity, practices, and secrets from the target's memory. The target remembers only what an average citizen of the larger society would know, which is typically nothing or a few rumors with very little detail. The spell is hard to detect: a [[Detect Magic]] spell or similar effect must be a higher rank than *oblivious expulsion* to detect it. You can Dismiss the spell. While casting the spell, you can choose to give the secondary casters the ability to Dismiss it. You can also choose to set a key phrase or event that causes the spell to be Dismissed. When the target witnesses this phrase or event, the spell immediately ends.
- **Success** As critical success, except the spell isn't harder to detect with *detect magic*.
- **Failure** The ritual fails.
- **Critical Failure** The ritual fails, and the target is temporarily immune for 1 month.

**Source:** `= this.source` (`= this.source-type`)
