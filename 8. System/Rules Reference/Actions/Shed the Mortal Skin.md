---
type: action
source-type: "Remaster"
traits: ["[[Healing]]", "[[Light]]", "[[Transcendence]]", "[[Vitality]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Like the serpent, that most ancient of immortals, you shed your skin, revealing a glowing divine form. If you are currently taking persistent fire or acid damage, you immediately end the effect. Until the beginning of your next turn, you shed bright light in a 20-foot radius (and dim light for the next 20 feet) like a torch. The next time you are dealt damage by an enemy before the beginning of your next turn, you shed glowing ichor in a square adjacent to you, and where it hits the earth, a glowing, thorned herb grows. A creature other than you can pluck and consume the herb with an Interact action to regain a number of Hit Points equal to half of the damage you were dealt by the attack that sprouted the herb.

**Source:** `= this.source` (`= this.source-type`)
