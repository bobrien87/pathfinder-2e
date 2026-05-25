---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Auditory]]", "[[Aura]]", "[[Concentrate]]", "[[Manipulate]]", "[[Sonic]]"]
cast: "`pf2:2`"
area: "40-foot emanation"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your voice trills in perfect vibrato. When casting the spell, you can make the area any radius you choose, up to 40 feet. The reverberations of your voice continue to shimmer and hang in the air as long as you Sustain the spell but can't be heard at all outside of the area. A creature must attempt a Will save if it's within the area when you Cast the Spell or as soon as it enters the area while the spell is in effect. Once a creature has attempted the save, it uses the same result for that casting of vibrant vibrato.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes 5d10 persistent,sonic damage at the end of their turn as long as they remain within the aura's area of effect.
- **Failure** As success, but if the creature leaves the area, or if you move far enough from the creature that they're no longer in the area, the creature hears a shattering sound and takes 5d10 sonic damage and is [[Stunned]] 1. The creature is then [[Deafened]] for the rest of the spell's duration.
- **Critical Failure** As failure, but the creature takes double the sonic damage and is [[Stunned]] 3.

**Heightened (+1)** The damage on a failed save increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
