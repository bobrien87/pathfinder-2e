---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "9"
cast: "1 hour"
duration: "3 hours"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

When several companions or followers have reached a point of undying love and trust in you, they might be willing to die to save your life. You can grant them that wish. The secondary casters must be living creatures willing to sacrifice their energy to you, by allowing their life essence to drain out of them to protect you whenever you're in danger. If you're undead, the secondary casters must be undead instead, and if you're neither living nor undead, you can't cast vital singularity. Whenever you take damage, after calculating the total amount of damage, including immunities, resistances, weaknesses, and any other increases or mitigation, divide the amount by 4, rounding down. You and each of the secondary casters lose that many Hit Points. If a secondary caster doesn't have enough Hit Points to give before dropping to 0 Hit Points, you take any remaining damage for them as well. When a secondary caster reaches 0 Hit Points in this way, their skin dries out like leather as the last of their life leaves their bodies; this is a death effect.
- **Critical Success** The light from your secondary casters envelops you in a warm radiance. In addition to the effects described above, you're healed to full Hit Points upon completion of the ritual.
- **Success** The secondary casters channel their energies to you, protecting you as described above.
- **Failure** The secondary casters cry out in sorrow, reaching out to you to feel your embrace, then they grow sad that they couldn't live up to your expectations. Nothing else happens.
- **Critical Failure** The secondary casters' attempts to unite with you become desperate, but ultimately, the only function of the link was to disorient all of you, making your bodies feel like they aren't your own. You and all secondary casters become [[Clumsy]] 3 for 3 days.

**Source:** `= this.source` (`= this.source-type`)
