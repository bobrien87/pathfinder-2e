---
type: hazard
sub-type: "{sub-type}"
source-type: "{source-type}"
level: "{level}"
traits:
stealth: "{stealth}"
disable: "{disable}"
ac: "{ac}"
fort: "{fort}"
ref: "{ref}"
will: "{will}"
hp: "{hp}"
hardness: "{hardness}"
immunities: "{immunities}"
reset: "{reset}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.sub-type != null and this.sub-type != "", "**Hazard (" + this.sub-type + ")**", "**Hazard**")` `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, ", "), "")`

**Stealth** `= this.stealth`
**Disable** `= this.disable`

`= choice(this.ac != null and this.ac != "" or this.fort != null and this.fort != "" or this.ref != null and this.ref != "" or this.will != null and this.will != "", "**AC** " + choice(this.ac != null and this.ac != "", this.ac, "—") + "; **Fort** " + choice(this.fort != null and this.fort != "", "+" + this.fort, "—") + ", **Ref** " + choice(this.ref != null and this.ref != "", "+" + this.ref, "—") + ", **Will** " + choice(this.will != null and this.will != "", "+" + this.will, "—"), "")`
`= choice(this.hp != null and this.hp != "" or this.hardness != null and this.hardness != "", "**HP** " + choice(this.hp != null and this.hp != "", this.hp, "—") + choice(this.hardness != null and this.hardness != "", "; **Hardness** " + this.hardness, "") + choice(this.immunities != null and this.immunities != "", "; **Immunities** " + this.immunities, ""), "")`
`= choice(this.reset != null and this.reset != "", "**Reset** " + this.reset, "")`

{description}

#### Attacks / Actions
{attacks-and-actions}

**Source:** `= this.source` (`= this.source-type`)
