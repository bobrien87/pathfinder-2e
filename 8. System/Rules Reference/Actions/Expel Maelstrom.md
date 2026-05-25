---
type: action
source-type: "Remaster"
traits: ["[[Curse]]", "[[Occult]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're in a curse maelstrom state

**Effect** You expel the maelstrom from your body, sending the energy to reside in one unlucky creature within 60 feet. Your curse maelstrom state ends. The result depends on the creature's [[Will]] save.
- **Critical Success** The creature is unaffected, and the curse's energy dissipates harmlessly.
- **Success** The creature comes to house the maelstrom's wrath within it. It takes a -1 status penalty to all saving throws and skill checks for 1 minute.

> [!danger] Effect: Expel Maelstrom (Success)
- **Failure** The maelstrom strikes deep into the creature's soul. It takes a -2 status penalty to all saving throws and skill checks for 10 minutes.
- **Critical Failure** The maelstrom pitches the creature into a single fit of utter misfortune before burrowing into its soul. As failure, but the creature also must roll twice and take the lower result on its next saving throw or skill check; this is a misfortune effect.

> [!danger] Effect: Expel Maelstrom (Failure or Critical Failure)

**Source:** `= this.source` (`= this.source-type`)
