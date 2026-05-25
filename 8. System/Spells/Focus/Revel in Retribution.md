---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Oracle]]"]
cast: "`pf2:1`"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Time seems to slow for you, allowing you to strike your opponents mid-move. You gain the [[Reactive Strike]] ability, and you immediately gain a second reaction that you can use only to use Reactive Strike. At the start of each of your subsequent turns when you regain your actions, you gain an additional reaction that can be used only to attempt a Reactive Strike.

> [!danger] Effect: Spell Effect: Revel in Retribution

Lashing out at a defenseless enemy invigorates you with the thrill of combat, granting you 5 temporary Hit Points whenever you successfully hit with a Reactive Strike. The temporary Hit Points last for the spell's duration.

**Heightened (+1)** The temporary Hit Points you gain from a successful Reactive Strike increase by 1.

**Source:** `= this.source` (`= this.source-type`)
