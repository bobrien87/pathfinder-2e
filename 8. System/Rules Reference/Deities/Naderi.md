---
type: deity
source-type: "Remaster"
domains: "Death, Passion, Sorrow, Water"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Soothe]], Rank 3: [[Veil Of Privacy]], Rank 8: [[Dream Council]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Lost Maiden

**Areas of Concern** Drowning, romantic tragedy, suicide

**Edicts** Comfort and encourage lovers, help the suffering escape their circumstances in life or in death

**Anathema** Dismiss or mock a creature's grief, separate lovers, torture a creature

**Religious Symbol** ornate golden dagger

**Sacred Animal** swan

**Sacred Colors** blue, red

**Source:** `= this.source` (`= this.source-type`)
