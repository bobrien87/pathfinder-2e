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

**Requirements** You are in a square that contains a narrow surface, uneven ground, or another similar feature.

You move across a narrow surface or uneven ground, attempting an Acrobatics check against its Balance DC. You are [[Off Guard]] while on a narrow surface or uneven ground.
- **Critical Success** You move up to your Speed.
- **Success** You move up to your Speed, treating it as difficult terrain (every 5 feet costs 10 feet of movement).
- **Failure** You must remain stationary to keep your balance (wasting the action) or you fall. If you fall, your turn ends.
- **Critical Failure** You fall and your turn ends.

Sample Balance Tasks- **Untrained** tangled roots, uneven cobblestones
- **Trained** wooden beam
- **Expert** deep, loose gravel
- **Master** tightrope, smooth sheet of ice
- **Legendary** razor's edge, chunks of floor falling in midair

**Source:** `= this.source` (`= this.source-type`)
