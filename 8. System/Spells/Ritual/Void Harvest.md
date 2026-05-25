---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "9"
traits: ["[[Curse]]", "[[Mythic]]", "[[Void]]"]
cast: "8 hours"
range: "1-mile radius circle centered on you"
duration: "1 year"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The sky darkens over the affected area and the air becomes oppressive as you open a direct conduit to the Void, a plane of vast nothingness. Living creatures start to feel their life force draining away as the terror of oblivion begins to grip their hearts.

Each year on the anniversary of the ritual's casting, a total of four casters can spend 1 hour at the center of the affected area to sustain the effect. To do so, one caster must spend 1 Mythic Point and succeed at a Religion check against the ritual's casting DC. Each year the ritual is successfully sustained, the radius increases from its original point by 1 mile. The effect fades away if the check fails or if there are no other attempts to sustain the ritual.
- **Critical Success** As success, but living creatures in the area take a –2 status penalty to saves against death effects or effects that deal void damage.
- **Success** The first time each day a living creature in the area takes damage, it must succeed at a Will save with a DC equal to the ritual's casting DC or gain the [[Doomed]] 1 condition; if it already has the doomed condition, it instead increases the value of it by 1. Dead creatures can't be raised or resurrected so long as their body remains in the ritual's area. Undead creatures gain vitality resistance equal to their level while in the area.
- **Failure** The ritual has no effect.
- **Critical Failure** An explosion of energy from the Void washes over the casters. Each caster becomes [[Drained]] 4. This condition can't be removed for 1 week.

**Source:** `= this.source` (`= this.source-type`)
