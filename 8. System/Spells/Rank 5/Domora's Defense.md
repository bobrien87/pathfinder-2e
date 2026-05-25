---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "up to 3 creatures"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Domora Hume is considered by most to be the first god caller, conjuring a god from the Plane of Water named Dyzad to protect his town from Mammoth Lord raiders. A lost story of this defense claims that Dyzad appeared to be in three places at once, blocking the raiders' spears, swords, and torches. The intended lesson is that Dyzad will overcome any barrier to protect the people of Sarkoris. This spell gives that intention physical form, allowing the caster to protect their people.

When you Cast this Spell, a watery replica of the eidolon Dyzad appears in front of each of the targets, granting them a +1 circumstance bonus to AC and fire resistance 5.

> [!danger] Effect: Spell Effect: Domora's Defense

While the replica persists, a target can use the Shield Block reaction with the replica. The replica has Hardness 15 (or Hardness 20 against fire damage). They can use this reaction to reduce damage from any spell or magical effect, even if it doesn't deal physical damage. After a target uses Shield Block, the replica dissipates. The spell ends when you no longer Sustain it or if all three replicas have dissipated, whichever happens first.

**Source:** `= this.source` (`= this.source-type`)
