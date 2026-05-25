---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy within 60 feet uses an ability that has the trait corresponding to your deviation damage type.

Your connection to energy is so much stronger than the offending display in front of you, allowing you to claim it for yourself. Attempt a Deviant check{counteract check} against the triggering effect as you draw it into your body. If you successfully counteract the ability, you gain temporary Hit Points equal to double the counteract rank of the ability, which last for 1 minute.

**Awakening** The energy you consume helps empower your abilities. The next ability from the dragon classification that you use increases its range by 30 feet if it has a range, or increases its area by 10 feet if it's a cone or line. If you don't use this benefit within 1 minute, it fades.

@Template[cone|distance:40]

@Template[line|distance:70]

**Awakening** You channel some of the seized energy into your next attack. Choose one of your weapons or unarmed attacks. Until the end of your next turn, Strikes with the chosen weapon or unarmed attack deal an additional 1d6 damage of a type matching the energy you consumed.

> [!danger] Effect: Consume Energy (Augment Strike)

**Source:** `= this.source` (`= this.source-type`)
