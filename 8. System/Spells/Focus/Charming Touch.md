---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Emotion]]", "[[Focus]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Subtle]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 creature that could find you attractive"
defense: "Will"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You infuse your target with attraction, causing it to act friendlier toward you. The target attempts a Will save. It gains a +4 circumstance bonus to this save if you or your allies recently threatened or were hostile to it.
- **Critical Success** The target is unaffected and aware you tried to charm it.
- **Success** The target is unaffected but thinks your spell was something harmless instead of *charming touch*, unless it identifies the spell.
- **Failure** The target's attitude becomes [[Friendly]] toward you. If it was Friendly, it becomes [[Helpful]]. It can't use hostile actions against you. If you use a hostile action against the target, the spell ends. You can Dismiss the spell. After the spell ends, the target doesn't necessarily realize it was charmed unless its friendship with you or the actions you convinced it to take clash with its expectations. If it doesn't realize you charmed it, you could potentially convince it to continue being your friend via mundane means.
- **Critical Failure** As failure, but the target is helpful.

**Source:** `= this.source` (`= this.source-type`)
