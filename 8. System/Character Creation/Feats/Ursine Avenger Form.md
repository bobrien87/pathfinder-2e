---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ursine Avenger Hood|Ursine Avenger Hood]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Artifact]]", "[[Morph]]", "[[Primal]]"]
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You draw the *Ursine Avenger Hood* over your head and its fur over your arms, assuming an ursine form that has traits of your original form as well as that of a bear. In your ursine form, you gain a jaws unarmed attack that deals 1d8 piercing damage and a claws unarmed attack that deals 1d6 slashing damage and has the agile trait. Both unarmed attacks are in the brawling group. You lose the ability to speak complex sentences while transformed and can only communicate through grunts and gestures; this prevents you from using effects that require a shared or spoken language until you revert back to your non-hybrid form. You can use this action while transformed to remove the hood and return to your original form.

**Source:** `= this.source` (`= this.source-type`)
