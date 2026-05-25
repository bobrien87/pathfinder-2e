---
type: deity
source-type: "Remaster"
divine-skill: "Medicine"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Laws of Mortality originated in the Garundi nation of Rahadoum as a response to the Oath Wars, a series of internecine conflicts that were tearing the nation's society apart. The fundamental principle behind the Laws is a relatively simple assertion that deific aid-even the best intentioned-ultimately comes at too high a price. The slaughter of fellow mortals for the glory of distant, unfathomable beings is not something that should be permitted within a society. Instead, mortal beings must shape their own fate, aware of their own limitations, trusting in their reliance upon one another and their shared values rather than divine intervention and guidance. This philosophy is summed up in the primary tenet of the Laws of Mortality: Let no mortal be beholden to a god.

**Areas of Concern** mortal affairs, peace, self-rule

**Edicts** challenge religious power and the spread of religion, expose and eradicate hidden worship, provide a peaceful and autonomous society in which the people are cared for through social infrastructure

**Anathema** worship or swear an oath by a deity or religion, solicit or receive divine or religious aid, take a side in conflicts between religions

**Source:** `= this.source` (`= this.source-type`)
