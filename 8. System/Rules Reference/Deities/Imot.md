---
type: deity
source-type: "Remaster"
domains: "Death, Destruction, Fate, Glyph"
favored-weapon: "Shield-boss"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Paranoia]], Rank 6: [[Phantasmal Calamity]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Imot is an agender psychopomp usher born from the guilt and desire for hindsight felt by mortals after a tragedy. It arranges calamities to kill off cultures that overstay their welcome. Imot is compelled to hide clues to every natural disaster using symbolism and equations; these clues induce a subconscious unease in those that do not understand them, and provide insight to those that do (though they usually end up figuring them out too late). For this reason, Imot is concerned with fear (particularly of personal failures) and self-blame for inevitable disasters, and judges souls who died unavoidable deaths.

**Title** The Symbol of Doom

**Areas of Concern** Inevitability, mathematics, portents

**Edicts** Search for omens in the natural world, push the boundaries of mathematics, study past disasters

**Anathema** Withhold your understanding of a portent, prevent the destruction of things that cannot be saved

**Religious Symbol** three adjacent circles arranged above, bisected by, and below a horizontal line

**Sacred Animal** scarab

**Sacred Colors** black, gold

**Source:** `= this.source` (`= this.source-type`)
