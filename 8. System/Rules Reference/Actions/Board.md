---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are adjacent to a point of entry on the vehicle you are attempting to board.

You board a vehicle through an open top, a door, a portal, or a hatch; if you're already on board, you can instead use this action to disembark into an empty space adjacent to the vehicle's point of entry. Using this action while the vehicle is in motion is challenging, requiring a successful Acrobatics or Athletics check with a DC equal to the vehicle's AC.

**Source:** `= this.source` (`= this.source-type`)
