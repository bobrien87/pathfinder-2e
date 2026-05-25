---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "10 minutes"
range: "touch"
targets: "1 corpse"
defense: "Will"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grant the target corpse a semblance of life, which it uses to speak the answers to three questions posed to it. This spell calls on the physical body's latent memories rather than summoning back the deceased's spirit, so the corpse must be mostly intact for the spell to function. The more damage the corpse has taken, the more inaccurate or patchwork its answers are, and it must have a throat and mouth to speak at all. If anyone has previously cast this spell on the corpse in the last week, the spell automatically fails. The corpse can attempt a Will save to resist answering the questions using the statistics of the original creature at its time of death, with the following effects.
- **Critical Success** The target can lie or refuse to answer your questions, and the target's spirit haunts you for 24 hours, bothering you and causing you to be unable to gain any rest for that time.
- **Success** The target can provide false information or refuse to answer your questions.
- **Failure** The target must answer truthfully, but its answers can be brief, cryptic, and repetitive. It can still mislead you or attempt to stall so that the spell's duration runs out before you can ask all your questions.
- **Critical Failure** As failure, but the target's answers are more direct and less repetitive, though still cryptic. It takes a -2 status penalty to Deception checks to deceive or mislead you.

**Source:** `= this.source` (`= this.source-type`)
