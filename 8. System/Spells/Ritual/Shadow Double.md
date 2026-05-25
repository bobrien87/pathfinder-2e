---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
traits: ["[[Illusion]]"]
cast: "1 day"
targets: "1 living creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an illusory duplicate of the target creature by drawing shadowy material from the Netherworld and sculpting it into a semi-solid form. The shadow double is a 4th-level creature with no special abilities. If it needs to attempt a roll or use a DC, use the moderate number for a monster, except as noted below. It doesn't have any specific memories from the target, but it can use information about the creature gained from any of the casters to Impersonate the target. It looks exactly like the target and has a Deception modifier to Impersonate that creature equal to the modifier of the secondary spellcaster who rolled the Deception check, with a +4 status bonus. Though it doesn't have any of the original's special abilities, like a dragon's breath, illusions allow it to appear to use those abilities; they just never seem to have an effect. For instance, against a double's dragon's breath, all creatures in the area seem to critically succeed at their saving throws and take no damage. Creatures can attempt to disbelieve the illusion by attempting a Perception check against the Deception DC of the secondary spellcaster who rolled the Deception check.
- **Critical Success** You create the shadow double. It has the minion trait and is under your absolute control. You gain a direct mental link with the shadow double and can spend an action to command the shadow double via this link, even at a distance.
- **Success** As a critical success, but there is no special link between you and the shadow double. You must spend an action to command it verbally or by some other means.
- **Failure** The ritual fails and has no effect.
- **Critical Failure** The shadow double is created, but it isn't your minion and is hostile to all the casters. It does everything it can to destroy them, but if it can't immediately slay them, the shadow double tries to escape and plots their demise.

**Source:** `= this.source` (`= this.source-type`)
