---
type: deity
source-type: "Remaster"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In a world where the gods demonstrably exist, few people uphold a strictly atheistic or agnostic worldview. That is, a belief that there are no gods or that the existence of gods is unknowable. However, a good number of people choose not to worship any deities whatsoever. In some cases, this is not a deliberate choice so much as an inadvertent apathy, as the gods can seem distant compared to the pressing trials of life. Many other atheists choose not to worship because of the value they place on freedom—not being beholden to a deity means no limitations, no censure, no anathema, and no strictures. While this decision might sound amoral to some, for atheists, it can be motivated by a desire for autonomy and the right to choose one's own fate.

**Edicts** none

**Anathema** none

**Source:** `= this.source` (`= this.source-type`)
