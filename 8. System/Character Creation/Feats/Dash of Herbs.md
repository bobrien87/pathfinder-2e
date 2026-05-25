---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Healing]]", "[[Impulse]]", "[[Kineticist]]", "[[Plant]]", "[[Primal]]", "[[Vitality]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A small cloud of medicinal herbs heal a creature. The type of herbs depends on which malady you decide to treat: [[Confused]], disease, poison, [[Sickened]], or injuries. Target one living creature within 30 feet, who regains @Damage[((floor((max(6,@actor.level)-6)/2)+2)d8+4)[healing]] HP and can attempt a new save against one malady of the chosen kind. If you chose injuries, instead increase the healing dice to @Damage[((floor((max(6,@actor.level)-6)/2)+2)d10+4)[healing]]{d10s}. The creature becomes temporarily immune to Dash of Herbs for 10 minutes.

Alternatively, you can add the herbs to a dish of food being prepared for up to six people. Creatures who partake in the meal gain the benefits. The herbs' healing effects wear off if not eaten within an hour, though their flavor remains.

**Level (+2)** The healing increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
