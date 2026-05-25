---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Electricity]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:r`"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You would take electricity damage.

When lightning is turned against you, you store the charge safely within yourself, unleashing it when the time is right. You gain electricity resistance 10 against the triggering effect. If you successfully prevent damage in this way, at any time during the spell's duration, you can spend a single action, which has the attack trait, to expend the charge and make a spell attack against the AC of a target within 60 feet. This attack deals electricity damage equal to the damage prevented by *bottle the storm*. If you Cast *bottle the storm* a second time before the original duration elapses, or if you do not make this attack within 1 minute, the stored charge dissipates harmlessly.

**Heightened (7th)** The resistance increases to 15, and you can immediately make the spell attack granted by *bottle the storm* as part of the reaction used to Cast the Spell.

**Heightened (10th)** The resistance increases to 20, and you can immediately make the spell attack granted by *bottle the storm* as part of the reaction used to Cast the Spell.

> [!danger] Effect: Spell Effect: Bottle the Storm

**Source:** `= this.source` (`= this.source-type`)
