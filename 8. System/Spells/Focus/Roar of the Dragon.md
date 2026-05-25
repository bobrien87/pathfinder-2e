---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Auditory]]", "[[Cleric]]", "[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You channel the might of dragons into your voice, letting out a roar that engenders respect in dragonkind but that instills fear in most other creatures. The impressive roar grants you a +2 circumstance bonus to Diplomacy checks for 10 minutes against dragons that were in the area at the time of casting.

> [!danger] Effect: Spell Effect: Roar of the Dragon

Roar of the dragon affects non-dragon creatures with deep ties to dragonkind (such as a barbarian with the draconic instinct, a sorcerer with the draconic bloodline, or a member of a culture that reveres dragons) as if they had the dragon trait. The GM decides if a creature is aligned enough with dragonkind to be affected in this way. All enemies within the area other than dragons must attempt a Will save; to these enemies, roar of the dragon is a fear effect.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 3 and [[Fleeing]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
