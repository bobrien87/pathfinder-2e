---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Elf]]", "[[Holy]]", "[[Light]]"]
prerequisites: "Demon Hunter"
frequency: "once per day"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can deliver a melee blow to a demon that creates an explosion of holy light to try to finish the demon off. In addition to the normal damage from your melee Strike, you also inflict 10d6 spirit damage to the demon. The demon can resist this additional damage with a [[Fortitude]] save against your class DC. If the demon is slain by this strike, it explodes in a blast of holy light that fills a @Template[type:emanation|distance:30]. All creatures in this area that have the demon trait take @Damage[10d6[spirit]|options:area-damage] damage and must attempt a [[Fortitude]] save against your class DC.
- **Critical Success** The demon takes no damage.
- **Success** The demon takes half damage.
- **Failure** The demon takes full damage and is [[Dazzled]] for 1 round.
- **Critical Failure** The demon takes full damage and is permanently [[Blinded]].

**Source:** `= this.source` (`= this.source-type`)
