---
type: hazard
sub-type: "{sub-type}"
source-type: "{source-type}"
level: {level}
traits: "{traits}"
stealth: "{stealth}"
disable: "{disable}"
ac: {ac}
fort: {fort}
ref: {ref}
will: {will}
hp: {hp}
hardness: {hardness}
immunities: "{immunities}"
reset: "{reset}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.sub-type != null, "**Hazard (" + this.sub-type + ")**", "**Hazard**")` `= this.level`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

**Stealth** `= this.stealth`
**Disable** `= this.disable`

***

`= choice(this.ac != null or this.fort != null or this.ref != null or this.will != null, "**AC** " + choice(this.ac != null, this.ac, "—") + "; **Fort** " + choice(this.fort != null, "+" + this.fort, "—") + ", **Ref** " + choice(this.ref != null, "+" + this.ref, "—") + ", **Will** " + choice(this.will != null, "+" + this.will, "—"), "")`
`= choice(this.hp != null or this.hardness != null, "**HP** " + choice(this.hp != null, this.hp, "—") + choice(this.hardness != null, "; **Hardness** " + this.hardness, "") + choice(this.immunities != null, "; **Immunities** " + this.immunities, ""), "")`
`= choice(this.reset != null, "**Reset** " + this.reset, "")`

***

{description}

#### Attacks / Actions
{attacks-and-actions}

**Source:** `= this.source` (`= this.source-type`)
