---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
traits: ["[[Mental]]", "[[Water]]"]
cast: "1 day"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Ganhil developed this ritual to emulate the epiphanies and flowing mental states he experienced during 4718's Challenge of Sky and Heaven: intense focus, emotional acceptance, dilated perceptions, and growing awareness of elemental perfection.

During the casting of this ritual, your thoughts enter a mindscape whose subjective flow of time is different, allowing you to perform retraining that would take a least a week of downtime. Your physical body still requires food or shelter during this time, so the secondary caster must nourish you with milk porridge or protect you from the elements with a raised parasol or similar item.
- **Critical Success** At the end of the ritual, you can retrain a class feature, feat, or skill.
- **Success** At the end of the ritual, you can retrain a feat or skill.
- **Failure** At the end of the ritual, you gain the [[Fatigued]] condition.
- **Critical Failure** As failure, and you also suffer from starvation and thirst as if you hadn't eaten for a week, taking @Damage[(10d4+7)] damage that cannot be healed until you eat and drink.

**Source:** `= this.source` (`= this.source-type`)
