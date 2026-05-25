---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Verduran Shadow|Verduran Shadow]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Stealth, trained in Survival"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your awareness of primal energies allows you to explore forests with preternatural ease. You become an expert in Survival. You can substitute your proficiency in Survival for your proficiency in Stealth when meeting feat prerequisites and gaining additional benefits from feats for being an expert, master, or legendary in Stealth; however, unless you also fulfill the Stealth prerequisite, you can only use those feats in forest terrain. While in forests, you can use your Survival modifier in place of your Stealth modifier when you [[Avoid Notice]], [[Hide]], [[Sneak]], or would use Stealth to roll initiative.

Verduran Shadow

**Source:** `= this.source` (`= this.source-type`)
