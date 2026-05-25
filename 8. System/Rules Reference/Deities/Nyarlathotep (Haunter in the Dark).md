---
type: deity
source-type: "Remaster"
domains: "Darkness, Knowledge, Nightmares, Trickery"
favored-weapon: "Kukri"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 4: [[Nightmare]], Rank 5: [[Summon Entity]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Nyarlathotep is often venerated by grioths in a bat-like incarnation with a three-lobed burning eye known as the Haunter in the Dark. His symbol is a circle with wing-shaped arms.

**Title** Haunter in the Dark

**Areas of Concern** Conspiracies, conquest, darkness, long-term plans

**Edicts** Create darkness, encourage authorities to bring the apocalypse

**Anathema** None

**Religious Symbol** Circle with wing-shaped arms

**Sacred Animal** Bat

**Sacred Colors** black, gray

**Source:** `= this.source` (`= this.source-type`)
