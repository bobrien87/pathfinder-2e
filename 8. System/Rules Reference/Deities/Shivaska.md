---
type: deity
source-type: "Remaster"
domains: "Abomination, Darkness, Pain, Time"
favored-weapon: "War-flail"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Tether]], Rank 3: [[Phantom Prison]], Rank 5: [[Slither]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Shivaska preys upon the forgotten and marginalized: orphans, the unhoused, refugees, and the like. The Chained Maiden's current form is that of a tall zecui with elongated limbs, a face that is completely smooth save for a large maw, and multiple black eyes studding her torso. This form has changed over time, yet each always has thirteen animated, hooked chains protruding from her back. Her symbol, the thirteen-hour clock, represents her association with inevitable extinction events, time ticking away toward destruction, prison sentences, and the relief that never comes after a terrible event. Her cults form around any institution of encasement and control: prisons, oppressive orphanages or monasteries, sweatshops, and the like. As a result, followers tend to be those with authority, but ones with a petty amount of power and never rulers of countries.

**Title** The Chained Maiden

**Areas of Concern** Aberrations, clocks, prisons

**Edicts** Accelerate impending doom, demand subservience from your lessers, oppress the weak

**Anathema** Allow a prisoner to go free, show mercy without personal benefit

**Religious Symbol** clock face with 13 hours

**Sacred Animal** tarantula

**Sacred Colors** brown, red

**Source:** `= this.source` (`= this.source-type`)
