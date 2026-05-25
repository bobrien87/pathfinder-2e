---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You try to provide food and shelter for yourself, and possibly others as well, with a standard of living. This typically uses Society if you're in a settlement or Survival if you're in the wild. The GM determines the DC based on the nature of the place where you're trying to Subsist. You might need a minimum proficiency rank to Subsist in particularly strange environments. Unlike most downtime activities, you can Subsist after 8 hours or less of exploration, but if you do, you take a –5 penalty.

Sample Subsist Tasks- **Untrained** a lush forest with calm weather or a large city with plentiful resources
- **Trained** typical hillside or village
- **Expert** typical mountains or insular hamlet
- **Master** typical desert or city under siege
- **Legendary** barren wasteland or city of undead
- **Critical Success** You either provide a subsistence living for yourself and one additional creature, or you improve your own food and shelter, granting yourself a comfortable living.
- **Success** You find enough food and shelter with basic protection from the elements to provide you a subsistence living.
- **Failure** You're exposed to the elements and don't get enough food, becoming [[Fatigued]] until you attain sufficient food and shelter.
- **Critical Failure** You attract trouble, eat something you shouldn't, or otherwise worsen your situation. You take a –2 circumstance penalty to checks to Subsist for 1 week. You don't find any food at all; if you don't have any stored up, you're in danger of starving or dying of thirst if you continue failing.

> [!danger] Effect: Adverse Subsist Situation

**Source:** `= this.source` (`= this.source-type`)
