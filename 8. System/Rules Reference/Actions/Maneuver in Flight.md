---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You have a fly Speed.

You try a difficult maneuver while flying. Attempt an Acrobatics check. The GM determines what maneuvers are possible, but they rarely allow you to move farther than your fly Speed.
- **Success** You succeed at the maneuver.
- **Failure** Your maneuver fails. The GM chooses if you simply can't move or if some other detrimental effect happens. The outcome should be appropriate for the maneuver you attempted (for instance, being blown off course if you were trying to fly against a strong wind).
- **Critical Failure** As failure, but the consequence is more dire.

Sample Maneuver in Flight Tasks- **Trained** steep ascent or descent
- **Expert** fly against the wind
- **Master** reverse direction
- **Legendary** fly through gale force winds

**Source:** `= this.source` (`= this.source-type`)
