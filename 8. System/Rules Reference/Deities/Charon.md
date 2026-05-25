---
type: deity
source-type: "Remaster"
domains: "Death, Knowledge, Soul, Water"
favored-weapon: "Staff"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 5: [[Wave Of Despair]], Rank 9: [[Phantasmagoria]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Charon, eldest of his counterparts and the Boatman of the Styx, is a patient and cunning figure. Content to allow plans to take hold over time, Charon freely offers his power only to collect on his bargain decades or even centuries later. As the Rider of Death, Charon concerns himself with miserable, pointless deaths that are devoid of any faith, mercy, or meaning, dragging those who perish in the depths of hopelessness and nihilism down into Abaddon and oblivion.

**Title** The Boatman

**Areas of Concern** Death

**Edicts** End all mortal life, exploit those who fear death

**Anathema** Offer anything for free, extend mortal lifespans, grant true salvation to the doomed or dying

**Religious Symbol** skull with coins on eyes

**Sacred Animal** horse, raven

**Sacred Colors** pale green

**Source:** `= this.source` (`= this.source-type`)
