---
type: deity
source-type: "Remaster"
domains: "Cities, Destruction, Earth, Indulgence"
favored-weapon: "Ranseur"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Pummeling Rubble]], Rank 2: [[Feast Of Ashes]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Xoveron jealously guards his spheres of gargoyles, reckless consumption, and ruins. When the fourarmed, four-headed Horned Prince hunts, the air fills with the horrific sound of stone grinding on stone. The demon lord particularly exalts in the destruction of cities, encouraging people to use more resources than they contribute, while bandits that prey on cities and villages often ask for his blessing upon them and his curse on their targets. He also enjoys the ruination and suffering of architects, sculptors, and those who aim to build something lasting. Unlike most other demon lords, Xoveron has the patience for longterm disruption, as befit the venerated prince of stony gargoyles. Cults form from either the aforementioned bandits or the absurdly wealthy, who often benefit from slowly crushing of those beneath them for the slightest taste of the finest things life can offer

**Title** Horned Prince

**Areas of Concern** Gargoyles, gluttony, ruins

**Edicts** Acquire and consume more resources than you need, embrace stillness, ensure ruins remain in their dilapidated state

**Anathema** Allow a structure to be rebuilt or maintained, practice moderation in consumption

**Religious Symbol** five-horned gargoyle skull

**Sacred Animal** boar

**Sacred Colors** black, brown

**Source:** `= this.source` (`= this.source-type`)
