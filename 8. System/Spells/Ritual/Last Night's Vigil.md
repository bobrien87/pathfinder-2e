---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
traits: ["[[Healing]]"]
cast: "8 hours"
range: "10 feet"
targets: "1 creature whom you love"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Obscure folktales state on the first day of spring, the Mother of Secrets wanders Tian Xia to dispense blessings of health upon the elderly. Last night's vigil is a folk ritual inspired by these stories.

This simple ritual can only be performed at night, in the presence of someone whom you love and who's ill, hurt, or otherwise unwell. You must stay awake through the night, keeping the sticks of incense lit to guide the goddess's passage. If you're indoors, you should keep a door or window slightly ajar to receive her holy presence. If performed on a winter night, the DCs of the ritual's skill checks are reduced by 1; if performed on the last night of winter before spring, the DCs are instead reduced by 2.

If the ritual is successful, you fall asleep for the briefest of moments to the sound of snowfall and the swishing of a horse tail whisk. When you awaken moments later, your loved one smiles at you, hopefully in better health.
- **Critical Success** The target's Hit Points are fully restored, and all diseases that are equal or lower level than twice the ritual's spell rank that they're currently suffering from reduce their stage by 1. If this reduces a disease's stage below 1, it cures that affliction.
- **Success** The target's Hit Points are fully restored, and one disease of a level that's equal to or lower than twice the ritual's spell rank that they're currently suffering from reduces its stage by 1. If this reduces the disease's stage below 1, it cures that affliction.
- **Failure** The ritual has no effect.
- **Critical Failure** You're [[Fatigued]] for the next 24 hours.

**Heightened (4th)** You can choose when you perform the ritual whether it affects curses or diseases.

**Heightened (6th)** You can affect curses and diseases simultaneously.

**Source:** `= this.source` (`= this.source-type`)
