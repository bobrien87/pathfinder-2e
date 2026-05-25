---
type: action
source-type: "Remaster"
traits: ["[[Attack]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
cast: "`pf2:1`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

`pf2:1` or `pf2:2`

With a wave of your hand, you collect elemental matter from your aura and swing or hurl it. Choose one of your kinetic elements and a damage type listed for that element, then make a melee or ranged impulse attack against the AC of one creature. Add your Strength modifier to the damage roll for a melee Elemental Blast. If you make a 2-action Elemental Blast, you gain a status bonus to the damage roll equal to your Constitution modifier. The element determines the damage die, damage type, and range (for a ranged blast). A damage type other than a physical damage type adds its trait to the blast.

- **Air** 1d6 electricity or slashing, 60 feet

- **Earth** 1d8 bludgeoning or piercing, 30 feet

- **Fire** 1d6 fire, range 60 feet

- **Metal** 1d8 piercing or slashing, 30 feet

- **Water** 1d8 bludgeoning or cold, 30 feet

- **Wood** 1d8 bludgeoning or vitality, 30 feet
- **Critical Success** The target takes double damage.
- **Success** The target takes full damage.

**Level (+4)** The damage increases by one die.

**Source:** `= this.source` (`= this.source-type`)
