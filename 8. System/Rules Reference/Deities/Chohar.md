---
type: deity
source-type: "Remaster"
domains: "Fire, Family, Cities, Sun"
favored-weapon: "Starknife"
divine-font: "Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 3: [[Fireball]], Rank 4: [[Fire Shield]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The old gods of the threefold sun were all but forgotten under the rule of Walkena, the child god. The immortal tyrant punishes anyone who lacks faith with death, and there is no worse blasphemy than to worship a rival god in his city. But the freedom fighter Sihar and her followers, the Bright Lions, have spread the word of the old sun gods in secret, and now they are returning to the people.

**Title** The Golden Lion

**Areas of Concern** Justice, loyalty, work

**Edicts** Finish any and all tasks you accept, bring those who are cruel to justice, show pride in your home and your heritage

**Anathema** Break your word, be cruel to the innocent, rebuke someone due to their homeland

**Religious Symbol** lion face shield

**Sacred Animal** lion

**Sacred Colors** brown, gold

**Source:** `= this.source` (`= this.source-type`)
