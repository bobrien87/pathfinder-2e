---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You designate a single, non-mindless creature as your focus and assess its motivations. You must be able to see and hear the creature. You gain a +2 circumstance bonus to Perception checks when you Sense the Motive of your focus and a +2 circumstance bonus to your Perception DC should your focus attempt to Lie or `act feint` against you. You gain a +2 circumstance bonus to Deception, Diplomacy, and Intimidation checks against your focus. You can only have one creature designated as your focus at a time. If you use Size Up against a creature when you already have a creature designated, the prior creature loses the designation and the new focus gains the designation. Your designation otherwise lasts until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
