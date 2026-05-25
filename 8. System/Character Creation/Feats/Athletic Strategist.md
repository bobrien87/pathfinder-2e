---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Investigator]]"]
prerequisites: "trained in Athletics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know how to calculatedly manipulate joints and body weight. In addition to using an attack stratagem's roll substitution for a Strike, you can use it to modify a [[Disarm]], [[Grapple]], [[Reposition]], [[Shove]], or [[Trip]] attempt, substituting your [[Devise a Stratagem]] roll for the Athletics check. You must apply the substitution to the first eligible attack you make, whether it's a Strike or one of the Athletics actions.

You can also use your Intelligence modifier instead of Strength for the Athletics check when you substitute your Devise a Stratagem roll, unless you're using a weapon for the maneuver and the weapon doesn't fit the restrictions for using Intelligence with a stratagem.

**Source:** `= this.source` (`= this.source-type`)
